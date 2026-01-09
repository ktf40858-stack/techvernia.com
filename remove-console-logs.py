#!/usr/bin/env python3
"""
==============================================
TechVernia - Remove Console Logs for Production
==============================================

This script removes console.log, console.warn, console.error, and console.debug
statements from JavaScript files for production deployment.

Usage:
    python remove-console-logs.py [--dry-run] [--directory path]

Options:
    --dry-run       Show what would be changed without modifying files
    --directory     Specify the directory to process (default: techvernia.com/js)
    --backup        Create .backup files before modifying (default: True)
"""

import os
import re
import argparse
import sys
from pathlib import Path

# Regex patterns to match console statements
CONSOLE_PATTERNS = [
    # Match full console.log/warn/error/debug statements
    r'console\.(log|warn|error|debug|info|trace)\s*\([^)]*\)\s*;?',
    # Match multi-line console statements
    r'console\.(log|warn|error|debug|info|trace)\s*\(\s*[^)]*\s*\)\s*;?',
]

def remove_console_logs(content, dry_run=False):
    """Remove console statements from JavaScript content."""
    original = content
    modified = content
    changes = []

    for pattern in CONSOLE_PATTERNS:
        matches = re.finditer(pattern, modified, re.MULTILINE | re.DOTALL)
        for match in matches:
            changes.append({
                'line': modified[:match.start()].count('\n') + 1,
                'text': match.group(0)[:50] + ('...' if len(match.group(0)) > 50 else '')
            })

        # Replace console statements with empty string
        modified = re.sub(pattern, '', modified, flags=re.MULTILINE | re.DOTALL)

    # Clean up empty lines (optional - preserves formatting)
    # modified = re.sub(r'\n\s*\n\s*\n', '\n\n', modified)

    return modified, changes, original != modified

def process_file(file_path, dry_run=False, create_backup=True):
    """Process a single JavaScript file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        modified_content, changes, has_changes = remove_console_logs(content, dry_run)

        if has_changes:
            if dry_run:
                print(f"\n[FILE] {file_path}")
                print(f"   Would remove {len(changes)} console statement(s):")
                for change in changes[:5]:  # Show first 5
                    print(f"   - Line {change['line']}: {change['text']}")
                if len(changes) > 5:
                    print(f"   ... and {len(changes) - 5} more")
            else:
                # Create backup if requested
                if create_backup:
                    backup_path = f"{file_path}.backup"
                    with open(backup_path, 'w', encoding='utf-8') as f:
                        f.write(content)

                # Write modified content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)

                print(f"[OK] {file_path}")
                print(f"   Removed {len(changes)} console statement(s)")

        return has_changes, len(changes)

    except Exception as e:
        print(f"[ERROR] Error processing {file_path}: {e}", file=sys.stderr)
        return False, 0

def process_directory(directory, dry_run=False, create_backup=True, exclude_patterns=None):
    """Process all JavaScript files in a directory."""
    if exclude_patterns is None:
        exclude_patterns = ['node_modules', '.git', 'vendor', 'dist', 'build']

    js_files = []
    for root, dirs, files in os.walk(directory):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_patterns]

        for file in files:
            if file.endswith('.js') and not file.endswith('.min.js'):
                js_files.append(os.path.join(root, file))

    if not js_files:
        print(f"[WARNING]  No JavaScript files found in {directory}")
        return

    mode_text = "DRY RUN MODE" if dry_run else "PROCESSING"
    print(f"\n{mode_text}")
    print(f"{'=' * 60}")
    print(f"Directory: {directory}")
    print(f"Files found: {len(js_files)}")
    print(f"{'=' * 60}\n")

    total_changes = 0
    files_modified = 0

    for js_file in js_files:
        has_changes, num_changes = process_file(js_file, dry_run, create_backup)
        if has_changes:
            files_modified += 1
            total_changes += num_changes

    print(f"\n{'=' * 60}")
    print(f"[SUMMARY] Summary:")
    print(f"   Files processed: {len(js_files)}")
    print(f"   Files {'would be ' if dry_run else ''}modified: {files_modified}")
    print(f"   Total console statements {'would be ' if dry_run else ''}removed: {total_changes}")
    print(f"{'=' * 60}\n")

    if dry_run:
        print("[TIP] Run without --dry-run to apply changes")

def main():
    parser = argparse.ArgumentParser(
        description='Remove console statements from JavaScript files for production'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )
    parser.add_argument(
        '--directory',
        default='techvernia.com/js',
        help='Directory to process (default: techvernia.com/js)'
    )
    parser.add_argument(
        '--no-backup',
        action='store_true',
        help='Do not create backup files'
    )

    args = parser.parse_args()

    directory = Path(args.directory)
    if not directory.exists():
        print(f"[ERROR] Directory not found: {directory}", file=sys.stderr)
        sys.exit(1)

    process_directory(
        directory,
        dry_run=args.dry_run,
        create_backup=not args.no_backup
    )

if __name__ == '__main__':
    main()
