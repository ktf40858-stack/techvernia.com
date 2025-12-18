#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

# Chemin des reviews
reviews_path = '/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/reviews/networking/'

# Configurations pour chaque outil
certifications_config = {
    'juniper-mist.html': {
        'intro': 'To maximize the value of Juniper Mist AI and advance your wireless networking career, consider these industry-recognized Juniper certifications. Each credential validates specific skills for implementing and managing AI-driven wireless networks.',
        'certs': [
            {
                'name': 'JNCIA-MistAI',
                'level': 'Associate Level',
                'badge': 'jncia-mistai.png',
                'description': 'Foundational understanding of WLAN and Mist AI technology, features, and functionality.',
                'exam': 'JN0-452',
                'link': '#'
            },
            {
                'name': 'JNCIS-MistAI Wireless',
                'level': 'Specialist Level',
                'badge': 'jncia-mistai.png',
                'description': 'Advanced wireless implementation with Mist AI, including troubleshooting and optimization.',
                'exam': 'JN0-1452',
                'link': '#'
            },
            {
                'name': 'JNCIP-MistAI',
                'level': 'Professional Level',
                'badge': 'jncia-mistai.png',
                'description': 'Professional-level expertise in complex Mist AI deployments and integrations.',
                'exam': 'JN0-2452',
                'link': '#'
            }
        ]
    },
    'ansible.html': {
        'intro': 'To excel in network automation with Ansible and advance your DevOps career, pursue these Red Hat certifications. Each validates critical automation and infrastructure-as-code skills.',
        'certs': [
            {
                'name': 'Red Hat Ansible Automation',
                'level': 'Specialist Level',
                'badge': 'ansible-automation.png',
                'description': 'Automate management and deployment of systems in enterprise environments using Ansible.',
                'exam': 'EX407',
                'link': '#'
            },
            {
                'name': 'RHCE (Red Hat Certified Engineer)',
                'level': 'Professional Level',
                'badge': 'ansible-automation.png',
                'description': 'Advanced skills in automation, including Ansible Playbooks and system administration.',
                'exam': 'EX294',
                'link': '#'
            },
            {
                'name': 'Advanced Ansible Automation',
                'level': 'Advanced Level',
                'badge': 'ansible-automation.png',
                'description': 'Best practices for automating large or complex networks with Ansible Automation Platform.',
                'exam': 'EX447',
                'link': '#'
            }
        ]
    },
    'terraform.html': {
        'intro': 'To demonstrate proficiency in infrastructure-as-code and cloud automation with Terraform, consider these HashiCorp certifications. They validate your ability to provision and manage infrastructure efficiently.',
        'certs': [
            {
                'name': 'Terraform Associate',
                'level': 'Associate Level',
                'badge': 'terraform-associate.png',
                'description': 'Foundational knowledge of Terraform concepts, workflows, and multi-cloud infrastructure provisioning.',
                'exam': '003',
                'link': '#'
            },
            {
                'name': 'Terraform Professional',
                'level': 'Professional Level',
                'badge': 'terraform-associate.png',
                'description': 'Advanced Terraform patterns, enterprise-scale deployments, and complex state management.',
                'exam': 'Coming 2026',
                'link': '#'
            }
        ]
    },
    'splunk.html': {
        'intro': 'To leverage Splunk for IT operations and security analytics, pursue these official Splunk certifications. Each validates skills in data analysis, monitoring, and enterprise deployment.',
        'certs': [
            {
                'name': 'Splunk Core Certified User',
                'level': 'User Level',
                'badge': 'splunk-core-user.png',
                'description': 'Search, use fields, create alerts, lookups, and build basic reports and dashboards.',
                'exam': 'SPLK-1001',
                'link': '#'
            },
            {
                'name': 'Splunk Core Certified Power User',
                'level': 'Power User Level',
                'badge': 'splunk-core-user.png',
                'description': 'Advanced searching, reporting, and correlation techniques for complex data analysis.',
                'exam': 'SPLK-1002',
                'link': '#'
            },
            {
                'name': 'Splunk Enterprise Admin',
                'level': 'Administrator Level',
                'badge': 'splunk-core-user.png',
                'description': 'Install, configure, and manage Splunk Enterprise environments at scale.',
                'exam': 'SPLK-1003',
                'link': '#'
            },
            {
                'name': 'Splunk Enterprise Architect',
                'level': 'Architect Level',
                'badge': 'splunk-core-user.png',
                'description': 'Design and deploy large-scale Splunk environments with high availability and performance.',
                'exam': 'SPLK-2002',
                'link': '#'
            }
        ]
    },
    'zabbix.html': {
        'intro': 'To master Zabbix monitoring and advance your infrastructure monitoring career, consider these official Zabbix certifications. They demonstrate expertise in enterprise monitoring solutions.',
        'certs': [
            {
                'name': 'Zabbix Certified Specialist',
                'level': 'Specialist Level',
                'badge': 'zabbix-certified.png',
                'description': 'Core monitoring capabilities, template creation, triggers, and basic troubleshooting.',
                'exam': 'ZCS 7.0',
                'link': '#'
            },
            {
                'name': 'Zabbix Certified Professional',
                'level': 'Professional Level',
                'badge': 'zabbix-certified.png',
                'description': 'Advanced monitoring techniques, distributed monitoring, and enterprise-scale deployments.',
                'exam': 'ZCP 7.0',
                'link': '#'
            },
            {
                'name': 'Zabbix Certified Expert',
                'level': 'Expert Level',
                'badge': 'zabbix-certified.png',
                'description': 'Expert-level mastery of Zabbix architecture, optimization, and complex integrations.',
                'exam': 'ZCE 7.0',
                'link': '#'
            }
        ]
    }
}

