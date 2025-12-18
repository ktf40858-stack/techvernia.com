#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# Dossier de sortie
output_dir = '/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/certifications/'

# Données détaillées pour toutes les certifications
certifications = {
    # JUNIPER CERTIFICATIONS
    "jncia-mistai": {
        "title": "JNCIA-MistAI Certification",
        "full_name": "Juniper Networks Certified Associate - Mist AI",
        "level": "Associate",
        "badge": "jncia-mistai.png",
        "vendor": "Juniper Networks",
        "exam_code": "JN0-452",
        "duration": "90 minutes",
        "questions": "65 questions",
        "passing_score": "65%",
        "cost": "$200 USD",
        "validity": "3 years",
        "rating": "4.7/5",
        "color": "#2DD4BF",
        "description": "The JNCIA-MistAI certification validates foundational knowledge of wireless LAN (WLAN) technology and Juniper's Mist AI platform. This entry-level credential demonstrates your understanding of AI-driven wireless networking, cloud management, and network automation.",
        "overview": [
            "The Juniper Networks Certified Associate - Mist AI (JNCIA-MistAI) certification is designed for WLAN technologists with introductory knowledge of Wi-Fi networks and Juniper Networks' Mist AI technologies. This certification validates basic understanding of WLAN technology, Mist AI features, and cloud-managed networking fundamentals.",
            "As organizations increasingly adopt AI-driven networking solutions, the JNCIA-MistAI credential provides a solid foundation for professionals looking to specialize in modern wireless infrastructure. The certification covers essential topics including Wi-Fi standards, Mist AI dashboard navigation, Access Point configuration, and basic troubleshooting techniques.",
            "This certification serves as the first step in the Juniper Mist AI certification path, preparing candidates for more advanced wireless networking roles and specialist-level certifications. It's ideal for network administrators, wireless engineers, and IT professionals transitioning to AI-powered network management."
        ],
        "topics": [
            "Wi-Fi Fundamentals: 802.11 standards, RF principles, channel planning, and wireless security basics",
            "Mist AI Platform: Cloud architecture, dashboard navigation, organization hierarchy, and site configuration",
            "Access Point Deployment: AP models, claiming procedures, configuration templates, and firmware management",
            "Client Connectivity: Authentication methods, WLAN profiles, PSK/802.1X, and guest access setup",
            "Network Services: DHCP, DNS, VLAN tagging, NAT, and basic QoS for wireless traffic",
            "Monitoring & Troubleshooting: Client insights, AP status monitoring, event logs, and basic packet captures"
        ],
        "why_matters": "JNCIA-MistAI certification demonstrates your ability to deploy and manage modern AI-driven wireless networks. With the explosive growth of IoT devices, mobile workforce, and cloud applications, organizations need professionals who understand cloud-managed Wi-Fi infrastructure. This certification validates skills in Mist AI's unique capabilities including AI-driven troubleshooting, proactive anomaly detection, and user experience optimization—making you valuable for enterprise wireless deployments.",
        "study_resources": [
            "Juniper Open Learning - Free online courses on Mist AI fundamentals and wireless networking",
            "Mist AI Documentation - Official product documentation, configuration guides, and best practices",
            "Juniper Learning Portal - Instructor-led training courses (JN452 - Mist AI, Associate)",
            "Mist AI Community Forums - Peer discussions, real-world scenarios, and troubleshooting tips",
            "Wi-Fi Alliance Resources - Understanding Wi-Fi 6/6E standards and certifications",
            "Practice Labs - Hands-on experience with Mist AI demo environment and trial accounts",
            "YouTube Channels - Juniper Networks official channel with Mist AI tutorials and demos"
        ],
        "career_paths": [
            "Wireless Network Engineer - Design and implement enterprise Wi-Fi solutions",
            "Network Operations Center (NOC) Technician - Monitor and troubleshoot wireless infrastructure",
            "IT Support Specialist - Provide technical support for wireless connectivity issues",
            "Cloud Network Administrator - Manage cloud-managed networking infrastructure",
            "Wireless Site Surveyor - Conduct RF surveys and optimize wireless coverage",
            "Junior Network Architect - Contribute to wireless network design and planning"
        ],
        "salary_range": "$55,000 - $85,000 USD annually (entry to mid-level positions)",
        "next_steps": "After earning JNCIA-MistAI, advance to JNCIS-MistAI Wireless for specialist-level expertise in complex wireless deployments, troubleshooting, and Mist AI automation features.",
        "credly_url": "https://www.credly.com/org/juniper-networks/badge/juniper-networks-certified-associate-mist-ai-jncia-mistai",
        "learning_url": "https://learningportal.juniper.net/juniper/user_activity_info.aspx?id=JUNIPER-OPEN-LEARNING"
    },

    "jncis-mistai-wireless": {
        "title": "JNCIS-MistAI Wireless Certification",
        "full_name": "Juniper Networks Certified Specialist - Mist AI Wireless",
        "level": "Specialist",
        "badge": "jncia-mistai.png",
        "vendor": "Juniper Networks",
        "exam_code": "JN0-1452",
        "duration": "120 minutes",
        "questions": "65 questions",
        "passing_score": "70%",
        "cost": "$300 USD",
        "validity": "3 years",
        "rating": "4.8/5",
        "color": "#2DD4BF",
        "description": "The JNCIS-MistAI Wireless certification validates specialist-level skills in deploying, configuring, and troubleshooting complex enterprise wireless networks using Juniper Mist AI technology. It demonstrates advanced proficiency in AI-driven network operations and automation.",
        "overview": [
            "The Juniper Networks Certified Specialist - Mist AI Wireless (JNCIS-MistAI Wireless) certification is designed for experienced wireless engineers who implement and manage large-scale Mist AI deployments. This specialist-level credential validates advanced skills in wireless design, RF optimization, security implementation, and leveraging Mist AI's machine learning capabilities.",
            "Candidates for this certification should have hands-on experience with multi-site Mist AI deployments, complex authentication schemes, advanced troubleshooting techniques, and integrating Mist AI with enterprise systems. The exam tests both theoretical knowledge and practical problem-solving abilities in real-world scenarios.",
            "This certification positions you as a subject matter expert in AI-driven wireless networking, capable of architecting high-performance, self-optimizing wireless infrastructures that provide exceptional user experiences across diverse environments including campuses, branch offices, and high-density venues."
        ],
        "topics": [
            "Advanced Wi-Fi Design: Multi-building campus planning, capacity analysis, high-density design, and RF modeling",
            "Mist AI Automation: Virtual Network Assistant (Marvis), AI-driven troubleshooting, proactive insights, and anomaly detection",
            "Enterprise Security: 802.1X/EAP methods, RADIUS integration, ClearPass/ISE integration, dynamic VLAN assignment, and certificate management",
            "Location Services: Mist SDK, virtual BLE beacons, wayfinding, asset tracking, and occupancy analytics",
            "Advanced Troubleshooting: Packet captures, roaming analysis, RF interference identification, Dynamic Packet Capture, and performance optimization",
            "Integration & APIs: Webhooks, RESTful APIs, SSO integration, directory services (Active Directory/LDAP), and third-party platform integration",
            "WAN Edge & SD-WAN: Mist Edge deployment, WAN uplink configuration, SRX integration, and branch office automation"
        ],
        "why_matters": "JNCIS-MistAI Wireless certification establishes you as an expert in next-generation wireless infrastructure. As enterprises adopt AI-driven networking to reduce operational costs and improve user experiences, specialists with Mist AI expertise are in high demand. This certification validates your ability to leverage machine learning for network optimization, automate troubleshooting workflows, and implement location-based services—skills critical for digital transformation initiatives.",
        "study_resources": [
            "Juniper Mist AI Specialist Training (JN1452) - Official instructor-led course covering all exam objectives",
            "Mist AI Academy - Advanced online courses on location services, automation, and Marvis AI",
            "Hands-On Labs - Production-like lab environments with multi-site configurations and integration scenarios",
            "Mist AI API Documentation - RESTful API guides for automation and third-party integrations",
            "Community Slack Channels - Direct access to Mist engineers and certified professionals for guidance",
            "Case Studies & White Papers - Real-world deployment scenarios and best practices from enterprise customers",
            "Practice Exams - Juniper-authorized practice tests to assess readiness and identify knowledge gaps"
        ],
        "career_paths": [
            "Senior Wireless Network Engineer - Lead enterprise wireless infrastructure projects",
            "Network Architect - Design complex multi-site wireless and wired network solutions",
            "Wireless Solutions Consultant - Provide expert consulting on wireless deployments and migrations",
            "Network Automation Engineer - Develop automation workflows using Mist AI APIs",
            "RF Engineer - Optimize wireless performance through advanced RF planning and analysis",
            "Technical Account Manager - Provide post-sales technical guidance for enterprise customers",
            "Pre-Sales Systems Engineer - Demonstrate and design Mist AI solutions for prospective clients"
        ],
        "salary_range": "$85,000 - $130,000 USD annually (mid to senior-level positions)",
        "next_steps": "Progress to JNCIP-MistAI for professional-level expertise in large-scale Mist AI architectures, advanced automation, and complex enterprise integrations.",
        "credly_url": "https://www.credly.com/org/juniper-networks/badge/juniper-networks-certified-specialist-mist-ai-wireless",
        "learning_url": "https://learningportal.juniper.net/juniper/user_activity_info.aspx?id=JUNIPER-MIST-AI-SPECIALIST"
    },

    "jncip-mistai": {
        "title": "JNCIP-MistAI Certification",
        "full_name": "Juniper Networks Certified Professional - Mist AI",
        "level": "Professional",
        "badge": "jncia-mistai.png",
        "vendor": "Juniper Networks",
        "exam_code": "JN0-2452",
        "duration": "150 minutes",
        "questions": "65 questions",
        "passing_score": "75%",
        "cost": "$400 USD",
        "validity": "3 years",
        "rating": "4.9/5",
        "color": "#2DD4BF",
        "description": "The JNCIP-MistAI certification validates professional-level expertise in architecting, implementing, and optimizing enterprise-scale Mist AI deployments with advanced automation, integration, and AI-driven operations.",
        "overview": [
            "The Juniper Networks Certified Professional - Mist AI (JNCIP-MistAI) represents the pinnacle of Mist AI wireless expertise. This professional-level certification validates your ability to design and implement large-scale, mission-critical wireless infrastructures leveraging the full capabilities of the Mist AI platform, including AI/ML-driven automation, predictive analytics, and seamless integration with enterprise ecosystems.",
            "Candidates for JNCIP-MistAI should have extensive experience managing multi-thousand-AP deployments, implementing complex automation workflows, integrating Mist with SD-WAN/SASE architectures, and leveraging Mist APIs for custom solutions. The exam challenges your ability to solve complex real-world problems and optimize network operations using advanced Mist AI features.",
            "This certification positions you as a thought leader in AI-driven networking, capable of transforming enterprise IT operations through intelligent automation, data-driven decision-making, and innovative use of location and occupancy analytics for business insights beyond traditional networking."
        ],
        "topics": [
            "Enterprise Architecture: Multi-tenant deployments, global template strategies, hierarchical org design, and scalability planning for 10,000+ APs",
            "Advanced AI/ML Operations: Marvis Actions automation, custom conversational AI queries, predictive maintenance, and AIOps workflow optimization",
            "Comprehensive Security: Zero Trust wireless architecture, micro-segmentation, threat detection integration (SIEM/EDR), and compliance automation",
            "Location Intelligence: Indoor positioning systems, real-time asset tracking, proximity tracing, occupancy heatmaps, and business analytics integration",
            "Full-Stack Integration: Mist AI with SRX (SD-WAN), Session Smart Router, Apstra (data center), third-party ITSM platforms (ServiceNow), and BI tools",
            "Performance Optimization: Advanced SLE troubleshooting, capacity planning, predictive failure analysis, and AI-driven configuration recommendations",
            "API Mastery & Automation: Python scripting for Mist APIs, webhook automation, CI/CD pipelines for network configs, and custom integrations",
            "Business Intelligence: Leveraging Mist data for user experience metrics, location-based services ROI, and executive dashboards"
        ],
        "why_matters": "JNCIP-MistAI certification establishes you as an elite network architect in the AI-driven networking domain. As enterprises undergo digital transformation and adopt cloud-first, AI-powered IT strategies, professionals with deep Mist AI expertise command premium compensation. This certification validates your ability to deliver measurable business outcomes through network automation, reduce MTTR by 90% using AI troubleshooting, and unlock new revenue streams through location-based services—making you indispensable for strategic IT initiatives.",
        "study_resources": [
            "Juniper Mist AI Professional Training (JN2452) - Advanced instructor-led course with real-world case studies",
            "Mist AI Advanced Labs - Hands-on labs covering multi-org deployments, API automation, and complex integrations",
            "Juniper Engineering Webinars - Direct learning from Mist product managers and principal engineers",
            "GitHub Repositories - Community-contributed Mist API scripts and automation examples",
            "Mist AI Partner Portal - Exclusive resources, architecture guides, and competitive positioning materials",
            "Industry Conferences - Juniper NXTWORK, Wireless Field Day, and Mist customer summit presentations",
            "Technical Documentation - Advanced configuration guides, API reference, and integration blueprints",
            "Mentorship Programs - Direct engagement with Mist SE team and certified professionals"
        ],
        "career_paths": [
            "Principal Network Architect - Design global enterprise network infrastructures",
            "Chief Network Engineer - Lead network engineering teams and set technical strategy",
            "Solutions Architect (Pre-Sales) - Design complex solutions for Fortune 500 customers",
            "Network Automation Architect - Build and maintain network automation frameworks",
            "Technical Evangelist - Represent Juniper/Mist at industry events and create thought leadership content",
            "Professional Services Consultant - Deliver high-value consulting for enterprise migrations and transformations",
            "Product Manager - Guide product development based on customer requirements and market trends"
        ],
        "salary_range": "$120,000 - $180,000 USD annually (senior to principal-level positions)",
        "next_steps": "Continue expanding expertise across Juniper's portfolio with certifications in SD-WAN (Mist WAN Edge), Data Center (Apstra), Security (SRX), or pursue leadership roles in network architecture and automation.",
        "credly_url": "https://www.credly.com/org/juniper-networks/badge/juniper-networks-certified-professional-mist-ai-jncip-mistai",
        "learning_url": "https://learningportal.juniper.net/juniper/user_activity_info.aspx?id=JUNIPER-MIST-AI-PROFESSIONAL"
    }
}

