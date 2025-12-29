#!/usr/bin/env python3
"""
Batch update certification HTML files with i18n support
"""

import re

# File configurations: (filename, cert_key, i18n_file, back_link)
FILES = [
    ("ansible-automation.html", "ansible", "ansible-automation-i18n.js", "ansible.html"),
    ("ansible-advanced.html", "ansibleAdvanced", "ansible-advanced-i18n.js", "ansible.html"),
    ("terraform-associate.html", "terraform", "terraform-associate-i18n.js", "terraform.html"),
    ("terraform-professional.html", "terraformPro", "terraform-professional-i18n.js", "terraform.html"),
    ("zabbix-specialist.html", "zabbixSpec", "zabbix-specialist-i18n.js", "zabbix.html"),
    ("zabbix-professional.html", "zabbixPro", "zabbix-professional-i18n.js", "zabbix.html"),
    ("zabbix-expert.html", "zabbixExp", "zabbix-expert-i18n.js", "zabbix.html"),
    ("rhce.html", "rhce", "rhce-i18n.js", "ansible.html"),
]

LANGUAGE_SELECTOR = '''        <!-- Language Selector -->
        <div class="language-selector" style="position:relative;">
            <button id="languageToggle" style="background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-lg);padding:var(--space-sm) var(--space-md);color:var(--text-primary);cursor:pointer;font-size:var(--text-sm);display:flex;align-items:center;gap:var(--space-sm);">
                <span id="currentLang">EN</span>
                <svg style="width:16px;height:16px;stroke:currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7"></path></svg>
            </button>
            <div id="languageDropdown" style="display:none;position:absolute;top:calc(100% + 8px);right:0;background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-lg);min-width:150px;box-shadow:var(--shadow-glow);z-index:1000;">
                <button class="lang-option" data-lang="en" style="width:100%;text-align:left;padding:var(--space-sm) var(--space-md);background:none;border:none;color:var(--text-primary);cursor:pointer;font-size:var(--text-sm);border-bottom:1px solid var(--border-color);">English (EN)</button>
                <button class="lang-option" data-lang="fr" style="width:100%;text-align:left;padding:var(--space-sm) var(--space-md);background:none;border:none;color:var(--text-primary);cursor:pointer;font-size:var(--text-sm);border-bottom:1px solid var(--border-color);">Français (FR)</button>
                <button class="lang-option" data-lang="de" style="width:100%;text-align:left;padding:var(--space-sm) var(--space-md);background:none;border:none;color:var(--text-primary);cursor:pointer;font-size:var(--text-sm);border-bottom:1px solid var(--border-color);">Deutsch (DE)</button>
                <button class="lang-option" data-lang="es" style="width:100%;text-align:left;padding:var(--space-sm) var(--space-md);background:none;border:none;color:var(--text-primary);cursor:pointer;font-size:var(--text-sm);border-bottom:1px solid var(--border-color);">Español (ES)</button>
                <button class="lang-option" data-lang="pt" style="width:100%;text-align:left;padding:var(--space-sm) var(--space-md);background:none;border:none;color:var(--text-primary);cursor:pointer;font-size:var(--text-sm);border-bottom:1px solid var(--border-color);">Português (PT)</button>
                <button class="lang-option" data-lang="zh" style="width:100%;text-align:left;padding:var(--space-sm) var(--space-md);background:none;border:none;color:var(--text-primary);cursor:pointer;font-size:var(--text-sm);border-bottom:1px solid var(--border-color);">中文 (ZH)</button>
                <button class="lang-option" data-lang="ja" style="width:100%;text-align:left;padding:var(--space-sm) var(--space-md);background:none;border:none;color:var(--text-primary);cursor:pointer;font-size:var(--text-sm);border-bottom:1px solid var(--border-color);">日本語 (JA)</button>
                <button class="lang-option" data-lang="ko" style="width:100%;text-align:left;padding:var(--space-sm) var(--space-md);background:none;border:none;color:var(--text-primary);cursor:pointer;font-size:var(--text-sm);border-bottom:1px solid var(--border-color);">한국어 (KO)</button>
                <button class="lang-option" data-lang="ar" style="width:100%;text-align:left;padding:var(--space-sm) var(--space-md);background:none;border:none;color:var(--text-primary);cursor:pointer;font-size:var(--text-sm);border-bottom:1px solid var(--border-color);">العربية (AR)</button>
                <button class="lang-option" data-lang="hi" style="width:100%;text-align:left;padding:var(--space-sm) var(--space-md);background:none;border:none;color:var(--text-primary);cursor:pointer;font-size:var(--text-sm);">हिन्दी (HI)</button>
            </div>
        </div>'''

