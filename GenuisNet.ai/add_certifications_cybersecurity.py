#!/usr/bin/env python3
"""
Script pour ajouter les sections de certifications aux pages AI Cybersecurity
"""

import os
import re

# Définition des certifications pour chaque outil
CERTIFICATIONS = {
    'fortinet.html': {
        'title': 'Fortinet NSE (Network Security Expert) Program',
        'certs': [
            {
                'name': 'NSE 1 - Information Security Awareness',
                'level': 'Entry',
                'cost': 'FREE',
                'description': 'Introduction to cybersecurity fundamentals and threat landscape',
                'duration': '2 hours',
                'exam': 'Online quiz'
            },
            {
                'name': 'NSE 2 - The Fundamentals of Cybersecurity',
                'level': 'Entry',
                'cost': 'FREE',
                'description': 'Core concepts of network security and FortiGate basics',
                'duration': '4 hours',
                'exam': 'Online quiz'
            },
            {
                'name': 'NSE 3 - FortiGate Associate',
                'level': 'Associate',
                'cost': '$0',
                'description': 'FortiGate configuration and basic security features',
                'duration': '8 hours',
                'exam': 'Online proctored'
            },
            {
                'name': 'NSE 4 - FortiGate Security',
                'level': 'Professional',
                'cost': '$400',
                'description': 'Advanced FortiGate configuration, VPN, and security features (Most Popular)',
                'duration': '16 hours',
                'exam': 'Proctored exam'
            },
            {
                'name': 'NSE 5 - FortiAnalyzer/FortiManager/FortiSIEM',
                'level': 'Professional',
                'cost': '$400 each',
                'description': 'Specialized certifications for Fortinet management and analytics tools',
                'duration': '16 hours each',
                'exam': 'Proctored exam'
            },
            {
                'name': 'NSE 6 - Security Specialist',
                'level': 'Specialist',
                'cost': '$400 each',
                'description': 'FortiMail, FortiWeb, FortiADC specializations',
                'duration': '16 hours',
                'exam': 'Proctored exam'
            },
            {
                'name': 'NSE 7 - Enterprise Firewall/Public Cloud',
                'level': 'Advanced',
                'cost': '$400 each',
                'description': 'Enterprise-level architecture and cloud security',
                'duration': '24 hours',
                'exam': 'Proctored exam'
            },
            {
                'name': 'NSE 8 - Written Exam',
                'level': 'Expert',
                'cost': '$1,500',
                'description': 'Highest level certification demonstrating expert-level knowledge',
                'duration': '40+ hours prep',
                'exam': 'In-person written exam'
            }
        ],
        'url': 'https://training.fortinet.com/local/staticpage/view.php?page=certifications'
    },

    'palo-alto-ngfw.html': {
        'title': 'Palo Alto Networks Certification Program',
        'certs': [
            {
                'name': 'PCCET - Cybersecurity Entry-level Technician',
                'level': 'Entry',
                'cost': '$100',
                'description': 'Foundation-level cybersecurity knowledge and Palo Alto basics',
                'duration': '40 hours',
                'exam': '75 questions, 80 minutes'
            },
            {
                'name': 'PCNSA - Network Security Administrator',
                'level': 'Associate',
                'cost': '$185',
                'description': 'Configure and manage Palo Alto Networks firewalls',
                'duration': '40 hours',
                'exam': '75 questions, 80 minutes'
            },
            {
                'name': 'PCNSE - Network Security Engineer',
                'level': 'Professional',
                'cost': '$425',
                'description': 'Advanced firewall deployment and troubleshooting',
                'duration': '80 hours',
                'exam': '75 questions, 80 minutes'
            },
            {
                'name': 'PCCSA - Cybersecurity Associate',
                'level': 'Associate',
                'cost': '$100',
                'description': 'Cloud security fundamentals with Prisma Cloud',
                'duration': '32 hours',
                'exam': '50 questions, 60 minutes'
            },
            {
                'name': 'PCCSE - Cybersecurity Engineer',
                'level': 'Professional',
                'cost': '$400',
                'description': 'Advanced cloud security with Prisma Cloud',
                'duration': '80 hours',
                'exam': '75 questions, 90 minutes'
            },
            {
                'name': 'PCSAE - Security Automation Engineer',
                'level': 'Professional',
                'cost': '$400',
                'description': 'Security automation with Cortex XSOAR',
                'duration': '60 hours',
                'exam': '60 questions, 90 minutes'
            }
        ],
        'url': 'https://www.paloaltonetworks.com/services/education/certification'
    },

    'microsoft-sentinel.html': {
        'title': 'Microsoft Security Certifications',
        'certs': [
            {
                'name': 'SC-900 - Security, Compliance, and Identity Fundamentals',
                'level': 'Fundamentals',
                'cost': '$99',
                'description': 'Foundation concepts of security, compliance, and identity',
                'duration': '8-16 hours',
                'exam': '40-60 questions, 45 minutes'
            },
            {
                'name': 'SC-200 - Security Operations Analyst',
                'level': 'Associate',
                'cost': '$165',
                'description': 'Investigate, respond, and hunt threats using Microsoft Sentinel',
                'duration': '40 hours',
                'exam': '40-60 questions, 100 minutes'
            },
            {
                'name': 'SC-300 - Identity and Access Administrator',
                'level': 'Associate',
                'cost': '$165',
                'description': 'Implement and manage identity and access with Azure AD',
                'duration': '40 hours',
                'exam': '40-60 questions, 100 minutes'
            },
            {
                'name': 'SC-400 - Information Protection Administrator',
                'level': 'Associate',
                'cost': '$165',
                'description': 'Implement information protection and data loss prevention',
                'duration': '32 hours',
                'exam': '40-60 questions, 100 minutes'
            },
            {
                'name': 'AZ-500 - Azure Security Technologies',
                'level': 'Associate',
                'cost': '$165',
                'description': 'Implement security controls and threat protection on Azure',
                'duration': '48 hours',
                'exam': '40-60 questions, 120 minutes'
            },
            {
                'name': 'MS-500 - Microsoft 365 Security Administration',
                'level': 'Associate',
                'cost': '$165',
                'description': 'Implement and manage security and compliance in M365',
                'duration': '40 hours',
                'exam': '40-60 questions, 120 minutes'
            }
        ],
        'url': 'https://learn.microsoft.com/en-us/certifications/'
    },

    'cisco-securex.html': {
        'title': 'Cisco Security Certifications',
        'certs': [
            {
                'name': 'CyberOps Associate - 200-201 CBROPS',
                'level': 'Associate',
                'cost': '$300',
                'description': 'Security operations center (SOC) fundamentals',
                'duration': '40 hours',
                'exam': '90-110 questions, 120 minutes'
            },
            {
                'name': 'CCNP Security - 350-701 SCOR',
                'level': 'Professional',
                'cost': '$400',
                'description': 'Implement core security technologies (Core exam)',
                'duration': '80 hours',
                'exam': '90-110 questions, 120 minutes'
            },
            {
                'name': 'CCNP Security Concentration - SVPN/SISE/SAUI/SESA',
                'level': 'Professional',
                'cost': '$300 each',
                'description': 'Choose one: Secure VPN, ISE, AMP, or Email Security',
                'duration': '40 hours each',
                'exam': '90 minutes each'
            },
            {
                'name': 'CCIE Security - Lab',
                'level': 'Expert',
                'cost': '$1,600',
                'description': 'Expert-level security implementation and troubleshooting',
                'duration': '200+ hours',
                'exam': '8-hour hands-on lab'
            },
            {
                'name': 'Cisco Specialist Certifications',
                'level': 'Specialist',
                'cost': '$300 each',
                'description': 'Firepower, Umbrella, ISE, Duo, and more',
                'duration': 'Varies',
                'exam': '90 minutes'
            }
        ],
        'url': 'https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/security.html'
    },

    'splunk-security.html': {
        'title': 'Splunk Certifications',
        'certs': [
            {
                'name': 'Splunk Core Certified User',
                'level': 'User',
                'cost': '$125',
                'description': 'Basic Splunk searching and navigation',
                'duration': '16 hours',
                'exam': '57 questions, 60 minutes'
            },
            {
                'name': 'Splunk Core Certified Power User',
                'level': 'Power User',
                'cost': '$125',
                'description': 'Advanced searching and reporting',
                'duration': '24 hours',
                'exam': '70 questions, 90 minutes'
            },
            {
                'name': 'Splunk Enterprise Certified Admin',
                'level': 'Admin',
                'cost': '$125',
                'description': 'Install, configure, and manage Splunk',
                'duration': '40 hours',
                'exam': '60 questions, 60 minutes'
            },
            {
                'name': 'Splunk Enterprise Security Certified Admin',
                'level': 'Specialist',
                'cost': '$250',
                'description': 'Deploy and configure Splunk ES for security operations',
                'duration': '40 hours',
                'exam': '60 questions, 60 minutes'
            },
            {
                'name': 'Splunk SOAR Certified Automation Developer',
                'level': 'Specialist',
                'cost': '$250',
                'description': 'Build security automation with Splunk SOAR',
                'duration': '32 hours',
                'exam': '58 questions, 90 minutes'
            },
            {
                'name': 'Splunk Enterprise Certified Architect',
                'level': 'Architect',
                'cost': '$250',
                'description': 'Design and deploy large-scale Splunk environments',
                'duration': '80 hours',
                'exam': '60 questions, 90 minutes'
            }
        ],
        'url': 'https://www.splunk.com/en_us/training/certification-track.html'
    },

    'crowdstrike.html': {
        'title': 'CrowdStrike University Certifications',
        'certs': [
            {
                'name': 'CCFA - CrowdStrike Certified Falcon Administrator',
                'level': 'Administrator',
                'cost': 'Contact Sales',
                'description': 'Deploy and manage CrowdStrike Falcon platform',
                'duration': '16 hours',
                'exam': 'Online proctored'
            },
            {
                'name': 'CCFR - CrowdStrike Certified Falcon Responder',
                'level': 'Analyst',
                'cost': 'Contact Sales',
                'description': 'Detect and respond to threats using Falcon',
                'duration': '24 hours',
                'exam': 'Online proctored'
            },
            {
                'name': 'CCFH - CrowdStrike Certified Falcon Hunter',
                'level': 'Advanced',
                'cost': 'Contact Sales',
                'description': 'Proactive threat hunting with Falcon platform',
                'duration': '32 hours',
                'exam': 'Online proctored'
            },
            {
                'name': 'CrowdStrike University - Various Courses',
                'level': 'All Levels',
                'cost': 'Included with license',
                'description': 'Comprehensive training library for customers',
                'duration': 'Self-paced',
                'exam': 'Course-dependent'
            }
        ],
        'url': 'https://www.crowdstrike.com/university/'
    },

    'ibm-qradar.html': {
        'title': 'IBM Security QRadar Certifications',
        'certs': [
            {
                'name': 'IBM Certified Associate Analyst - Security QRadar SIEM',
                'level': 'Associate',
                'cost': 'Contact IBM',
                'description': 'Fundamentals of QRadar SIEM operations',
                'duration': '24 hours',
                'exam': 'Pearson VUE'
            },
            {
                'name': 'IBM Certified Specialist - Security QRadar SIEM V7.4.3',
                'level': 'Specialist',
                'cost': 'Contact IBM',
                'description': 'Deploy and configure QRadar SIEM',
                'duration': '40 hours',
                'exam': 'Pearson VUE'
            },
            {
                'name': 'IBM Security QRadar V7.4 Deployment',
                'level': 'Implementation',
                'cost': 'Contact IBM',
                'description': 'Install and deploy QRadar environments',
                'duration': '32 hours',
                'exam': 'Pearson VUE'
            },
            {
                'name': 'IBM Security QRadar V7.4 Analysis',
                'level': 'Analyst',
                'cost': 'Contact IBM',
                'description': 'Analyze security events and incidents',
                'duration': '32 hours',
                'exam': 'Pearson VUE'
            }
        ],
        'url': 'https://www.ibm.com/training/certification'
    },

    'cyberark.html': {
        'title': 'CyberArk PAM Certifications',
        'certs': [
            {
                'name': 'CyberArk Defender - PAM',
                'level': 'Defender',
                'cost': '$350',
                'description': 'Core PAM concepts and CyberArk fundamentals',
                'duration': '24 hours',
                'exam': 'Online proctored, 90 minutes'
            },
            {
                'name': 'CyberArk Sentry - PAM',
                'level': 'Sentry',
                'cost': '$500',
                'description': 'Install, configure, and manage CyberArk Vault',
                'duration': '40 hours',
                'exam': 'Online proctored, 120 minutes'
            },
            {
                'name': 'CyberArk Guardian - PAM',
                'level': 'Guardian',
                'cost': '$700',
                'description': 'Advanced PAM architecture and troubleshooting',
                'duration': '60 hours',
                'exam': 'Online proctored, 150 minutes'
            },
            {
                'name': 'CyberArk Trustee - Secrets Management',
                'level': 'Trustee',
                'cost': '$500',
                'description': 'Implement secrets management and DevOps security',
                'duration': '32 hours',
                'exam': 'Online proctored, 120 minutes'
            }
        ],
        'url': 'https://www.cyberark.com/services-support/training-certification/'
    },

    'okta.html': {
        'title': 'Okta Certifications',
        'certs': [
            {
                'name': 'Okta Certified Professional',
                'level': 'Professional',
                'cost': '$150',
                'description': 'Core Okta concepts and identity management',
                'duration': '24 hours',
                'exam': 'Online, 60 questions, 90 minutes'
            },
            {
                'name': 'Okta Certified Administrator',
                'level': 'Administrator',
                'cost': '$250',
                'description': 'Configure and manage Okta environments',
                'duration': '40 hours',
                'exam': 'Online, 75 questions, 120 minutes'
            },
            {
                'name': 'Okta Certified Consultant',
                'level': 'Consultant',
                'cost': '$400',
                'description': 'Design and implement enterprise Okta solutions',
                'duration': '60 hours',
                'exam': 'Online, 90 questions, 150 minutes'
            },
            {
                'name': 'Okta Certified Developer',
                'level': 'Developer',
                'cost': '$300',
                'description': 'Integrate applications with Okta APIs',
                'duration': '48 hours',
                'exam': 'Online, 70 questions, 120 minutes'
            }
        ],
        'url': 'https://www.okta.com/services/training-and-certification/'
    },

    'qualys.html': {
        'title': 'Qualys Certifications',
        'certs': [
            {
                'name': 'Qualys Certified Specialist (QCS) - VMDR',
                'level': 'Specialist',
                'cost': 'FREE',
                'description': 'Vulnerability Management, Detection and Response',
                'duration': '16 hours',
                'exam': 'Online, 60 minutes'
            },
            {
                'name': 'Qualys Certified Specialist - Web Application Scanning',
                'level': 'Specialist',
                'cost': 'FREE',
                'description': 'Web application security scanning',
                'duration': '16 hours',
                'exam': 'Online, 60 minutes'
            },
            {
                'name': 'Qualys Certified Specialist - Policy Compliance',
                'level': 'Specialist',
                'cost': 'FREE',
                'description': 'Compliance scanning and reporting',
                'duration': '16 hours',
                'exam': 'Online, 60 minutes'
            }
        ],
        'url': 'https://www.qualys.com/training/'
    },

    'rapid7.html': {
        'title': 'Rapid7 Certifications',
        'certs': [
            {
                'name': 'Rapid7 Certified Administrator - InsightVM',
                'level': 'Administrator',
                'cost': 'FREE',
                'description': 'Vulnerability management with InsightVM',
                'duration': '16 hours',
                'exam': 'Online assessment'
            },
            {
                'name': 'Rapid7 Certified Administrator - InsightIDR',
                'level': 'Administrator',
                'cost': 'FREE',
                'description': 'SIEM and incident response with InsightIDR',
                'duration': '20 hours',
                'exam': 'Online assessment'
            },
            {
                'name': 'Rapid7 Product Certifications',
                'level': 'Product',
                'cost': 'FREE',
                'description': 'Various product-specific certifications',
                'duration': 'Varies',
                'exam': 'Online'
            }
        ],
        'url': 'https://www.rapid7.com/services/training-certification/'
    },

    'tenable.html': {
        'title': 'Tenable Certifications',
        'certs': [
            {
                'name': 'Tenable Certified Sales Engineer (TCSE)',
                'level': 'Sales Engineering',
                'cost': 'FREE',
                'description': 'Tenable product portfolio and use cases',
                'duration': '16 hours',
                'exam': 'Online'
            },
            {
                'name': 'Nessus Certified',
                'level': 'Technical',
                'cost': 'FREE for customers',
                'description': 'Nessus vulnerability scanner operations',
                'duration': '12 hours',
                'exam': 'Online'
            }
        ],
        'url': 'https://www.tenable.com/education'
    },

    'darktrace.html': {
        'title': 'Darktrace Training & Certification',
        'certs': [
            {
                'name': 'Darktrace Certified Engineer',
                'level': 'Engineer',
                'cost': 'For partners/customers',
                'description': 'Deploy and configure Darktrace AI platform',
                'duration': '24 hours',
                'exam': 'Practical assessment'
            },
            {
                'name': 'Darktrace Threat Visualizer Training',
                'level': 'Analyst',
                'cost': 'For partners/customers',
                'description': 'Threat investigation and visualization',
                'duration': '16 hours',
                'exam': 'Course completion'
            },
            {
                'name': 'Darktrace Antigena Training',
                'level': 'Advanced',
                'cost': 'For partners/customers',
                'description': 'Autonomous response configuration',
                'duration': '16 hours',
                'exam': 'Course completion'
            }
        ],
        'url': 'https://customerportal.darktrace.com/training'
    },

    'sentinelone.html': {
        'title': 'SentinelOne Training Programs',
        'certs': [
            {
                'name': 'SentinelOne Core Administrator',
                'level': 'Core',
                'cost': 'For customers',
                'description': 'Basic platform administration',
                'duration': '16 hours',
                'exam': 'Online assessment'
            },
            {
                'name': 'SentinelOne Advanced Administrator',
                'level': 'Advanced',
                'cost': 'For customers',
                'description': 'Advanced features and automation',
                'duration': '24 hours',
                'exam': 'Online assessment'
            },
            {
                'name': 'SentinelOne Threat Hunter',
                'level': 'Analyst',
                'cost': 'For customers',
                'description': 'Threat hunting and investigation',
                'duration': '20 hours',
                'exam': 'Practical assessment'
            }
        ],
        'url': 'https://www.sentinelone.com/platform/university/'
    },

    'sophos-interceptx.html': {
        'title': 'Sophos Certifications',
        'certs': [
            {
                'name': 'Sophos Certified Engineer',
                'level': 'Engineer',
                'cost': 'For partners',
                'description': 'Deploy and configure Sophos solutions',
                'duration': '32 hours',
                'exam': 'Online proctored'
            },
            {
                'name': 'Sophos Certified Architect',
                'level': 'Architect',
                'cost': 'For partners',
                'description': 'Design enterprise Sophos architectures',
                'duration': '48 hours',
                'exam': 'Online proctored'
            },
            {
                'name': 'Sophos Certified Sales Professional',
                'level': 'Sales',
                'cost': 'For partners',
                'description': 'Sophos product portfolio and positioning',
                'duration': '16 hours',
                'exam': 'Online'
            }
        ],
        'url': 'https://www.sophos.com/en-us/partners/training-and-certification'
    },

    'trend-micro-vision-one.html': {
        'title': 'Trend Micro Certifications',
        'certs': [
            {
                'name': 'Trend Micro Certified Professional',
                'level': 'Professional',
                'cost': 'Varies',
                'description': 'Trend Micro security solutions',
                'duration': '24 hours',
                'exam': 'Online'
            },
            {
                'name': 'Trend Micro Certified Expert',
                'level': 'Expert',
                'cost': 'Varies',
                'description': 'Advanced product knowledge',
                'duration': '40 hours',
                'exam': 'Online proctored'
            }
        ],
        'url': 'https://www.trendmicro.com/en_us/partners/certifications.html'
    },

    'cortex-xdr.html': {
        'title': 'Palo Alto Networks - Cortex Certifications',
        'note': 'See Palo Alto PCCSA and PCCSE certifications',
        'certs': [
            {
                'name': 'PCCSA - Cybersecurity Associate',
                'level': 'Associate',
                'cost': '$100',
                'description': 'Prisma Cloud and Cortex fundamentals',
                'duration': '32 hours',
                'exam': '50 questions, 60 minutes'
            },
            {
                'name': 'PCCSE - Cybersecurity Engineer',
                'level': 'Professional',
                'cost': '$400',
                'description': 'Advanced Cortex XDR and Prisma Cloud',
                'duration': '80 hours',
                'exam': '75 questions, 90 minutes'
            }
        ],
        'url': 'https://www.paloaltonetworks.com/services/education/certification'
    }
}