def create_cert_section(config):
    """Génère le HTML pour la section de certifications"""
    intro = config['intro']
    certs = config['certs']

    # Générer les cartes de certifications
    cert_cards = ''
    for cert in certs:
        cert_cards += f'''
<a href="{cert['link']}" class="cert-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: var(--space-lg); transition: all 0.3s ease; text-decoration: none; display: block; cursor: pointer;">
<div style="text-align: center; margin-bottom: var(--space-md);">
<img src="../../../assets/images/certifications/{cert['badge']}" alt="{cert['name']} Badge" style="width: 100px; height: 100px; object-fit: contain;"/>
</div>
<h3 style="margin-bottom: var(--space-xs); color: var(--text-primary); font-size: var(--text-lg);">{cert['name']}</h3>
<div style="color: var(--accent-color); font-weight: 600; font-size: var(--text-sm); margin-bottom: var(--space-sm);">{cert['level']}</div>
<p style="color: var(--text-secondary); font-size: var(--text-sm); line-height: 1.5;">{cert['description']}</p>
<div style="margin-top: var(--space-md); padding-top: var(--space-md); border-top: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
<span style="color: var(--text-tertiary); font-size: var(--text-xs);">Exam: {cert['exam']}</span>
<span style="color: var(--accent-color); font-size: var(--text-sm); font-weight: 600;">Learn More →</span>
</div>
</a>
'''

    # Template de la section complète
    section = f'''<section class="review-section" id="certifications">
<h2><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 15l-2 2-2-2m4-6l2-2 2 2m-4 4V3m0 18v-6"/><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 12h8"/></svg> Recommended Certifications</h2>
<p style="margin-bottom: var(--space-xl); color: var(--text-secondary);">{intro}</p>

<div class="certifications-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-lg); margin: var(--space-xl) 0; position: relative; z-index: 100;">
{cert_cards}
</div>

<style>
/* Certification Cards Styles */
.certifications-grid {{
    position: relative;
    z-index: 100 !important;
}}

.cert-card {{
    position: relative;
    overflow: hidden;
    z-index: 101 !important;
}}

.cert-card:hover {{
    transform: translateY(-5px);
    border-color: var(--accent-color);
    box-shadow: 0 10px 30px rgba(4, 159, 217, 0.2);
    z-index: 102 !important;
}}

.cert-card::before {{
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(4, 159, 217, 0.1), transparent);
    transition: left 0.5s;
    pointer-events: none !important;
    z-index: -1;
}}

.cert-card:hover::before {{
    left: 100%;
}}
</style>

</section>
'''

    return section

# Traiter chaque fichier
for filename, config in certifications_config.items():
    filepath = os.path.join(reviews_path, filename)

    if not os.path.exists(filepath):
        print(f'❌ {filename} - Fichier non trouvé')
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Vérifier si la section existe déjà
    if 'id="certifications"' in content or 'Recommended Certifications' in content:
        print(f'✓ {filename} - Section déjà présente')
        continue

    # Trouver la section "Final Verdict" pour insérer avant
    verdict_pattern = r'<section class="review-section" id="verdict">'

    if verdict_pattern in content:
        # Créer la section de certifications
        cert_section = create_cert_section(config)

        # Insérer avant verdict
        content = content.replace(
            '<section class="review-section" id="verdict">',
            cert_section + '\n<section class="review-section" id="verdict">'
        )

        # Sauvegarder
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f'✅ {filename} - Section ajoutée ({len(config["certs"])} certifications)')
    else:
        print(f'⚠️  {filename} - Section verdict non trouvée')

print('\n✅ Toutes les sections de certifications ont été ajoutées!')
