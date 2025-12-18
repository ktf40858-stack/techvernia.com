#!/usr/bin/env python3
"""
Génère toutes les 37 pages de certification restantes
"""

from pathlib import Path

def create_cert_html(cert_data):
    """Génère le HTML pour une page de certification"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{cert_data['name']} - {cert_data['vendor']} Certification | GenuisNet.ai</title>
    <meta name="description" content="Comprehensive guide to {cert_data['full_name']} certification. Learn about exam requirements, study resources, and career opportunities.">
    <link rel="stylesheet" href="../../assets/css/styles.css">
    <link rel="stylesheet" href="../../assets/css/theme.css">
    <link rel="stylesheet" href="../../assets/css/components.css">
    <link rel="icon" type="image/svg+xml" href="../../assets/images/logo-neon.svg">
    <style>
        :root {{
            --brand-color: {cert_data['brand_color']};
        }}

        .cert-hero {{
            background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--bg-primary) 100%);
            padding: var(--space-2xl) var(--space-lg);
            border-radius: var(--radius-lg);
            margin-bottom: var(--space-xl);
            border: 1px solid var(--border-color);
            text-align: center;
        }}

        .cert-badge {{
            width: 180px;
            height: 180px;
            margin: 0 auto var(--space-lg);
            filter: drop-shadow(0 0 20px rgba(var(--accent-rgb), 0.3));
        }}

        .cert-meta {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: var(--space-md);
            margin-top: var(--space-lg);
        }}

        .cert-meta-item {{
            background: var(--bg-primary);
            padding: var(--space-md);
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
        }}

        .cert-meta-label {{
            font-size: var(--text-sm);
            color: var(--text-secondary);
            margin-bottom: var(--space-xs);
        }}

        .cert-meta-value {{
            font-size: var(--text-lg);
            font-weight: 600;
            color: var(--brand-color);
        }}

        .topics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: var(--space-md);
            margin-top: var(--space-lg);
        }}

        .topic-item {{
            background: var(--bg-secondary);
            padding: var(--space-md);
            border-radius: var(--radius-md);
            border-left: 3px solid var(--brand-color);
        }}

        .resource-list {{
            list-style: none;
            padding: 0;
        }}

        .resource-list li {{
            background: var(--bg-secondary);
            padding: var(--space-md);
            margin-bottom: var(--space-sm);
            border-radius: var(--radius-md);
            border-left: 3px solid var(--accent-color);
        }}

        .career-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: var(--space-md);
            margin-top: var(--space-lg);
        }}

        .career-card {{
            background: var(--bg-secondary);
            padding: var(--space-lg);
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
        }}
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="main-nav">
        <div class="nav-container">
            <a href="../../index.html" class="nav-logo">
                <img src="../../assets/images/logo-neon.svg" alt="GenuisNet.ai Logo" class="logo-image">
                <span class="logo-text">GenuisNet.ai</span>
            </a>
            <ul class="nav-menu">
                <li><a href="../../index.html" class="nav-link" data-i18n="nav.home">Home</a></li>
                <li><a href="../categories.html" class="nav-link" data-i18n="nav.categories">Categories</a></li>
                <li><a href="../certifications.html" class="nav-link active" data-i18n="nav.certifications">Certifications</a></li>
                <li><a href="../about.html" class="nav-link" data-i18n="nav.about">About</a></li>
            </ul>
            <div class="nav-actions">
                <button id="theme-toggle" class="theme-toggle" aria-label="Toggle theme">
                    <svg class="sun-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                        <circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/>
                        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
                        <line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/>
                        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
                    </svg>
                    <svg class="moon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
                    </svg>
                </button>
                <select id="language-selector" class="language-selector">
                    <option value="en">EN</option>
                    <option value="fr">FR</option>
                    <option value="de">DE</option>
                    <option value="es">ES</option>
                </select>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="main-content">
        <div class="container">
            <!-- Breadcrumb -->
            <nav class="breadcrumb">
                <a href="../../index.html">Home</a>
                <span>/</span>
                <a href="../certifications.html">Certifications</a>
                <span>/</span>
                <span>{cert_data['name']}</span>
            </nav>

            <!-- Hero Section -->
            <div class="cert-hero">
                <img src="../../assets/images/certifications/{cert_data['badge']}" alt="{cert_data['name']} Badge" class="cert-badge">
                <h1>{cert_data['name']}</h1>
                <p class="subtitle">{cert_data['full_name']}</p>
                <div class="cert-level" style="color: var(--brand-color); font-size: var(--text-xl); font-weight: 600; margin-top: var(--space-md);">
                    {cert_data['level']} | {cert_data['vendor']}
                </div>

                <div class="cert-meta">
                    <div class="cert-meta-item">
                        <div class="cert-meta-label">Exam Code</div>
                        <div class="cert-meta-value">{cert_data['exam_code']}</div>
                    </div>
                    <div class="cert-meta-item">
                        <div class="cert-meta-label">Duration</div>
                        <div class="cert-meta-value">{cert_data['duration']}</div>
                    </div>
                    <div class="cert-meta-item">
                        <div class="cert-meta-label">Cost</div>
                        <div class="cert-meta-value">{cert_data['cost']}</div>
                    </div>
                    <div class="cert-meta-item">
                        <div class="cert-meta-label">Validity</div>
                        <div class="cert-meta-value">{cert_data['validity']}</div>
                    </div>
                </div>
            </div>

            <!-- Overview -->
            <section class="content-section">
                <h2>
                    <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                        <circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/>
                    </svg>
                    Overview
                </h2>
                {cert_data['overview']}
            </section>

            <!-- Key Topics -->
            <section class="content-section">
                <h2>
                    <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
                    </svg>
                    Key Topics Covered
                </h2>
                <div class="topics-grid">
"""

    for topic in cert_data['topics']:
        html += f"""                    <div class="topic-item">
                        <h3 style="color: var(--brand-color); margin-bottom: var(--space-sm);">{topic['title']}</h3>
                        <p>{topic['description']}</p>
                    </div>
"""

    html += f"""                </div>
            </section>

            <!-- Study Resources -->
            <section class="content-section">
                <h2>
                    <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                        <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
                    </svg>
                    Study Resources
                </h2>
                <ul class="resource-list">
"""

    for resource in cert_data['resources']:
        html += f"""                    <li>
                        <strong>{resource['title']}</strong><br>
                        {resource['description']}
                    </li>
"""

    html += f"""                </ul>
            </section>

            <!-- Career Opportunities -->
            <section class="content-section">
                <h2>
                    <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>
                    </svg>
                    Career Opportunities
                </h2>
                <div class="career-grid">
"""

    for career in cert_data['careers']:
        html += f"""                    <div class="career-card">
                        <h3 style="color: var(--accent-color);">{career}</h3>
                    </div>
"""

    html += f"""                </div>
                <div style="margin-top: var(--space-lg); padding: var(--space-lg); background: var(--bg-secondary); border-radius: var(--radius-md); border-left: 4px solid var(--brand-color);">
                    <strong>Average Salary Range:</strong> {cert_data['salary']}
                </div>
            </section>

            <!-- Next Steps -->
            <section class="content-section">
                <h2>
                    <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                        <polyline points="9 18 15 12 9 6"/>
                    </svg>
                    Next Steps
                </h2>
                <div style="background: var(--bg-secondary); padding: var(--space-xl); border-radius: var(--radius-md); border: 1px solid var(--border-color);">
                    <ol style="margin-left: var(--space-lg);">
                        <li style="margin-bottom: var(--space-md);">Review the official exam blueprint and objectives</li>
                        <li style="margin-bottom: var(--space-md);">Enroll in training courses and study materials</li>
                        <li style="margin-bottom: var(--space-md);">Get hands-on practice with {cert_data['vendor']} products</li>
                        <li style="margin-bottom: var(--space-md);">Take practice exams to assess readiness</li>
                        <li style="margin-bottom: var(--space-md);">Schedule your exam through the official portal</li>
                        <li>Maintain certification through continuing education</li>
                    </ol>
                    <div style="margin-top: var(--space-xl); text-align: center;">
                        <a href="{cert_data['vendor_url']}" class="btn btn-primary" target="_blank" rel="noopener">
                            Visit {cert_data['vendor']} Training Portal
                            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="width: 16px; height: 16px; display: inline; margin-left: 8px;">
                                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/>
                            </svg>
                        </a>
                    </div>
                </div>
            </section>
        </div>
    </main>

    <!-- Footer -->
    <footer class="main-footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>GenuisNet.ai</h3>
                    <p>Your trusted guide to AI tools and certifications</p>
                </div>
                <div class="footer-section">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="../../index.html">Home</a></li>
                        <li><a href="../categories.html">Categories</a></li>
                        <li><a href="../certifications.html">Certifications</a></li>
                        <li><a href="../about.html">About</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 GenuisNet.ai. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="../../assets/js/theme.js"></script>
    <script src="../../assets/js/i18n.js"></script>
</body>
</html>"""

    return html