def create_certification_section_html(tool_file):
    """Crée le HTML pour la section certifications"""

    if tool_file not in CERTIFICATIONS:
        return None

    data = CERTIFICATIONS[tool_file]

    html = f'''
<!-- Certifications Section -->
<section class="review-section" id="certifications">
<h2><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 14l9-5-9-5-9 5 9 5z"/><path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/><path stroke-linecap="round" stroke-linejoin="round" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222"/></svg> Certifications & Training</h2>
<p>Professional certifications and training programs to validate your skills:</p>

<h3 style="margin-top: var(--space-xl); margin-bottom: var(--space-lg);">{data['title']}</h3>

<div class="features-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
'''

    for cert in data['certs']:
        # Déterminer la couleur du badge selon le niveau
        level_colors = {
            'Entry': '#10b981',
            'Fundamentals': '#10b981',
            'User': '#10b981',
            'Associate': '#3b82f6',
            'Administrator': '#3b82f6',
            'Professional': '#8b5cf6',
            'Specialist': '#8b5cf6',
            'Analyst': '#f59e0b',
            'Advanced': '#ef4444',
            'Expert': '#ef4444',
            'Architect': '#dc2626',
        }

        level_color = level_colors.get(cert['level'], '#6b7280')

        # Badge de coût
        is_free = 'FREE' in cert['cost'].upper() or '$0' in cert['cost']
        cost_badge = f'<span style="background: #10b981; color: white; padding: 4px 12px; border-radius: 12px; font-size: 0.75rem; font-weight: 600;">FREE</span>' if is_free else f'<span style="color: var(--text-tertiary); font-size: 0.875rem;">{cert["cost"]}</span>'

        html += f'''
<div class="feature-card">
    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: var(--space-sm);">
        <span style="background: {level_color}; color: white; padding: 4px 12px; border-radius: 12px; font-size: 0.75rem; font-weight: 600;">{cert['level']}</span>
        {cost_badge}
    </div>
    <h4 style="margin-bottom: var(--space-sm); line-height: 1.4;">{cert['name']}</h4>
    <p style="margin-bottom: var(--space-sm);">{cert['description']}</p>
    <div style="display: flex; gap: var(--space-md); font-size: 0.875rem; color: var(--text-tertiary); margin-top: var(--space-md);">
        <span>⏱️ {cert['duration']}</span>
        <span>📝 {cert['exam']}</span>
    </div>
</div>
'''

    html += f'''
</div>

<div style="background: var(--bg-tertiary); border-radius: var(--radius-lg); padding: var(--space-xl); margin-top: var(--space-xl);">
    <h4 style="margin-bottom: var(--space-md);">📚 Get Started with Certification</h4>
    <p style="margin-bottom: var(--space-md);">Official training and certification resources:</p>
    <a href="{data['url']}" class="btn btn-primary" target="_blank" rel="noopener noreferrer">Visit Certification Portal →</a>
</div>
</section>
'''

    return html