# Template HTML (similaire aux pages Cisco existantes)
def create_cert_page(cert_id, data):
    topics_html = ''.join([f'<li><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>{topic}</li>' for topic in data['topics']])

    resources_html = ''.join([f'<li><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>{resource}</li>' for resource in data['study_resources']])

    career_html = ''.join([f'<li><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="7.5 4.21 12 6.81 16.5 4.21"/><polyline points="7.5 19.79 7.5 14.6 3 12"/><polyline points="21 12 16.5 14.6 16.5 19.79"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" x2="12" y1="22.08" y2="12"/></svg>{career}</li>' for career in data['career_paths']])

    overview_html = ''.join([f'<p>{paragraph}</p>' for paragraph in data['overview']])

    html = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['title']} | GenuisNet.ai</title>
    <meta name="description" content="{data['description']}">
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="../../css/animations.css">
    <link rel="stylesheet" href="../../css/neon-icons.css">
    <style>
        .cert-hero {{
            padding: calc(80px + var(--space-4xl)) var(--space-lg) var(--space-3xl);
            background: linear-gradient(135deg, rgba(45, 212, 191, 0.08) 0%, transparent 50%);
            text-align: center;
        }}
        .cert-badge {{
            width: 180px;
            height: 180px;
            margin: 0 auto var(--space-xl);
            padding: var(--space-lg);
            background: var(--bg-card);
            border: 2px solid {data['color']};
            border-radius: var(--radius-xl);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 0 30px rgba(45, 212, 191, 0.3);
        }}
        .cert-badge img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
        }}
        .cert-level {{
            display: inline-block;
            padding: var(--space-sm) var(--space-lg);
            background: linear-gradient(135deg, {data['color']}22, {data['color']}11);
            border: 1px solid {data['color']};
            border-radius: var(--radius-full);
            color: {data['color']};
            font-weight: 600;
            margin-bottom: var(--space-lg);
        }}
        .exam-info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: var(--space-lg);
            margin: var(--space-2xl) 0;
        }}
        .exam-info-card {{
            padding: var(--space-lg);
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            text-align: center;
        }}
        .exam-info-card svg {{
            width: 32px;
            height: 32px;
            margin-bottom: var(--space-sm);
            color: {data['color']};
        }}
        .topics-list, .resources-list, .career-list {{
            list-style: none;
            padding: 0;
        }}
        .topics-list li, .resources-list li, .career-list li {{
            padding: var(--space-md) 0;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            align-items: flex-start;
            gap: var(--space-md);
        }}
        .topics-list li:last-child, .resources-list li:last-child, .career-list li:last-child {{
            border-bottom: none;
        }}
        .topics-list li svg, .resources-list li svg, .career-list li svg {{
            width: 20px;
            height: 20px;
            flex-shrink: 0;
            margin-top: 2px;
            color: {data['color']};
        }}
        .cta-section {{
            margin-top: var(--space-4xl);
            padding: var(--space-2xl);
            background: linear-gradient(135deg, rgba(45, 212, 191, 0.05) 0%, rgba(0, 80, 115, 0.02) 100%);
            border-radius: var(--radius-lg);
            border-left: 4px solid {data['color']};
            text-align: center;
        }}
        .btn-group {{
            display: flex;
            gap: var(--space-md);
            justify-content: center;
            flex-wrap: wrap;
            margin-top: var(--space-xl);
        }}
    </style>
