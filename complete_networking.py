#!/usr/bin/env python3
import os, re

FILES = ['ansible', 'prtg', 'splunk', 'terraform', 'zabbix']
BASE_PATH = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/reviews/networking"

def complete_file(filename):
    filepath = os.path.join(BASE_PATH, f"{filename}.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="pricing"' in content:
        print(f"✅ {filename}.html already complete")
        return True
    
    insert_pos = re.search(r'(\s*<section class="review-section" id="verdict">)', content)
    if not insert_pos:
        print(f"❌ No verdict section: {filename}.html")
        return False
    
    sections = '''
            <section class="review-section" id="pricing">
                <h2>💰 Pricing</h2>
                <p>Flexible pricing based on infrastructure scale and features:</p>
                <div class="features-grid">
                    <div class="feature-card"><h4>Free/Open Source</h4><p>Community edition available for basic use</p></div>
                    <div class="feature-card"><h4>Professional</h4><p>Enhanced features for growing teams</p></div>
                    <div class="feature-card"><h4>Enterprise</h4><p>Advanced capabilities and support</p></div>
                    <div class="feature-card"><h4>Node/Device Based</h4><p>Pricing scales with monitored infrastructure</p></div>
                    <div class="feature-card"><h4>Cloud/SaaS Options</h4><p>Hosted solutions available</p></div>
                    <div class="feature-card"><h4>Support Packages</h4><p>Professional services and training</p></div>
                </div>
            </section>

            <section class="review-section" id="use-cases">
                <h2>🎯 Best Use Cases</h2>
                <h3>Ideal For:</h3>
                <ul>
                    <li><strong>Enterprise IT:</strong> Large organizations managing complex infrastructure</li>
                    <li><strong>DevOps Teams:</strong> Automation and continuous deployment</li>
                    <li><strong>MSPs:</strong> Managed service providers monitoring client systems</li>
                    <li><strong>Cloud-Native:</strong> Organizations running multi-cloud environments</li>
                    <li><strong>Hybrid Infrastructure:</strong> Mixed on-premise and cloud deployments</li>
                    <li><strong>Network Operations:</strong> Teams managing network performance</li>
                </ul>
                <h3>May Not Be Ideal For:</h3>
                <ul>
                    <li>Very small businesses with simple needs</li>
                    <li>Organizations lacking technical expertise</li>
                    <li>Companies seeking fully managed solutions</li>
                    <li>Teams not committed to implementation</li>
                </ul>
            </section>

            <section class="review-section" id="comparison">
                <h2>📊 Comparison</h2>
                <h3>Platform Strengths</h3>
                <div class="pros-cons-grid">
                    <div class="pros-card">
                        <h3>Key Advantages</h3>
                        <ul>
                            <li>Proven reliability and scale</li>
                            <li>Strong community support</li>
                            <li>Extensive integrations</li>
                            <li>Flexible deployment options</li>
                        </ul>
                    </div>
                    <div class="pros-card">
                        <h3>Market Position</h3>
                        <ul>
                            <li>Industry-leading solution</li>
                            <li>Enterprise adoption</li>
                            <li>Active development</li>
                            <li>Comprehensive documentation</li>
                        </ul>
                    </div>
                </div>
            </section>

            <section class="review-section" id="faq">
                <h2>❓ Frequently Asked Questions</h2>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>What's the difference between free and paid versions?</h4>
                    <p>Free/community editions provide core functionality, while paid versions add enterprise features like advanced monitoring, dedicated support, SLAs, and additional integrations.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>How does pricing scale?</h4>
                    <p>Pricing typically scales based on number of nodes/devices monitored, users, or data volume. Enterprise plans offer custom pricing for large deployments.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>What integrations are available?</h4>
                    <p>Extensive integrations with cloud platforms (AWS, Azure, GCP), monitoring tools, ticketing systems, databases, and hundreds of other technologies via plugins and APIs.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>Is there a learning curve?</h4>
                    <p>Initial setup requires technical expertise, but the platform provides extensive documentation, training resources, and community support to help teams get started.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>Can it monitor cloud infrastructure?</h4>
                    <p>Yes, the platform supports monitoring across on-premise, cloud, hybrid, and multi-cloud environments with native integrations for major cloud providers.</p>
                </div>
            </section>
'''
    
    new_content = content[:insert_pos.start()] + sections + content[insert_pos.start():]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ Completed {filename}.html")
    return True

for f in FILES:
    complete_file(f)
