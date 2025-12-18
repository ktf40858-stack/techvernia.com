#!/usr/bin/env python3
"""
Met à jour les sections de certification avec le format détaillé (style Cisco)
Inclut les logos de certification et le contenu enrichi
"""

import re

# Données détaillées des certifications
CERTIFICATIONS_DETAILED = {
    'fortinet.html': {
        'intro': 'To maximize the value of Fortinet security solutions, professionals should pursue the NSE (Network Security Expert) certification program. This comprehensive program offers 8 levels, from basic security awareness to expert-level network defense capabilities.',
        'certs': [
            {
                'name': 'NSE 4 - FortiGate Security',
                'level': 'Professional Level',
                'image': 'fortinet-nse4.png',
                'description': 'Deploy, configure, and manage FortiGate devices. Core skills for firewall administration, VPN, and security policies.',
                'exam': 'NSE 4 Exam',
                'exam_code': 'NSE4_FGT-7.2'
            },
            {
                'name': 'NSE 7 - Enterprise Firewall',
                'level': 'Expert Level',
                'image': 'fortinet-nse7.png',
                'description': 'Design and deploy complex FortiGate solutions for large enterprises. Advanced routing, HA clusters, and troubleshooting.',
                'exam': 'NSE 7 Exam',
                'exam_code': 'NSE7_EFW-7.2'
            },
            {
                'name': 'NSE 8 - Written Exam',
                'level': 'Master Level',
                'image': 'fortinet-nse8.png',
                'description': 'Highest level certification demonstrating complete mastery of Fortinet security architecture and strategic implementation.',
                'exam': 'Written + Practical',
                'exam_code': 'NSE8'
            }
        ],
        'url': 'https://training.fortinet.com'
    },

    'palo-alto-ngfw.html': {
        'intro': 'Palo Alto Networks offers comprehensive certifications covering next-generation firewall deployment, cybersecurity operations, and security automation. These industry-recognized credentials validate expertise in modern threat prevention and zero-trust architecture.',
        'certs': [
            {
                'name': 'PCCET',
                'level': 'Entry-Level Technician',
                'image': 'paloalto-pccet.png',
                'description': 'Foundation-level certification covering cybersecurity concepts, network security basics, and cloud security fundamentals.',
                'exam': 'PCCET Exam',
                'exam_code': 'PCCET'
            },
            {
                'name': 'PCNSA',
                'level': 'Administrator Level',
                'image': 'paloalto-pcnsa.png',
                'description': 'Configure, manage, and monitor Palo Alto Networks next-generation firewalls. Essential for NGFW administrators.',
                'exam': 'PCNSA Exam',
                'exam_code': 'PCNSA'
            },
            {
                'name': 'PCNSE',
                'level': 'Engineer Level',
                'image': 'paloalto-pcnse.png',
                'description': 'Advanced troubleshooting, optimization, and deployment of Palo Alto NGFW in complex enterprise environments.',
                'exam': 'PCNSE Exam',
                'exam_code': 'PCNSE'
            },
            {
                'name': 'PCCSA',
                'level': 'Cybersecurity Associate',
                'image': 'paloalto-pccsa.png',
                'description': 'Detect, prevent, and respond to cyber threats using Cortex XDR and threat intelligence platforms.',
                'exam': 'PCCSA Exam',
                'exam_code': 'PCCSA'
            },
            {
                'name': 'PCCSE',
                'level': 'Cybersecurity Engineer',
                'image': 'paloalto-pccse.png',
                'description': 'Expert-level SOC operations, incident response, and advanced threat hunting with Palo Alto security platforms.',
                'exam': 'PCCSE Exam',
                'exam_code': 'PCCSE'
            },
            {
                'name': 'PCSAE',
                'level': 'Security Automation',
                'image': 'paloalto-pcsae.png',
                'description': 'Automate security operations and orchestrate responses using SOAR (Security Orchestration, Automation, Response).',
                'exam': 'PCSAE Exam',
                'exam_code': 'PCSAE'
            }
        ],
        'url': 'https://www.paloaltonetworks.com/services/education'
    },

    'microsoft-sentinel.html': {
        'intro': 'Microsoft offers a comprehensive security certification path covering cloud security, identity management, compliance, and security operations. These role-based certifications align with real-world job responsibilities in modern cloud-first environments.',
        'certs': [
            {
                'name': 'SC-900: Security Fundamentals',
                'level': 'Fundamentals',
                'image': 'microsoft-sc900.png',
                'description': 'Entry-level certification covering security, compliance, and identity concepts across Microsoft cloud services.',
                'exam': 'SC-900',
                'exam_code': 'SC-900'
            },
            {
                'name': 'SC-200: Security Operations Analyst',
                'level': 'Associate Level',
                'image': 'microsoft-sc200.png',
                'description': 'Investigate, respond to, and hunt for threats using Microsoft Sentinel, Defender XDR, and threat intelligence.',
                'exam': 'SC-200',
                'exam_code': 'SC-200'
            },
            {
                'name': 'SC-300: Identity Administrator',
                'level': 'Associate Level',
                'image': 'microsoft-sc300.png',
                'description': 'Design and implement identity and access management solutions using Azure AD, conditional access, and PIM.',
                'exam': 'SC-300',
                'exam_code': 'SC-300'
            },
            {
                'name': 'SC-400: Information Protection',
                'level': 'Associate Level',
                'image': 'microsoft-sc400.png',
                'description': 'Implement data loss prevention, information governance, and insider risk management in Microsoft 365.',
                'exam': 'SC-400',
                'exam_code': 'SC-400'
            },
            {
                'name': 'AZ-500: Azure Security',
                'level': 'Associate Level',
                'image': 'microsoft-az500.png',
                'description': 'Secure Azure infrastructure, implement platform protection, manage identity, and configure security operations.',
                'exam': 'AZ-500',
                'exam_code': 'AZ-500'
            }
        ],
        'url': 'https://learn.microsoft.com/certifications'
    },

    'cisco-securex.html': {
        'intro': 'Cisco security certifications validate skills in SOC operations, network defense, and cybersecurity engineering. From associate-level CyberOps to expert-level CCIE Security, these credentials demonstrate proficiency with Cisco security platforms and SecureX integration.',
        'certs': [
            {
                'name': 'CyberOps Associate',
                'level': 'Associate Level',
                'image': 'cisco-cyberops.png',
                'description': 'Security monitoring, host-based and network intrusion analysis, and security event management for SOC environments.',
                'exam': 'CBROPS 200-201',
                'exam_code': '200-201'
            },
            {
                'name': 'CCNP Security',
                'level': 'Professional Level',
                'image': 'cisco-ccnp-security.png',
                'description': 'Implement and troubleshoot Cisco security solutions including firewalls, VPN, IPS, and secure network access.',
                'exam': 'SCOR 350-701 + Concentration',
                'exam_code': '350-701'
            },
            {
                'name': 'CCIE Security',
                'level': 'Expert Level',
                'image': 'cisco-ccie-security.png',
                'description': 'Elite-level certification requiring deep expertise in Cisco security architecture, advanced troubleshooting, and design.',
                'exam': 'Written + 8-hour Lab',
                'exam_code': 'CCIE Security'
            }
        ],
        'url': 'https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/security.html'
    },

    'splunk-security.html': {
        'intro': 'Splunk certifications demonstrate proficiency in security information and event management (SIEM), enterprise security administration, and SOAR automation. These credentials are highly valued for SOC analysts and security engineers.',
        'certs': [
            {
                'name': 'Splunk ES Certified Admin',
                'level': 'Administrator',
                'image': 'splunk-es-admin.png',
                'description': 'Deploy, configure, and manage Splunk Enterprise Security for threat detection and incident response.',
                'exam': 'ES Admin Exam',
                'exam_code': 'SPLK-3003'
            },
            {
                'name': 'Splunk SOAR Certified Dev',
                'level': 'Developer',
                'image': 'splunk-soar-dev.png',
                'description': 'Build automated security workflows and orchestrate responses using Splunk SOAR (Phantom) platform.',
                'exam': 'SOAR Dev Exam',
                'exam_code': 'SPLK-2003'
            }
        ],
        'url': 'https://www.splunk.com/en_us/training.html'
    },

    'crowdstrike.html': {
        'intro': 'CrowdStrike University offers specialized certifications focused on the Falcon platform. These credentials validate skills in endpoint detection and response (EDR), threat hunting, and incident response using AI-powered cybersecurity.',
        'certs': [
            {
                'name': 'CCFA - Falcon Administrator',
                'level': 'Administrator',
                'image': 'crowdstrike-ccfa.png',
                'description': 'Configure and manage CrowdStrike Falcon platform, including prevention policies, detection configuration, and response actions.',
                'exam': 'Online Proctored',
                'exam_code': 'CCFA'
            },
            {
                'name': 'CCFR - Falcon Responder',
                'level': 'Analyst Level',
                'image': 'crowdstrike-ccfr.png',
                'description': 'Investigate and respond to security incidents using Falcon EDR, Real Time Response, and threat intelligence.',
                'exam': 'Online Proctored',
                'exam_code': 'CCFR'
            },
            {
                'name': 'CCFH - Falcon Hunter',
                'level': 'Advanced Hunter',
                'image': 'crowdstrike-ccfh.png',
                'description': 'Proactive threat hunting using advanced queries, behavioral analytics, and custom IOAs with the Falcon platform.',
                'exam': 'Online Proctored',
                'exam_code': 'CCFH'
            }
        ],
        'url': 'https://www.crowdstrike.com/university/'
    },

    'ibm-qradar.html': {
        'intro': 'IBM Security certifications validate expertise in QRadar SIEM deployment, security analytics, and threat detection. These credentials demonstrate proficiency in enterprise security monitoring and compliance reporting.',
        'certs': [
            {
                'name': 'QRadar SIEM V7.4.3 Specialist',
                'level': 'Specialist',
                'image': 'ibm-qradar-siem.png',
                'description': 'Deploy, configure, and administer IBM QRadar SIEM. Create custom rules, manage log sources, and generate compliance reports.',
                'exam': 'QRadar SIEM Exam',
                'exam_code': 'C1000-142'
            },
            {
                'name': 'QRadar Associate Analyst',
                'level': 'Associate',
                'image': 'ibm-qradar-analyst.png',
                'description': 'Analyze security events, investigate offenses, and respond to threats using QRadar dashboards and investigation tools.',
                'exam': 'QRadar Analyst Exam',
                'exam_code': 'C1000-123'
            }
        ],
        'url': 'https://www.ibm.com/training/certification'
    },

    'cyberark.html': {
        'intro': 'CyberArk certifications validate expertise in privileged access management (PAM), secrets management, and credential security. These credentials demonstrate proficiency in protecting against privilege escalation and credential theft.',
        'certs': [
            {
                'name': 'CyberArk Defender - PAM',
                'level': 'Defender',
                'image': 'cyberark-defender.png',
                'description': 'Deploy and configure CyberArk PAM solution. Onboard privileged accounts, manage safes, and implement security policies.',
                'exam': 'PAM Defender Exam',
                'exam_code': 'PAM-DEF'
            },
            {
                'name': 'CyberArk Sentry - PAM',
                'level': 'Sentry',
                'image': 'cyberark-sentry.png',
                'description': 'Advanced PAM administration including CPM configuration, PSM hardening, and high-availability deployment.',
                'exam': 'PAM Sentry Exam',
                'exam_code': 'PAM-SEN'
            },
            {
                'name': 'CyberArk Guardian - PAM',
                'level': 'Guardian',
                'image': 'cyberark-guardian.png',
                'description': 'Design and architect enterprise PAM solutions. Integrate with SIEM, implement disaster recovery, and optimize performance.',
                'exam': 'PAM Guardian Exam',
                'exam_code': 'PAM-CDE'
            }
        ],
        'url': 'https://www.cyberark.com/services-support/education-training/'
    },

    'okta.html': {
        'intro': 'Okta certifications validate skills in identity and access management (IAM), single sign-on (SSO), multi-factor authentication (MFA), and API integration. These credentials demonstrate expertise in modern cloud-based identity solutions.',
        'certs': [
            {
                'name': 'Okta Certified Professional',
                'level': 'Professional',
                'image': 'okta-professional.png',
                'description': 'Core Okta platform knowledge including SSO configuration, MFA deployment, and lifecycle management.',
                'exam': 'Online Proctored',
                'exam_code': 'OCP'
            },
            {
                'name': 'Okta Certified Administrator',
                'level': 'Administrator',
                'image': 'okta-administrator.png',
                'description': 'Advanced administration of Okta environments including user management, app integrations, and security policies.',
                'exam': 'Online Proctored',
                'exam_code': 'OCA'
            },
            {
                'name': 'Okta Certified Consultant',
                'level': 'Consultant',
                'image': 'okta-consultant.png',
                'description': 'Design and implement complex Okta solutions for enterprise customers including custom workflows and integrations.',
                'exam': 'Online Proctored',
                'exam_code': 'OCC'
            },
            {
                'name': 'Okta Certified Developer',
                'level': 'Developer',
                'image': 'okta-developer.png',
                'description': 'Develop custom applications using Okta APIs, implement authentication flows, and integrate Okta SDKs.',
                'exam': 'Online Proctored',
                'exam_code': 'OCD'
            }
        ],
        'url': 'https://www.okta.com/services/training/'
    },

    'qualys.html': {
        'intro': 'Qualys certifications validate expertise in vulnerability management, web application scanning, and policy compliance. These FREE certifications demonstrate proficiency with the Qualys Cloud Platform and continuous monitoring.',
        'certs': [
            {
                'name': 'Qualys VMDR Specialist',
                'level': 'Specialist',
                'image': 'qualys-vmdr.png',
                'description': 'Vulnerability Management, Detection, and Response using Qualys VMDR. Scan configuration, remediation, and patch management.',
                'exam': 'Online Free',
                'exam_code': 'VMDR'
            },
            {
                'name': 'Qualys WAS Specialist',
                'level': 'Specialist',
                'image': 'qualys-was.png',
                'description': 'Web Application Scanning for detecting OWASP Top 10 vulnerabilities, SQL injection, XSS, and security misconfigurations.',
                'exam': 'Online Free',
                'exam_code': 'WAS'
            }
        ],
        'url': 'https://www.qualys.com/training/'
    },

    'rapid7.html': {
        'intro': 'Rapid7 offers FREE product certifications for InsightVM (vulnerability management) and InsightIDR (detection and response). These credentials validate hands-on skills with Rapid7\'s security analytics platform.',
        'certs': [
            {
                'name': 'Rapid7 InsightVM Certified',
                'level': 'Administrator',
                'image': 'rapid7-insightvm.png',
                'description': 'Deploy and manage InsightVM for vulnerability assessment, asset discovery, and risk-based prioritization.',
                'exam': 'Online Free',
                'exam_code': 'InsightVM'
            },
            {
                'name': 'Rapid7 InsightIDR Certified',
                'level': 'Administrator',
                'image': 'rapid7-insightidr.png',
                'description': 'Configure InsightIDR for SIEM, user behavior analytics (UBA), and incident detection and response (IDR).',
                'exam': 'Online Free',
                'exam_code': 'InsightIDR'
            }
        ],
        'url': 'https://www.rapid7.com/services/training-certification/'
    },

    'tenable.html': {
        'intro': 'Tenable certifications validate proficiency with Nessus vulnerability scanning and Tenable.io cloud-based vulnerability management. These credentials demonstrate expertise in continuous exposure management.',
        'certs': [
            {
                'name': 'Nessus Certified Professional',
                'level': 'Professional',
                'image': 'tenable-nessus.png',
                'description': 'Deploy Nessus scanners, configure credentialed scans, analyze vulnerability data, and generate compliance reports.',
                'exam': 'Online',
                'exam_code': 'Nessus Pro'
            }
        ],
        'url': 'https://www.tenable.com/education'
    },

    'darktrace.html': {
        'intro': 'Darktrace training programs validate expertise in AI-powered threat detection, autonomous response, and cyber AI analyst capabilities. These certifications demonstrate proficiency with self-learning security technology.',
        'certs': [
            {
                'name': 'Darktrace Certified Engineer',
                'level': 'Engineer',
                'image': 'darktrace-engineer.png',
                'description': 'Deploy, configure, and optimize Darktrace AI for network defense, cloud security, and autonomous response (Antigena).',
                'exam': 'Partner/Customer',
                'exam_code': 'DCE'
            }
        ],
        'url': 'https://www.darktrace.com/en/resources/training/'
    },

    'sentinelone.html': {
        'intro': 'SentinelOne training programs provide hands-on knowledge of autonomous endpoint protection, EDR, and threat hunting. These credentials validate skills in next-generation antivirus and behavioral AI protection.',
        'certs': [
            {
                'name': 'SentinelOne Core Administrator',
                'level': 'Core',
                'image': 'sentinelone-core.png',
                'description': 'Configure SentinelOne agents, manage policies, investigate threats, and perform remote remediation actions.',
                'exam': 'Customer Training',
                'exam_code': 'S1-Core'
            },
            {
                'name': 'SentinelOne Advanced Admin',
                'level': 'Advanced',
                'image': 'sentinelone-advanced.png',
                'description': 'Advanced threat hunting, Deep Visibility queries, STAR rules, and integration with third-party security tools.',
                'exam': 'Customer Training',
                'exam_code': 'S1-Advanced'
            }
        ],
        'url': 'https://www.sentinelone.com/resources/training/'
    },

    'sophos-interceptx.html': {
        'intro': 'Sophos certifications validate expertise in endpoint protection, server security, and Intercept X with deep learning AI. These partner-focused credentials demonstrate proficiency in Sophos security solutions.',
        'certs': [
            {
                'name': 'Sophos Certified Engineer',
                'level': 'Engineer',
                'image': 'sophos-engineer.png',
                'description': 'Deploy and manage Sophos Central platform, Intercept X endpoint protection, and synchronized security.',
                'exam': 'Partner Certification',
                'exam_code': 'SCE'
            },
            {
                'name': 'Sophos Certified Architect',
                'level': 'Architect',
                'image': 'sophos-architect.png',
                'description': 'Design enterprise Sophos security architecture including XG Firewall, Intercept X, and email security integration.',
                'exam': 'Partner Certification',
                'exam_code': 'SCA'
            }
        ],
        'url': 'https://www.sophos.com/en-us/partners/training'
    },

    'trend-micro-vision-one.html': {
        'intro': 'Trend Micro certifications validate expertise in XDR (Extended Detection and Response), threat intelligence, and multi-layered security. These credentials demonstrate proficiency with Vision One unified security platform.',
        'certs': [
            {
                'name': 'Trend Micro Certified Professional',
                'level': 'Professional',
                'image': 'trendmicro-professional.png',
                'description': 'Deploy and manage Trend Micro security solutions including Vision One XDR, endpoint security, and email protection.',
                'exam': 'Online Exam',
                'exam_code': 'TMCP'
            },
            {
                'name': 'Trend Micro Certified Expert',
                'level': 'Expert',
                'image': 'trendmicro-expert.png',
                'description': 'Advanced XDR threat hunting, custom detection rules, API integration, and enterprise architecture design.',
                'exam': 'Online Exam',
                'exam_code': 'TMCE'
            }
        ],
        'url': 'https://www.trendmicro.com/en_us/partners/training-certification.html'
    },

    'cortex-xdr.html': {
        'intro': 'Cortex XDR certifications are part of the Palo Alto Networks security certification program. These credentials validate skills in extended detection and response, behavioral analytics, and cloud-native security.',
        'certs': [
            {
                'name': 'PCCSA',
                'level': 'Cybersecurity Associate',
                'image': 'paloalto-pccsa.png',
                'description': 'Detect, prevent, and respond to cyber threats using Cortex XDR and threat intelligence platforms.',
                'exam': 'PCCSA Exam',
                'exam_code': 'PCCSA'
            },
            {
                'name': 'PCCSE',
                'level': 'Cybersecurity Engineer',
                'image': 'paloalto-pccse.png',
                'description': 'Expert-level SOC operations, incident response, and advanced threat hunting with Cortex XDR and Prisma Cloud.',
                'exam': 'PCCSE Exam',
                'exam_code': 'PCCSE'
            }
        ],
        'url': 'https://www.paloaltonetworks.com/services/education'
    }
}