SCRIPTS_TEMPLATE = '''<script>
    document.addEventListener('DOMContentLoaded', () => {{
        const toggle = document.getElementById('languageToggle');
        const dropdown = document.getElementById('languageDropdown');
        const langOptions = document.querySelectorAll('.lang-option');

        toggle?.addEventListener('click', () => {{
            dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
        }});

        langOptions.forEach(option => {{
            option.addEventListener('click', () => {{
                const lang = option.getAttribute('data-lang');
                document.getElementById('currentLang').textContent = lang.toUpperCase();
                dropdown.style.display = 'none';
                if (window.i18n?.setLanguage) {{
                    window.i18n.setLanguage(lang);
                }}
            }});
        }});

        document.addEventListener('click', (e) => {{
            if (!e.target.closest('.language-selector')) {{
                dropdown.style.display = 'none';
            }}
        }});
    }});
</script>

<script src="../../js/i18n.js?v=20251227h"></script>
<script src="../../js/complete-translate.js"></script>
<script src="../../js/{i18n_file}?v=20251227h"></script>

</body>
</html>'''

def update_file(filepath, cert_key, i18n_file, back_link):
    """Update a single certification HTML file"""
    print(f"Updating {filepath}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Update navbar
    # Replace old navbar with new one including language selector
    old_navbar_pattern = r'<nav class="navbar">.*?</nav>'
    new_navbar = f'''<nav class="navbar">
    <div class="container" style="display:flex;justify-content:space-between;align-items:center;">
        <a href="../../reviews/networking/{back_link}" data-i18n="nav.back_to_review">← Back to Review</a>

{LANGUAGE_SELECTOR}
    </div>
</nav>'''

    content = re.sub(old_navbar_pattern, new_navbar, content, flags=re.DOTALL)

    # Step 2: Add data-i18n attributes
    # H1 title
    content = re.sub(r'<h1>([^<]+)</h1>',
                    f'<h1 data-i18n="cert.{cert_key}.title">\\1</h1>', content)

    # Cert level
    content = re.sub(r'<div class="cert-level">([^<]+)</div>',
                    f'<div class="cert-level" data-i18n="cert.{cert_key}.level">\\1</div>', content)

    # Description paragraph
    content = re.sub(r'(<p style="max-width:800px[^>]*>)([^<]+)(</p>)',
                    f'\\1<span data-i18n="cert.{cert_key}.description">\\2</span>\\3', content, count=1)

    # Meta items
    content = re.sub(r'(<span>)(Exam:[^<]+)(</span>)',
                    f'<span data-i18n="cert.{cert_key}.exam_code_value">\\2</span>', content, count=1)
    content = re.sub(r'(<span>)(\d+ min)(</span>)',
                    f'<span data-i18n="cert.{cert_key}.duration_value">\\2</span>', content, count=1)
    content = re.sub(r'(<span>)(\$\d+)(</span>)',
                    f'<span data-i18n="cert.{cert_key}.cost_value">\\2</span>', content, count=1)
    content = re.sub(r'(<span>)(Valid:[^<]+)(</span>)',
                    f'<span data-i18n="cert.{cert_key}.validity_value">\\2</span>', content, count=1)

    # Section headings
    content = re.sub(r'(>\s*)Overview(\s*</h2>)',
                    f'>      <span data-i18n="cert.overview">Overview</span>\\2', content, count=1)
    content = re.sub(r'(>\s*)Key Topics Covered(\s*</h2>)',
                    f'>            <span data-i18n="cert.key_topics">Key Topics Covered</span>\\2', content, count=1)
    content = re.sub(r'(>\s*)Exam Information(\s*</h2>)',
                    f'>            <span data-i18n="cert.exam_info">Exam Information</span>\\2', content, count=1)
    content = re.sub(r'(>\s*)Study Resources(\s*</h2>)',
                    f'>            <span data-i18n="cert.study_resources">Study Resources</span>\\2', content, count=1)
    content = re.sub(r'(>\s*)Next Steps(\s*</h2>)',
                    f'>            <span data-i18n="cert.next_steps">Next Steps</span>\\2', content, count=1)

    # Overview section paragraphs
    overview_section = re.search(r'(<h2>.*?Overview.*?</h2>)(.*?)(</section>)', content, re.DOTALL)
    if overview_section:
        section_content = overview_section.group(2)
        # First p tag
        section_content = re.sub(r'<p>([^<]+)</p>',
                                f'<p data-i18n="cert.{cert_key}.overview_text">\\1</p>', section_content, count=1)
        # Second p tag
        section_content = re.sub(r'<p>([^<]+)</p>',
                                f'<p data-i18n="cert.{cert_key}.expertise">\\1</p>', section_content, count=1)
        content = content.replace(overview_section.group(2), section_content)

    # Key Topics section
    topics_section = re.search(r'(<h2>.*?Key Topics.*?</h2>)(.*?)(</section>)', content, re.DOTALL)
    if topics_section:
        section_content = topics_section.group(2)
        section_content = re.sub(r'<p>([^<]+)</p>',
                                f'<p data-i18n="cert.{cert_key}.topics_intro">\\1</p>', section_content, count=1)
        content = content.replace(topics_section.group(2), section_content)

    # Exam Information cards
    content = re.sub(r'<h4>Exam Code</h4>',
                    f'<h4 data-i18n="cert.exam_code">Exam Code</h4>', content)
    content = re.sub(r'<h4>Duration</h4>',
                    f'<h4 data-i18n="cert.duration">Duration</h4>', content)
    content = re.sub(r'<h4>Exam Cost</h4>',
                    f'<h4 data-i18n="cert.cost">Exam Cost</h4>', content)
    content = re.sub(r'<h4>Validity</h4>',
                    f'<h4 data-i18n="cert.validity">Validity</h4>', content)

    # Exam info card values
    exam_info_section = re.search(r'(<h2>.*?Exam Information.*?</h2>)(.*?)(</section>)', content, re.DOTALL)
    if exam_info_section:
        section_content = exam_info_section.group(2)
        section_content = re.sub(r'(<div class="value">)([^<]+)(</div>)',
                                lambda m: f'{m.group(1)}<span data-i18n="cert.{cert_key}.{determine_value_key(m.group(2))}">{m.group(2)}</span>{m.group(3)}',
                                section_content)
        content = content.replace(exam_info_section.group(2), section_content)

    # Study Resources section
    resources_section = re.search(r'(<h2>.*?Study Resources.*?</h2>)(.*?)(</section>)', content, re.DOTALL)
    if resources_section:
        section_content = resources_section.group(2)
        section_content = re.sub(r'(<p>)([^<]+)(</p>)',
                                f'\\1<span data-i18n="cert.resources_intro">\\2</span>\\3', section_content, count=1)
        section_content = re.sub(r'<li>Official[^<]+</li>',
                                '<li data-i18n="cert.official_training">Official Training Courses</li>', section_content, count=1)
        section_content = re.sub(r'<li>Practice[^<]+</li>',
                                '<li data-i18n="cert.practice_exams">Practice Exams and Labs</li>', section_content, count=1)
        section_content = re.sub(r'<li>Study[^<]+</li>',
                                '<li data-i18n="cert.study_guides">Study Guides and Documentation</li>', section_content, count=1)
        content = content.replace(resources_section.group(2), section_content)

    # Next Steps section
    next_section = re.search(r'(<h2>.*?Next Steps.*?</h2>)(.*?)(</section>)', content, re.DOTALL)
    if next_section:
        section_content = next_section.group(2)
        section_content = re.sub(r'(<div class="highlight-box">.*?<p>)([^<]+)(</p>)',
                                f'\\1<span data-i18n="cert.ready">\\2</span>\\3', section_content, flags=re.DOTALL, count=1)
        section_content = re.sub(r'(<p style="margin-top:var\(--space-xl\)">)([^<]+)(</p>)',
                                f'\\1<span data-i18n="cert.visit_portal">\\2</span>\\3', section_content, count=1)
        content = content.replace(next_section.group(2), section_content)

    # Footer
    content = re.sub(r'(<p>)(&copy; 2025[^<]+)(</p>)',
                    f'\\1<span data-i18n="footer.copyright">\\2</span>\\3', content, count=1)
    content = re.sub(r'(<p style="margin-top:var\(--space-sm\)">)([^<]+)(</p>)',
                    f'\\1<span data-i18n="footer.trademark">\\2</span>\\3', content, count=1)

    # Step 3: Add scripts before </body>
    # Remove existing </body></html> and replace with scripts
    content = re.sub(r'</body>\s*</html>\s*$', SCRIPTS_TEMPLATE.format(i18n_file=i18n_file), content)

    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"[OK] Updated {filepath}")

def determine_value_key(value):
    """Determine the i18n key based on value content"""
    value = value.strip()
    if value.startswith('Exam:') or 'ANSIBLE' in value.upper() or 'TERRAFORM' in value.upper() or 'ZABBIX' in value.upper() or 'EX294' in value or 'RHCE' in value or 'ZCS' in value or 'ZCP' in value or 'ZCE' in value:
        return 'exam_code_value'
    elif 'min' in value or 'hour' in value:
        return 'duration_value'
    elif '$' in value:
        return 'cost_value'
    elif 'Valid' in value or 'year' in value:
        return 'validity_value'
    else:
        return 'exam_code_value'  # default

if __name__ == '__main__':
    import os
    import sys

    # Set console encoding to UTF-8
    if sys.platform.startswith('win'):
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

    os.chdir(r'C:\Users\Freddy\Desktop\GeniusNet.ai\GenuisNet.ai\pages\certifications')

    for filename, cert_key, i18n_file, back_link in FILES:
        try:
            update_file(filename, cert_key, i18n_file, back_link)
        except Exception as e:
            print(f"ERROR updating {filename}: {e}")
            import traceback
            traceback.print_exc()

    print("\n[DONE] All files processed successfully!")