# Données complètes pour les 37 certifications restantes
REMAINING_CERTS = {
    'fortinet-nse8': {
        'name': 'NSE 8 - Written Exam',
        'full_name': 'Fortinet Network Security Expert 8',
        'level': 'Master Level',
        'vendor': 'Fortinet',
        'brand_color': '#EE3124',
        'badge': 'fortinet-nse8.png',
        'exam_code': 'NSE8',
        'duration': '120 minutes',
        'cost': '$400 USD',
        'validity': '2 years',
        'vendor_url': 'https://training.fortinet.com/',
        'overview': '''<p>The NSE 8 certification represents the pinnacle of Fortinet security expertise, designed for senior network security professionals and architects who design, implement, and manage enterprise-scale Fortinet solutions.</p>
<p>This master-level certification validates your ability to architect complex security infrastructures, design multi-site deployments, and provide strategic guidance on Fortinet security solutions in large enterprise environments.</p>
<p>Earning NSE 8 demonstrates mastery-level knowledge of Fortinet products and positions you as a trusted security architect capable of handling the most challenging security implementations.</p>''',
        'topics': [
            {'title': 'Advanced Architecture Design', 'description': 'Design enterprise-scale security architectures using Fortinet solutions across multiple sites and cloud environments.'},
            {'title': 'Strategic Security Planning', 'description': 'Develop comprehensive security strategies aligned with business objectives and compliance requirements.'},
            {'title': 'Multi-Site Deployment', 'description': 'Architect and implement Fortinet solutions across geographically distributed enterprise networks.'},
            {'title': 'Performance Optimization', 'description': 'Design high-performance security infrastructures with advanced optimization techniques.'},
            {'title': 'Integration & Orchestration', 'description': 'Integrate Fortinet solutions with third-party systems and orchestrate security workflows.'},
            {'title': 'Advanced Troubleshooting', 'description': 'Diagnose and resolve complex security infrastructure issues in enterprise environments.'},
            {'title': 'Security Best Practices', 'description': 'Implement industry best practices for security architecture and deployment.'},
            {'title': 'Technical Leadership', 'description': 'Provide technical guidance and mentorship to security teams on Fortinet implementations.'}
        ],
        'resources': [
            {'title': 'NSE 8 Written Study Guide', 'description': 'Official Fortinet study materials covering all master-level exam objectives.'},
            {'title': 'Advanced Architecture Documentation', 'description': 'Enterprise deployment guides and architecture best practices from Fortinet.'},
            {'title': 'Fortinet Design Workshops', 'description': 'Hands-on workshops focusing on enterprise security architecture design.'},
            {'title': 'Technical Community Forums', 'description': 'Engage with Fortinet experts and NSE 8 certified professionals.'}
        ],
        'careers': [
            'Principal Security Architect',
            'Chief Security Officer',
            'Enterprise Security Consultant',
            'Security Infrastructure Director',
            'Senior Solutions Architect'
        ],
        'salary': '$140,000 - $200,000+ USD annually'
    },
    'paloalto-pccet': {
        'name': 'PCCET',
        'full_name': 'Palo Alto Networks Certified Cybersecurity Entry-level Technician',
        'level': 'Entry-Level Technician',
        'vendor': 'Palo Alto Networks',
        'brand_color': '#FA582D',
        'badge': 'paloalto-pccet.png',
        'exam_code': 'PCCET',
        'duration': '60 minutes',
        'cost': '$100 USD',
        'validity': '3 years',
        'vendor_url': 'https://www.paloaltonetworks.com/services/education',
        'overview': '''<p>The PCCET certification is your entry point into the world of cybersecurity with Palo Alto Networks. This foundational certification validates your understanding of essential cybersecurity concepts and Palo Alto Networks products.</p>
<p>Designed for beginners and career changers, PCCET provides a solid foundation in network security, cloud security, security operations, and security architecture fundamentals.</p>
<p>This certification is ideal for students, recent graduates, or professionals looking to transition into cybersecurity roles with one of the industry's leading security vendors.</p>''',
        'topics': [
            {'title': 'Cybersecurity Fundamentals', 'description': 'Core concepts of information security, threat landscape, and security principles.'},
            {'title': 'Network Security', 'description': 'Basic networking concepts, firewall technologies, and network protection mechanisms.'},
            {'title': 'Cloud Security Basics', 'description': 'Introduction to cloud computing and cloud security fundamentals.'},
            {'title': 'Security Operations', 'description': 'Fundamentals of security monitoring, incident response, and SOC operations.'},
            {'title': 'Palo Alto Products Overview', 'description': 'Introduction to Palo Alto Networks product portfolio and capabilities.'},
            {'title': 'Threat Prevention', 'description': 'Understanding malware, exploits, and threat prevention techniques.'}
        ],
        'resources': [
            {'title': 'PCCET Digital Learning', 'description': 'Free self-paced digital learning course from Palo Alto Networks.'},
            {'title': 'Cybersecurity Fundamentals Guide', 'description': 'Comprehensive guide covering all entry-level cybersecurity concepts.'},
            {'title': 'Practice Exams', 'description': 'Official practice tests to prepare for the PCCET exam.'},
            {'title': 'Palo Alto Learning Center', 'description': 'Access to product documentation and training videos.'}
        ],
        'careers': [
            'Junior Security Analyst',
            'SOC Analyst Level 1',
            'Help Desk Security Specialist',
            'Security Operations Assistant',
            'Cybersecurity Intern'
        ],
        'salary': '$45,000 - $65,000 USD annually'
    },
    'paloalto-pccsa': {
        'name': 'PCCSA',
        'full_name': 'Palo Alto Networks Certified Cybersecurity Associate',
        'level': 'Cybersecurity Associate',
        'vendor': 'Palo Alto Networks',
        'brand_color': '#FA582D',
        'badge': 'paloalto-pccsa.png',
        'exam_code': 'PCCSA',
        'duration': '80 minutes',
        'cost': '$200 USD',
        'validity': '3 years',
        'vendor_url': 'https://www.paloaltonetworks.com/services/education',
        'overview': '''<p>The PCCSA certification validates your skills in deploying and configuring Palo Alto Networks next-generation firewalls and operating the Cortex XSOAR platform for security orchestration and automation.</p>
<p>This associate-level certification demonstrates practical knowledge of implementing security policies, threat prevention, and security automation using Palo Alto Networks technologies.</p>
<p>PCCSA certification is ideal for security analysts and administrators who work with Palo Alto Networks products in daily security operations.</p>''',
        'topics': [
            {'title': 'Firewall Configuration', 'description': 'Deploy and configure Palo Alto Networks next-generation firewalls for network security.'},
            {'title': 'Security Policies', 'description': 'Create and manage security policies, NAT rules, and application-based policies.'},
            {'title': 'Threat Prevention', 'description': 'Configure and manage threat prevention profiles including antivirus, anti-spyware, and IPS.'},
            {'title': 'Cortex XSOAR', 'description': 'Operate and use Cortex XSOAR for security orchestration, automation, and response.'},
            {'title': 'Security Operations', 'description': 'Monitor security events, investigate incidents, and respond to threats.'},
            {'title': 'VPN Technologies', 'description': 'Configure site-to-site and remote access VPNs using Palo Alto firewalls.'},
            {'title': 'Logging & Reporting', 'description': 'Configure logging, generate reports, and analyze security data.'}
        ],
        'resources': [
            {'title': 'PCCSA Instructor-Led Training', 'description': 'Official training course covering firewall and Cortex XSOAR operations.'},
            {'title': 'Hands-On Lab Environment', 'description': 'Virtual labs for practicing firewall configuration and XSOAR automation.'},
            {'title': 'Configuration Guides', 'description': 'Step-by-step guides for common configuration scenarios.'},
            {'title': 'Certification Study Guide', 'description': 'Comprehensive study materials aligned with exam objectives.'}
        ],
        'careers': [
            'Security Operations Analyst',
            'Firewall Administrator',
            'Network Security Engineer',
            'SOC Analyst Level 2',
            'Security Automation Specialist'
        ],
        'salary': '$70,000 - $95,000 USD annually'
    },
    'paloalto-pccse': {
        'name': 'PCCSE',
        'full_name': 'Palo Alto Networks Certified Cybersecurity Engineer',
        'level': 'Cybersecurity Engineer',
        'vendor': 'Palo Alto Networks',
        'brand_color': '#FA582D',
        'badge': 'paloalto-pccse.png',
        'exam_code': 'PCCSE',
        'duration': '90 minutes',
        'cost': '$250 USD',
        'validity': '2 years',
        'vendor_url': 'https://www.paloaltonetworks.com/services/education',
        'overview': '''<p>The PCCSE certification validates advanced engineering skills in designing, deploying, and troubleshooting Palo Alto Networks security solutions in complex enterprise environments.</p>
<p>This engineer-level certification demonstrates expertise in implementing comprehensive security architectures using the full Palo Alto Networks product portfolio including firewalls, Panorama, and advanced security services.</p>
<p>PCCSE-certified professionals are recognized for their ability to handle complex security implementations and provide expert-level technical guidance.</p>''',
        'topics': [
            {'title': 'Advanced Firewall Deployment', 'description': 'Design and deploy enterprise-scale firewall architectures with high availability.'},
            {'title': 'Panorama Management', 'description': 'Configure centralized management using Panorama for multi-firewall environments.'},
            {'title': 'Advanced Threat Prevention', 'description': 'Implement advanced threat prevention including WildFire, URL filtering, and DNS security.'},
            {'title': 'Zone-Based Architecture', 'description': 'Design security zone architectures for complex network topologies.'},
            {'title': 'Advanced VPN', 'description': 'Configure complex VPN scenarios including hub-and-spoke and full-mesh topologies.'},
            {'title': 'Decryption & SSL Inspection', 'description': 'Implement SSL/TLS decryption and inspection for encrypted traffic.'},
            {'title': 'Performance Tuning', 'description': 'Optimize firewall performance for high-throughput environments.'},
            {'title': 'Advanced Troubleshooting', 'description': 'Diagnose and resolve complex firewall and security issues.'}
        ],
        'resources': [
            {'title': 'PCCSE Training Course', 'description': 'Advanced instructor-led training covering enterprise deployment scenarios.'},
            {'title': 'Enterprise Architecture Guide', 'description': 'Best practices for designing enterprise security architectures.'},
            {'title': 'Advanced Labs', 'description': 'Complex lab scenarios simulating enterprise environments.'},
            {'title': 'Technical Documentation', 'description': 'In-depth technical documentation for all advanced features.'}
        ],
        'careers': [
            'Senior Security Engineer',
            'Network Security Architect',
            'Principal Firewall Engineer',
            'Security Infrastructure Engineer',
            'Lead Security Consultant'
        ],
        'salary': '$95,000 - $140,000 USD annually'
    },
    'paloalto-pcsae': {
        'name': 'PCSAE',
        'full_name': 'Palo Alto Networks Certified Security Automation Engineer',
        'level': 'Security Automation Engineer',
        'vendor': 'Palo Alto Networks',
        'brand_color': '#FA582D',
        'badge': 'paloalto-pcsae.png',
        'exam_code': 'PCSAE',
        'duration': '90 minutes',
        'cost': '$250 USD',
        'validity': '2 years',
        'vendor_url': 'https://www.paloaltonetworks.com/services/education',
        'overview': '''<p>The PCSAE certification validates expertise in designing, building, and optimizing security automation playbooks using Cortex XSOAR. This specialized certification focuses on security orchestration, automation, and response (SOAR) capabilities.</p>
<p>PCSAE-certified engineers are experts in developing custom integrations, building complex automation workflows, and optimizing security operations through intelligent automation.</p>
<p>This certification is ideal for security engineers focused on improving SOC efficiency through automation and orchestration technologies.</p>''',
        'topics': [
            {'title': 'Playbook Development', 'description': 'Design and build advanced automation playbooks for incident response workflows.'},
            {'title': 'Custom Integrations', 'description': 'Develop custom integrations to connect Cortex XSOAR with third-party systems.'},
            {'title': 'Scripting & Automation', 'description': 'Write Python scripts and automation tasks within the XSOAR platform.'},
            {'title': 'Incident Management', 'description': 'Automate incident classification, investigation, and remediation processes.'},
            {'title': 'SOAR Best Practices', 'description': 'Implement best practices for security orchestration and automation.'},
            {'title': 'Performance Optimization', 'description': 'Optimize playbook performance and resource utilization.'},
            {'title': 'Content Management', 'description': 'Manage and version control automation content and playbooks.'},
            {'title': 'Metrics & Reporting', 'description': 'Build dashboards and reports to measure automation effectiveness.'}
        ],
        'resources': [
            {'title': 'PCSAE Development Course', 'description': 'Comprehensive training on XSOAR development and automation.'},
            {'title': 'Python for XSOAR', 'description': 'Python scripting guide specifically for Cortex XSOAR automation.'},
            {'title': 'Integration Development Kit', 'description': 'Tools and documentation for building custom integrations.'},
            {'title': 'Playbook Library', 'description': 'Example playbooks and automation workflows for reference.'}
        ],
        'careers': [
            'Security Automation Engineer',
            'SOAR Developer',
            'Security Orchestration Specialist',
            'SOC Automation Architect',
            'DevSecOps Engineer'
        ],
        'salary': '$90,000 - $135,000 USD annually'
    },
    'microsoft-sc900': {
        'name': 'SC-900',
        'full_name': 'Microsoft Security, Compliance, and Identity Fundamentals',
        'level': 'Security Fundamentals',
        'vendor': 'Microsoft',
        'brand_color': '#00A4EF',
        'badge': 'microsoft-sc900.png',
        'exam_code': 'SC-900',
        'duration': '60 minutes',
        'cost': '$99 USD',
        'validity': 'Does not expire',
        'vendor_url': 'https://learn.microsoft.com/certifications/',
        'overview': '''<p>The SC-900 certification provides a foundational understanding of security, compliance, and identity concepts within Microsoft cloud services. This entry-level certification is perfect for those beginning their journey in Microsoft security technologies.</p>
<p>You'll learn about core security concepts, Microsoft security and compliance solutions, and identity and access management capabilities across Microsoft 365 and Azure.</p>
<p>This certification is ideal for students, business users, or IT professionals seeking to understand the fundamentals of Microsoft's security ecosystem.</p>''',
        'topics': [
            {'title': 'Security Concepts', 'description': 'Understand core security concepts including Zero Trust, shared responsibility, and defense in depth.'},
            {'title': 'Identity & Access', 'description': 'Learn about authentication, authorization, and identity management with Azure AD.'},
            {'title': 'Microsoft Security Solutions', 'description': 'Overview of Microsoft security solutions including Defender and Sentinel.'},
            {'title': 'Compliance Concepts', 'description': 'Understand compliance management, data governance, and privacy concepts.'},
            {'title': 'Microsoft Compliance Tools', 'description': 'Introduction to Microsoft Purview and compliance management capabilities.'},
            {'title': 'Threat Protection', 'description': 'Basics of threat protection and security management in Microsoft 365.'}
        ],
        'resources': [
            {'title': 'Microsoft Learn Path', 'description': 'Free self-paced learning path covering all SC-900 objectives.'},
            {'title': 'Study Guide', 'description': 'Official exam study guide from Microsoft.'},
            {'title': 'Practice Assessment', 'description': 'Free practice test to assess readiness.'},
            {'title': 'Documentation', 'description': 'Microsoft security documentation and white papers.'}
        ],
        'careers': [
            'IT Support Specialist',
            'Junior Security Analyst',
            'Compliance Coordinator',
            'Help Desk Technician',
            'Cloud Support Associate'
        ],
        'salary': '$45,000 - $70,000 USD annually'
    },
    'microsoft-sc300': {
        'name': 'SC-300',
        'full_name': 'Microsoft Identity and Access Administrator',
        'level': 'Identity Administrator',
        'vendor': 'Microsoft',
        'brand_color': '#00A4EF',
        'badge': 'microsoft-sc300.png',
        'exam_code': 'SC-300',
        'duration': '120 minutes',
        'cost': '$165 USD',
        'validity': '1 year',
        'vendor_url': 'https://learn.microsoft.com/certifications/',
        'overview': '''<p>The SC-300 certification validates your ability to design, implement, and operate identity and access management systems using Azure Active Directory (Azure AD) and related Microsoft identity technologies.</p>
<p>You'll demonstrate expertise in implementing and managing secure authentication, authorization, conditional access, and identity governance across Microsoft cloud and hybrid environments.</p>
<p>This certification is essential for identity administrators responsible for managing enterprise identity infrastructures using Microsoft technologies.</p>''',
        'topics': [
            {'title': 'Azure AD Implementation', 'description': 'Deploy and configure Azure Active Directory for enterprise environments.'},
            {'title': 'Authentication Solutions', 'description': 'Implement multi-factor authentication, passwordless authentication, and SSO.'},
            {'title': 'Conditional Access', 'description': 'Design and implement conditional access policies for Zero Trust security.'},
            {'title': 'Identity Governance', 'description': 'Manage identity lifecycle, access reviews, and privileged identity management.'},
            {'title': 'Application Integration', 'description': 'Integrate applications with Azure AD for secure authentication and authorization.'},
            {'title': 'B2B & B2C', 'description': 'Configure Azure AD B2B collaboration and B2C customer identity solutions.'},
            {'title': 'Identity Protection', 'description': 'Implement Azure AD Identity Protection for risk-based policies.'},
            {'title': 'Monitoring & Reporting', 'description': 'Monitor identity activities and generate compliance reports.'}
        ],
        'resources': [
            {'title': 'SC-300 Learning Path', 'description': 'Comprehensive Microsoft Learn modules for identity administrators.'},
            {'title': 'Hands-On Labs', 'description': 'Azure sandbox environments for practicing identity configurations.'},
            {'title': 'Instructor-Led Training', 'description': 'Official Microsoft training course for SC-300.'},
            {'title': 'Practice Tests', 'description': 'Full-length practice exams with detailed explanations.'}
        ],
        'careers': [
            'Identity Administrator',
            'Azure AD Specialist',
            'IAM Engineer',
            'Security Architect',
            'Cloud Identity Consultant'
        ],
        'salary': '$85,000 - $125,000 USD annually'
    },
    'microsoft-sc400': {
        'name': 'SC-400',
        'full_name': 'Microsoft Information Protection Administrator',
        'level': 'Information Protection',
        'vendor': 'Microsoft',
        'brand_color': '#00A4EF',
        'badge': 'microsoft-sc400.png',
        'exam_code': 'SC-400',
        'duration': '120 minutes',
        'cost': '$165 USD',
        'validity': '1 year',
        'vendor_url': 'https://learn.microsoft.com/certifications/',
        'overview': '''<p>The SC-400 certification demonstrates your expertise in implementing and managing information protection and data loss prevention within Microsoft 365 and Azure environments.</p>
<p>You'll validate skills in protecting sensitive information, preventing data loss, managing data lifecycle, and ensuring compliance with data governance requirements using Microsoft Purview.</p>
<p>This certification is crucial for information protection administrators responsible for securing organizational data and ensuring regulatory compliance.</p>''',
        'topics': [
            {'title': 'Information Protection', 'description': 'Implement sensitivity labels, encryption, and rights management for data protection.'},
            {'title': 'Data Loss Prevention', 'description': 'Configure DLP policies to prevent unauthorized data sharing and exfiltration.'},
            {'title': 'Data Lifecycle Management', 'description': 'Manage retention policies, labels, and data disposition across Microsoft 365.'},
            {'title': 'Insider Risk Management', 'description': 'Detect and investigate insider risks using Microsoft Purview.'},
            {'title': 'eDiscovery', 'description': 'Manage eDiscovery cases and legal hold for compliance investigations.'},
            {'title': 'Data Governance', 'description': 'Implement data governance policies and classify sensitive information.'},
            {'title': 'Compliance Monitoring', 'description': 'Monitor compliance posture and generate audit reports.'},
            {'title': 'Records Management', 'description': 'Configure records management for regulatory compliance.'}
        ],
        'resources': [
            {'title': 'SC-400 Learning Path', 'description': 'Microsoft Learn modules covering all information protection topics.'},
            {'title': 'Purview Documentation', 'description': 'Comprehensive documentation for Microsoft Purview capabilities.'},
            {'title': 'Training Course', 'description': 'Official instructor-led training for SC-400 preparation.'},
            {'title': 'Lab Simulations', 'description': 'Hands-on lab environments for practicing information protection.'}
        ],
        'careers': [
            'Information Protection Administrator',
            'Data Governance Specialist',
            'Compliance Manager',
            'Data Privacy Officer',
            'Security Compliance Analyst'
        ],
        'salary': '$80,000 - $120,000 USD annually'
    },
    'microsoft-az500': {
        'name': 'AZ-500',
        'full_name': 'Microsoft Azure Security Engineer',
        'level': 'Azure Security',
        'vendor': 'Microsoft',
        'brand_color': '#00A4EF',
        'badge': 'microsoft-az500.png',
        'exam_code': 'AZ-500',
        'duration': '120 minutes',
        'cost': '$165 USD',
        'validity': '1 year',
        'vendor_url': 'https://learn.microsoft.com/certifications/',
        'overview': '''<p>The AZ-500 certification validates your ability to implement security controls and threat protection across Azure cloud environments. This role-based certification demonstrates expertise in securing Azure workloads and managing security operations.</p>
<p>You'll prove skills in implementing identity and access management, platform protection, security operations, and data and application security within Azure infrastructure.</p>
<p>This certification is essential for Azure security engineers responsible for protecting cloud environments and ensuring compliance in Azure deployments.</p>''',
        'topics': [
            {'title': 'Identity & Access', 'description': 'Implement Azure AD security, conditional access, and privileged identity management.'},
            {'title': 'Platform Protection', 'description': 'Secure network infrastructure, compute resources, and storage in Azure.'},
            {'title': 'Security Operations', 'description': 'Configure Microsoft Sentinel, monitor security events, and respond to incidents.'},
            {'title': 'Data & Applications', 'description': 'Implement security for applications, databases, and Key Vault.'},
            {'title': 'Network Security', 'description': 'Configure Azure Firewall, NSGs, Application Gateway, and DDoS protection.'},
            {'title': 'Threat Protection', 'description': 'Implement Microsoft Defender for Cloud and security baselines.'},
            {'title': 'Compliance & Governance', 'description': 'Manage Azure Policy, Blueprints, and compliance frameworks.'},
            {'title': 'Security Monitoring', 'description': 'Monitor and analyze security logs using Azure Monitor and Log Analytics.'}
        ],
        'resources': [
            {'title': 'AZ-500 Learning Path', 'description': 'Complete Microsoft Learn path for Azure security engineers.'},
            {'title': 'Azure Security Labs', 'description': 'Hands-on lab exercises using Azure sandbox environments.'},
            {'title': 'Official Training', 'description': 'Microsoft Certified Trainer-led course for AZ-500.'},
            {'title': 'Practice Exams', 'description': 'Full-length practice tests with performance analytics.'}
        ],
        'careers': [
            'Azure Security Engineer',
            'Cloud Security Architect',
            'DevSecOps Engineer',
            'Cloud Security Consultant',
            'Security Operations Engineer'
        ],
        'salary': '$95,000 - $145,000 USD annually'
    },
    'cisco-cyberops': {
        'name': 'CyberOps Associate',
        'full_name': 'Cisco Certified CyberOps Associate',
        'level': 'Associate Level',
        'vendor': 'Cisco',
        'brand_color': '#1BA0D7',
        'badge': 'cisco-cyberops.png',
        'exam_code': '200-201 CBROPS',
        'duration': '120 minutes',
        'cost': '$300 USD',
        'validity': '3 years',
        'vendor_url': 'https://www.cisco.com/c/en/us/training-events/training-certifications/certifications.html',
        'overview': '''<p>The CyberOps Associate certification validates your knowledge and skills needed to successfully handle tasks, duties, and responsibilities of an associate-level Security Analyst working in a Security Operations Center (SOC).</p>
<p>You'll demonstrate understanding of security concepts, security monitoring, host-based analysis, network intrusion analysis, and security policies and procedures.</p>
<p>This certification prepares you for entry-level cybersecurity analyst positions focusing on threat detection, incident response, and security operations.</p>''',
        'topics': [
            {'title': 'Security Concepts', 'description': 'Understand security principles, attack methodologies, and defense strategies.'},
            {'title': 'Security Monitoring', 'description': 'Monitor security events using SIEM, IDS/IPS, and network monitoring tools.'},
            {'title': 'Host-Based Analysis', 'description': 'Analyze endpoint security events and investigate host-based threats.'},
            {'title': 'Network Intrusion Analysis', 'description': 'Detect and analyze network-based attacks and intrusions.'},
            {'title': 'Security Event Analysis', 'description': 'Investigate security alerts and determine incident severity.'},
            {'title': 'Incident Response', 'description': 'Follow incident response procedures and document security incidents.'},
            {'title': 'Forensics Fundamentals', 'description': 'Collect and preserve evidence for security investigations.'},
            {'title': 'Security Tools', 'description': 'Utilize various security tools for monitoring and analysis.'}
        ],
        'resources': [
            {'title': 'CyberOps Associate Training', 'description': 'Official Cisco training course covering all exam objectives.'},
            {'title': 'NetAcad Course', 'description': 'Cisco Networking Academy CyberOps curriculum.'},
            {'title': 'Virtual Lab Access', 'description': 'Hands-on virtual labs for practicing SOC operations.'},
            {'title': 'Study Materials', 'description': 'Official cert guide and practice questions.'}
        ],
        'careers': [
            'SOC Analyst',
            'Security Operations Analyst',
            'Cybersecurity Analyst',
            'Incident Response Analyst',
            'Threat Detection Specialist'
        ],
        'salary': '$65,000 - $90,000 USD annually'
    },
    'cisco-ccnp-security': {
        'name': 'CCNP Security',
        'full_name': 'Cisco Certified Network Professional Security',
        'level': 'Professional Level',
        'vendor': 'Cisco',
        'brand_color': '#1BA0D7',
        'badge': 'cisco-ccnp-security.png',
        'exam_code': '350-701 SCOR',
        'duration': '120 minutes',
        'cost': '$400 USD',
        'validity': '3 years',
        'vendor_url': 'https://www.cisco.com/c/en/us/training-events/training-certifications/certifications.html',
        'overview': '''<p>The CCNP Security certification validates the knowledge and skills required to implement and operate core security technologies including secure network access, VPN, firewall, intrusion prevention, and web and email security.</p>
<p>You'll demonstrate expertise in deploying Cisco security solutions, implementing security policies, and maintaining security infrastructure in enterprise environments.</p>
<p>This professional-level certification is essential for network security engineers managing Cisco security technologies.</p>''',
        'topics': [
            {'title': 'Network Security', 'description': 'Implement network security concepts including segmentation and access control.'},
            {'title': 'Cisco Firepower', 'description': 'Deploy and configure Cisco Firepower NGFW and NGIPS solutions.'},
            {'title': 'VPN Technologies', 'description': 'Implement site-to-site and remote access VPN using Cisco technologies.'},
            {'title': 'Secure Network Access', 'description': 'Configure ISE for network access control and 802.1X authentication.'},
            {'title': 'Cloud Security', 'description': 'Implement security for cloud-based and hybrid environments.'},
            {'title': 'Threat Defense', 'description': 'Configure advanced malware protection and threat intelligence.'},
            {'title': 'Endpoint Security', 'description': 'Deploy endpoint security solutions including AMP and ClamAV.'},
            {'title': 'Security Management', 'description': 'Manage security policies using Cisco security management tools.'}
        ],
        'resources': [
            {'title': 'CCNP Security Training', 'description': 'Official Cisco instructor-led training for CCNP Security.'},
            {'title': 'Certification Guide', 'description': 'Comprehensive study guide covering all exam topics.'},
            {'title': 'Lab Environment', 'description': 'Access to Cisco VIRL or CML for hands-on practice.'},
            {'title': 'Practice Tests', 'description': 'Full-length practice exams from Cisco Press.'}
        ],
        'careers': [
            'Network Security Engineer',
            'Security Infrastructure Engineer',
            'Firewall Administrator',
            'Security Architect',
            'Senior Security Consultant'
        ],
        'salary': '$90,000 - $130,000 USD annually'
    },
    'cisco-ccie-security': {
        'name': 'CCIE Security',
        'full_name': 'Cisco Certified Internetwork Expert Security',
        'level': 'Expert Level',
        'vendor': 'Cisco',
        'brand_color': '#1BA0D7',
        'badge': 'cisco-ccie-security.png',
        'exam_code': 'CCIE Security Lab',
        'duration': '8 hours (lab exam)',
        'cost': '$1,600 USD (lab exam)',
        'validity': '3 years',
        'vendor_url': 'https://www.cisco.com/c/en/us/training-events/training-certifications/certifications.html',
        'overview': '''<p>The CCIE Security certification represents the highest level of achievement in Cisco security expertise. This expert-level certification validates your ability to design, deploy, operate, and optimize complex security infrastructures.</p>
<p>You'll demonstrate mastery-level knowledge of security solutions including network security, cloud security, content security, endpoint protection, and secure network access across large-scale enterprise environments.</p>
<p>Earning CCIE Security positions you as an elite security expert recognized globally for technical excellence and problem-solving abilities.</p>''',
        'topics': [
            {'title': 'Advanced Network Security', 'description': 'Design and implement complex security architectures for enterprise networks.'},
            {'title': 'Firepower NGFW/NGIPS', 'description': 'Deploy advanced Firepower solutions with custom security policies.'},
            {'title': 'Identity Services Engine', 'description': 'Implement complex ISE deployments with advanced policies and integrations.'},
            {'title': 'Advanced VPN', 'description': 'Configure complex VPN topologies including FlexVPN and DMVPN.'},
            {'title': 'Cloud Security Architecture', 'description': 'Design security for multi-cloud and hybrid cloud environments.'},
            {'title': 'Advanced Threat Protection', 'description': 'Implement comprehensive threat protection and incident response.'},
            {'title': 'Secure Email & Web', 'description': 'Deploy and optimize Email Security Appliance and Web Security Appliance.'},
            {'title': 'Troubleshooting', 'description': 'Advanced troubleshooting of complex security infrastructure issues.'}
        ],
        'resources': [
            {'title': 'CCIE Security Lab Training', 'description': 'Advanced lab training for CCIE candidates.'},
            {'title': 'Mock Lab Sessions', 'description': '8-hour mock lab exams simulating real CCIE lab environment.'},
            {'title': 'Expert-Level Documentation', 'description': 'In-depth technical documentation for all security products.'},
            {'title': 'Mentoring Programs', 'description': 'One-on-one mentoring from CCIE Security experts.'}
        ],
        'careers': [
            'Principal Security Engineer',
            'Chief Security Architect',
            'Distinguished Engineer',
            'Security Practice Director',
            'Technical Solutions Architect'
        ],
        'salary': '$130,000 - $200,000+ USD annually'
    },
    'crowdstrike-ccfr': {
        'name': 'CCFR',
        'full_name': 'CrowdStrike Certified Falcon Responder',
        'level': 'Falcon Responder',
        'vendor': 'CrowdStrike',
        'brand_color': '#E01F3D',
        'badge': 'crowdstrike-ccfr.png',
        'exam_code': 'CCFR',
        'duration': '90 minutes',
        'cost': 'Contact CrowdStrike Sales',
        'validity': '2 years',
        'vendor_url': 'https://www.crowdstrike.com/university/',
        'overview': '''<p>The CCFR certification validates your ability to effectively use CrowdStrike Falcon platform for incident response and threat remediation. This certification focuses on responding to and containing security incidents using CrowdStrike technologies.</p>
<p>You'll demonstrate skills in investigating detections, performing host containment, analyzing forensic data, and executing response actions using the Falcon platform.</p>
<p>This certification is ideal for incident responders and SOC analysts who use CrowdStrike Falcon for threat detection and response operations.</p>''',
        'topics': [
            {'title': 'Incident Investigation', 'description': 'Investigate security detections and alerts in the Falcon platform.'},
            {'title': 'Host Containment', 'description': 'Execute network containment and isolation for compromised endpoints.'},
            {'title': 'Real-Time Response', 'description': 'Use Real Time Response (RTR) for live endpoint investigation and remediation.'},
            {'title': 'Forensic Analysis', 'description': 'Analyze endpoint forensic data and timeline of events.'},
            {'title': 'Detection Management', 'description': 'Manage and respond to various detection types including malware and IOAs.'},
            {'title': 'Response Actions', 'description': 'Execute appropriate response actions based on incident severity.'},
            {'title': 'Threat Hunting', 'description': 'Conduct proactive threat hunting using Falcon capabilities.'},
            {'title': 'Remediation', 'description': 'Perform malware removal and system remediation tasks.'}
        ],
        'resources': [
            {'title': 'CCFR Training Course', 'description': 'Official CrowdStrike training for incident responders.'},
            {'title': 'Falcon Platform Labs', 'description': 'Hands-on labs with real incident response scenarios.'},
            {'title': 'Response Playbooks', 'description': 'Best practice playbooks for incident response.'},
            {'title': 'CrowdStrike University', 'description': 'Access to online learning resources and documentation.'}
        ],
        'careers': [
            'Incident Response Analyst',
            'SOC Analyst',
            'Threat Response Specialist',
            'Security Operations Engineer',
            'Endpoint Security Analyst'
        ],
        'salary': '$75,000 - $110,000 USD annually'
    },
    'crowdstrike-ccfh': {
        'name': 'CCFH',
        'full_name': 'CrowdStrike Certified Falcon Hunter',
        'level': 'Falcon Hunter',
        'vendor': 'CrowdStrike',
        'brand_color': '#E01F3D',
        'badge': 'crowdstrike-ccfh.png',
        'exam_code': 'CCFH',
        'duration': '90 minutes',
        'cost': 'Contact CrowdStrike Sales',
        'validity': '2 years',
        'vendor_url': 'https://www.crowdstrike.com/university/',
        'overview': '''<p>The CCFH certification demonstrates advanced skills in proactive threat hunting using the CrowdStrike Falcon platform. This certification focuses on identifying hidden threats and advanced persistent threats through active hunting techniques.</p>
<p>You'll validate expertise in custom query creation, advanced search techniques, threat intelligence integration, and developing hunting hypotheses using CrowdStrike's threat hunting capabilities.</p>
<p>This certification is perfect for threat hunters and advanced SOC analysts focused on proactively discovering sophisticated threats.</p>''',
        'topics': [
            {'title': 'Threat Hunting Methodology', 'description': 'Develop and execute threat hunting hypotheses and campaigns.'},
            {'title': 'Advanced Search', 'description': 'Create complex queries for threat discovery using Falcon search capabilities.'},
            {'title': 'Event Search', 'description': 'Utilize event search to analyze endpoint telemetry and identify threats.'},
            {'title': 'Threat Intelligence', 'description': 'Leverage threat intelligence for informed hunting activities.'},
            {'title': 'Custom IOA', 'description': 'Create custom Indicators of Attack (IOAs) for threat detection.'},
            {'title': 'Pattern Analysis', 'description': 'Identify attack patterns and adversary techniques.'},
            {'title': 'Advanced Analytics', 'description': 'Use analytics and visualization for threat discovery.'},
            {'title': 'Hunt Reporting', 'description': 'Document findings and communicate hunt results effectively.'}
        ],
        'resources': [
            {'title': 'CCFH Training Course', 'description': 'Advanced threat hunting training from CrowdStrike.'},
            {'title': 'Threat Hunting Labs', 'description': 'Practical hunting exercises with realistic threat scenarios.'},
            {'title': 'Hunting Playbooks', 'description': 'Curated hunting playbooks and methodologies.'},
            {'title': 'Threat Intelligence Feeds', 'description': 'Access to CrowdStrike threat intelligence for hunting.'}
        ],
        'careers': [
            'Threat Hunter',
            'Advanced SOC Analyst',
            'Threat Intelligence Analyst',
            'Security Research Analyst',
            'Detection Engineer'
        ],
        'salary': '$90,000 - $135,000 USD annually'
    },
    'ibm-qradar-siem': {
        'name': 'QRadar SIEM',
        'full_name': 'IBM QRadar SIEM Specialist',
        'level': 'Specialist',
        'vendor': 'IBM',
        'brand_color': '#0F62FE',
        'badge': 'ibm-qradar-siem.png',
        'exam_code': 'C1000-142',
        'duration': '90 minutes',
        'cost': '$200 USD',
        'validity': 'Does not expire',
        'vendor_url': 'https://www.ibm.com/training/',
        'overview': '''<p>The IBM QRadar SIEM Specialist certification validates your ability to deploy, configure, and operate IBM QRadar SIEM for security event monitoring and threat detection.</p>
<p>You'll demonstrate expertise in configuring log sources, creating custom rules, building offenses, and using QRadar for security operations and compliance reporting.</p>
<p>This certification is essential for security analysts and SIEM administrators working with IBM QRadar in enterprise security operations centers.</p>''',
        'topics': [
            {'title': 'QRadar Architecture', 'description': 'Understand QRadar components, deployment models, and architecture.'},
            {'title': 'Log Source Configuration', 'description': 'Configure and manage log sources for security event collection.'},
            {'title': 'Custom Rules', 'description': 'Create custom rules and building blocks for threat detection.'},
            {'title': 'Offense Management', 'description': 'Manage security offenses and configure offense prioritization.'},
            {'title': 'Dashboards & Reports', 'description': 'Build custom dashboards and generate compliance reports.'},
            {'title': 'Network Flow Analysis', 'description': 'Analyze network flows for threat detection and investigation.'},
            {'title': 'Use Case Development', 'description': 'Develop and implement security use cases in QRadar.'},
            {'title': 'Integration', 'description': 'Integrate QRadar with third-party security tools and ticketing systems.'}
        ],
        'resources': [
            {'title': 'QRadar SIEM Training', 'description': 'Official IBM training course for QRadar administrators.'},
            {'title': 'Community Edition', 'description': 'Free QRadar CE for hands-on practice and learning.'},
            {'title': 'Documentation Library', 'description': 'Comprehensive QRadar documentation and knowledge center.'},
            {'title': 'Practice Exam', 'description': 'Sample questions and practice test for certification preparation.'}
        ],
        'careers': [
            'SIEM Administrator',
            'Security Operations Analyst',
            'QRadar Specialist',
            'SOC Engineer',
            'Security Monitoring Analyst'
        ],
        'salary': '$75,000 - $115,000 USD annually'
    },
    'ibm-qradar-analyst': {
        'name': 'QRadar Analyst',
        'full_name': 'IBM QRadar SIEM Security Analyst',
        'level': 'Associate',
        'vendor': 'IBM',
        'brand_color': '#0F62FE',
        'badge': 'ibm-qradar-analyst.png',
        'exam_code': 'C1000-123',
        'duration': '90 minutes',
        'cost': '$200 USD',
        'validity': 'Does not expire',
        'vendor_url': 'https://www.ibm.com/training/',
        'overview': '''<p>The IBM QRadar Security Analyst certification validates your skills in using QRadar SIEM for day-to-day security operations, threat detection, and incident investigation.</p>
<p>You'll demonstrate proficiency in analyzing security offenses, investigating threats, using QRadar search capabilities, and responding to security incidents using the QRadar platform.</p>
<p>This certification is ideal for SOC analysts and security professionals who use QRadar for security monitoring and analysis.</p>''',
        'topics': [
            {'title': 'Offense Analysis', 'description': 'Analyze and investigate security offenses generated by QRadar.'},
            {'title': 'Event Investigation', 'description': 'Investigate security events and identify potential threats.'},
            {'title': 'QRadar Search', 'description': 'Use AQL (Ariel Query Language) for advanced search and investigation.'},
            {'title': 'Threat Indicators', 'description': 'Identify indicators of compromise using QRadar data.'},
            {'title': 'Asset Management', 'description': 'Manage assets and understand asset profiles in QRadar.'},
            {'title': 'Reference Sets', 'description': 'Utilize reference sets and threat intelligence in investigations.'},
            {'title': 'Reporting', 'description': 'Generate reports for security incidents and compliance.'},
            {'title': 'Workflow', 'description': 'Follow security analyst workflows for incident handling.'}
        ],
        'resources': [
            {'title': 'Analyst Training Course', 'description': 'IBM training focused on QRadar analysis and investigation.'},
            {'title': 'QRadar CE Practice', 'description': 'Hands-on practice using QRadar Community Edition.'},
            {'title': 'AQL Guide', 'description': 'Comprehensive guide to Ariel Query Language.'},
            {'title': 'Use Case Library', 'description': 'Common security use cases and investigation techniques.'}
        ],
        'careers': [
            'Security Operations Analyst',
            'SOC Analyst',
            'Incident Response Analyst',
            'Threat Detection Analyst',
            'Security Monitoring Specialist'
        ],
        'salary': '$65,000 - $95,000 USD annually'
    },
    'cyberark-defender': {
        'name': 'CyberArk Defender',
        'full_name': 'CyberArk Defender - Privileged Access Management',
        'level': 'Defender',
        'vendor': 'CyberArk',
        'brand_color': '#0066B1',
        'badge': 'cyberark-defender.png',
        'exam_code': 'PAM-DEF',
        'duration': '90 minutes',
        'cost': 'Varies by region',
        'validity': '2 years',
        'vendor_url': 'https://www.cyberark.com/services-support/technical-certifications/',
        'overview': '''<p>The CyberArk Defender certification validates foundational knowledge of CyberArk Privileged Access Security Solution. This entry-level certification demonstrates understanding of PAM concepts and basic CyberArk implementation.</p>
<p>You'll learn about privileged account security, vault architecture, safe management, and basic administration of the CyberArk platform.</p>
<p>This certification is ideal for IT professionals beginning their journey in privileged access management with CyberArk.</p>''',
        'topics': [
            {'title': 'PAM Fundamentals', 'description': 'Understand privileged access management concepts and best practices.'},
            {'title': 'Vault Architecture', 'description': 'Learn CyberArk Vault architecture and core components.'},
            {'title': 'Safe Management', 'description': 'Create and manage safes for privileged account storage.'},
            {'title': 'Account Onboarding', 'description': 'Onboard privileged accounts into the CyberArk Vault.'},
            {'title': 'Password Policies', 'description': 'Configure password management policies and rotation.'},
            {'title': 'User Access', 'description': 'Manage user permissions and access to privileged accounts.'},
            {'title': 'Session Management', 'description': 'Understand privileged session management and monitoring.'},
            {'title': 'Compliance', 'description': 'Implement PAM for compliance and audit requirements.'}
        ],
        'resources': [
            {'title': 'Defender Training Course', 'description': 'Official CyberArk Defender training program.'},
            {'title': 'CyberArk University', 'description': 'Online learning platform with video tutorials and labs.'},
            {'title': 'Product Documentation', 'description': 'Comprehensive documentation for CyberArk products.'},
            {'title': 'Practice Environment', 'description': 'Access to CyberArk demo environment for practice.'}
        ],
        'careers': [
            'PAM Administrator',
            'Privileged Access Analyst',
            'Identity Security Specialist',
            'IAM Analyst',
            'Security Administrator'
        ],
        'salary': '$70,000 - $100,000 USD annually'
    },
    'cyberark-sentry': {
        'name': 'CyberArk Sentry',
        'full_name': 'CyberArk Sentry - Privileged Access Management',
        'level': 'Sentry',
        'vendor': 'CyberArk',
        'brand_color': '#0066B1',
        'badge': 'cyberark-sentry.png',
        'exam_code': 'PAM-SEN',
        'duration': '120 minutes',
        'cost': 'Varies by region',
        'validity': '2 years',
        'vendor_url': 'https://www.cyberark.com/services-support/technical-certifications/',
        'overview': '''<p>The CyberArk Sentry certification demonstrates advanced skills in installing, configuring, and managing CyberArk Privileged Access Security Solution in enterprise environments.</p>
<p>You'll validate expertise in deploying CyberArk components, implementing advanced configurations, integrating with enterprise systems, and troubleshooting PAM solutions.</p>
<p>This professional-level certification is essential for CyberArk administrators and PAM engineers.</p>''',
        'topics': [
            {'title': 'Installation & Configuration', 'description': 'Install and configure CyberArk components in enterprise environments.'},
            {'title': 'Advanced Safe Management', 'description': 'Implement advanced safe configurations and access workflows.'},
            {'title': 'PSM Deployment', 'description': 'Deploy and configure Privileged Session Manager for session recording.'},
            {'title': 'CPM Configuration', 'description': 'Configure Central Policy Manager for automated password management.'},
            {'title': 'PVWA Setup', 'description': 'Deploy and configure Password Vault Web Access portal.'},
            {'title': 'Platform Management', 'description': 'Create and manage target system platforms and connection components.'},
            {'title': 'Integration', 'description': 'Integrate CyberArk with LDAP, SIEM, and ticketing systems.'},
            {'title': 'Troubleshooting', 'description': 'Diagnose and resolve CyberArk implementation issues.'}
        ],
        'resources': [
            {'title': 'Sentry Training Course', 'description': 'Advanced CyberArk Sentry training program.'},
            {'title': 'Implementation Guides', 'description': 'Detailed implementation and configuration guides.'},
            {'title': 'Hands-On Labs', 'description': 'Virtual lab environment for practicing installations.'},
            {'title': 'Technical Documentation', 'description': 'In-depth technical documentation for all components.'}
        ],
        'careers': [
            'PAM Engineer',
            'CyberArk Administrator',
            'Senior IAM Engineer',
            'Privileged Access Architect',
            'Identity Security Engineer'
        ],
        'salary': '$95,000 - $140,000 USD annually'
    },
    'cyberark-guardian': {
        'name': 'CyberArk Guardian',
        'full_name': 'CyberArk Certified Delivery Engineer',
        'level': 'Guardian',
        'vendor': 'CyberArk',
        'brand_color': '#0066B1',
        'badge': 'cyberark-guardian.png',
        'exam_code': 'PAM-CDE',
        'duration': '150 minutes',
        'cost': 'Varies by region',
        'validity': '2 years',
        'vendor_url': 'https://www.cyberark.com/services-support/technical-certifications/',
        'overview': '''<p>The CyberArk Guardian (Certified Delivery Engineer) certification represents expert-level mastery in designing, deploying, and optimizing enterprise-scale CyberArk solutions.</p>
<p>You'll demonstrate ability to architect complex PAM deployments, implement high availability configurations, perform advanced integrations, and provide strategic PAM consulting.</p>
<p>This elite certification is designed for senior PAM architects and delivery engineers who lead large-scale CyberArk implementations.</p>''',
        'topics': [
            {'title': 'Enterprise Architecture', 'description': 'Design enterprise-scale PAM architectures with high availability.'},
            {'title': 'Disaster Recovery', 'description': 'Implement DR strategies and vault replication for business continuity.'},
            {'title': 'Performance Tuning', 'description': 'Optimize CyberArk performance for large-scale deployments.'},
            {'title': 'Advanced Integration', 'description': 'Integrate with complex enterprise systems and cloud platforms.'},
            {'title': 'Security Hardening', 'description': 'Implement security best practices and hardening configurations.'},
            {'title': 'Migration & Upgrade', 'description': 'Plan and execute migrations and major version upgrades.'},
            {'title': 'Custom Development', 'description': 'Develop custom platforms and automation scripts.'},
            {'title': 'Solution Design', 'description': 'Design PAM solutions aligned with enterprise security requirements.'}
        ],
        'resources': [
            {'title': 'Guardian Training Program', 'description': 'Comprehensive expert-level training for CyberArk architects.'},
            {'title': 'Architecture Workshops', 'description': 'Hands-on workshops for enterprise architecture design.'},
            {'title': 'Best Practices Guide', 'description': 'Enterprise deployment and architecture best practices.'},
            {'title': 'Advanced Labs', 'description': 'Complex lab scenarios for HA, DR, and enterprise deployments.'}
        ],
        'careers': [
            'PAM Architect',
            'Principal Security Engineer',
            'CyberArk Delivery Lead',
            'Identity Security Architect',
            'Senior PAM Consultant'
        ],
        'salary': '$120,000 - $170,000+ USD annually'
    },
    'okta-professional': {
        'name': 'Okta Professional',
        'full_name': 'Okta Certified Professional',
        'level': 'Professional',
        'vendor': 'Okta',
        'brand_color': '#007DC1',
        'badge': 'okta-professional.png',
        'exam_code': 'OCP',
        'duration': '90 minutes',
        'cost': 'Varies by region',
        'validity': '2 years',
        'vendor_url': 'https://www.okta.com/services/training/',
        'overview': '''<p>The Okta Certified Professional certification validates foundational knowledge of Okta identity and access management platform. This certification demonstrates understanding of basic Okta implementation and administration.</p>
<p>You'll learn about user lifecycle management, application integration, authentication policies, and basic Okta administration tasks.</p>
<p>This certification is perfect for IT professionals new to Okta or those seeking to validate their basic Okta skills.</p>''',
        'topics': [
            {'title': 'Okta Fundamentals', 'description': 'Understand Okta architecture, features, and core capabilities.'},
            {'title': 'User Management', 'description': 'Manage user lifecycle, groups, and user attributes.'},
            {'title': 'Application Integration', 'description': 'Integrate applications with Okta for SSO and authentication.'},
            {'title': 'Authentication Policies', 'description': 'Configure sign-on policies and authentication requirements.'},
            {'title': 'Directory Integration', 'description': 'Integrate Okta with Active Directory and LDAP directories.'},
            {'title': 'Multi-Factor Authentication', 'description': 'Configure and manage MFA factors and policies.'},
            {'title': 'Reporting', 'description': 'Generate reports and monitor Okta usage and events.'},
            {'title': 'Basic Administration', 'description': 'Perform day-to-day administrative tasks in Okta.'}
        ],
        'resources': [
            {'title': 'Okta Foundations Course', 'description': 'Self-paced online course covering Okta fundamentals.'},
            {'title': 'Admin Console Guide', 'description': 'Comprehensive guide to Okta Admin Console.'},
            {'title': 'Practice Environment', 'description': 'Free Okta developer account for hands-on practice.'},
            {'title': 'Certification Study Guide', 'description': 'Official study materials for OCP exam.'}
        ],
        'careers': [
            'Identity Administrator',
            'Okta Administrator',
            'IAM Analyst',
            'IT Support Specialist',
            'Access Management Specialist'
        ],
        'salary': '$65,000 - $95,000 USD annually'
    },
    'okta-administrator': {
        'name': 'Okta Administrator',
        'full_name': 'Okta Certified Administrator',
        'level': 'Administrator',
        'vendor': 'Okta',
        'brand_color': '#007DC1',
        'badge': 'okta-administrator.png',
        'exam_code': 'OCA',
        'duration': '120 minutes',
        'cost': 'Varies by region',
        'validity': '2 years',
        'vendor_url': 'https://www.okta.com/services/training/',
        'overview': '''<p>The Okta Certified Administrator certification demonstrates advanced skills in administering and managing Okta identity platform in enterprise environments.</p>
<p>You'll validate expertise in advanced user management, complex application integrations, lifecycle management, security policies, and Okta administration best practices.</p>
<p>This certification is essential for Okta administrators responsible for managing enterprise identity infrastructure.</p>''',
        'topics': [
            {'title': 'Advanced User Management', 'description': 'Implement complex user provisioning and lifecycle automation.'},
            {'title': 'App Integrations', 'description': 'Configure advanced application integrations including SAML and OIDC.'},
            {'title': 'Lifecycle Management', 'description': 'Automate user provisioning and deprovisioning workflows.'},
            {'title': 'Security Policies', 'description': 'Implement advanced authentication and authorization policies.'},
            {'title': 'Okta Workflows', 'description': 'Create automation workflows using Okta Workflows.'},
            {'title': 'API Integration', 'description': 'Utilize Okta APIs for custom integrations and automation.'},
            {'title': 'Troubleshooting', 'description': 'Diagnose and resolve complex Okta implementation issues.'},
            {'title': 'Best Practices', 'description': 'Implement Okta best practices for security and performance.'}
        ],
        'resources': [
            {'title': 'Administrator Training', 'description': 'Comprehensive administrator training from Okta.'},
            {'title': 'Advanced Integration Guide', 'description': 'Detailed guides for complex application integrations.'},
            {'title': 'Workflows Documentation', 'description': 'Complete documentation for Okta Workflows automation.'},
            {'title': 'Practice Labs', 'description': 'Hands-on labs for advanced administration scenarios.'}
        ],
        'careers': [
            'Senior Identity Administrator',
            'Okta Solutions Engineer',
            'IAM Engineer',
            'Identity Architect',
            'Access Management Lead'
        ],
        'salary': '$85,000 - $125,000 USD annually'
    },
    'okta-consultant': {
        'name': 'Okta Consultant',
        'full_name': 'Okta Certified Consultant',
        'level': 'Consultant',
        'vendor': 'Okta',
        'brand_color': '#007DC1',
        'badge': 'okta-consultant.png',
        'exam_code': 'OCC',
        'duration': '120 minutes',
        'cost': 'Varies by region',
        'validity': '2 years',
        'vendor_url': 'https://www.okta.com/services/training/',
        'overview': '''<p>The Okta Certified Consultant certification validates expertise in designing, implementing, and optimizing Okta solutions for enterprise customers. This certification demonstrates consulting-level knowledge and strategic thinking.</p>
<p>You'll prove ability to assess customer requirements, design identity solutions, lead implementations, and provide strategic guidance on identity and access management using Okta.</p>
<p>This certification is designed for Okta consultants, solution architects, and implementation specialists.</p>''',
        'topics': [
            {'title': 'Solution Design', 'description': 'Design comprehensive identity solutions aligned with business requirements.'},
            {'title': 'Requirements Analysis', 'description': 'Assess customer requirements and recommend appropriate Okta solutions.'},
            {'title': 'Implementation Planning', 'description': 'Plan and execute enterprise-scale Okta implementations.'},
            {'title': 'Integration Architecture', 'description': 'Architect complex integrations with enterprise applications and systems.'},
            {'title': 'Migration Strategies', 'description': 'Plan and execute migrations from legacy identity systems to Okta.'},
            {'title': 'Security Architecture', 'description': 'Design security architectures using Okta capabilities.'},
            {'title': 'Change Management', 'description': 'Manage organizational change during Okta deployments.'},
            {'title': 'Best Practices', 'description': 'Apply industry best practices for identity and access management.'}
        ],
        'resources': [
            {'title': 'Consultant Training Program', 'description': 'Advanced training for Okta consultants and architects.'},
            {'title': 'Implementation Playbooks', 'description': 'Best practice playbooks for enterprise implementations.'},
            {'title': 'Architecture Patterns', 'description': 'Reference architectures and design patterns.'},
            {'title': 'Customer Case Studies', 'description': 'Real-world case studies and implementation examples.'}
        ],
        'careers': [
            'Identity Consultant',
            'Okta Solutions Architect',
            'IAM Architect',
            'Identity Strategy Consultant',
            'Senior Implementation Specialist'
        ],
        'salary': '$100,000 - $150,000 USD annually'
    },
    'okta-developer': {
        'name': 'Okta Developer',
        'full_name': 'Okta Certified Developer',
        'level': 'Developer',
        'vendor': 'Okta',
        'brand_color': '#007DC1',
        'badge': 'okta-developer.png',
        'exam_code': 'OCD',
        'duration': '90 minutes',
        'cost': 'Varies by region',
        'validity': '2 years',
        'vendor_url': 'https://www.okta.com/services/training/',
        'overview': '''<p>The Okta Certified Developer certification validates skills in developing applications that integrate with Okta for authentication, authorization, and user management using Okta APIs and SDKs.</p>
<p>You'll demonstrate expertise in implementing OAuth 2.0, OIDC, SAML integrations, using Okta SDKs, and building custom applications with Okta identity services.</p>
<p>This certification is perfect for developers building applications that leverage Okta for identity and access management.</p>''',
        'topics': [
            {'title': 'OAuth 2.0 & OIDC', 'description': 'Implement OAuth 2.0 and OpenID Connect for application authentication.'},
            {'title': 'Okta APIs', 'description': 'Use Okta APIs for user management, authentication, and authorization.'},
            {'title': 'SDK Integration', 'description': 'Integrate applications using Okta SDKs for various platforms.'},
            {'title': 'SAML Integration', 'description': 'Implement SAML 2.0 for enterprise SSO integration.'},
            {'title': 'Custom UI', 'description': 'Build custom authentication UIs using Okta widgets and APIs.'},
            {'title': 'Token Management', 'description': 'Manage access tokens, ID tokens, and refresh tokens.'},
            {'title': 'Authorization', 'description': 'Implement authorization and access control in applications.'},
            {'title': 'Security Best Practices', 'description': 'Apply security best practices for identity integration.'}
        ],
        'resources': [
            {'title': 'Developer Training Course', 'description': 'Hands-on training for Okta developers.'},
            {'title': 'SDK Documentation', 'description': 'Complete documentation for all Okta SDKs.'},
            {'title': 'API Reference', 'description': 'Comprehensive Okta API reference documentation.'},
            {'title': 'Code Samples', 'description': 'Sample applications and code examples for various platforms.'}
        ],
        'careers': [
            'Application Developer',
            'Identity Developer',
            'Full Stack Developer',
            'Security Developer',
            'Integration Engineer'
        ],
        'salary': '$80,000 - $130,000 USD annually'
    },
    'qualys-vmdr': {
        'name': 'Qualys VMDR',
        'full_name': 'Qualys Vulnerability Management, Detection and Response Specialist',
        'level': 'Specialist',
        'vendor': 'Qualys',
        'brand_color': '#ED2E27',
        'badge': 'qualys-vmdr.png',
        'exam_code': 'VMDR',
        'duration': '90 minutes',
        'cost': 'FREE',
        'validity': '2 years',
        'vendor_url': 'https://www.qualys.com/training/',
        'overview': '''<p>The Qualys VMDR certification validates your skills in using Qualys Vulnerability Management, Detection and Response platform for identifying, prioritizing, and remediating security vulnerabilities.</p>
<p>You'll demonstrate expertise in vulnerability scanning, asset management, patch management, and continuous monitoring using the Qualys cloud platform.</p>
<p>This certification is ideal for vulnerability analysts and security engineers using Qualys for vulnerability management.</p>''',
        'topics': [
            {'title': 'Vulnerability Scanning', 'description': 'Configure and execute vulnerability scans across IT infrastructure.'},
            {'title': 'Asset Management', 'description': 'Manage and track assets using Qualys asset inventory.'},
            {'title': 'Vulnerability Prioritization', 'description': 'Prioritize vulnerabilities based on risk and business impact.'},
            {'title': 'Patch Management', 'description': 'Identify missing patches and manage patching workflows.'},
            {'title': 'Reporting & Dashboards', 'description': 'Create reports and dashboards for vulnerability metrics.'},
            {'title': 'Remediation Tracking', 'description': 'Track vulnerability remediation and validate fixes.'},
            {'title': 'Compliance Scanning', 'description': 'Scan for compliance with security standards and policies.'},
            {'title': 'Continuous Monitoring', 'description': 'Implement continuous vulnerability monitoring and detection.'}
        ],
        'resources': [
            {'title': 'VMDR Training Course', 'description': 'Free online training for Qualys VMDR.'},
            {'title': 'Community Edition', 'description': 'Free Qualys Community Edition for hands-on practice.'},
            {'title': 'Knowledge Base', 'description': 'Comprehensive documentation and how-to guides.'},
            {'title': 'Practice Exam', 'description': 'Free practice test for certification preparation.'}
        ],
        'careers': [
            'Vulnerability Analyst',
            'Security Assessment Specialist',
            'Vulnerability Management Engineer',
            'Security Compliance Analyst',
            'Risk Assessment Analyst'
        ],
        'salary': '$70,000 - $105,000 USD annually'
    },
    'qualys-was': {
        'name': 'Qualys WAS',
        'full_name': 'Qualys Web Application Scanning Specialist',
        'level': 'Specialist',
        'vendor': 'Qualys',
        'brand_color': '#ED2E27',
        'badge': 'qualys-was.png',
        'exam_code': 'WAS',
        'duration': '90 minutes',
        'cost': 'FREE',
        'validity': '2 years',
        'vendor_url': 'https://www.qualys.com/training/',
        'overview': '''<p>The Qualys WAS certification validates expertise in using Qualys Web Application Scanning to identify and remediate web application vulnerabilities.</p>
<p>You'll demonstrate skills in configuring web app scans, analyzing scan results, identifying OWASP Top 10 vulnerabilities, and integrating WAS into development workflows.</p>
<p>This certification is perfect for application security engineers and web application security specialists.</p>''',
        'topics': [
            {'title': 'Web App Scanning', 'description': 'Configure and execute automated web application vulnerability scans.'},
            {'title': 'OWASP Top 10', 'description': 'Identify and understand OWASP Top 10 web application vulnerabilities.'},
            {'title': 'Scan Configuration', 'description': 'Configure scan profiles, authentication, and crawling options.'},
            {'title': 'Vulnerability Analysis', 'description': 'Analyze scan results and validate web application vulnerabilities.'},
            {'title': 'False Positive Management', 'description': 'Identify and manage false positives in scan results.'},
            {'title': 'Remediation Guidance', 'description': 'Provide remediation guidance for identified vulnerabilities.'},
            {'title': 'CI/CD Integration', 'description': 'Integrate WAS into DevOps and CI/CD pipelines.'},
            {'title': 'Reporting', 'description': 'Generate reports for development teams and stakeholders.'}
        ],
        'resources': [
            {'title': 'WAS Training Course', 'description': 'Free online training for Qualys WAS.'},
            {'title': 'OWASP Guide', 'description': 'Guide to OWASP vulnerabilities and remediation.'},
            {'title': 'API Documentation', 'description': 'API docs for WAS automation and integration.'},
            {'title': 'Best Practices', 'description': 'Web application security scanning best practices.'}
        ],
        'careers': [
            'Application Security Engineer',
            'Web Application Security Analyst',
            'DevSecOps Engineer',
            'Security Testing Specialist',
            'AppSec Consultant'
        ],
        'salary': '$75,000 - $115,000 USD annually'
    },
    'rapid7-insightvm': {
        'name': 'Rapid7 InsightVM',
        'full_name': 'Rapid7 InsightVM Administrator',
        'level': 'Administrator',
        'vendor': 'Rapid7',
        'brand_color': '#FF6700',
        'badge': 'rapid7-insightvm.png',
        'exam_code': 'InsightVM',
        'duration': '90 minutes',
        'cost': 'FREE',
        'validity': 'Does not expire',
        'vendor_url': 'https://www.rapid7.com/services/training-certification/',
        'overview': '''<p>The Rapid7 InsightVM Administrator certification validates skills in deploying and managing Rapid7's vulnerability management and assessment platform.</p>
<p>You'll demonstrate expertise in vulnerability scanning, risk-based prioritization, remediation workflows, and reporting using InsightVM.</p>
<p>This certification is ideal for security professionals using InsightVM for vulnerability management and risk assessment.</p>''',
        'topics': [
            {'title': 'InsightVM Deployment', 'description': 'Deploy and configure InsightVM components including consoles and scan engines.'},
            {'title': 'Vulnerability Scanning', 'description': 'Configure and execute vulnerability assessments across IT assets.'},
            {'title': 'Asset Discovery', 'description': 'Discover and inventory IT assets using dynamic discovery.'},
            {'title': 'Risk Prioritization', 'description': 'Prioritize vulnerabilities using risk scores and real risk analytics.'},
            {'title': 'Remediation Projects', 'description': 'Create and manage remediation projects and workflows.'},
            {'title': 'Integration', 'description': 'Integrate InsightVM with ticketing, SIEM, and orchestration tools.'},
            {'title': 'Reporting & Metrics', 'description': 'Generate vulnerability reports and track security metrics.'},
            {'title': 'Policy Scanning', 'description': 'Perform compliance and policy scanning.'}
        ],
        'resources': [
            {'title': 'InsightVM Training', 'description': 'Free online training for InsightVM administrators.'},
            {'title': 'Product Documentation', 'description': 'Comprehensive InsightVM documentation and guides.'},
            {'title': 'University Portal', 'description': 'Rapid7 University with video tutorials and labs.'},
            {'title': 'Community Forums', 'description': 'Rapid7 community for Q&A and best practices.'}
        ],
        'careers': [
            'Vulnerability Management Specialist',
            'Security Risk Analyst',
            'Infrastructure Security Engineer',
            'Security Operations Analyst',
            'Compliance Analyst'
        ],
        'salary': '$70,000 - $110,000 USD annually'
    },
    'rapid7-insightidr': {
        'name': 'Rapid7 InsightIDR',
        'full_name': 'Rapid7 InsightIDR Administrator',
        'level': 'Administrator',
        'vendor': 'Rapid7',
        'brand_color': '#FF6700',
        'badge': 'rapid7-insightidr.png',
        'exam_code': 'InsightIDR',
        'duration': '90 minutes',
        'cost': 'FREE',
        'validity': 'Does not expire',
        'vendor_url': 'https://www.rapid7.com/services/training-certification/',
        'overview': '''<p>The Rapid7 InsightIDR Administrator certification validates expertise in deploying and operating Rapid7's SIEM and incident detection and response platform.</p>
<p>You'll demonstrate skills in threat detection, incident investigation, UEBA, and security monitoring using InsightIDR.</p>
<p>This certification is essential for SOC analysts and security engineers using InsightIDR for threat detection and incident response.</p>''',
        'topics': [
            {'title': 'InsightIDR Deployment', 'description': 'Deploy and configure InsightIDR collectors and integrations.'},
            {'title': 'Log Management', 'description': 'Collect and manage security logs from various sources.'},
            {'title': 'Threat Detection', 'description': 'Configure detection rules and alerts for threat identification.'},
            {'title': 'Investigation', 'description': 'Investigate security incidents using InsightIDR investigation tools.'},
            {'title': 'UEBA', 'description': 'Utilize user and entity behavior analytics for anomaly detection.'},
            {'title': 'Attacker Behavior Analytics', 'description': 'Detect attacker techniques using ABA capabilities.'},
            {'title': 'Response Actions', 'description': 'Execute response actions and contain threats.'},
            {'title': 'Dashboards & Reporting', 'description': 'Create dashboards and reports for security operations.'}
        ],
        'resources': [
            {'title': 'InsightIDR Training', 'description': 'Free online training for InsightIDR users.'},
            {'title': 'Detection Library', 'description': 'Library of pre-built detection rules and use cases.'},
            {'title': 'Investigation Guide', 'description': 'Guide to incident investigation workflows.'},
            {'title': 'API Documentation', 'description': 'API docs for automation and integration.'}
        ],
        'careers': [
            'SOC Analyst',
            'Incident Response Analyst',
            'Threat Detection Engineer',
            'Security Operations Engineer',
            'SIEM Administrator'
        ],
        'salary': '$75,000 - $115,000 USD annually'
    },
    'tenable-nessus': {
        'name': 'Nessus Certified',
        'full_name': 'Tenable Nessus Certified Professional',
        'level': 'Professional',
        'vendor': 'Tenable',
        'brand_color': '#00B388',
        'badge': 'tenable-nessus.png',
        'exam_code': 'Nessus-Pro',
        'duration': '90 minutes',
        'cost': 'Varies by region',
        'validity': '2 years',
        'vendor_url': 'https://www.tenable.com/education',
        'overview': '''<p>The Tenable Nessus Certified Professional certification validates proficiency in using Nessus for vulnerability assessment and security scanning.</p>
<p>You'll demonstrate skills in vulnerability scanning, scan configuration, result analysis, and remediation using Nessus Professional and Nessus Expert.</p>
<p>This certification is ideal for security professionals using Nessus for vulnerability assessment and penetration testing.</p>''',
        'topics': [
            {'title': 'Nessus Fundamentals', 'description': 'Understand Nessus architecture, features, and capabilities.'},
            {'title': 'Scan Configuration', 'description': 'Configure vulnerability scans with appropriate policies and plugins.'},
            {'title': 'Credentialed Scanning', 'description': 'Perform authenticated scans for comprehensive assessment.'},
            {'title': 'Result Analysis', 'description': 'Analyze scan results and identify critical vulnerabilities.'},
            {'title': 'Compliance Scanning', 'description': 'Perform compliance audits and configuration assessments.'},
            {'title': 'Custom Policies', 'description': 'Create custom scan policies and audit files.'},
            {'title': 'Remediation', 'description': 'Provide remediation guidance and validate fixes.'},
            {'title': 'Reporting', 'description': 'Generate and customize vulnerability reports.'}
        ],
        'resources': [
            {'title': 'Nessus Training Course', 'description': 'Official training for Nessus Professional.'},
            {'title': 'Nessus Essentials', 'description': 'Free Nessus Essentials for hands-on practice.'},
            {'title': 'Plugin Documentation', 'description': 'Comprehensive plugin and policy documentation.'},
            {'title': 'Community Forum', 'description': 'Tenable community for support and best practices.'}
        ],
        'careers': [
            'Vulnerability Analyst',
            'Penetration Tester',
            'Security Assessment Specialist',
            'Network Security Engineer',
            'Compliance Auditor'
        ],
        'salary': '$70,000 - $110,000 USD annually'
    },
    'darktrace-engineer': {
        'name': 'Darktrace Engineer',
        'full_name': 'Darktrace Certified Engineer',
        'level': 'Engineer',
        'vendor': 'Darktrace',
        'brand_color': '#E94E1B',
        'badge': 'darktrace-engineer.png',
        'exam_code': 'DCE',
        'duration': '90 minutes',
        'cost': 'Partner Program',
        'validity': '2 years',
        'vendor_url': 'https://www.darktrace.com/en/services/',
        'overview': '''<p>The Darktrace Certified Engineer certification validates expertise in deploying, configuring, and managing Darktrace's AI-powered cybersecurity platform.</p>
<p>You'll demonstrate skills in threat detection using AI, incident investigation, autonomous response configuration, and Darktrace platform administration.</p>
<p>This certification is designed for security engineers implementing Darktrace for autonomous threat detection and response.</p>''',
        'topics': [
            {'title': 'Darktrace Architecture', 'description': 'Understand Darktrace architecture and AI-powered threat detection.'},
            {'title': 'Deployment & Configuration', 'description': 'Deploy and configure Darktrace appliances and sensors.'},
            {'title': 'AI Threat Detection', 'description': 'Leverage AI for detecting anomalous behavior and threats.'},
            {'title': 'Model Breach Investigation', 'description': 'Investigate model breaches and security incidents.'},
            {'title': 'Autonomous Response', 'description': 'Configure Antigena for autonomous threat response.'},
            {'title': 'Network Visibility', 'description': 'Gain network visibility and understand traffic patterns.'},
            {'title': 'Compliance Monitoring', 'description': 'Monitor compliance and policy violations.'},
            {'title': 'Advanced Analytics', 'description': 'Utilize advanced analytics for threat hunting.'}
        ],
        'resources': [
            {'title': 'Engineer Training Course', 'description': 'Official Darktrace engineer training program.'},
            {'title': 'Threat Visualizer Guide', 'description': 'Guide to using Threat Visualizer for investigation.'},
            {'title': 'Best Practices', 'description': 'Deployment and configuration best practices.'},
            {'title': 'Partner Portal', 'description': 'Access to partner resources and documentation.'}
        ],
        'careers': [
            'Darktrace Engineer',
            'AI Security Specialist',
            'Threat Detection Engineer',
            'SOC Engineer',
            'Cybersecurity Analyst'
        ],
        'salary': '$85,000 - $130,000 USD annually'
    },
    'sentinelone-core': {
        'name': 'SentinelOne Core',
        'full_name': 'SentinelOne Core Administrator',
        'level': 'Administrator',
        'vendor': 'SentinelOne',
        'brand_color': '#6A1B9A',
        'badge': 'sentinelone-core.png',
        'exam_code': 'S1-Core',
        'duration': '90 minutes',
        'cost': 'Customer Program',
        'validity': '2 years',
        'vendor_url': 'https://www.sentinelone.com/services/',
        'overview': '''<p>The SentinelOne Core Administrator certification validates foundational knowledge of SentinelOne Singularity platform for endpoint protection and EDR.</p>
<p>You'll demonstrate skills in agent deployment, policy configuration, threat detection, and incident response using SentinelOne Core capabilities.</p>
<p>This certification is ideal for endpoint security administrators managing SentinelOne deployments.</p>''',
        'topics': [
            {'title': 'Platform Overview', 'description': 'Understand SentinelOne Singularity architecture and capabilities.'},
            {'title': 'Agent Deployment', 'description': 'Deploy and manage SentinelOne agents across endpoints.'},
            {'title': 'Policy Management', 'description': 'Configure security policies for threat prevention and detection.'},
            {'title': 'Threat Detection', 'description': 'Monitor and investigate threat detections and alerts.'},
            {'title': 'Incident Response', 'description': 'Respond to threats using remediation and rollback capabilities.'},
            {'title': 'Quarantine Management', 'description': 'Manage quarantined threats and restore files.'},
            {'title': 'Reporting', 'description': 'Generate reports for security metrics and compliance.'},
            {'title': 'Console Administration', 'description': 'Administer the SentinelOne management console.'}
        ],
        'resources': [
            {'title': 'Core Training Course', 'description': 'Official SentinelOne Core administrator training.'},
            {'title': 'Admin Guide', 'description': 'Comprehensive administrator guide and documentation.'},
            {'title': 'Knowledge Base', 'description': 'Access to SentinelOne knowledge base articles.'},
            {'title': 'Customer Portal', 'description': 'Customer portal with resources and support.'}
        ],
        'careers': [
            'Endpoint Security Administrator',
            'EDR Analyst',
            'Security Operations Specialist',
            'Incident Response Analyst',
            'SOC Analyst'
        ],
        'salary': '$70,000 - $105,000 USD annually'
    },
    'sentinelone-advanced': {
        'name': 'SentinelOne Advanced',
        'full_name': 'SentinelOne Advanced Administrator',
        'level': 'Advanced',
        'vendor': 'SentinelOne',
        'brand_color': '#6A1B9A',
        'badge': 'sentinelone-advanced.png',
        'exam_code': 'S1-Adv',
        'duration': '120 minutes',
        'cost': 'Customer Program',
        'validity': '2 years',
        'vendor_url': 'https://www.sentinelone.com/services/',
        'overview': '''<p>The SentinelOne Advanced Administrator certification validates advanced skills in managing enterprise SentinelOne deployments including threat hunting, automation, and integration.</p>
<p>You'll demonstrate expertise in advanced threat hunting, Deep Visibility, Storylines investigation, automation, and API integration.</p>
<p>This certification is designed for senior security engineers and threat hunters using advanced SentinelOne capabilities.</p>''',
        'topics': [
            {'title': 'Advanced Threat Hunting', 'description': 'Conduct proactive threat hunting using SentinelOne capabilities.'},
            {'title': 'Deep Visibility', 'description': 'Utilize Deep Visibility for advanced endpoint forensics.'},
            {'title': 'Storylines Investigation', 'description': 'Investigate threats using Storylines for full attack context.'},
            {'title': 'Custom Detection Rules', 'description': 'Create custom detection rules and STAR queries.'},
            {'title': 'API Integration', 'description': 'Integrate SentinelOne with SIEM and orchestration platforms using APIs.'},
            {'title': 'Automation', 'description': 'Automate response actions and workflows.'},
            {'title': 'Performance Tuning', 'description': 'Optimize SentinelOne performance for large deployments.'},
            {'title': 'Advanced Configuration', 'description': 'Implement advanced configurations for enterprise environments.'}
        ],
        'resources': [
            {'title': 'Advanced Training Course', 'description': 'Advanced SentinelOne training for threat hunters.'},
            {'title': 'API Documentation', 'description': 'Comprehensive API documentation for integrations.'},
            {'title': 'Threat Hunting Guide', 'description': 'Guide to threat hunting with SentinelOne.'},
            {'title': 'Advanced Labs', 'description': 'Hands-on labs for advanced scenarios.'}
        ],
        'careers': [
            'Threat Hunter',
            'Senior EDR Engineer',
            'Security Architect',
            'Advanced SOC Analyst',
            'Detection Engineer'
        ],
        'salary': '$95,000 - $145,000 USD annually'
    },
    'sophos-engineer': {
        'name': 'Sophos Engineer',
        'full_name': 'Sophos Certified Engineer',
        'level': 'Engineer',
        'vendor': 'Sophos',
        'brand_color': '#00BFFF',
        'badge': 'sophos-engineer.png',
        'exam_code': 'SCE',
        'duration': '90 minutes',
        'cost': 'Partner Program',
        'validity': '2 years',
        'vendor_url': 'https://www.sophos.com/en-us/support/professional-services',
        'overview': '''<p>The Sophos Certified Engineer certification validates technical skills in deploying and managing Sophos security solutions including firewall, endpoint, and email security.</p>
<p>You'll demonstrate expertise in Sophos product deployment, configuration, troubleshooting, and integration across the Sophos security portfolio.</p>
<p>This certification is designed for security engineers and consultants implementing Sophos solutions.</p>''',
        'topics': [
            {'title': 'Sophos Firewall', 'description': 'Deploy and configure Sophos XG/XGS Firewall solutions.'},
            {'title': 'Endpoint Protection', 'description': 'Manage Sophos Central endpoint security and Intercept X.'},
            {'title': 'Email Security', 'description': 'Configure Sophos Email Security for threat protection.'},
            {'title': 'Synchronized Security', 'description': 'Implement Security Heartbeat and synchronized security.'},
            {'title': 'Central Management', 'description': 'Manage Sophos products through Sophos Central.'},
            {'title': 'VPN Configuration', 'description': 'Configure site-to-site and remote access VPNs.'},
            {'title': 'Threat Response', 'description': 'Respond to threats using Sophos EDR capabilities.'},
            {'title': 'Troubleshooting', 'description': 'Diagnose and resolve Sophos product issues.'}
        ],
        'resources': [
            {'title': 'Engineer Training Course', 'description': 'Official Sophos engineer certification training.'},
            {'title': 'Product Documentation', 'description': 'Comprehensive documentation for all Sophos products.'},
            {'title': 'Partner Portal', 'description': 'Access to partner resources and tools.'},
            {'title': 'Lab Environment', 'description': 'Virtual labs for hands-on practice.'}
        ],
        'careers': [
            'Sophos Engineer',
            'Network Security Engineer',
            'Security Solutions Engineer',
            'Endpoint Security Specialist',
            'Security Consultant'
        ],
        'salary': '$80,000 - $120,000 USD annually'
    },
    'sophos-architect': {
        'name': 'Sophos Architect',
        'full_name': 'Sophos Certified Architect',
        'level': 'Architect',
        'vendor': 'Sophos',
        'brand_color': '#00BFFF',
        'badge': 'sophos-architect.png',
        'exam_code': 'SCA',
        'duration': '120 minutes',
        'cost': 'Partner Program',
        'validity': '2 years',
        'vendor_url': 'https://www.sophos.com/en-us/support/professional-services',
        'overview': '''<p>The Sophos Certified Architect certification validates advanced expertise in designing and architecting enterprise-scale Sophos security solutions.</p>
<p>You'll demonstrate ability to design comprehensive security architectures using the full Sophos portfolio, implement high availability, and provide strategic security guidance.</p>
<p>This certification is designed for senior architects and consultants designing enterprise Sophos deployments.</p>''',
        'topics': [
            {'title': 'Security Architecture', 'description': 'Design enterprise security architectures using Sophos solutions.'},
            {'title': 'High Availability', 'description': 'Design and implement HA configurations for business continuity.'},
            {'title': 'Enterprise Deployment', 'description': 'Plan and execute large-scale Sophos deployments.'},
            {'title': 'Integration Architecture', 'description': 'Architect integrations with third-party security and IT systems.'},
            {'title': 'Performance Optimization', 'description': 'Design for optimal performance in enterprise environments.'},
            {'title': 'Security Best Practices', 'description': 'Apply security best practices and industry standards.'},
            {'title': 'Multi-Tenant Design', 'description': 'Design multi-tenant and MSP architectures.'},
            {'title': 'Migration Planning', 'description': 'Plan migrations from legacy security solutions to Sophos.'}
        ],
        'resources': [
            {'title': 'Architect Training Program', 'description': 'Advanced training for Sophos architects.'},
            {'title': 'Architecture Guides', 'description': 'Reference architectures and design guides.'},
            {'title': 'Best Practices Library', 'description': 'Enterprise deployment best practices.'},
            {'title': 'Advanced Labs', 'description': 'Complex lab scenarios for enterprise architectures.'}
        ],
        'careers': [
            'Security Architect',
            'Solutions Architect',
            'Principal Security Engineer',
            'Security Consulting Lead',
            'Enterprise Architect'
        ],
        'salary': '$110,000 - $160,000 USD annually'
    },
    'trendmicro-professional': {
        'name': 'Trend Micro Pro',
        'full_name': 'Trend Micro Certified Professional',
        'level': 'Professional',
        'vendor': 'Trend Micro',
        'brand_color': '#D71920',
        'badge': 'trendmicro-professional.png',
        'exam_code': 'TMCP',
        'duration': '90 minutes',
        'cost': 'Varies by region',
        'validity': '2 years',
        'vendor_url': 'https://www.trendmicro.com/en_us/partners/training-certification.html',
        'overview': '''<p>The Trend Micro Certified Professional certification validates skills in deploying and managing Trend Micro security solutions including endpoint, network, and cloud security.</p>
<p>You'll demonstrate expertise in implementing Trend Micro products, configuring policies, managing threats, and integrating solutions across hybrid environments.</p>
<p>This certification is ideal for security professionals working with Trend Micro enterprise security products.</p>''',
        'topics': [
            {'title': 'Apex One', 'description': 'Deploy and manage Trend Micro Apex One endpoint security.'},
            {'title': 'Deep Security', 'description': 'Configure Deep Security for server and cloud workload protection.'},
            {'title': 'Cloud App Security', 'description': 'Implement Cloud App Security for SaaS and cloud protection.'},
            {'title': 'Network Defense', 'description': 'Configure TippingPoint network security solutions.'},
            {'title': 'Policy Management', 'description': 'Create and manage security policies across Trend Micro products.'},
            {'title': 'Threat Intelligence', 'description': 'Leverage Trend Micro threat intelligence and Smart Protection Network.'},
            {'title': 'Integration', 'description': 'Integrate Trend Micro solutions with SIEM and security tools.'},
            {'title': 'Troubleshooting', 'description': 'Diagnose and resolve Trend Micro product issues.'}
        ],
        'resources': [
            {'title': 'Professional Training', 'description': 'Official Trend Micro professional certification training.'},
            {'title': 'Product Documentation', 'description': 'Comprehensive documentation for all Trend Micro products.'},
            {'title': 'Training Portal', 'description': 'Online training portal with courses and labs.'},
            {'title': 'Success Portal', 'description': 'Access to technical resources and best practices.'}
        ],
        'careers': [
            'Trend Micro Specialist',
            'Endpoint Security Engineer',
            'Cloud Security Engineer',
            'Security Solutions Engineer',
            'Enterprise Security Administrator'
        ],
        'salary': '$80,000 - $120,000 USD annually'
    },
    'trendmicro-expert': {
        'name': 'Trend Micro Expert',
        'full_name': 'Trend Micro Certified Expert',
        'level': 'Expert',
        'vendor': 'Trend Micro',
        'brand_color': '#D71920',
        'badge': 'trendmicro-expert.png',
        'exam_code': 'TMCE',
        'duration': '120 minutes',
        'cost': 'Varies by region',
        'validity': '2 years',
        'vendor_url': 'https://www.trendmicro.com/en_us/partners/training-certification.html',
        'overview': '''<p>The Trend Micro Certified Expert certification demonstrates advanced expertise in designing, deploying, and optimizing enterprise-scale Trend Micro security solutions.</p>
<p>You'll validate mastery-level knowledge in security architecture, advanced configurations, performance tuning, and strategic security planning using the full Trend Micro portfolio.</p>
<p>This expert-level certification is designed for senior security architects and technical leaders.</p>''',
        'topics': [
            {'title': 'Enterprise Architecture', 'description': 'Design enterprise security architectures using Trend Micro solutions.'},
            {'title': 'Advanced Deployment', 'description': 'Deploy complex multi-site and hybrid cloud configurations.'},
            {'title': 'Performance Optimization', 'description': 'Optimize performance for large-scale deployments.'},
            {'title': 'Advanced Threat Defense', 'description': 'Implement advanced threat defense and zero-day protection.'},
            {'title': 'XDR Implementation', 'description': 'Deploy and optimize Trend Micro Vision One XDR platform.'},
            {'title': 'Automation & Orchestration', 'description': 'Automate security operations and response workflows.'},
            {'title': 'Advanced Integration', 'description': 'Architect complex integrations with enterprise systems.'},
            {'title': 'Solution Design', 'description': 'Design comprehensive security solutions for complex requirements.'}
        ],
        'resources': [
            {'title': 'Expert Training Program', 'description': 'Advanced training for Trend Micro experts and architects.'},
            {'title': 'Architecture Library', 'description': 'Reference architectures and advanced design patterns.'},
            {'title': 'Advanced Labs', 'description': 'Complex lab scenarios for enterprise deployments.'},
            {'title': 'Technical Workshops', 'description': 'Hands-on workshops for advanced topics.'}
        ],
        'careers': [
            'Security Architect',
            'Principal Security Engineer',
            'Solution Architect',
            'Technical Director',
            'Security Strategy Consultant'
        ],
        'salary': '$110,000 - $165,000 USD annually'
    },
    'splunk-es-admin': {
        'name': 'Splunk ES Admin',
        'full_name': 'Splunk Enterprise Security Administrator',
        'level': 'Administrator',
        'vendor': 'Splunk',
        'brand_color': '#FF6B00',
        'badge': 'splunk-es-admin.png',
        'exam_code': 'SPLK-3003',
        'duration': '57 minutes',
        'cost': '$250 USD',
        'validity': '3 years',
        'vendor_url': 'https://www.splunk.com/en_us/training.html',
        'overview': '''<p>The Splunk Enterprise Security Administrator certification validates skills in deploying, configuring, and maintaining Splunk Enterprise Security for security operations.</p>
<p>You'll demonstrate expertise in ES data models, correlation searches, notable event management, threat intelligence, and ES administration.</p>
<p>This certification is essential for Splunk ES administrators and SOC engineers managing Splunk for security operations.</p>''',
        'topics': [
            {'title': 'ES Architecture', 'description': 'Understand Splunk ES architecture, components, and data flow.'},
            {'title': 'Data Models', 'description': 'Configure and maintain Common Information Model (CIM) data models.'},
            {'title': 'Correlation Searches', 'description': 'Create and tune correlation searches for threat detection.'},
            {'title': 'Notable Events', 'description': 'Manage notable events and incident review workflows.'},
            {'title': 'Threat Intelligence', 'description': 'Integrate and utilize threat intelligence in ES.'},
            {'title': 'Asset & Identity', 'description': 'Manage asset and identity frameworks for context enrichment.'},
            {'title': 'Dashboards', 'description': 'Configure ES dashboards and security posture views.'},
            {'title': 'ES Administration', 'description': 'Perform administrative tasks and maintain ES health.'}
        ],
        'resources': [
            {'title': 'ES Admin Course', 'description': 'Official Splunk Enterprise Security Admin training.'},
            {'title': 'ES Documentation', 'description': 'Comprehensive Enterprise Security documentation.'},
            {'title': 'Practice Exam', 'description': 'Official practice test for certification preparation.'},
            {'title': 'Splunk Education', 'description': 'Access to Splunk Education portal and labs.'}
        ],
        'careers': [
            'Splunk ES Administrator',
            'SOC Engineer',
            'Security Operations Analyst',
            'SIEM Administrator',
            'Security Architect'
        ],
        'salary': '$90,000 - $135,000 USD annually'
    },
    'splunk-soar-dev': {
        'name': 'Splunk SOAR Dev',
        'full_name': 'Splunk SOAR Developer',
        'level': 'Developer',
        'vendor': 'Splunk',
        'brand_color': '#FF6B00',
        'badge': 'splunk-soar-dev.png',
        'exam_code': 'SPLK-2003',
        'duration': '57 minutes',
        'cost': '$250 USD',
        'validity': '3 years',
        'vendor_url': 'https://www.splunk.com/en_us/training.html',
        'overview': '''<p>The Splunk SOAR Developer certification validates skills in developing automation playbooks and custom integrations using Splunk SOAR (formerly Phantom).</p>
<p>You'll demonstrate expertise in playbook development, custom app creation, Python scripting, and building security automation workflows.</p>
<p>This certification is perfect for security developers and automation engineers building SOAR solutions.</p>''',
        'topics': [
            {'title': 'Playbook Development', 'description': 'Design and build automation playbooks for security operations.'},
            {'title': 'Custom Apps', 'description': 'Develop custom apps and connectors for third-party integrations.'},
            {'title': 'Python Scripting', 'description': 'Write Python scripts for custom actions and automation.'},
            {'title': 'API Integration', 'description': 'Integrate SOAR with security tools using REST APIs.'},
            {'title': 'Decision Trees', 'description': 'Implement logic and decision trees in playbooks.'},
            {'title': 'Data Manipulation', 'description': 'Manipulate and format data within automation workflows.'},
            {'title': 'Error Handling', 'description': 'Implement error handling and debugging in playbooks.'},
            {'title': 'Best Practices', 'description': 'Apply development best practices for maintainable automation.'}
        ],
        'resources': [
            {'title': 'SOAR Developer Course', 'description': 'Official Splunk SOAR developer training.'},
            {'title': 'App Development Guide', 'description': 'Guide to developing custom SOAR apps.'},
            {'title': 'Python SDK', 'description': 'Python SDK documentation for SOAR development.'},
            {'title': 'Community Apps', 'description': 'Community-developed apps and playbooks for reference.'}
        ],
        'careers': [
            'SOAR Developer',
            'Security Automation Engineer',
            'DevSecOps Engineer',
            'Security Orchestration Specialist',
            'SOC Automation Developer'
        ],
        'salary': '$95,000 - $145,000 USD annually'
    }
}

# Générer toutes les pages
print("╔═══════════════════════════════════════════════════════════════╗")
print("║     🚀 GÉNÉRATION DES 37 PAGES DE CERTIFICATION              ║")
print("╚═══════════════════════════════════════════════════════════════╝\n")

output_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/certifications')
created_count = 0

for cert_id, cert_data in REMAINING_CERTS.items():
    output_file = output_dir / f"{cert_id}.html"

    try:
        html_content = create_cert_html(cert_data)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        created_count += 1
        print(f"✓ {cert_id}.html")

    except Exception as e:
        print(f"✗ Erreur pour {cert_id}: {e}")

print(f"\n{'═' * 65}")
print(f"✅ GÉNÉRATION TERMINÉE")
print(f"{'═' * 65}")
print(f"Pages créées: {created_count}/37")
print(f"{'═' * 65}\n")
