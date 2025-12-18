#!/usr/bin/env python3
"""
Fix closing tags for converted cards
"""

from pathlib import Path

file_path = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0

while i < len(lines):
    line = lines[i]

    # Si on trouve un <a href="guides/...class="guide-card">
    if '<a href="guides/' in line and 'class="guide-card"' in line:
        new_lines.append(line)
        i += 1

        # Compter la profondeur des divs
        depth = 0
        while i < len(lines):
            current = lines[i]

            # Compter les <div> et </div>
            depth += current.count('<div')
            depth -= current.count('</div>')

            # Si on trouve </div> et que depth == -1, c'est la fermeture de notre carte
            if '</div>' in current and depth == -1:
                # Remplacer la dernière occurrence de </div> par </a>
                new_lines.append(current.replace('</div>', '</a>', 1))
                i += 1
                break
            else:
                new_lines.append(current)
                i += 1
    else:
        new_lines.append(line)
        i += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("✅ Tags de fermeture corrigés")