def generate_cert_section_html(data):
    """Génère le HTML pour la section certifications au format Cisco"""

    intro = data['intro']
    certs = data['certs']
    url = data['url']

    html = f'''<section class="review-section" id="certifications">
<h2><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 15l-2 2-2-2m4-6l2-2 2 2m-4 4V3m0 18v-6"/><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 12h8"/></svg> Recommended Certifications</h2>
<p style="margin-bottom: var(--space-xl); color: var(--text-secondary);">{intro}</p>

<div class="certifications-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-lg); margin: var(--space-xl) 0; position: relative; z-index: 1000;">

'''

    for cert in certs:
        html += f'''<!-- {cert['name']} -->
<div class="cert-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: var(--space-lg); text-decoration: none; display: block; position: relative; z-index: 1001;">
<div style="text-align: center; margin-bottom: var(--space-md);">
<img src="../../../assets/images/certifications/{cert['image']}" alt="{cert['name']} Badge" style="width: 100px; height: 100px; object-fit: contain;"/>
</div>
<h3 style="margin-bottom: var(--space-xs); color: var(--text-primary); font-size: var(--text-lg);">{cert['name']}</h3>
<div style="color: var(--accent-color); font-weight: 600; font-size: var(--text-sm); margin-bottom: var(--space-sm);">{cert['level']}</div>
<p style="color: var(--text-secondary); font-size: var(--text-sm); line-height: 1.5;">{cert['description']}</p>
<div style="margin-top: var(--space-md); padding-top: var(--space-md); border-top: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
<span style="color: var(--text-tertiary); font-size: var(--text-xs);">Exam: {cert['exam_code']}</span>
</div>
</div>

'''

    html += f'''</div>

<div style="background: var(--bg-tertiary); border-radius: var(--radius-lg); padding: var(--space-xl); margin-top: var(--space-xl);">
<h4 style="margin-bottom: var(--space-md);">📚 Get Started with Certification</h4>
<p style="margin-bottom: var(--space-md);">Official training and certification resources:</p>
<a href="{url}" class="btn btn-primary" target="_blank" rel="noopener noreferrer">Visit Certification Portal →</a>
</div>
</section>

'''

    return html


def update_certification_section(file_path, new_content):
    """Remplace la section certifications avec le nouveau contenu"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern pour trouver la section certifications complète
    pattern = r'<section class="review-section" id="certifications">.*?</section>\s*</section>'

    # Remplacer
    updated_content = re.sub(pattern, new_content + '</section>', content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)


# Main - Mettre à jour toutes les pages
base_path = '/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/reviews/cybersecurity/'

print("Mise à jour des sections certifications avec le format détaillé...\n")

for filename, data in CERTIFICATIONS_DETAILED.items():
    file_path = base_path + filename

    # Générer le nouveau HTML
    new_section = generate_cert_section_html(data)

    # Mettre à jour le fichier
    try:
        update_certification_section(file_path, new_section)
        print(f"✓ {filename}")
    except Exception as e:
        print(f"✗ {filename}: {e}")

print("\n✅ Toutes les pages ont été mises à jour avec succès!")
print("📊 Format: Logos + descriptions détaillées + exam codes")
print("🎨 Style: Format Cisco avec cartes de certification")
