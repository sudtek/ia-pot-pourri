#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
# =============================================================================
# GROK CHAT HISTORY EXPORTER - VERSION ENHANCED
# =============================================================================

Résumé :
    Cet outil permet d’exporter l’intégralité de vos conversations Grok (depuis 
    grok.com et x.com/i/grok) à partir du fichier prod-grok-backend.json obtenu 
    via l’export officiel de xAI.

Fonctionnalités principales :
    • Export en Markdown (.md), Texte brut (.txt) ou JSON Lines (.jsonl)
    • Gestion automatique des doublons de titres (_1, _2, etc.)
    • Formatage des dates en français lisible
    • Détection et intégration automatique des images/assets dans les fichiers Markdown
    • Option d’inclusion des traces de raisonnement interne de Grok (🧠 Thinking Process)
    • Nettoyage sécurisé des noms de fichiers (protection path traversal)

Version     : 2.0 Enhanced (DeepSeek + Grok)
Date        : 15 juin 2026
Auteur      : Fork DeepSeek + améliorations Grok (xAI)
Licence     : MIT

Commande de lancement recommandée (mode interactif) :
    python grok_exporter_DEEPSEEK_enhanced.py -i

Utilisation rapide en ligne de commande :
    python grok_exporter_DEEPSEEK_enhanced.py prod-grok-backend.json -md -t
    (export Markdown avec traces de raisonnement)

