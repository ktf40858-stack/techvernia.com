#!/usr/bin/env python3
"""
Reformate les 37 certifications au format CCNA avec le background du website
"""

from pathlib import Path

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return f"{int(hex_color[0:2], 16)}, {int(hex_color[2:4], 16)}, {int(hex_color[4:6], 16)}"

def create_ccna_format(cert_id, data):
    rgb = hex_to_rgb(data['c'])
    t = "\n".join([f"            <li>{x}</li>" for x in data['t']])
    r = "\n".join([f"            <li>{x}</li>" for x in data['r']])
    cr = "\n".join([f"            <li>{x}</li>" for x in data['cr']])
    o = "\n".join([f"        <p>{x}</p>" for x in data['o']])
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{data['n']} - {data['v']} | GenuisNet.ai</title>
    <link href="../../assets/images/favicon.png" rel="icon" type="image/png"/>
    <style>
:root{{--bg-primary:#0a0e27;--bg-secondary:#111530;--bg-card:#1a1f3a;--text-primary:#e2e8f0;--text-secondary:#94a3b8;--text-tertiary:#64748b;--accent-color:{data['c']};--border-color:rgba(148,163,184,0.1);--space-xs:0.25rem;--space-sm:0.5rem;--space-md:1rem;--space-lg:1.5rem;--space-xl:2rem;--space-2xl:3rem;--space-3xl:4rem;--space-4xl:6rem;--text-xs:0.75rem;--text-sm:0.875rem;--text-lg:1.125rem;--text-xl:1.25rem;--text-2xl:1.5rem;--text-4xl:2.25rem;--radius-lg:0.75rem;--radius-xl:1rem}}
[data-theme="light"]{{--bg-primary:#f8fafc;--bg-secondary:#f1f5f9;--bg-card:#ffffff;--text-primary:#0f172a;--text-secondary:#475569;--border-color:rgba(15,23,42,0.1)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;background:var(--bg-primary);color:var(--text-primary);line-height:1.6}}
.container{{max-width:1200px;margin:0 auto;padding:0 var(--space-lg)}}
.cert-hero{{padding:calc(80px + var(--space-4xl)) var(--space-lg) var(--space-3xl);background:linear-gradient(135deg,rgba({rgb},0.1) 0%,rgba({rgb},0.05) 100%);text-align:center}}
.cert-badge{{width:180px;height:180px;margin:0 auto var(--space-xl)}}
.cert-badge img{{width:100%;height:100%;object-fit:contain}}
.cert-hero h1{{font-size:clamp(var(--text-2xl),5vw,var(--text-4xl));font-weight:800;margin-bottom:var(--space-sm)}}
.cert-level{{color:var(--accent-color);font-size:var(--text-xl);font-weight:600;margin-bottom:var(--space-lg)}}
.cert-meta{{display:flex;gap:var(--space-xl);justify-content:center;flex-wrap:wrap;margin-top:var(--space-lg)}}
.meta-item{{display:flex;align-items:center;gap:var(--space-xs);color:var(--text-secondary);font-size:var(--text-sm)}}
.review-section{{padding:var(--space-3xl) 0;border-bottom:1px solid var(--border-color)}}
.review-section h2{{display:flex;align-items:center;gap:var(--space-md);font-size:var(--text-2xl);margin-bottom:var(--space-xl);color:var(--text-primary)}}
.review-section p{{color:var(--text-secondary);line-height:1.8;margin-bottom:var(--space-md)}}
.review-section ul{{list-style:none;padding:0}}
.review-section ul li{{padding:var(--space-sm) 0;padding-left:var(--space-lg);color:var(--text-secondary);position:relative}}
.review-section ul li:before{{content:"▹";position:absolute;left:0;color:var(--accent-color);font-weight:bold}}
.info-box{{background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-lg);padding:var(--space-xl);margin:var(--space-xl) 0}}
.info-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:var(--space-lg);margin:var(--space-xl) 0}}
.info-card{{background:var(--bg-card);border:1px solid var(--border-color);border-radius:var(--radius-lg);padding:var(--space-lg)}}
.info-card h4{{color:var(--accent-color);font-size:var(--text-sm);text-transform:uppercase;margin-bottom:var(--space-sm)}}
.info-card .value{{color:var(--text-primary);font-size:var(--text-xl);font-weight:700}}
.highlight-box{{background:linear-gradient(135deg,rgba({rgb},0.05) 0%,rgba({rgb},0.02) 100%);border-radius:var(--radius-lg);border-left:4px solid var(--accent-color);padding:var(--space-xl);margin:var(--space-xl) 0}}
.neon-icon{{width:24px;height:24px;stroke:var(--accent-color)}}
.navbar{{position:fixed;top:0;width:100%;background:var(--bg-secondary);z-index:1000;padding:var(--space-md) 0;border-bottom:1px solid var(--border-color)}}
@media (max-width:768px){{.cert-meta{{flex-direction:column;gap:var(--space-md)}} .info-grid{{grid-template-columns:1fr}}}}
    </style>
</head>
<body>
<nav class="navbar">
    <div class="container">
        <a href="../../index.html" style="color:var(--accent-color);text-decoration:none;font-weight:700;font-size:var(--text-lg)">← Back to GenuisNet.ai</a>
    </div>
</nav>

<header class="cert-hero">
    <div class="container">
        <div class="cert-badge">
            <img src="../../assets/images/certifications/{data['b']}" alt="{data['n']} Badge"/>
        </div>
        <h1>{data['n']}</h1>
        <div class="cert-level">{data['l']} | {data['v']}</div>
        <p style="max-width:800px;margin:0 auto;color:var(--text-secondary);font-size:var(--text-lg)">{data['h']}</p>

        <div class="cert-meta">
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <span>Exam: {data['e']}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
                </svg>
                <span>{data['d']}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <line x1="12" x2="12" y1="1" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"></path>
                </svg>
                <span>{data['co']}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                </svg>
                <span>Validity: {data['va']}</span>
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
{o}
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
            </svg>
            Key Topics Covered
        </h2>
        <p>The {data['n']} certification covers the following key areas:</p>
        <ul>
{t}
        </ul>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            Exam Information
        </h2>
        <div class="info-grid">
            <div class="info-card"><h4>Exam Code</h4><div class="value">{data['e']}</div></div>
            <div class="info-card"><h4>Duration</h4><div class="value">{data['d']}</div></div>
            <div class="info-card"><h4>Exam Cost</h4><div class="value">{data['co']}</div></div>
            <div class="info-card"><h4>Validity Period</h4><div class="value">{data['va']}</div></div>
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
{r}
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
{cr}
        </ul>
        <div class="info-box">
            <h3>Expected Salary Range</h3>
            <p style="font-size:var(--text-xl);color:var(--accent-color);font-weight:700;margin-top:var(--space-sm)">{data['s']}</p>
            <p style="margin-top:var(--space-md);font-size:var(--text-sm)">Salary ranges vary by location, experience, and company size.</p>
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
            <p>{data['nx']}</p>
        </div>
        <p style="margin-top:var(--space-xl)">Ready to get started? Visit the <a href="{data['u']}" style="color:var(--accent-color)" target="_blank">{data['v']} Training Portal</a> for official training materials.</p>
    </section>
</main>

<footer style="background:var(--bg-secondary);padding:var(--space-xl) 0;margin-top:var(--space-4xl);border-top:1px solid var(--border-color);text-align:center;color:var(--text-tertiary)">
    <div class="container">
        <p>&copy; 2025 GenuisNet.ai. All rights reserved.</p>
        <p style="margin-top:var(--space-sm);font-size:var(--text-sm)">{data['v']} and related trademarks are property of {data['v']}.</p>
    </div>
</footer>

</body>
</html>'''

# Données des 37 certifications (format compact)
# n=name, v=vendor, l=level, c=color, b=badge, e=exam, d=duration, co=cost, va=validity
# h=hero, o=overview(list), t=topics(list), r=resources(list), cr=careers(list), s=salary, nx=next, u=url
CERTS = {
  'fortinet-nse8': {'n':'NSE 8','v':'Fortinet','l':'Master Level','c':'#EE3124','b':'fortinet-nse8.png','e':'NSE8','d':'120 min','co':'$400','va':'2 years','u':'https://training.fortinet.com/','h':'Master-level certification for enterprise security architects.','o':['The NSE 8 certification represents the pinnacle of Fortinet security expertise.','Validates your ability to architect complex security infrastructures.'],'t':['Advanced Architecture Design','Strategic Security Planning','Multi-Site Deployment','Performance Optimization'],'r':['NSE 8 Study Guide','Architecture Documentation','Design Workshops'],'cr':['Principal Security Architect','Chief Security Officer','Enterprise Security Consultant'],'s':'$140,000 - $200,000+','nx':'NSE 8 is the apex of Fortinet certification.'},
  'paloalto-pccet': {'n':'PCCET','v':'Palo Alto Networks','l':'Entry-Level','c':'#FA582D','b':'paloalto-pccet.png','e':'PCCET','d':'60 min','co':'$100','va':'3 years','u':'https://www.paloaltonetworks.com/services/education','h':'Entry-level certification validating foundational cybersecurity knowledge.','o':['PCCET is your entry point into Palo Alto Networks cybersecurity.','Designed for beginners and career changers.'],'t':['Cybersecurity Fundamentals','Network Security','Cloud Security Basics'],'r':['PCCET Digital Learning','Cybersecurity Guide','Practice Exams'],'cr':['Junior Security Analyst','SOC Analyst Level 1','Help Desk Security Specialist'],'s':'$45,000 - $65,000','nx':'After PCCET, pursue PCCSA for administrator skills.'},
  'paloalto-pccsa': {'n':'PCCSA','v':'Palo Alto Networks','l':'Associate','c':'#FA582D','b':'paloalto-pccsa.png','e':'PCCSA','d':'80 min','co':'$200','va':'3 years','u':'https://www.paloaltonetworks.com/services/education','h':'Associate-level certification for security administrators.','o':['PCCSA validates skills in deploying and configuring Palo Alto Networks firewalls.'],'t':['Firewall Configuration','Security Policies','Threat Prevention'],'r':['PCCSA Training','Hands-On Labs','Configuration Guides'],'cr':['Security Operations Analyst','Firewall Administrator','Network Security Engineer'],'s':'$70,000 - $95,000','nx':'After PCCSA, pursue PCCSE for engineering skills.'},
  'paloalto-pccse': {'n':'PCCSE','v':'Palo Alto Networks','l':'Engineer','c':'#FA582D','b':'paloalto-pccse.png','e':'PCCSE','d':'90 min','co':'$250','va':'2 years','u':'https://www.paloaltonetworks.com/services/education','h':'Engineer-level certification for advanced deployments.','o':['PCCSE validates advanced engineering skills in Palo Alto Networks solutions.'],'t':['Advanced Firewall Deployment','Panorama Management','Advanced Threat Prevention'],'r':['PCCSE Training','Enterprise Architecture Guide','Advanced Labs'],'cr':['Senior Security Engineer','Network Security Architect','Principal Firewall Engineer'],'s':'$95,000 - $140,000','nx':'PCCSE demonstrates expert-level proficiency.'},
  'paloalto-pcsae': {'n':'PCSAE','v':'Palo Alto Networks','l':'Automation Engineer','c':'#FA582D','b':'paloalto-pcsae.png','e':'PCSAE','d':'90 min','co':'$250','va':'2 years','u':'https://www.paloaltonetworks.com/services/education','h':'Security automation engineer certification.','o':['PCSAE validates expertise in security orchestration and automation.'],'t':['Playbook Development','Custom Integrations','Security Automation'],'r':['PCSAE Training','Python for XSOAR','Playbook Library'],'cr':['Security Automation Engineer','SOAR Developer','DevSecOps Engineer'],'s':'$90,000 - $135,000','nx':'PCSAE is essential for SOAR specialists.'},
  'microsoft-sc900': {'n':'SC-900','v':'Microsoft','l':'Fundamentals','c':'#00A4EF','b':'microsoft-sc900.png','e':'SC-900','d':'60 min','co':'$99','va':'Lifetime','u':'https://learn.microsoft.com/certifications/','h':'Foundational Microsoft security certification.','o':['SC-900 provides foundational understanding of Microsoft security solutions.'],'t':['Security Concepts','Identity & Access','Microsoft Security Solutions'],'r':['Microsoft Learn Path','Study Guide','Practice Assessment'],'cr':['IT Support Specialist','Junior Security Analyst','Help Desk Technician'],'s':'$45,000 - $70,000','nx':'After SC-900, pursue SC-200 or SC-300.'},
  'microsoft-sc300': {'n':'SC-300','v':'Microsoft','l':'Identity Administrator','c':'#00A4EF','b':'microsoft-sc300.png','e':'SC-300','d':'120 min','co':'$165','va':'1 year','u':'https://learn.microsoft.com/certifications/','h':'Identity and access management certification.','o':['SC-300 validates skills in Azure AD and identity management.'],'t':['Azure AD Implementation','Authentication Solutions','Conditional Access'],'r':['SC-300 Learning Path','Hands-On Labs','Practice Tests'],'cr':['Identity Administrator','Azure AD Specialist','IAM Engineer'],'s':'$85,000 - $125,000','nx':'SC-300 is essential for identity professionals.'},
  'microsoft-sc400': {'n':'SC-400','v':'Microsoft','l':'Information Protection','c':'#00A4EF','b':'microsoft-sc400.png','e':'SC-400','d':'120 min','co':'$165','va':'1 year','u':'https://learn.microsoft.com/certifications/','h':'Information protection certification.','o':['SC-400 demonstrates expertise in Microsoft Purview and data protection.'],'t':['Information Protection','Data Loss Prevention','Data Lifecycle Management'],'r':['SC-400 Learning Path','Purview Documentation','Training Course'],'cr':['Information Protection Administrator','Data Governance Specialist','Compliance Manager'],'s':'$80,000 - $120,000','nx':'SC-400 is crucial for data protection roles.'},
  'microsoft-az500': {'n':'AZ-500','v':'Microsoft','l':'Azure Security','c':'#00A4EF','b':'microsoft-az500.png','e':'AZ-500','d':'120 min','co':'$165','va':'1 year','u':'https://learn.microsoft.com/certifications/','h':'Azure security engineer certification.','o':['AZ-500 validates ability to implement Azure security controls.'],'t':['Identity & Access','Platform Protection','Security Operations'],'r':['AZ-500 Learning Path','Azure Security Labs','Practice Exams'],'cr':['Azure Security Engineer','Cloud Security Architect','DevSecOps Engineer'],'s':'$95,000 - $145,000','nx':'AZ-500 is essential for Azure security professionals.'},
  'cisco-cyberops': {'n':'CyberOps Associate','v':'Cisco','l':'Associate','c':'#1BA0D7','b':'cisco-cyberops.png','e':'200-201','d':'120 min','co':'$300','va':'3 years','u':'https://www.cisco.com/c/en/us/training-events/training-certifications/certifications.html','h':'SOC analyst certification.','o':['CyberOps Associate validates SOC analyst skills.'],'t':['Security Concepts','Security Monitoring','Host-Based Analysis'],'r':['CyberOps Training','NetAcad Course','Virtual Labs'],'cr':['SOC Analyst','Security Operations Analyst','Incident Response Analyst'],'s':'$65,000 - $90,000','nx':'After CyberOps, pursue CCNP Security.'},
  'cisco-ccnp-security': {'n':'CCNP Security','v':'Cisco','l':'Professional','c':'#1BA0D7','b':'cisco-ccnp-security.png','e':'350-701','d':'120 min','co':'$400','va':'3 years','u':'https://www.cisco.com/c/en/us/training-events/training-certifications/certifications.html','h':'Professional security certification.','o':['CCNP Security validates professional-level security skills.'],'t':['Network Security','Cisco Firepower','VPN Technologies'],'r':['CCNP Security Training','Certification Guide','Lab Environment'],'cr':['Network Security Engineer','Security Infrastructure Engineer','Security Architect'],'s':'$90,000 - $130,000','nx':'CCNP Security demonstrates professional expertise.'},
  'cisco-ccie-security': {'n':'CCIE Security','v':'Cisco','l':'Expert','c':'#1BA0D7','b':'cisco-ccie-security.png','e':'CCIE Lab','d':'8 hours','co':'$1,600','va':'3 years','u':'https://www.cisco.com/c/en/us/training-events/training-certifications/certifications.html','h':'Expert-level security certification.','o':['CCIE Security represents the highest level of Cisco security expertise.'],'t':['Advanced Network Security','Firepower NGFW/NGIPS','ISE'],'r':['CCIE Lab Training','Mock Labs','Expert Documentation'],'cr':['Principal Security Engineer','Chief Security Architect','Distinguished Engineer'],'s':'$130,000 - $200,000+','nx':'CCIE Security is the apex of Cisco certification.'},
  'crowdstrike-ccfr': {'n':'CCFR','v':'CrowdStrike','l':'Falcon Responder','c':'#E01F3D','b':'crowdstrike-ccfr.png','e':'CCFR','d':'90 min','co':'Contact Sales','va':'2 years','u':'https://www.crowdstrike.com/university/','h':'Incident response certification.','o':['CCFR validates incident response skills with CrowdStrike Falcon.'],'t':['Incident Investigation','Host Containment','Real-Time Response'],'r':['CCFR Training','Falcon Platform Labs','Response Playbooks'],'cr':['Incident Response Analyst','SOC Analyst','Threat Response Specialist'],'s':'$75,000 - $110,000','nx':'After CCFR, pursue CCFH for hunting skills.'},
  'crowdstrike-ccfh': {'n':'CCFH','v':'CrowdStrike','l':'Falcon Hunter','c':'#E01F3D','b':'crowdstrike-ccfh.png','e':'CCFH','d':'90 min','co':'Contact Sales','va':'2 years','u':'https://www.crowdstrike.com/university/','h':'Threat hunting certification.','o':['CCFH demonstrates advanced threat hunting skills.'],'t':['Threat Hunting Methodology','Advanced Search','Custom IOA'],'r':['CCFH Training','Hunting Labs','Hunting Playbooks'],'cr':['Threat Hunter','Advanced SOC Analyst','Detection Engineer'],'s':'$90,000 - $135,000','nx':'CCFH is essential for threat hunters.'},
  'ibm-qradar-siem': {'n':'QRadar SIEM','v':'IBM','l':'Specialist','c':'#0F62FE','b':'ibm-qradar-siem.png','e':'C1000-142','d':'90 min','co':'$200','va':'Lifetime','u':'https://www.ibm.com/training/','h':'SIEM specialist certification.','o':['QRadar SIEM Specialist validates SIEM administration skills.'],'t':['QRadar Architecture','Log Source Configuration','Custom Rules'],'r':['QRadar Training','Community Edition','Documentation'],'cr':['SIEM Administrator','Security Operations Analyst','SOC Engineer'],'s':'$75,000 - $115,000','nx':'QRadar Specialist is essential for SIEM admins.'},
  'ibm-qradar-analyst': {'n':'QRadar Analyst','v':'IBM','l':'Associate','c':'#0F62FE','b':'ibm-qradar-analyst.png','e':'C1000-123','d':'90 min','co':'$200','va':'Lifetime','u':'https://www.ibm.com/training/','h':'Security analyst certification.','o':['QRadar Analyst validates security analysis skills.'],'t':['Offense Analysis','Event Investigation','QRadar Search'],'r':['Analyst Training','QRadar CE','AQL Guide'],'cr':['Security Operations Analyst','SOC Analyst','Incident Response Analyst'],'s':'$65,000 - $95,000','nx':'QRadar Analyst is key for SOC roles.'},
  'cyberark-defender': {'n':'CyberArk Defender','v':'CyberArk','l':'Defender','c':'#0066B1','b':'cyberark-defender.png','e':'PAM-DEF','d':'90 min','co':'Varies','va':'2 years','u':'https://www.cyberark.com/services-support/technical-certifications/','h':'PAM foundational certification.','o':['CyberArk Defender validates foundational PAM knowledge.'],'t':['PAM Fundamentals','Vault Architecture','Safe Management'],'r':['Defender Training','CyberArk University','Product Documentation'],'cr':['PAM Administrator','Privileged Access Analyst','Security Administrator'],'s':'$70,000 - $100,000','nx':'After Defender, pursue Sentry.'},
  'cyberark-sentry': {'n':'CyberArk Sentry','v':'CyberArk','l':'Sentry','c':'#0066B1','b':'cyberark-sentry.png','e':'PAM-SEN','d':'120 min','co':'Varies','va':'2 years','u':'https://www.cyberark.com/services-support/technical-certifications/','h':'PAM professional certification.','o':['CyberArk Sentry demonstrates advanced PAM skills.'],'t':['Installation & Configuration','PSM Deployment','CPM Configuration'],'r':['Sentry Training','Implementation Guides','Hands-On Labs'],'cr':['PAM Engineer','CyberArk Administrator','Senior IAM Engineer'],'s':'$95,000 - $140,000','nx':'Sentry is essential for PAM engineers.'},
  'cyberark-guardian': {'n':'CyberArk Guardian','v':'CyberArk','l':'Guardian','c':'#0066B1','b':'cyberark-guardian.png','e':'PAM-CDE','d':'150 min','co':'Varies','va':'2 years','u':'https://www.cyberark.com/services-support/technical-certifications/','h':'PAM expert certification.','o':['CyberArk Guardian represents expert-level PAM mastery.'],'t':['Enterprise Architecture','Disaster Recovery','Performance Tuning'],'r':['Guardian Training','Architecture Workshops','Best Practices Guide'],'cr':['PAM Architect','Principal Security Engineer','CyberArk Delivery Lead'],'s':'$120,000 - $170,000+','nx':'Guardian is the apex of CyberArk certification.'},
  'okta-professional': {'n':'Okta Professional','v':'Okta','l':'Professional','c':'#007DC1','b':'okta-professional.png','e':'OCP','d':'90 min','co':'Varies','va':'2 years','u':'https://www.okta.com/services/training/','h':'Okta foundational certification.','o':['Okta Professional validates foundational Okta knowledge.'],'t':['Okta Fundamentals','User Management','Application Integration'],'r':['Okta Foundations','Admin Console Guide','Practice Environment'],'cr':['Identity Administrator','Okta Administrator','IAM Analyst'],'s':'$65,000 - $95,000','nx':'After Professional, pursue Administrator.'},
  'okta-administrator': {'n':'Okta Administrator','v':'Okta','l':'Administrator','c':'#007DC1','b':'okta-administrator.png','e':'OCA','d':'120 min','co':'Varies','va':'2 years','u':'https://www.okta.com/services/training/','h':'Okta administration certification.','o':['Okta Administrator demonstrates advanced Okta skills.'],'t':['Advanced User Management','App Integrations','Lifecycle Management'],'r':['Administrator Training','Advanced Integration Guide','Workflows Documentation'],'cr':['Senior Identity Administrator','Okta Solutions Engineer','IAM Engineer'],'s':'$85,000 - $125,000','nx':'Administrator is essential for Okta admins.'},
  'okta-consultant': {'n':'Okta Consultant','v':'Okta','l':'Consultant','c':'#007DC1','b':'okta-consultant.html','e':'OCC','d':'120 min','co':'Varies','va':'2 years','u':'https://www.okta.com/services/training/','h':'Okta consulting certification.','o':['Okta Consultant validates solution design skills.'],'t':['Solution Design','Requirements Analysis','Implementation Planning'],'r':['Consultant Training','Implementation Playbooks','Architecture Patterns'],'cr':['Identity Consultant','Okta Solutions Architect','IAM Architect'],'s':'$100,000 - $150,000','nx':'Consultant is key for architects.'},
  'okta-developer': {'n':'Okta Developer','v':'Okta','l':'Developer','c':'#007DC1','b':'okta-developer.png','e':'OCD','d':'90 min','co':'Varies','va':'2 years','u':'https://www.okta.com/services/training/','h':'Okta development certification.','o':['Okta Developer validates application integration skills.'],'t':['OAuth 2.0 & OIDC','Okta APIs','SDK Integration'],'r':['Developer Training','SDK Documentation','API Reference'],'cr':['Application Developer','Identity Developer','Security Developer'],'s':'$80,000 - $130,000','nx':'Developer is essential for app developers.'},
  'qualys-vmdr': {'n':'Qualys VMDR','v':'Qualys','l':'Specialist','c':'#ED2E27','b':'qualys-vmdr.png','e':'VMDR','d':'90 min','co':'FREE','va':'2 years','u':'https://www.qualys.com/training/','h':'Vulnerability management certification.','o':['Qualys VMDR validates vulnerability management skills.'],'t':['Vulnerability Scanning','Asset Management','Patch Management'],'r':['VMDR Training','Community Edition','Knowledge Base'],'cr':['Vulnerability Analyst','Security Assessment Specialist','Risk Assessment Analyst'],'s':'$70,000 - $105,000','nx':'VMDR is essential for vulnerability analysts.'},
  'qualys-was': {'n':'Qualys WAS','v':'Qualys','l':'Specialist','c':'#ED2E27','b':'qualys-was.png','e':'WAS','d':'90 min','co':'FREE','va':'2 years','u':'https://www.qualys.com/training/','h':'Web application security certification.','o':['Qualys WAS validates web application security skills.'],'t':['Web App Scanning','OWASP Top 10','Scan Configuration'],'r':['WAS Training','OWASP Guide','API Documentation'],'cr':['Application Security Engineer','Web Application Security Analyst','DevSecOps Engineer'],'s':'$75,000 - $115,000','nx':'WAS is key for AppSec professionals.'},
  'rapid7-insightvm': {'n':'Rapid7 InsightVM','v':'Rapid7','l':'Administrator','c':'#FF6700','b':'rapid7-insightvm.png','e':'InsightVM','d':'90 min','co':'FREE','va':'Lifetime','u':'https://www.rapid7.com/services/training-certification/','h':'Vulnerability management certification.','o':['InsightVM Administrator validates vulnerability management skills.'],'t':['InsightVM Deployment','Vulnerability Scanning','Risk Prioritization'],'r':['InsightVM Training','Product Documentation','University Portal'],'cr':['Vulnerability Management Specialist','Security Risk Analyst','Infrastructure Security Engineer'],'s':'$70,000 - $110,000','nx':'InsightVM is essential for vulnerability management.'},
  'rapid7-insightidr': {'n':'Rapid7 InsightIDR','v':'Rapid7','l':'Administrator','c':'#FF6700','b':'rapid7-insightidr.png','e':'InsightIDR','d':'90 min','co':'FREE','va':'Lifetime','u':'https://www.rapid7.com/services/training-certification/','h':'SIEM and incident response certification.','o':['InsightIDR Administrator validates SIEM skills.'],'t':['InsightIDR Deployment','Threat Detection','Investigation'],'r':['InsightIDR Training','Detection Library','Investigation Guide'],'cr':['SOC Analyst','Incident Response Analyst','SIEM Administrator'],'s':'$75,000 - $115,000','nx':'InsightIDR is key for SOC analysts.'},
  'tenable-nessus': {'n':'Nessus Certified','v':'Tenable','l':'Professional','c':'#00B388','b':'tenable-nessus.png','e':'Nessus-Pro','d':'90 min','co':'Varies','va':'2 years','u':'https://www.tenable.com/education','h':'Vulnerability scanning certification.','o':['Nessus Certified validates vulnerability scanning proficiency.'],'t':['Nessus Fundamentals','Scan Configuration','Credentialed Scanning'],'r':['Nessus Training','Nessus Essentials','Plugin Documentation'],'cr':['Vulnerability Analyst','Penetration Tester','Security Assessment Specialist'],'s':'$70,000 - $110,000','nx':'Nessus is essential for pentesters.'},
  'darktrace-engineer': {'n':'Darktrace Engineer','v':'Darktrace','l':'Engineer','c':'#E94E1B','b':'darktrace-engineer.png','e':'DCE','d':'90 min','co':'Partner Program','va':'2 years','u':'https://www.darktrace.com/en/services/','h':'AI security platform certification.','o':['Darktrace Engineer validates AI-powered threat detection skills.'],'t':['Darktrace Architecture','AI Threat Detection','Autonomous Response'],'r':['Engineer Training','Threat Visualizer Guide','Best Practices'],'cr':['Darktrace Engineer','AI Security Specialist','Threat Detection Engineer'],'s':'$85,000 - $130,000','nx':'Darktrace Engineer is key for AI security.'},
  'sentinelone-core': {'n':'SentinelOne Core','v':'SentinelOne','l':'Administrator','c':'#6A1B9A','b':'sentinelone-core.png','e':'S1-Core','d':'90 min','co':'Customer Program','va':'2 years','u':'https://www.sentinelone.com/services/','h':'Endpoint security certification.','o':['SentinelOne Core validates endpoint security skills.'],'t':['Platform Overview','Agent Deployment','Policy Management'],'r':['Core Training','Admin Guide','Knowledge Base'],'cr':['Endpoint Security Administrator','EDR Analyst','SOC Analyst'],'s':'$70,000 - $105,000','nx':'Core is essential for endpoint security.'},
  'sentinelone-advanced': {'n':'SentinelOne Advanced','v':'SentinelOne','l':'Advanced','c':'#6A1B9A','b':'sentinelone-advanced.png','e':'S1-Adv','d':'120 min','co':'Customer Program','va':'2 years','u':'https://www.sentinelone.com/services/','h':'Advanced endpoint security certification.','o':['SentinelOne Advanced validates advanced EDR skills.'],'t':['Advanced Threat Hunting','Deep Visibility','Storylines Investigation'],'r':['Advanced Training','API Documentation','Threat Hunting Guide'],'cr':['Threat Hunter','Senior EDR Engineer','Advanced SOC Analyst'],'s':'$95,000 - $145,000','nx':'Advanced is key for threat hunters.'},
  'sophos-engineer': {'n':'Sophos Engineer','v':'Sophos','l':'Engineer','c':'#00BFFF','b':'sophos-engineer.png','e':'SCE','d':'90 min','co':'Partner Program','va':'2 years','u':'https://www.sophos.com/en-us/support/professional-services','h':'Sophos security certification.','o':['Sophos Engineer validates Sophos product expertise.'],'t':['Sophos Firewall','Endpoint Protection','Email Security'],'r':['Engineer Training','Product Documentation','Partner Portal'],'cr':['Sophos Engineer','Network Security Engineer','Security Solutions Engineer'],'s':'$80,000 - $120,000','nx':'Engineer is essential for Sophos specialists.'},
  'sophos-architect': {'n':'Sophos Architect','v':'Sophos','l':'Architect','c':'#00BFFF','b':'sophos-architect.png','e':'SCA','d':'120 min','co':'Partner Program','va':'2 years','u':'https://www.sophos.com/en-us/support/professional-services','h':'Sophos architecture certification.','o':['Sophos Architect validates solution design expertise.'],'t':['Security Architecture','High Availability','Enterprise Deployment'],'r':['Architect Training','Architecture Guides','Best Practices Library'],'cr':['Security Architect','Solutions Architect','Principal Security Engineer'],'s':'$110,000 - $160,000','nx':'Architect is key for solution architects.'},
  'trendmicro-professional': {'n':'Trend Micro Pro','v':'Trend Micro','l':'Professional','c':'#D71920','b':'trendmicro-professional.png','e':'TMCP','d':'90 min','co':'Varies','va':'2 years','u':'https://www.trendmicro.com/en_us/partners/training-certification.html','h':'Trend Micro security certification.','o':['Trend Micro Professional validates product expertise.'],'t':['Apex One','Deep Security','Cloud App Security'],'r':['Professional Training','Product Documentation','Training Portal'],'cr':['Trend Micro Specialist','Endpoint Security Engineer','Cloud Security Engineer'],'s':'$80,000 - $120,000','nx':'Professional is essential for Trend Micro users.'},
  'trendmicro-expert': {'n':'Trend Micro Expert','v':'Trend Micro','l':'Expert','c':'#D71920','b':'trendmicro-expert.png','e':'TMCE','d':'120 min','co':'Varies','va':'2 years','u':'https://www.trendmicro.com/en_us/partners/training-certification.html','h':'Advanced Trend Micro certification.','o':['Trend Micro Expert demonstrates advanced expertise.'],'t':['Enterprise Architecture','Advanced Deployment','XDR Implementation'],'r':['Expert Training','Architecture Library','Advanced Labs'],'cr':['Security Architect','Principal Security Engineer','Solution Architect'],'s':'$110,000 - $165,000','nx':'Expert is the apex of Trend Micro certification.'},
  'splunk-es-admin': {'n':'Splunk ES Admin','v':'Splunk','l':'Administrator','c':'#FF6B00','b':'splunk-es-admin.png','e':'SPLK-3003','d':'57 min','co':'$250','va':'3 years','u':'https://www.splunk.com/en_us/training.html','h':'Splunk Enterprise Security certification.','o':['Splunk ES Admin validates Splunk ES expertise.'],'t':['ES Architecture','Data Models','Correlation Searches'],'r':['ES Admin Course','ES Documentation','Practice Exam'],'cr':['Splunk ES Administrator','SOC Engineer','SIEM Administrator'],'s':'$90,000 - $135,000','nx':'ES Admin is essential for Splunk ES users.'},
  'splunk-soar-dev': {'n':'Splunk SOAR Dev','v':'Splunk','l':'Developer','c':'#FF6B00','b':'splunk-soar-dev.png','e':'SPLK-2003','d':'57 min','co':'$250','va':'3 years','u':'https://www.splunk.com/en_us/training.html','h':'Splunk SOAR development certification.','o':['Splunk SOAR Dev validates automation development skills.'],'t':['Playbook Development','Custom Apps','API Integration'],'r':['SOAR Developer Course','App Development Guide','Python SDK'],'cr':['SOAR Developer','Security Automation Engineer','DevSecOps Engineer'],'s':'$95,000 - $145,000','nx':'SOAR Dev is key for automation engineers.'},
}

print("╔═══════════════════════════════════════════════════════════════╗")
print("║   🚀 REFORMATAGE DE TOUTES LES CERTIFICATIONS                ║")
print("╚═══════════════════════════════════════════════════════════════╝\n")

output_dir = Path('pages/certifications')
total = len(CERTS)
done = 0

for cert_id, data in CERTS.items():
    html = create_ccna_format(cert_id, data)
    filepath = output_dir / f"{cert_id}.html"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    done += 1
    print(f"✓ {cert_id}.html ({done}/{total})")

print(f"\n{'═' * 65}")
print(f"✅ REFORMATAGE TERMINÉ")
print(f"{'═' * 65}")
print(f"Pages reformatées: {done}/{total}")
print(f"Format: CCNA avec background du website")
print(f"{'═' * 65}\n")

