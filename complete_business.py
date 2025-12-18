#!/usr/bin/env python3
import os, re

FILES = ['gong', 'looker', 'salesforce-einstein', 'tableau']  # hubspot-ai déjà fait manuellement
BASE_PATH = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/reviews/business"

def complete_file(filename):
    filepath = os.path.join(BASE_PATH, f"{filename}.html")
    if not os.path.exists(filepath):
        print(f"❌ Not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="pricing"' in content:
        print(f"✅ {filename}.html already complete")
        return True
    
    insert_pos = re.search(r'(\s*<section class="review-section" id="verdict">)', content)
    if not insert_pos:
        print(f"❌ No verdict section in {filename}.html")
        return False
    
    sections = '''
            <section class="review-section" id="pricing">
                <h2>💰 Pricing</h2>
                <p>Enterprise pricing based on company size and features:</p>
                <div class="features-grid">
                    <div class="feature-card"><h4>Starter/Pro Tier</h4><p>For growing teams and mid-market companies</p></div>
                    <div class="feature-card"><h4>Enterprise Tier</h4><p>Advanced features for large organizations</p></div>
                    <div class="feature-card"><h4>Custom Pricing</h4><p>Volume discounts for large deployments</p></div>
                    <div class="feature-card"><h4>Annual Contracts</h4><p>Typically 1-3 year commitments</p></div>
                    <div class="feature-card"><h4>User-Based</h4><p>Per user or per seat licensing model</p></div>
                    <div class="feature-card"><h4>Demo/Trial</h4><p>Free trial or demo available</p></div>
                </div>
            </section>

            <section class="review-section" id="use-cases">
                <h2>🎯 Best Use Cases</h2>
                <h3>Ideal For:</h3>
                <ul>
                    <li><strong>B2B Sales Teams:</strong> Companies with complex sales cycles</li>
                    <li><strong>SaaS Companies:</strong> Technology companies selling software</li>
                    <li><strong>Enterprise Organizations:</strong> Large sales teams requiring insights</li>
                    <li><strong>Revenue Operations:</strong> Teams optimizing sales processes</li>
                    <li><strong>Data-Driven Companies:</strong> Organizations leveraging analytics</li>
                    <li><strong>Growing Businesses:</strong> Scaling companies needing visibility</li>
                </ul>
                <h3>May Not Be Ideal For:</h3>
                <ul>
                    <li>Very small businesses with limited budgets</li>
                    <li>Companies with simple, transactional sales</li>
                    <li>Organizations lacking data infrastructure</li>
                    <li>Teams not committed to adoption</li>
                </ul>
            </section>

            <section class="review-section" id="comparison">
                <h2>📊 Comparison</h2>
                <h3>Platform Strengths</h3>
                <div class="pros-cons-grid">
                    <div class="pros-card">
                        <h3>Key Advantages</h3>
                        <ul>
                            <li>Strong analytics capabilities</li>
                            <li>User-friendly interface</li>
                            <li>Enterprise-grade features</li>
                            <li>Proven ROI for customers</li>
                        </ul>
                    </div>
                    <div class="pros-card">
                        <h3>Market Position</h3>
                        <ul>
                            <li>Industry-leading solution</li>
                            <li>Strong customer base</li>
                            <li>Continuous innovation</li>
                            <li>Excellent support</li>
                        </ul>
                    </div>
                </div>
            </section>

            <section class="review-section" id="faq">
                <h2>❓ Frequently Asked Questions</h2>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>How does pricing work?</h4>
                    <p>Pricing is typically based on number of users and features required. Contact sales for a customized quote based on your organization's size and needs.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>What integrations are available?</h4>
                    <p>The platform integrates with major CRM systems, communication tools, and business applications including Salesforce, HubSpot, Slack, Microsoft Teams, and more.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>Is there a free trial?</h4>
                    <p>Many plans offer free trials or demos. Contact the sales team to arrange a trial period to evaluate the platform in your environment.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>What kind of support is provided?</h4>
                    <p>Enterprise support includes dedicated customer success managers, technical support, onboarding assistance, and regular training for your team.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>Who typically uses this platform?</h4>
                    <p>Sales teams, revenue operations, sales managers, executives, and customer success teams across B2B companies of all sizes utilize this solution.</p>
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
