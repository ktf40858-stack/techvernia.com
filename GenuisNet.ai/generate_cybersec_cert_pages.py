#!/usr/bin/env python3
"""
Génère toutes les pages de certification individuelles pour Cybersecurity
+ Met à jour les pages de review pour rendre les certifications cliquables
"""

import os
import re
from pathlib import Path

# Données complètes des certifications cybersecurity
CERTIFICATIONS_DATA = {
    'fortinet-nse4': {
        'name': 'NSE 4 - FortiGate Security',
        'full_name': 'Fortinet Network Security Expert 4',
        'level': 'Professional Level',
        'vendor': 'Fortinet',
        'brand_color': '#EE3124',
        'badge': 'fortinet-nse4.png',
        'exam_code': 'NSE4_FGT-7.2',
        'duration': '120 minutes',
        'cost': '$400 USD',
        'validity': '2 years',
        'rating': '7',
        'description': 'The Fortinet NSE 4 certification validates your ability to deploy, configure, and manage FortiGate devices. This professional-level certification is the most popular in the NSE program and is essential for firewall administrators.',
        'topics': [
            'FortiGate initial configuration and system settings',
            'Security policies and NAT',
            'Firewall authentication and user management',
            'SSL VPN and IPsec VPN configuration',
            'High availability (HA) and clustering',
            'Web filtering and application control',
            'Antivirus and IPS configuration',
            'Logging, monitoring, and troubleshooting'
        ],
        'exam_format': 'Multiple choice and scenario-based questions',
        'prerequisites': 'None required (NSE 1-3 recommended)',
        'resources': [
            'Official Fortinet Training Course (NSE 4)',
            'FortiGate Administration Study Guide',
            'FortiGate hands-on labs',
            'Practice exams from Fortinet',
            'Community forums and study groups'
        ],
        'careers': [
            'Network Security Administrator',
            'Firewall Administrator',
            'Security Engineer',
            'NOC Engineer',
            'Systems Administrator'
        ],
        'salary': '$80,000 - $120,000 USD annually',
        'next_steps': 'After NSE 4, pursue NSE 5 for FortiAnalyzer or FortiManager specialization, or NSE 7 for enterprise-level expertise.',
        'vendor_url': 'https://training.fortinet.com'
    },

    'fortinet-nse7': {
        'name': 'NSE 7 - Enterprise Firewall',
        'full_name': 'Fortinet Network Security Expert 7 - Enterprise Firewall',
        'level': 'Expert Level',
        'vendor': 'Fortinet',
        'brand_color': '#EE3124',
        'badge': 'fortinet-nse7.png',
        'exam_code': 'NSE7_EFW-7.2',
        'duration': '150 minutes',
        'cost': '$400 USD',
        'validity': '2 years',
        'rating': '8',
        'description': 'NSE 7 Enterprise Firewall demonstrates expert-level knowledge in designing and deploying complex FortiGate solutions for large enterprises. This certification validates advanced routing, high availability, and troubleshooting skills.',
        'topics': [
            'Advanced routing (OSPF, BGP, route maps)',
            'FortiGate high availability clusters',
            'Virtual domains (VDOMs) configuration',
            'Advanced VPN topologies',
            'Security Fabric integration',
            'Performance optimization',
            'Advanced troubleshooting techniques',
            'Enterprise deployment best practices'
        ],
        'exam_format': 'Advanced scenario-based questions and troubleshooting',
        'prerequisites': 'NSE 4 FortiGate Security required',
        'resources': [
            'Fortinet NSE 7 Official Training',
            'Enterprise Firewall Lab Guide',
            'FortiGate Cookbook',
            'Advanced troubleshooting workshops',
            'Fortinet TAC case studies'
        ],
        'careers': [
            'Senior Security Engineer',
            'Network Architect',
            'Security Consultant',
            'Technical Lead - Security',
            'Principal Network Engineer'
        ],
        'salary': '$110,000 - $160,000 USD annually',
        'next_steps': 'Pursue NSE 8 for the highest level of Fortinet expertise, demonstrating mastery of security architecture.',
        'vendor_url': 'https://training.fortinet.com'
    },

    'paloalto-pcnsa': {
        'name': 'PCNSA',
        'full_name': 'Palo Alto Networks Certified Network Security Administrator',
        'level': 'Administrator Level',
        'vendor': 'Palo Alto Networks',
        'brand_color': '#FA582D',
        'badge': 'paloalto-pcnsa.png',
        'exam_code': 'PCNSA',
        'duration': '80 minutes',
        'cost': '$200 USD',
        'validity': '2 years',
        'rating': '8',
        'description': 'The PCNSA certification validates your ability to configure, manage, and monitor Palo Alto Networks next-generation firewalls. Essential for NGFW administrators working with PAN-OS.',
        'topics': [
            'PAN-OS initial configuration',
            'Interface types and zones',
            'Security policies and NAT',
            'App-ID and Content-ID',
            'SSL decryption',
            'GlobalProtect VPN',
            'User-ID and authentication',
            'Monitoring and reporting'
        ],
        'exam_format': 'Multiple choice, 70 questions, 80% passing score',
        'prerequisites': 'None (PCCET recommended for beginners)',
        'resources': [
            'Palo Alto Networks Education Services courses',
            'Configuration and Management (EDU-210) course',
            'Hands-on labs with virtual firewall',
            'Official study guide',
            'Practice exams'
        ],
        'careers': [
            'Network Security Administrator',
            'Firewall Administrator',
            'Security Operations Analyst',
            'Network Engineer',
            'SOC Analyst'
        ],
        'salary': '$85,000 - $125,000 USD annually',
        'next_steps': 'Advance to PCNSE for engineer-level expertise in Palo Alto Networks firewalls.',
        'vendor_url': 'https://www.paloaltonetworks.com/services/education'
    },

    'paloalto-pcnse': {
        'name': 'PCNSE',
        'full_name': 'Palo Alto Networks Certified Network Security Engineer',
        'level': 'Engineer Level',
        'vendor': 'Palo Alto Networks',
        'brand_color': '#FA582D',
        'badge': 'paloalto-pcnse.png',
        'exam_code': 'PCNSE',
        'duration': '90 minutes',
        'cost': '$250 USD',
        'validity': '2 years',
        'rating': '9',
        'description': 'PCNSE validates advanced skills in deploying, configuring, and troubleshooting Palo Alto Networks NGFWs. This engineer-level certification is highly respected in the industry.',
        'topics': [
            'Advanced security policies',
            'Decryption and certificates',
            'Advanced VPN configuration',
            'High availability and clustering',
            'Quality of Service (QoS)',
            'Advanced troubleshooting',
            'Panorama centralized management',
            'Performance optimization'
        ],
        'exam_format': 'Scenario-based questions, 75 questions, 70% passing',
        'prerequisites': 'PCNSA strongly recommended, 6-12 months experience',
        'resources': [
            'Firewall Essentials: Configuration and Management (EDU-210)',
            'Firewall: Troubleshooting (EDU-330)',
            'Official PCNSE study guide',
            'Lab topology practice',
            'Palo Alto Live Community'
        ],
        'careers': [
            'Senior Security Engineer',
            'Network Security Architect',
            'Security Consultant',
            'Lead Network Engineer',
            'Solutions Architect'
        ],
        'salary': '$120,000 - $170,000 USD annually',
        'next_steps': 'Specialize in PCCSA/PCCSE for SOC operations or PCSAE for security automation.',
        'vendor_url': 'https://www.paloaltonetworks.com/services/education'
    },

    'microsoft-sc200': {
        'name': 'SC-200',
        'full_name': 'Microsoft Security Operations Analyst',
        'level': 'Associate Level',
        'vendor': 'Microsoft',
        'brand_color': '#00A4EF',
        'badge': 'microsoft-sc200.png',
        'exam_code': 'SC-200',
        'duration': '120 minutes',
        'cost': '$165 USD',
        'validity': '1 year',
        'rating': '8',
        'description': 'SC-200 validates your ability to investigate, respond to, and hunt for threats using Microsoft Sentinel, Defender XDR, and threat intelligence. Essential for SOC analysts.',
        'topics': [
            'Microsoft Sentinel workspace configuration',
            'Data connectors and log analytics',
            'KQL queries for threat hunting',
            'Incident investigation and response',
            'Microsoft Defender for Endpoint',
            'Microsoft Defender for Cloud',
            'Threat intelligence integration',
            'Automation and orchestration'
        ],
        'exam_format': 'Multiple choice, case studies, and drag-and-drop',
        'prerequisites': 'None (Azure and security fundamentals helpful)',
        'resources': [
            'Microsoft Learn SC-200 learning path',
            'SC-200 official study guide',
            'Microsoft Sentinel workshop',
            'KQL query practice',
            'Microsoft security community'
        ],
        'careers': [
            'Security Operations Analyst',
            'SOC Analyst',
            'Threat Hunter',
            'Incident Responder',
            'Security Engineer'
        ],
        'salary': '$75,000 - $110,000 USD annually',
        'next_steps': 'Combine with SC-300 (Identity) or SC-400 (Information Protection) for broader security expertise.',
        'vendor_url': 'https://learn.microsoft.com/certifications'
    },

    'crowdstrike-ccfa': {
        'name': 'CCFA',
        'full_name': 'CrowdStrike Certified Falcon Administrator',
        'level': 'Administrator Level',
        'vendor': 'CrowdStrike',
        'brand_color': '#E01F3D',
        'badge': 'crowdstrike-ccfa.png',
        'exam_code': 'CCFA',
        'duration': '16 hours training + exam',
        'cost': 'Contact Sales',
        'validity': '2 years',
        'rating': '7',
        'description': 'CCFA certifies your ability to configure and manage the CrowdStrike Falcon platform, including prevention policies, detection configuration, and response actions.',
        'topics': [
            'Falcon platform architecture',
            'Host management and sensor deployment',
            'Prevention policy configuration',
            'Detection and response workflows',
            'Falcon X threat intelligence',
            'User and role management',
            'Dashboard and reporting',
            'Integration with SIEM and SOAR'
        ],
        'exam_format': 'Online proctored exam with practical scenarios',
        'prerequisites': 'CrowdStrike Falcon access recommended',
        'resources': [
            'CrowdStrike University courses',
            'Falcon Administrator Guide',
            'Platform documentation',
            'CrowdStrike community forums',
            'Official training labs'
        ],
        'careers': [
            'Endpoint Security Administrator',
            'SOC Analyst',
            'Security Operations Engineer',
            'Incident Response Analyst',
            'Security Administrator'
        ],
        'salary': '$80,000 - $115,000 USD annually',
        'next_steps': 'Advance to CCFR (Responder) or CCFH (Hunter) for specialized threat hunting and incident response skills.',
        'vendor_url': 'https://www.crowdstrike.com/university/'
    },
}

