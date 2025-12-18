#!/usr/bin/env python3
# -*- coding: utf-8 -*-

certifications = {
    "ccna": {
        "title": "CCNA Certification",
        "full_name": "Cisco Certified Network Associate (CCNA)",
        "level": "Foundational",
        "badge": "ccna.png",
        "exam_code": "200-301",
        "duration": "120 minutes",
        "cost": "$300 USD",
        "validity": "3 years",
        "rating": "4.8/5",
        "description": "The CCNA certification validates foundational networking knowledge essential for understanding how Cisco DNA Center manages network infrastructure. This industry-recognized certification covers network fundamentals, IP connectivity, security fundamentals, and automation basics—all critical for working with Cisco's AI-powered networking solutions.",
        "overview": """<p>The Cisco Certified Network Associate (CCNA) is the industry-standard foundational certification for networking professionals. This comprehensive certification validates your ability to install, configure, operate, and troubleshoot medium-sized routed and switched networks, including implementation and verification of connections to remote sites in a WAN.</p>
<p>The modern CCNA curriculum covers critical emerging technologies including automation, programmability, security, and wireless—skills essential for working with Cisco DNA Center and AI-powered network management platforms.</p>
<p>With over 1 million CCNA certifications earned worldwide, this credential opens doors to network administrator, network engineer, and network support roles across all industries.</p>""",
        "topics": [
            "Network fundamentals (OSI model, TCP/IP, VLANs, routing concepts)",
            "Network access technologies (switching, wireless LANs, Ethernet)",
            "IP connectivity (routing protocols, OSPF, EIGRP, static routing)",
            "IP services (NAT, DHCP, NTP, SNMP, QoS basics, syslog)",
            "Security fundamentals (ACLs, 802.1X, wireless security, VPNs)",
            "Automation and programmability (REST APIs, JSON, YAML, Python basics)"
        ],
        "why_matters": "CCNA provides the foundational understanding of networking concepts that Cisco DNA Center automates. Understanding routing, switching, VLANs, and network services helps you interpret AI-driven insights and troubleshoot issues that the platform identifies. The automation and programmability topics directly prepare you for DNA Center's API-driven workflows.",
        "exam_format": "Multiple choice, drag-and-drop, simulations, and testlets",
        "prerequisites": "None required (recommended: basic computer literacy and networking concepts)",
        "study_resources": [
            "Cisco Official Cert Guide (Wendell Odom)",
            "Cisco Learning Network (free resources, study groups)",
            "Cisco U. CCNA 200-301 Complete Video Course",
            "Packet Tracer labs (free Cisco network simulator)",
            "Boson ExSim-Max practice exams",
            "CBT Nuggets video training"
        ],
        "career_paths": [
            "Network Administrator",
            "Network Engineer",
            "Network Support Specialist",
            "Systems Administrator",
            "IT Technician",
            "Junior Network Architect"
        ],
        "salary_range": "$65,000 - $95,000 USD annually",
        "next_steps": "After CCNA, pursue DevNet Associate for automation skills or CCNP Enterprise for advanced networking expertise."
    },

    "devnet-associate": {
        "title": "DevNet Associate Certification",
        "full_name": "Cisco Certified DevNet Associate",
        "level": "Foundational - Automation Focus",
        "badge": "devnet-associate.png",
        "exam_code": "DEVASC 200-901",
        "duration": "120 minutes",
        "cost": "$300 USD",
        "validity": "3 years",
        "rating": "4.7/5",
        "description": "DevNet Associate certification validates software development skills for Cisco platforms, including DNA Center APIs. This certification is crucial for automating network operations and integrating DNA Center with external systems through REST APIs and Python scripting.",
        "overview": """<p>The Cisco Certified DevNet Associate certification validates your software development skills specifically designed for Cisco platforms and network automation. This modern certification bridges the gap between traditional networking and software development, preparing professionals for the era of programmable infrastructure.</p>
<p>DevNet Associate focuses on practical coding skills, API consumption, and automation workflows—exactly what's needed to maximize the value of Cisco DNA Center's extensive REST APIs and automation capabilities.</p>
<p>This certification is ideal for network engineers transitioning to DevOps roles, software developers working with network infrastructure, and anyone responsible for automating Cisco platforms.</p>""",
        "topics": [
            "Software development and design (modular code, version control with Git)",
            "Understanding and using APIs (REST, authentication, rate limiting, webhooks)",
            "Cisco platforms and development (DNA Center SDK, Meraki APIs, SD-WAN APIs)",
            "Application deployment and security (containers, Docker, Kubernetes, CI/CD)",
            "Infrastructure and automation (Python, Ansible, Terraform, YANG data models)",
            "Network programmability (NETCONF, RESTCONF, gRPC)"
        ],
        "why_matters": "Cisco DNA Center exposes extensive REST APIs for automation, configuration management, and integration with ITSM tools. DevNet Associate teaches you to leverage these APIs for custom workflows, build automated remediation scripts, and integrate DNA Center with ServiceNow, Splunk, and other enterprise platforms. The Python and Ansible skills are directly applicable to DNA Center automation.",
        "exam_format": "Multiple choice questions and hands-on coding challenges",
        "prerequisites": "Basic programming knowledge helpful but not required",
        "study_resources": [
            "Cisco DevNet Learning Labs (free, hands-on)",
            "DevNet Associate Official Cert Guide",
            "DevNet Sandbox (free lab environment)",
            "Python for Network Engineers course",
            "Cisco DNA Center API documentation",
            "GitHub repositories with sample code"
        ],
        "career_paths": [
            "Network Automation Engineer",
            "DevOps Engineer",
            "Site Reliability Engineer (SRE)",
            "Network Programmability Specialist",
            "Infrastructure as Code Developer",
            "Integration Engineer"
        ],
        "salary_range": "$75,000 - $110,000 USD annually",
        "next_steps": "Progress to DevNet Professional or combine with CCNP Enterprise for full-stack network automation expertise."
    },

    "ccnp-enterprise": {
        "title": "CCNP Enterprise Certification",
        "full_name": "Cisco Certified Network Professional Enterprise",
        "level": "Professional",
        "badge": "ccnp-enterprise.png",
        "exam_code": "ENCOR 350-401 + Concentration",
        "duration": "120 min (core) + 90 min (concentration)",
        "cost": "$400 USD per exam",
        "validity": "3 years",
        "rating": "4.9/5",
        "description": "CCNP Enterprise validates professional-level skills in implementing and troubleshooting enterprise networks. This certification demonstrates expertise in the technologies that DNA Center manages, including SD-Access, SD-WAN, wireless, and advanced routing.",
        "overview": """<p>The Cisco Certified Network Professional (CCNP) Enterprise certification validates advanced skills in implementing and troubleshooting complex enterprise networks. This professional-level certification demonstrates expertise in the exact technologies that Cisco DNA Center manages and optimizes.</p>
<p>CCNP Enterprise requires passing two exams: the ENCOR (Implementing Cisco Enterprise Network Core Technologies) core exam, plus one concentration exam of your choice (ENARSI for routing, ENWLSI for wireless, or ENSLD for design).</p>
<p>This certification directly covers DNA Center's core capabilities including SD-Access fabric, SD-WAN, network assurance, wireless optimization, and automation—making it the ideal credential for DNA Center administrators and network architects.</p>""",
        "topics": [
            "Enterprise network architecture and design principles",
            "Virtualization technologies (SD-WAN, SD-Access, LISP, VXLAN, VRF)",
            "Infrastructure (Layer 2/3 switching, routing protocols, STP, EtherChannel)",
            "Network assurance (analytics, streaming telemetry, DNA Center assurance)",
            "Security (TrustSec, MACsec, 802.1X, segmentation, firewall integration)",
            "Automation (Python, Ansible, DNA Center APIs, NETCONF, YANG models)"
        ],
        "why_matters": "CCNP Enterprise directly aligns with Cisco DNA Center's functionality. The ENCOR exam covers SD-Access fabric implementation, network assurance analytics, and Catalyst Center integration—the exact technologies DNA Center automates. This certification validates your ability to design, implement, and troubleshoot the enterprise networks that DNA Center's AI analyzes and optimizes.",
        "exam_format": "Multiple choice, drag-and-drop, simulations, and testlets",
        "prerequisites": "CCNA recommended but not required",
        "study_resources": [
            "CCNP Enterprise ENCOR 350-401 Official Cert Guide",
            "Cisco Learning Network Premium",
            "Cisco Modeling Labs (CML) for hands-on practice",
            "INE CCNP Enterprise video course",
            "Boson practice exams",
            "DNA Center sandbox labs"
        ],
        "career_paths": [
            "Senior Network Engineer",
            "Network Architect",
            "SD-Access Specialist",
            "DNA Center Administrator",
            "Enterprise Network Consultant",
            "Network Design Engineer"
        ],
        "salary_range": "$95,000 - $140,000 USD annually",
        "next_steps": "Pursue CCIE Enterprise Infrastructure for expert-level certification or add specialist certifications (wireless, automation, security)."
    },

    "cisco-wireless-specialist": {
        "title": "Cisco Wireless Specialist",
        "full_name": "Cisco Certified Specialist - Enterprise Wireless Implementation",
        "level": "Specialist",
        "badge": "enterprise-wireless.png",
        "exam_code": "ENWLSI 300-430",
        "duration": "90 minutes",
        "cost": "$300 USD",
        "validity": "3 years",
        "rating": "4.6/5",
        "description": "This specialist certification validates advanced wireless implementation skills essential for managing high-density wireless networks through DNA Center. It covers FlexConnect, advanced security, QoS, and location services—all areas where DNA Center's AI provides critical insights.",
        "overview": """<p>The Cisco Certified Specialist - Enterprise Wireless Implementation certification validates advanced skills in deploying and troubleshooting complex wireless networks. This specialist certification focuses on the technologies that Cisco DNA Center optimizes through AI-powered wireless analytics.</p>
<p>This certification covers FlexConnect for branch wireless deployments, advanced QoS and multicast optimization, wireless security with 802.1X and ISE integration, and location services—all critical components of modern enterprise wireless networks.</p>
<p>With the explosion of mobile devices and IoT, wireless expertise is more valuable than ever. This certification prepares you to manage high-density wireless environments using DNA Center's predictive analytics and automated optimization.</p>""",
        "topics": [
            "FlexConnect architecture and branch wireless deployment",
            "Wireless QoS policies and multicast optimization",
            "Advanced location services (CMX, Cisco Spaces, DNA Spaces)",
            "Security for wireless client connectivity (802.1X, ISE, guest access)",
            "Wireless device monitoring and troubleshooting (Client 360, RF analytics)",
            "Device and infrastructure hardening (rogue detection, containment)",
            "High-density wireless design and optimization",
            "Mobility groups and roaming optimization"
        ],
        "why_matters": "Cisco DNA Center's AI-powered wireless optimization relies on properly configured FlexConnect, QoS, and security policies. This certification ensures you can implement wireless infrastructure correctly so DNA Center's predictive analytics can identify real network issues rather than configuration problems. The Client 360 and RF analytics skills directly translate to interpreting DNA Center's wireless insights.",
        "exam_format": "Multiple choice, drag-and-drop, and wireless simulation questions",
        "prerequisites": "CCNA or equivalent knowledge recommended",
        "study_resources": [
            "Implementing Cisco Enterprise Wireless Networks (ENWLSI) course",
            "Cisco Wireless Controller configuration guides",
            "DNA Center wireless deployment guides",
            "Cisco ISE integration documentation",
            "Ekahau Site Survey tool training",
            "Real-world lab practice with WLC and DNA Center"
        ],
        "career_paths": [
            "Wireless Network Engineer",
            "WLAN Specialist",
            "Mobility Engineer",
            "Wireless Security Specialist",
            "RF Design Engineer",
            "IoT Network Architect"
        ],
        "salary_range": "$85,000 - $125,000 USD annually",
        "next_steps": "Combine with CCNP Enterprise or pursue additional specialist certifications in wireless design (ENWLSD) or security."
    },

    "cisco-infrastructure-specialist": {
        "title": "Cisco Infrastructure Specialist",
        "full_name": "Cisco Certified Specialist - Enterprise Advanced Infrastructure Implementation",
        "level": "Specialist",
        "badge": "enterprise-advanced-infra.png",
        "exam_code": "ENARSI 300-410",
        "duration": "90 minutes",
        "cost": "$400 USD",
        "validity": "3 years",
        "rating": "4.7/5",
        "description": "This specialist certification focuses on implementing and troubleshooting advanced routing and services in enterprise networks. It validates deep expertise in Layer 3 technologies, VPN services, and infrastructure automation—critical for interpreting DNA Center's network analytics.",
        "overview": """<p>The Cisco Certified Specialist - Enterprise Advanced Infrastructure Implementation certification validates deep expertise in advanced routing protocols, VPN services, and infrastructure troubleshooting. This specialist certification focuses on Layer 3 technologies that form the backbone of enterprise networks managed by DNA Center.</p>
<p>This certification covers advanced implementations of EIGRP, OSPF, and BGP, along with Layer 3 VPN services like DMVPN, MPLS, and VRF-Lite. You'll also master infrastructure security, high availability protocols, and network services troubleshooting.</p>
<p>When DNA Center's AI detects routing anomalies, path failures, or VPN issues, you need the advanced troubleshooting skills this certification provides to validate and remediate complex enterprise routing scenarios.</p>""",
        "topics": [
            "Advanced routing protocols (EIGRP named mode, OSPF multi-area, BGP)",
            "Layer 3 VPN services (MPLS L3VPN, DMVPN, GET VPN, VRF-Lite)",
            "Infrastructure security (AAA, device hardening, control plane security)",
            "Infrastructure services (FHRP optimization, NTP, SNMP v3, syslog, NetFlow)",
            "Network infrastructure automation (Python, Ansible, EEM scripting)",
            "Troubleshooting methodologies (structured troubleshooting, packet capture)"
        ],
        "why_matters": "When Cisco DNA Center's AI detects routing anomalies, convergence issues, or VPN problems, you need advanced troubleshooting skills to validate the alerts and implement fixes. This certification provides expertise in the exact Layer 3 technologies that DNA Center monitors—from OSPF neighbor relationships to BGP path selection and DMVPN tunnel states. The automation skills also help you build custom remediation workflows triggered by DNA Center events.",
        "exam_format": "Multiple choice, simulations, and troubleshooting scenarios",
        "prerequisites": "CCNA or equivalent routing/switching knowledge",
        "study_resources": [
            "Implementing Cisco Enterprise Advanced Routing (ENARSI) Official Cert Guide",
            "Cisco Modeling Labs (CML) for routing practice",
            "INE ENARSI video course and labs",
            "GNS3 or EVE-NG for topology building",
            "Boson NetSim for ENARSI",
            "Real-world troubleshooting scenarios"
        ],
        "career_paths": [
            "Senior Network Engineer",
            "Routing & Switching Specialist",
            "WAN Engineer",
            "Network Troubleshooting Expert",
            "Enterprise Network Architect",
            "Service Provider Network Engineer"
        ],
        "salary_range": "$90,000 - $135,000 USD annually",
        "next_steps": "Pair with other CCNP concentration exams (wireless, design) or pursue CCIE Enterprise Infrastructure for expert-level mastery."
    },

    "ccie-enterprise": {
        "title": "CCIE Enterprise Infrastructure",
        "full_name": "Cisco Certified Internetwork Expert - Enterprise Infrastructure",
        "level": "Expert",
        "badge": "ccie-enterprise.png",
        "exam_code": "ENCOR 350-401 + 8-hour Lab",
        "duration": "120 min (written) + 8 hours (lab)",
        "cost": "$1,600 USD (lab) + $400 (written)",
        "validity": "3 years",
        "rating": "5.0/5",
        "description": "CCIE Enterprise Infrastructure represents the pinnacle of Cisco networking expertise. This expert-level certification validates comprehensive knowledge in planning, designing, deploying, and optimizing complex enterprise networks—the exact environments where DNA Center delivers maximum value.",
        "overview": """<p>The Cisco Certified Internetwork Expert (CCIE) Enterprise Infrastructure certification represents the pinnacle of networking expertise. With fewer than 70,000 active CCIEs worldwide, this prestigious credential validates expert-level skills in designing, implementing, and troubleshooting the most complex enterprise networks.</p>
<p>CCIE Enterprise Infrastructure requires passing a 120-minute written exam (ENCOR 350-401) plus an intensive 8-hour hands-on lab exam that tests real-world implementation and troubleshooting skills under time pressure. The lab exam is widely considered one of the most challenging technical certifications in the IT industry.</p>
<p>This certification directly covers Cisco Catalyst Center (the new name for DNA Center), SD-Access fabric design, SD-WAN architecture, advanced automation with Python and Ansible, and network assurance—making it the ultimate credential for large-scale DNA Center deployments.</p>""",
        "topics": [
            "Advanced network architecture and design (campus, WAN, data center)",
            "Cisco Catalyst Center (DNA Center) deployment and operations",
            "SD-Access fabric (LISP, VXLAN, TrustSec, fabric design)",
            "SD-WAN architecture (vManage, vSmart, policy design)",
            "Automation and programmability (Python, Ansible, REST APIs, NETCONF, YANG)",
            "Infrastructure security and services (ISE, firewall integration, QoS)",
            "MPLS, multicast, QoS optimization, and IPv6",
            "Network assurance and telemetry (streaming telemetry, model-driven telemetry)",
            "High availability and redundancy design",
            "Troubleshooting complex multi-technology scenarios"
        ],
        "why_matters": "CCIE Enterprise Infrastructure is essential for architecting Cisco DNA Center deployments in large enterprise environments. The certification directly covers Catalyst Center (DNA Center's new branding), SD-Access fabric design, network assurance architecture, and the automation skills needed to maximize DNA Center's AI capabilities across multi-site, multi-thousand-device networks. CCIE-level expertise enables you to design greenfield SD-Access fabrics, migrate brownfield networks to DNA Center management, and architect custom automation workflows.",
        "exam_format": "120-minute written exam + 8-hour hands-on lab with multiple scenarios",
        "prerequisites": "CCNP Enterprise recommended (ENCOR exam required)",
        "study_resources": [
            "Cisco CCIE Enterprise Infrastructure Official Cert Guide Library",
            "Cisco Learning Network CCIE community",
            "INE CCIE Enterprise Infrastructure workbooks",
            "Cisco Modeling Labs (CML) Advanced",
            "Mock lab providers (INE, IEWB, Micronics)",
            "DNA Center DevNet sandboxes"
        ],
        "career_paths": [
            "Principal Network Architect",
            "Distinguished Engineer",
            "Network Consulting Engineer",
            "Enterprise Solutions Architect",
            "Technical Leader / CTO",
            "Cisco TAC Engineer (Advanced Services)"
        ],
        "salary_range": "$120,000 - $200,000+ USD annually",
        "next_steps": "Maintain through continuing education, pursue dual CCIEs (Security, Data Center), or transition to architectural/leadership roles."
    }
}