</head>
<body>
    <canvas id="neural-bg"></canvas>
    <div id="particles-container"></div>

    <!-- Navigation -->
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="../../index.html" class="logo">
                <img src="../../assets/images/logo-neon.svg" alt="GenuisNet.ai" style="height: 50px; width: auto;">
            </a>
            <ul class="nav-menu" id="nav-menu">
                <li class="nav-item"><a href="../../index.html" class="nav-link" data-i18n="nav.home">Home</a></li>
                <li class="nav-item"><a href="../categories/ai-networking.html" class="nav-link">Categories</a></li>
                <li class="nav-item"><a href="../guides.html" class="nav-link"><span data-i18n="nav.guides">Guides</span></a></li>
                <li class="nav-item"><a href="../comparisons.html" class="nav-link"><span data-i18n="nav.compare">Compare</span></a></li>
                <li class="nav-item"><a href="../about.html" class="nav-link"><span data-i18n="nav.about">About</span></a></li>
            </ul>
            <div class="nav-actions">
                <div class="language-selector">
                    <button class="lang-btn" id="lang-btn" aria-label="Select Language">
                        <span class="lang-icon"><svg class="neon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg></span>
                        <span class="lang-current">EN</span>
                        <svg class="chevron" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"></path></svg>
                    </button>
                    <div class="lang-dropdown" id="lang-dropdown">
                        <button class="lang-option active" data-lang="en"><span class="flag">🇺🇸</span> English</button>
                        <button class="lang-option" data-lang="es"><span class="flag">🇪🇸</span> Español</button>
                        <button class="lang-option" data-lang="fr"><span class="flag">🇫🇷</span> Français</button>
                        <button class="lang-option" data-lang="de"><span class="flag">🇩🇪</span> Deutsch</button>
                        <button class="lang-option" data-lang="pt"><span class="flag">🇧🇷</span> Português</button>
                    </div>
                </div>
                <button class="theme-toggle" id="theme-toggle" aria-label="Toggle Theme">
                    <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"></path></svg>
                    <svg class="moon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
                </button>
                <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu"><span></span><span></span><span></span></button>
            </div>
        </div>
    </nav>

    <!-- Hero -->
    <header class="cert-hero">
        <div class="container">
            <div class="cert-badge">
                <img src="../../assets/images/certifications/{data['badge']}" alt="{data['full_name']} Badge">
            </div>
            <div class="cert-level">{data['level']} Level</div>
            <h1>{data['full_name']}</h1>
            <p style="font-size: var(--text-lg); color: var(--text-secondary); max-width: 800px; margin: var(--space-lg) auto 0;">{data['description']}</p>
        </div>
    </header>

    <!-- Main Content -->
    <section class="section">
        <div class="container" style="max-width: 900px;">

            <!-- Exam Information -->
            <h2><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg> Exam Information</h2>
            <div class="exam-info-grid">
                <div class="exam-info-card">
                    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                    <div style="font-size: var(--text-sm); color: var(--text-tertiary); margin-bottom: var(--space-xs);">Exam Code</div>
                    <div style="font-weight: 600; color: var(--text-primary);">{data['exam_code']}</div>
                </div>
                <div class="exam-info-card">
                    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                    <div style="font-size: var(--text-sm); color: var(--text-tertiary); margin-bottom: var(--space-xs);">Duration</div>
                    <div style="font-weight: 600; color: var(--text-primary);">{data['duration']}</div>
                </div>
                <div class="exam-info-card">
                    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/></svg>
                    <div style="font-size: var(--text-sm); color: var(--text-tertiary); margin-bottom: var(--space-xs);">Format</div>
                    <div style="font-weight: 600; color: var(--text-primary);">{data['questions']}</div>
                </div>
                <div class="exam-info-card">
                    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    <div style="font-size: var(--text-sm); color: var(--text-tertiary); margin-bottom: var(--space-xs);">Passing Score</div>
                    <div style="font-weight: 600; color: var(--text-primary);">{data['passing_score']}</div>
                </div>
                <div class="exam-info-card">
                    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                    <div style="font-size: var(--text-sm); color: var(--text-tertiary); margin-bottom: var(--space-xs);">Cost</div>
                    <div style="font-weight: 600; color: var(--text-primary);">{data['cost']}</div>
                </div>
                <div class="exam-info-card">
                    <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                    <div style="font-size: var(--text-sm); color: var(--text-tertiary); margin-bottom: var(--space-xs);">Validity</div>
                    <div style="font-weight: 600; color: var(--text-primary);">{data['validity']}</div>
                </div>
            </div>

            <!-- Overview -->
            <h2 style="margin-top: var(--space-4xl);"><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg> Overview</h2>
            <div style="line-height: 1.8; color: var(--text-secondary);">
                {overview_html}
            </div>

            <!-- Key Topics -->
            <h2 style="margin-top: var(--space-4xl);"><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg> Key Topics Covered</h2>
            <ul class="topics-list">
                {topics_html}
            </ul>

            <!-- Why It Matters -->
            <h2 style="margin-top: var(--space-4xl);"><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09zM12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/></svg> Why This Certification Matters</h2>
            <p style="line-height: 1.8; color: var(--text-secondary);">{data['why_matters']}</p>

            <!-- Study Resources -->
            <h2 style="margin-top: var(--space-4xl);"><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg> Study Resources</h2>
            <ul class="resources-list">
                {resources_html}
            </ul>

            <!-- Career Paths -->
            <h2 style="margin-top: var(--space-4xl);"><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="8.5" cy="7" r="4"/><polyline points="17 11 19 13 23 9"/></svg> Career Opportunities</h2>
            <ul class="career-list">
                {career_html}
            </ul>

            <!-- Salary Range -->
            <h2 style="margin-top: var(--space-4xl);"><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg> Salary Range</h2>
            <p style="line-height: 1.8; color: var(--text-secondary); padding: var(--space-lg); background: var(--bg-card); border-radius: var(--radius-lg); border-left: 4px solid {data['color']};">
                <strong>{data['salary_range']}</strong><br><br>
                <span style="font-size: var(--text-sm);">Note: Salary varies based on location, experience, and company size. These figures represent typical ranges in North America for professionals holding this certification.</span>
            </p>

            <!-- Next Steps -->
            <div class="cta-section">
                <h2><svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg> Next Steps</h2>
                <p style="line-height: 1.8; color: var(--text-secondary); margin-bottom: var(--space-xl);">{data['next_steps']}</p>
                <div class="btn-group">
                    <a href="{data['credly_url']}" class="btn btn-primary" target="_blank" rel="nofollow">
                        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="width: 20px; height: 20px; margin-right: 8px;"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                        View on Credly
                    </a>
                    <a href="{data['learning_url']}" class="btn btn-secondary" target="_blank" rel="nofollow">
                        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="width: 20px; height: 20px; margin-right: 8px;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
                        Start Learning
                    </a>
                    <a href="../categories/ai-networking.html" class="btn btn-secondary">
                        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="width: 20px; height: 20px; margin-right: 8px;"><polyline points="15 18 9 12 15 6"/></svg>
                        Back to Networking
                    </a>
                </div>
            </div>

        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="../../index.html" class="footer-logo">
                        <img src="../../assets/images/logo-neon.svg" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">
                    </a>
                    <p class="footer-desc">Your trusted source for AI tool reviews, comparisons, and guides.</p>
                </div>
                <div class="footer-links">
                    <h4>Categories</h4>
                    <ul>
                        <li><a href="../categories/ai-chatbots.html">AI Chatbots</a></li>
                        <li><a href="../categories/ai-coding.html">AI Coding</a></li>
                        <li><a href="../categories/ai-networking.html">AI Networking</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Resources</h4>
                    <ul>
                        <li><a href="../guides.html"><span data-i18n="nav.guides">Guides</span></a></li>
                        <li><a href="../comparisons.html">Comparisons</a></li>
                        <li><a href="../about.html"><span data-i18n="nav.about">About</span></a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p class="copyright">© 2026 GenuisNet.ai. All rights reserved.</p>
                <p class="affiliate-notice">Some links may be affiliate links.</p>
            </div>
        </div>
    </footer>

    <script src="../../js/i18n.js"></script>
    <script src="../../js/auto-translate.js"></script>
    <script src="../../js/animations.js"></script>
    <script src="../../js/main.js"></script>
</body>
</html>'''

    return html

# Générer les 3 premières pages Juniper
for cert_id, cert_data in certifications.items():
    filename = f"{cert_id}.html"
    filepath = os.path.join(output_dir, filename)

    html_content = create_cert_page(cert_id, cert_data)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f'✅ {filename} créé - {cert_data["full_name"]}')

print('\n✅ 3 pages de certification Juniper créées!')
print('Continuer avec Ansible, Terraform, Splunk et Zabbix...')