def add_certifications_to_file(filepath):
    """Ajoute la section certifications à un fichier HTML"""

    filename = os.path.basename(filepath)

    if filename not in CERTIFICATIONS:
        print(f"⚠️  Pas de certifications définies pour {filename}")
        return False

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Vérifier si la section existe déjà
        if 'id="certifications"' in content:
            print(f"ℹ️  Section certifications existe déjà dans {filename}")
            return False

        # Créer la section HTML
        cert_html = create_certification_section_html(filename)

        if not cert_html:
            return False

        # Trouver où insérer (après pricing, avant use-cases ou verdict)
        insert_patterns = [
            (r'</section>\s*<section class="review-section" id="use-cases">', 'before use-cases'),
            (r'</section>\s*<section class="review-section" id="verdict">', 'before verdict'),
            (r'</section>\s*<section class="review-section" id="comparison">', 'before comparison'),
            (r'</section>\s*<!-- Screenshots Section -->', 'before screenshots'),
        ]

        inserted = False
        for pattern, location in insert_patterns:
            if re.search(pattern, content):
                content = re.sub(pattern, f'{cert_html}\\n</section>\\n<section class="review-section" id="{location.split()[1]}">', content, count=1)
                inserted = True
                print(f"✓ Certifications ajoutées à {filename} ({location})")
                break

        if not inserted:
            print(f"⚠️  Impossible de trouver le point d'insertion dans {filename}")
            return False

        # Sauvegarder
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    except Exception as e:
        print(f"❌ Erreur avec {filename}: {str(e)}")
        return False


if __name__ == "__main__":
    import sys

    cybersecurity_dir = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/reviews/cybersecurity"

    print("=" * 80)
    print("  AJOUT DES CERTIFICATIONS AUX PAGES AI CYBERSECURITY")
    print("=" * 80)
    print()

    success_count = 0
    total_count = 0

    for filename in sorted(CERTIFICATIONS.keys()):
        filepath = os.path.join(cybersecurity_dir, filename)

        if os.path.exists(filepath):
            total_count += 1
            if add_certifications_to_file(filepath):
                success_count += 1
        else:
            print(f"⚠️  Fichier non trouvé: {filename}")

    print()
    print("=" * 80)
    print(f"✓ {success_count}/{total_count} pages mises à jour avec succès")
    print("=" * 80)