# Read the template
with open('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/reviews/networking/cisco-ai.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Create certification pages
for cert_id, cert_data in certifications.items():
    # Create the HTML content
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>{cert_data["title"]} - Complete Guide & Review | GenuisNet.ai</title>
    <meta content="{cert_data["description"]}" name="description"/>
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
            --accent-color: #049FD9;
            --accent-hover: #0284c7;
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

        /* Hero Section */
        .cert-hero {{
            padding: calc(80px + var(--space-4xl)) var(--space-lg) var(--space-3xl);
            background: linear-gradient(135deg, rgba(4, 159, 217, 0.1) 0%, rgba(0, 80, 115, 0.05) 100%);
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

        /* Review Section */
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
            background: linear-gradient(135deg, rgba(4, 159, 217, 0.05) 0%, rgba(0, 80, 115, 0.02) 100%);
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

        /* Navbar placeholder */
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
            <img src="../../assets/images/certifications/{cert_data["badge"]}" alt="{cert_data["full_name"]} Badge"/>
        </div>
        <h1>{cert_data["full_name"]}</h1>
        <div class="cert-level">{cert_data["level"]}</div>
        <p style="max-width: 800px; margin: 0 auto; color: var(--text-secondary); font-size: var(--text-lg);">{cert_data["description"]}</p>

        <div class="cert-meta">
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <span>Exam: {cert_data["exam_code"]}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
                </svg>
                <span>{cert_data["duration"]}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <line x1="12" x2="12" y1="1" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"></path>
                </svg>
                <span>{cert_data["cost"]}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                </svg>
                <span>{cert_data["rating"]} Rating</span>
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
        {cert_data["overview"]}
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
            </svg>
            Key Topics Covered
        </h2>
        <p>The {cert_data["full_name"]} exam covers the following domains:</p>
        <ul>
            {''.join([f'<li>{topic}</li>' for topic in cert_data["topics"]])}
        </ul>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
                <line x1="12" x2="12.01" y1="17" y2="17"></line>
            </svg>
            Why This Certification Matters for DNA Center
        </h2>
        <div class="highlight-box">
            <p>{cert_data["why_matters"]}</p>
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
                <div class="value">{cert_data["exam_code"]}</div>
            </div>
            <div class="info-card">
                <h4>Duration</h4>
                <div class="value">{cert_data["duration"]}</div>
            </div>
            <div class="info-card">
                <h4>Exam Cost</h4>
                <div class="value">{cert_data["cost"]}</div>
            </div>
            <div class="info-card">
                <h4>Validity Period</h4>
                <div class="value">{cert_data["validity"]}</div>
            </div>
        </div>

        <div class="info-box">
            <h3>Exam Format</h3>
            <p>{cert_data["exam_format"]}</p>

            <h3>Prerequisites</h3>
            <p>{cert_data["prerequisites"]}</p>
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
            {''.join([f'<li>{resource}</li>' for resource in cert_data["study_resources"]])}
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
            {''.join([f'<li>{path}</li>' for path in cert_data["career_paths"]])}
        </ul>

        <div class="info-box">
            <h3>Expected Salary Range</h3>
            <p style="font-size: var(--text-xl); color: var(--accent-color); font-weight: 700; margin-top: var(--space-sm);">{cert_data["salary_range"]}</p>
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
            <p>{cert_data["next_steps"]}</p>
        </div>

        <p style="margin-top: var(--space-xl);">Ready to get started? Visit the <a href="https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html" style="color: var(--accent-color);">Cisco Learning Network</a> for official training materials and exam registration through <a href="https://home.pearsonvue.com/cisco" style="color: var(--accent-color);">Pearson VUE</a>.</p>

        <p style="margin-top: var(--space-md);">Download your digital badge from <a href="https://www.credly.com/organizations/cisco/badges" style="color: var(--accent-color);">Credly</a> after passing the exam to showcase your achievement on LinkedIn and other professional platforms.</p>
    </section>
</main>

<footer style="background: var(--bg-secondary); padding: var(--space-xl) 0; margin-top: var(--space-4xl); border-top: 1px solid var(--border-color); text-align: center; color: var(--text-tertiary);">
    <div class="container">
        <p>&copy; 2025 GenuisNet.ai. All rights reserved.</p>
        <p style="margin-top: var(--space-sm); font-size: var(--text-sm);">Cisco, CCNA, CCNP, CCIE, and DevNet are trademarks of Cisco Systems, Inc.</p>
    </div>
</footer>

</body>
</html>'''

    # Write the file
    output_path = f'/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/certifications/{cert_id}.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ Created {cert_id}.html")

print("\n✅ All 6 certification pages created successfully!")
