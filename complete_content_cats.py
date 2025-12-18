#!/usr/bin/env python3
import os, re

CATEGORIES = {
    'coding': ['codewhisperer', 'replit', 'tabnine'],
    'writing': ['jasper-ai', 'quillbot'],
    'seo': ['ahrefs', 'clearscope', 'frase', 'marketmuse', 'neuronwriter', 'scalenut', 'semrush', 'surfer-seo']
}

BASE_PATH = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/reviews"

sections_template = '''
            <section class="review-section" id="pricing">
                <h2>💰 Pricing</h2>
                <p>Flexible pricing for individuals and teams:</p>
                <div class="features-grid">
                    <div class="feature-card"><h4>Free Tier</h4><p>Limited features to get started</p></div>
                    <div class="feature-card"><h4>Individual/Pro</h4><p>$10-30/month for professionals</p></div>
                    <div class="feature-card"><h4>Team</h4><p>$20-50/user/month for teams</p></div>
                    <div class="feature-card"><h4>Enterprise</h4><p>Custom pricing for organizations</p></div>
                    <div class="feature-card"><h4>Annual Discounts</h4><p>Save 20-40% with annual billing</p></div>
                    <div class="feature-card"><h4>Free Trial</h4><p>Try before you buy</p></div>
                </div>
            </section>

            <section class="review-section" id="use-cases">
                <h2>🎯 Best Use Cases</h2>
                <h3>Ideal For:</h3>
                <ul>
                    <li><strong>Professionals:</strong> Individuals seeking productivity enhancements</li>
                    <li><strong>Teams:</strong> Collaborative work requiring quality and speed</li>
                    <li><strong>Content Creators:</strong> Bloggers, marketers, writers</li>
                    <li><strong>Businesses:</strong> Companies scaling content production</li>
                    <li><strong>Agencies:</strong> Service providers managing multiple clients</li>
                    <li><strong>Developers/SEOs:</strong> Technical professionals optimizing workflows</li>
                </ul>
                <h3>May Not Be Ideal For:</h3>
                <ul>
                    <li>Casual users with minimal needs</li>
                    <li>Budget-constrained individuals</li>
                    <li>Teams not needing collaboration</li>
                </ul>
            </section>

            <section class="review-section" id="comparison">
                <h2>📊 Comparison</h2>
                <h3>Platform Overview</h3>
                <div class="pros-cons-grid">
                    <div class="pros-card">
                        <h3>Key Strengths</h3>
                        <ul>
                            <li>Powerful AI capabilities</li>
                            <li>User-friendly interface</li>
                            <li>Regular updates and improvements</li>
                            <li>Strong customer support</li>
                        </ul>
                    </div>
                    <div class="pros-card">
                        <h3>Market Position</h3>
                        <ul>
                            <li>Leading solution in category</li>
                            <li>Large user base</li>
                            <li>Proven ROI</li>
                            <li>Continuous innovation</li>
                        </ul>
                    </div>
                </div>
            </section>

            <section class="review-section" id="faq">
                <h2>❓ Frequently Asked Questions</h2>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>What's included in the free plan?</h4>
                    <p>Free plans typically include basic features with usage limitations. Paid plans unlock advanced capabilities, higher limits, and priority support.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>How does pricing compare to alternatives?</h4>
                    <p>Pricing is competitive with similar tools, offering good value for the feature set. Team and enterprise plans provide volume discounts.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>Can I cancel anytime?</h4>
                    <p>Yes, subscriptions can typically be cancelled anytime. Monthly plans offer more flexibility, while annual plans provide cost savings.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>What integrations are available?</h4>
                    <p>Integrations include popular tools like VS Code, Chrome, WordPress, Google Docs, and many others depending on the category.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>Is there customer support?</h4>
                    <p>Yes, email support is standard. Higher tiers often include priority support, live chat, and dedicated account management.</p>
                </div>
            </section>
'''

def complete_file(cat, filename):
    filepath = os.path.join(BASE_PATH, cat, f"{filename}.html")
    if not os.path.exists(filepath):
        print(f"❌ Not found: {cat}/{filename}.html")
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="pricing"' in content and content.count('id="pricing"') > 1:
        print(f"✅ {cat}/{filename}.html already complete")
        return True
    
    insert_pos = re.search(r'(\s*<section class="review-section" id="verdict">)', content)
    if not insert_pos:
        # Try alternative pattern
        insert_pos = re.search(r'(\s*</main>)', content)
        if not insert_pos:
            print(f"❌ No insertion point: {cat}/{filename}.html")
            return False
    
    new_content = content[:insert_pos.start()] + sections_template + content[insert_pos.start():]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ Completed {cat}/{filename}.html")
    return True

for cat, files in CATEGORIES.items():
    print(f"\n=== {cat.upper()} ===")
    for f in files:
        complete_file(cat, f)