Ce script est conçu pour être autonome, sécurisé et facile à utiliser.
"""

import os
import json
import re
import sys
import argparse
from datetime import datetime
from collections import defaultdict

# ========== UTILITAIRES GÉNÉRAUX ==========
def safe_filename(title, counter=0):
    """Sanitized filename with duplicate counter support."""
    title = re.sub(r'[^\x00-\x7F]+', '', title)
    title = re.sub(r'[\\/*?:"<>|]', '_', title)
    title = re.sub(r'\.\.', '_', title)
    title = re.sub(r'[./\\]', '_', title)
    title = os.path.basename(title).strip()
    if not title or title == '.' or title == '..':
        title = 'untitled'
    if counter > 0:
        title = f"{title}_{counter}"
    return title

def format_datetime(timestamp):
    """Convert Grok timestamp to readable French format."""
    if not timestamp:
        return ""
    try:
        if isinstance(timestamp, (int, float)):
            dt = datetime.fromtimestamp(timestamp)
        else:
            ts = timestamp.replace('Z', '+00:00')
            dt = datetime.fromisoformat(ts)
        return dt.strftime("%d %B %Y à %H:%M")
    except:
        return str(timestamp)

def extract_asset_uuids(text):
    """Extract potential asset UUIDs from message text."""
    if not text:
        return []
    uuid_pattern = r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'
    return re.findall(uuid_pattern, text)

def replace_assets_in_markdown(message, asset_dir, output_dir):
    """Replace asset UUIDs with local Markdown image links."""
    if not message or not os.path.exists(asset_dir):
        return message
    uuids = extract_asset_uuids(message)
    for uuid in uuids:
        asset_file = os.path.join(asset_dir, uuid, "content")
        if os.path.exists(asset_file):
            rel_path = os.path.relpath(asset_file, start=output_dir)
            img_md = f"![Image]({rel_path})"
            message = message.replace(uuid, img_md)
    return message

def replace_assets_in_text(message):
    """Replace asset UUIDs with a simple text placeholder."""
    if not message:
        return message
    uuids = extract_asset_uuids(message)
    for uuid in uuids:
        message = message.replace(uuid, f"[Image: {uuid}]")
    return message

def get_asset_list(message):
    """Return list of asset UUIDs found in message."""
    return extract_asset_uuids(message)

# ========== EXTRACTION DES TRACES DE RAISONNEMENT ==========
def extract_thinking_text(traces):
    """Extract and format thinking traces from Grok responses."""
    if not traces:
        return ""
    thinking_parts = []
    if isinstance(traces, list):
        for trace in traces:
            if isinstance(trace, dict):
                text = trace.get('thinking_trace', '')
                if text:
                    thinking_parts.append(text)
            elif isinstance(trace, str):
                thinking_parts.append(trace)
    elif isinstance(traces, dict):
        text = traces.get('thinking_trace', '')
        if text:
            thinking_parts.append(text)
    elif isinstance(traces, str):
        thinking_parts.append(traces)
    return '\n\n'.join(thinking_parts) if thinking_parts else ""

def format_thinking_for_markdown(thinking_text):
    if not thinking_text:
        return ""
    lines = ["<details>", "<summary>🧠 AI Thinking Process</summary>", "", "```", thinking_text, "```", "", "</details>", ""]
    return '\n'.join(lines)

def format_thinking_for_text(thinking_text):
    if not thinking_text:
        return ""
    lines = ["=" * 60, "AI THINKING PROCESS:", "=" * 60, thinking_text, "=" * 60, ""]
    return '\n'.join(lines)

# ========== TRAITEMENT D'UNE CONVERSATION ==========
def process_conversation(conv, include_thinking=False):
    """Validate and extract conversation data."""
    if not isinstance(conv, dict) or 'conversation' not in conv or 'responses' not in conv:
        return None
    conv_data = conv['conversation']
    chat_id = conv_data.get('id', 'unknown')
    title = conv_data.get('title', '') or ''
    create_time = conv_data.get('create_time', '')
    responses = conv['responses']
    if not title or not responses:
        return None
    return {
        'chat_id': chat_id,
        'title': title,
        'create_time': create_time,
        'responses': responses,
        'include_thinking': include_thinking
    }

# ========== CONVERSION MARKDOWN ==========
def convert_to_markdown(processed_conv, output_dir, asset_dir, counter=0):
    """Generate .md file with asset linking and date formatting."""
    title = processed_conv['title']
    chat_id = processed_conv['chat_id']
    create_time = processed_conv['create_time']
    include_thinking = processed_conv['include_thinking']
    responses = processed_conv['responses']
    
    safe_title = safe_filename(title, counter)
    filename = os.path.join(output_dir, f"{safe_title}.md")
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"**Chat ID:** {chat_id}\n\n")
            if create_time:
                f.write(f"**Créé le :** {format_datetime(create_time)}\n\n")
            f.write("---\n\n")
            
            for resp_wrapper in responses:
                resp = resp_wrapper.get('response', {})
                if not isinstance(resp, dict) or 'sender' not in resp:
                    continue
                sender = resp.get('sender', 'unknown')
                message = resp.get('message', '')
                
                if asset_dir and os.path.exists(asset_dir):
                    message = replace_assets_in_markdown(message, asset_dir, output_dir)
                
                if include_thinking:
                    thinking_traces = resp.get('agent_thinking_traces', [])
                    thinking_text = extract_thinking_text(thinking_traces)
                    if thinking_text:
                        f.write(format_thinking_for_markdown(thinking_text))
                
                if message:
                    f.write(f"**{sender}:**\n\n{message}\n\n")
                f.write("---\n\n")
        return True
    except Exception as e:
        print(f"Error writing {filename}: {e}")
        return False

# ========== CONVERSION TEXTE BRUT ==========
def convert_to_text(processed_conv, output_dir, counter=0):
    """Generate .txt file with asset placeholders and date formatting."""
    title = processed_conv['title']
    chat_id = processed_conv['chat_id']
    create_time = processed_conv['create_time']
    include_thinking = processed_conv['include_thinking']
    responses = processed_conv['responses']
    
    safe_title = safe_filename(title, counter)
    filename = os.path.join(output_dir, f"{safe_title}.txt")
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Title: {title}\n")
            f.write(f"Chat ID: {chat_id}\n")
            if create_time:
                f.write(f"Created: {format_datetime(create_time)}\n")
            f.write("=" * 60 + "\n\n")
            
            for resp_wrapper in responses:
                resp = resp_wrapper.get('response', {})
                if not isinstance(resp, dict) or 'sender' not in resp:
                    continue
                sender = resp.get('sender', 'unknown')
                message = resp.get('message', '')
                
                # Remplacer les UUID par des placeholders texte
                message = replace_assets_in_text(message)
                
                if include_thinking:
                    thinking_traces = resp.get('agent_thinking_traces', [])
                    thinking_text = extract_thinking_text(thinking_traces)
                    if thinking_text:
                        f.write(format_thinking_for_text(thinking_text))
                
                if message:
                    f.write(f"{sender}:\n\n{message}\n\n")
                f.write("-" * 60 + "\n\n")
        return True
    except Exception as e:
        print(f"Error writing {filename}: {e}")
        return False

# ========== CONVERSION JSON LINES ==========
def convert_to_jsonl(processed_conv, output_dir, counter=0):
    """Generate .jsonl file with assets list and formatted date."""
    title = processed_conv['title']
    include_thinking = processed_conv['include_thinking']
    responses = processed_conv['responses']
    
    safe_title = safe_filename(title, counter)
    filename = os.path.join(output_dir, f"{safe_title}.jsonl")
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for resp_wrapper in responses:
                resp = resp_wrapper.get('response', {})
                if not isinstance(resp, dict):
                    continue
                
                message = resp.get('message', '')
                assets = get_asset_list(message)  # liste des UUIDs trouvés
                
                line_data = {
                    'sender': resp.get('sender', 'unknown'),
                    'message': message,
                    'create_time': format_datetime(resp.get('create_time', '')),
                    'model': resp.get('model', ''),
                    'assets': assets
                }
                
                if include_thinking:
                    thinking_traces = resp.get('agent_thinking_traces', [])
                    thinking_text = extract_thinking_text(thinking_traces)
                    line_data['thinking'] = thinking_text
                
                f.write(json.dumps(line_data, ensure_ascii=False) + '\n')
        return True
    except Exception as e:
        print(f"Error writing {filename}: {e}")
        return False

# ========== CHARGEMENT DU FICHIER JSON ==========
def load_conversations(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict) or 'conversations' not in data:
            print(f"Error: JSON file '{json_file}' does not contain Grok conversations format.")
            return None
        return data['conversations']
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_file}'.")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# ========== MENU INTERACTIF ==========
def interactive_menu():
    print("=" * 60)
    print("Grok Chat History Exporter (Enhanced by DeepSeek)")
    print("=" * 60)
    print()
    default_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'prod-grok-backend.json')
    json_file = input(f"Path to Grok conversations JSON file\n[default: {default_path}]: ").strip()
    if not json_file:
        json_file = default_path
    if not os.path.exists(json_file):
        print(f"Error: File '{json_file}' not found.")
        sys.exit(1)
    print()
    print("Select output format:")
    print("1. Markdown (.md)")
    print("2. Plain Text (.txt)")
    print("3. JSON Lines (.jsonl)")
    print("4. All formats")
    choice = input("Enter choice [1-4] (default: 1): ").strip()
    formats = []
    if choice == '2':
        formats = ['txt']
    elif choice == '3':
        formats = ['jsonl']
    elif choice == '4':
        formats = ['md', 'txt', 'jsonl']
    else:
        formats = ['md']
    print()
    print("Include AI thinking traces?")
    print("1. No (only final responses)")
    print("2. Yes (include thinking process)")
    thinking_choice = input("Enter choice [1-2] (default: 1): ").strip()
    include_thinking = thinking_choice == '2'
    return json_file, formats, include_thinking

# ========== MAIN ==========
def main():
    parser = argparse.ArgumentParser(description='Grok Chat History Exporter Enhanced')
    parser.add_argument('json_file', nargs='?', help='Path to Grok conversations JSON file')
    parser.add_argument('-o', '--output-dir', help='Output directory (default: script directory)')
    parser.add_argument('-md', '--markdown', action='store_true', help='Export to Markdown')
    parser.add_argument('-txt', '--text', action='store_true', help='Export to Plain Text')
    parser.add_argument('-jsonl', '--jsonlines', action='store_true', help='Export to JSON Lines')
    parser.add_argument('-all', '--all-formats', action='store_true', help='Export to all formats')
    parser.add_argument('-t', '--thinking', action='store_true', help='Include AI thinking traces')
    parser.add_argument('-i', '--interactive', action='store_true', help='Use interactive mode')
    parser.add_argument('--asset-dir', default='prod-mc-asset-server', help='Directory containing assets (default: prod-mc-asset-server)')
    args = parser.parse_args()
    
    if args.interactive or not args.json_file:
        json_file, formats, include_thinking = interactive_menu()
    else:
        json_file = args.json_file
        include_thinking = args.thinking
        if args.all_formats:
            formats = ['md', 'txt', 'jsonl']
        elif args.text:
            formats = ['txt']
        elif args.jsonlines:
            formats = ['jsonl']
        else:
            formats = ['md']
    
    output_dir = args.output_dir or os.path.dirname(os.path.abspath(__file__))
    os.makedirs(output_dir, exist_ok=True)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    asset_dir = os.path.join(script_dir, args.asset_dir)
    
    conversations = load_conversations(json_file)
    if not conversations:
        sys.exit(1)
    
    total = len(conversations)
    conversations_exported = 0
    conversations_skipped = 0
    files_written = 0
    title_counter = defaultdict(int)
    
    print()
    print(f"Processing {total} conversations...")
    print(f"Output formats: {', '.join(formats)}")
    print(f"Include thinking: {'Yes' if include_thinking else 'No'}")
    print()
    
    for conv in conversations:
        processed_conv = process_conversation(conv, include_thinking)
        if not processed_conv:
            conversations_skipped += 1
            continue
        
        title = processed_conv['title']
        counter = title_counter[title]
        title_counter[title] += 1
        
        success_for_this_conv = False
        for fmt in formats:
            if fmt == 'md':
                success = convert_to_markdown(processed_conv, output_dir, asset_dir, counter)
            elif fmt == 'txt':
                success = convert_to_text(processed_conv, output_dir, counter)
            elif fmt == 'jsonl':
                success = convert_to_jsonl(processed_conv, output_dir, counter)
            else:
                success = False
            
            if success:
                files_written += 1
                success_for_this_conv = True
        
        if success_for_this_conv:
            conversations_exported += 1
        else:
            conversations_skipped += 1
    
    print("--- Export Report ---")
    print(f"Total conversations: {total}")
    print(f"Conversations successfully exported (at least one format): {conversations_exported}")
    print(f"Conversations skipped (no format could be written): {conversations_skipped}")
    print(f"Total files written: {files_written}")
    print(f"Output directory: {output_dir}")

if __name__ == "__main__":
    main()
