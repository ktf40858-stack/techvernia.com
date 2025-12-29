import json

# Define the certification data
certs = [
    {
        "filename": "ansible-advanced-i18n.js",
        "windowObj": "ansibleAdvancedTranslations",
        "certKey": "ansibleAdvanced",
        "title": "Red Hat Certified Engineer in Ansible Automation",
        "level": "Advanced Level",
        "description": "The Red Hat Certified Engineer in Ansible Automation certification validates advanced skills in automation, configuration management, and infrastructure as code using Ansible. This advanced-level credential demonstrates mastery in designing complex automation solutions, implementing CI/CD pipelines, and optimizing enterprise-scale deployments.",
        "exam_code": "Exam: EX294",
        "duration": "4 hours",
        "cost": "$400",
        "validity": "Valid: 3 years",
        "back_vendor": "Ansible",
        "back_text": "Ansible Review",
        "vendor": "Red Hat, Inc.",
        "trademark": "Red Hat and Ansible are trademarks of Red Hat, Inc."
    },
    {
        "filename": "terraform-associate-i18n.js",
        "windowObj": "terraformAssociateTranslations",
        "certKey": "terraform",
        "title": "HashiCorp Certified: Terraform Associate",
        "level": "Associate Level",
        "description": "The HashiCorp Certified: Terraform Associate certification validates foundational knowledge of infrastructure as code using Terraform. This associate-level credential demonstrates understanding of Terraform workflow, configuration syntax, modules, and state management—essential for automating cloud infrastructure provisioning.",
        "exam_code": "Exam: 003",
        "duration": "60 min",
        "cost": "$70.50",
        "validity": "Valid: 2 years",
        "back_vendor": "Terraform",
        "back_text": "Terraform Review",
        "vendor": "HashiCorp",
        "trademark": "Terraform and HashiCorp are trademarks of HashiCorp."
    },
    {
        "filename": "terraform-professional-i18n.js",
        "windowObj": "terraformProfessionalTranslations",
        "certKey": "terraformPro",
        "title": "HashiCorp Certified: Terraform Professional",
        "level": "Professional Level",
        "description": "The HashiCorp Certified: Terraform Professional certification validates advanced expertise in infrastructure as code using Terraform. This professional-level credential demonstrates mastery in designing scalable infrastructure, implementing complex modules, managing multi-cloud environments, and optimizing Terraform workflows for enterprise deployments.",
        "exam_code": "Exam: PRO-003",
        "duration": "120 min",
        "cost": "$295",
        "validity": "Valid: 2 years",
        "back_vendor": "Terraform",
        "back_text": "Terraform Review",
        "vendor": "HashiCorp",
        "trademark": "Terraform and HashiCorp are trademarks of HashiCorp."
    },
    {
        "filename": "zabbix-specialist-i18n.js",
        "windowObj": "zabbixSpecialistTranslations",
        "certKey": "zabbixSpec",
        "title": "Zabbix 7.0 Certified Specialist (ZCS)",
        "level": "Specialist Level",
        "description": "The Zabbix 7.0 Certified Specialist (ZCS) certification validates foundational knowledge of Zabbix monitoring platform. This specialist-level credential demonstrates expertise in installing, configuring, and managing Zabbix for IT infrastructure monitoring, including network devices, servers, and applications.",
        "exam_code": "Exam: ZCS-7.0",
        "duration": "90 min",
        "cost": "$250",
        "validity": "Valid: 3 years",
        "back_vendor": "Zabbix",
        "back_text": "Zabbix Review",
        "vendor": "Zabbix LLC",
        "trademark": "Zabbix is a trademark of Zabbix LLC."
    },
    {
        "filename": "zabbix-professional-i18n.js",
        "windowObj": "zabbixProfessionalTranslations",
        "certKey": "zabbixPro",
        "title": "Zabbix 7.0 Certified Professional (ZCP)",
        "level": "Professional Level",
        "description": "The Zabbix 7.0 Certified Professional (ZCP) certification validates advanced knowledge of Zabbix monitoring platform. This professional-level credential demonstrates expertise in advanced monitoring configurations, custom integrations, distributed monitoring, and performance optimization for enterprise-scale deployments.",
        "exam_code": "Exam: ZCP-7.0",
        "duration": "120 min",
        "cost": "$350",
        "validity": "Valid: 3 years",
        "back_vendor": "Zabbix",
        "back_text": "Zabbix Review",
        "vendor": "Zabbix LLC",
        "trademark": "Zabbix is a trademark of Zabbix LLC."
    },
    {
        "filename": "zabbix-expert-i18n.js",
        "windowObj": "zabbixExpertTranslations",
        "certKey": "zabbixExp",
        "title": "Zabbix 7.0 Certified Expert (ZCE)",
        "level": "Expert Level",
        "description": "The Zabbix 7.0 Certified Expert (ZCE) certification validates expert-level knowledge of Zabbix monitoring platform. This expert-level credential demonstrates mastery in architecting complex monitoring solutions, developing custom extensions, implementing high-availability configurations, and optimizing Zabbix for large-scale enterprise environments.",
        "exam_code": "Exam: ZCE-7.0",
        "duration": "180 min",
        "cost": "$450",
        "validity": "Valid: 3 years",
        "back_vendor": "Zabbix",
        "back_text": "Zabbix Review",
        "vendor": "Zabbix LLC",
        "trademark": "Zabbix is a trademark of Zabbix LLC."
    },
    {
        "filename": "rhce-i18n.js",
        "windowObj": "rhceTranslations",
        "certKey": "rhce",
        "title": "Red Hat Certified Engineer (RHCE)",
        "level": "Professional Level",
        "description": "The Red Hat Certified Engineer (RHCE) certification validates advanced Linux system administration skills and automation capabilities. This professional-level credential demonstrates expertise in managing Red Hat Enterprise Linux systems, implementing automation with Ansible, and configuring enterprise services at scale.",
        "exam_code": "Exam: EX294",
        "duration": "4 hours",
        "cost": "$400",
        "validity": "Valid: 3 years",
        "back_vendor": "Ansible",
        "back_text": "Ansible Review",
        "vendor": "Red Hat, Inc.",
        "trademark": "Red Hat and RHCE are trademarks of Red Hat, Inc."
    }
]

print(f"Processing {len(certs)} certification files...")
for cert in certs:
    print(f"Would create: {cert['filename']}")