# Template HTML (utilise le template CCNA comme base)
def create_cert_page_html(cert_data):
    """Génère le HTML complet pour une page de certification"""

    brand_rgb = hex_to_rgb(cert_data['brand_color'])
    brand_dark = darken_color(cert_data['brand_color'])

    topics_html = '\n            '.join([f'<li>{topic}</li>' for topic in cert_data['topics']])
    resources_html = '\n            '.join([f'<li>{resource}</li>' for resource in cert_data['resources']])
    careers_html = '\n            '.join([f'<li>{career}</li>' for career in cert_data['careers']])

    overview_paragraphs = f"""<p>{cert_data['description']}</p>
<p>This certification is designed for security professionals who need to demonstrate proficiency with {cert_data['vendor']} security solutions. It validates both theoretical knowledge and practical skills required in real-world security operations.</p>
<p>Earning this certification demonstrates your commitment to staying current with modern cybersecurity technologies and best practices.</p>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>{cert_data['name']} - Complete Guide & Review | GenuisNet.ai</title>
    <meta content="{cert_data['description']}" name="description"/>
    <link href="../../assets/css/styles.css" rel="stylesheet"/>
    <link href="../../assets/images/favicon.png" rel="icon" type="image/png"/>
    <style>
        :root {{
            --bg-primary: #0a0e27;
            --bg-secondary: #111530;
            --bg-card: #1a1f3a;
            --text-primary: #e2e8f0;
            --text-secondary: #94a3b8;
            --text-tertiary: #64748b;
            --accent-color: {cert_data['brand_color']};
            --accent-hover: {brand_dark};
            --border-color: rgba(148, 163, 184, 0.1);
            --space-xs: 0.25rem;
            --space-sm: 0.5rem;
            --space-md: 1rem;
            --space-lg: 1.5rem;
            --space-xl: 2rem;
            --space-2xl: 3rem;
            --space-3xl: 4rem;
            --space-4xl: 6rem;
            --text-xs: 0.75rem;
            --text-sm: 0.875rem;
            --text-base: 1rem;
            --text-lg: 1.125rem;
            --text-xl: 1.25rem;
            --text-2xl: 1.5rem;
            --text-3xl: 1.875rem;
            --text-4xl: 2.25rem;
            --radius-sm: 0.25rem;
            --radius-md: 0.5rem;
            --radius-lg: 0.75rem;
            --radius-xl: 1rem;
        }}

        [data-theme="light"] {{
            --bg-primary: #f8fafc;
            --bg-secondary: #f1f5f9;
            --bg-card: #ffffff;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --text-tertiary: #64748b;
            --border-color: rgba(15, 23, 42, 0.1);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
            overflow-x: hidden;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 var(--space-lg);
        }}

        .cert-hero {{
            padding: calc(80px + var(--space-4xl)) var(--space-lg) var(--space-3xl);
            background: linear-gradient(135deg, rgba({brand_rgb}, 0.1) 0%, rgba({brand_rgb}, 0.05) 100%);
            text-align: center;
        }}

        .cert-badge {{
            width: 180px;
            height: 180px;
            margin: 0 auto var(--space-xl);
        }}

        .cert-badge img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
        }}

        .cert-hero h1 {{
            font-size: clamp(var(--text-2xl), 5vw, var(--text-4xl));
            font-weight: 800;
            margin-bottom: var(--space-sm);
        }}

        .cert-level {{
            color: var(--accent-color);
            font-size: var(--text-xl);
            font-weight: 600;
            margin-bottom: var(--space-lg);
        }}

        .cert-meta {{
            display: flex;
            gap: var(--space-xl);
            justify-content: center;
            flex-wrap: wrap;
            margin-top: var(--space-lg);
        }}

        .meta-item {{
            display: flex;
            align-items: center;
            gap: var(--space-xs);
            color: var(--text-secondary);
            font-size: var(--text-sm);
        }}

        .review-section {{
            padding: var(--space-3xl) 0;
            border-bottom: 1px solid var(--border-color);
        }}

        .review-section h2 {{
            display: flex;
            align-items: center;
            gap: var(--space-md);
            font-size: var(--text-2xl);
            margin-bottom: var(--space-xl);
            color: var(--text-primary);
        }}

        .review-section h3 {{
            font-size: var(--text-xl);
            margin: var(--space-xl) 0 var(--space-md);
            color: var(--text-primary);
        }}

        .review-section p {{
            color: var(--text-secondary);
            line-height: 1.8;
            margin-bottom: var(--space-md);
        }}

        .review-section ul {{
            list-style: none;
            padding: 0;
        }}

        .review-section ul li {{
            padding: var(--space-sm) 0;
            padding-left: var(--space-lg);
            color: var(--text-secondary);
            position: relative;
        }}

        .review-section ul li:before {{
            content: "▹";
            position: absolute;
            left: 0;
            color: var(--accent-color);
            font-weight: bold;
        }}

        .info-box {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: var(--space-xl);
            margin: var(--space-xl) 0;
        }}

        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: var(--space-lg);
            margin: var(--space-xl) 0;
        }}

        .info-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: var(--space-lg);
        }}

        .info-card h4 {{
            color: var(--accent-color);
            font-size: var(--text-sm);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: var(--space-sm);
        }}

        .info-card .value {{
            color: var(--text-primary);
            font-size: var(--text-xl);
            font-weight: 700;
        }}

        .highlight-box {{
            background: linear-gradient(135deg, rgba({brand_rgb}, 0.05) 0%, rgba({brand_rgb}, 0.02) 100%);
            border-radius: var(--radius-lg);
            border-left: 4px solid var(--accent-color);
            padding: var(--space-xl);
            margin: var(--space-xl) 0;
        }}

        .neon-icon {{
            width: 24px;
            height: 24px;
            stroke: var(--accent-color);
        }}

        .navbar {{
            position: fixed;
            top: 0;
            width: 100%;
            background: var(--bg-secondary);
            z-index: 1000;
            padding: var(--space-md) 0;
            border-bottom: 1px solid var(--border-color);
        }}

        @media (max-width: 768px) {{
            .cert-meta {{
                flex-direction: column;
                gap: var(--space-md);
            }}

            .info-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
<nav class="navbar">
    <div class="container">
        <a href="../../index.html" style="color: var(--accent-color); text-decoration: none; font-weight: 700; font-size: var(--text-lg);">← Back to GenuisNet.ai</a>
    </div>
</nav>

<header class="cert-hero">
    <div class="container">
        <div class="cert-badge">
            <img src="../../assets/images/certifications/{cert_data['badge']}" alt="{cert_data['name']} Badge"/>
        </div>
        <h1>{cert_data['full_name']}</h1>
        <div class="cert-level">{cert_data['level']}</div>
        <p style="max-width: 800px; margin: 0 auto; color: var(--text-secondary); font-size: var(--text-lg);">{cert_data['description']}</p>

        <div class="cert-meta">
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <span>Exam: {cert_data['exam_code']}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
                </svg>
                <span>{cert_data['duration']}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <line x1="12" x2="12" y1="1" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"></path>
                </svg>
                <span>{cert_data['cost']}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                </svg>
                <span>4.{cert_data['rating']}/5 Rating</span>
            </div>
        </div>
    </div>
</header>

<main class="container">
    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                <rect height="4" rx="1" ry="1" width="8" x="8" y="2"></rect>
            </svg>
            Overview
        </h2>
        {overview_paragraphs}
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
            </svg>
            Key Topics Covered
        </h2>
        <p>The {cert_data['name']} exam covers the following topics:</p>
        <ul>
            {topics_html}
        </ul>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
                <line x1="12" x2="12.01" y1="17" y2="17"></line>
            </svg>
            Why This Certification Matters
        </h2>
        <div class="highlight-box">
            <p>This certification validates your expertise with {cert_data['vendor']} security technologies, which are widely deployed in enterprise environments. Holding this credential demonstrates your commitment to cybersecurity excellence and opens doors to advanced career opportunities.</p>
        </div>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            Exam Information
        </h2>

        <div class="info-grid">
            <div class="info-card">
                <h4>Exam Code</h4>
                <div class="value">{cert_data['exam_code']}</div>
            </div>
            <div class="info-card">
                <h4>Duration</h4>
                <div class="value">{cert_data['duration']}</div>
            </div>
            <div class="info-card">
                <h4>Exam Cost</h4>
                <div class="value">{cert_data['cost']}</div>
            </div>
            <div class="info-card">
                <h4>Validity Period</h4>
                <div class="value">{cert_data['validity']}</div>
            </div>
        </div>

        <div class="info-box">
            <h3>Exam Format</h3>
            <p>{cert_data['exam_format']}</p>

            <h3>Prerequisites</h3>
            <p>{cert_data['prerequisites']}</p>
        </div>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
            </svg>
            Study Resources
        </h2>
        <p>Recommended resources for preparing for this certification:</p>
        <ul>
            {resources_html}
        </ul>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
            </svg>
            Career Opportunities
        </h2>
        <p>This certification opens doors to the following career paths:</p>
        <ul>
            {careers_html}
        </ul>

        <div class="info-box">
            <h3>Expected Salary Range</h3>
            <p style="font-size: var(--text-xl); color: var(--accent-color); font-weight: 700; margin-top: var(--space-sm);">{cert_data['salary']}</p>
            <p style="margin-top: var(--space-md); font-size: var(--text-sm);">Salary ranges vary by location, experience, and company size. These figures represent typical ranges in the United States market.</p>
        </div>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M9 5l7 7-7 7"></path>
            </svg>
            Next Steps
        </h2>
        <div class="highlight-box">
            <p>{cert_data['next_steps']}</p>
        </div>

        <p style="margin-top: var(--space-xl);">Ready to get started? Visit the <a href="{cert_data['vendor_url']}" style="color: var(--accent-color);">{cert_data['vendor']} Training Portal</a> for official training materials and exam registration.</p>

        <p style="margin-top: var(--space-md);">Download your digital badge from <a href="https://www.credly.com" style="color: var(--accent-color);">Credly</a> after passing the exam to showcase your achievement on LinkedIn and other professional platforms.</p>
    </section>
</main>

<footer style="background: var(--bg-secondary); padding: var(--space-xl) 0; margin-top: var(--space-4xl); border-top: 1px solid var(--border-color); text-align: center; color: var(--text-tertiary);">
    <div class="container">
        <p>&copy; 2025 GenuisNet.ai. All rights reserved.</p>
        <p style="margin-top: var(--space-sm); font-size: var(--text-sm);">{cert_data['vendor']} and all related trademarks are property of their respective owners.</p>
    </div>
</footer>

</body>
</html>"""

    return html

def hex_to_rgb(hex_color):
    """Convert hex to RGB string"""
    hex_color = hex_color.lstrip('#')
    return ', '.join(str(int(hex_color[i:i+2], 16)) for i in (0, 2, 4))

def darken_color(hex_color):
    """Darken hex color by 20%"""
    hex_color = hex_color.lstrip('#')
    rgb = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
    rgb = [max(0, int(c * 0.8)) for c in rgb]
    return '#' + ''.join(f'{c:02x}' for c in rgb)

# Main
print("Génération des pages de certification cybersecurity...\n")

cert_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/certifications')
cert_dir.mkdir(exist_ok=True)

count = 0
for cert_id, cert_data in CERTIFICATIONS_DATA.items():
    filename = f"{cert_id}.html"
    filepath = cert_dir / filename

    html_content = create_cert_page_html(cert_data)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)

    count += 1
    print(f"✓ {filename}")

print(f"\n✅ {count} pages de certification créées!")
print(f"📁 Emplacement: pages/certifications/")
