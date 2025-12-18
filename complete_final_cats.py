#!/usr/bin/env python3
import os, re

CATEGORIES = {
    'productivity': ['clickup-ai', 'firefliesai', 'mem-ai', 'motion', 'notion-ai', 'otterai', 'reclaim-ai', 'zapier'],
    'architecture': ['architechtures', 'arko-ai', 'finch3d', 'hypar', 'maket-ai', 'spacemaker-ai', 'testfit', 'veras-ai'],
    'medical': ['aidoc', 'butterfly-iq', 'nuance-dragon', 'paige-ai', 'pathai', 'tempus', 'viz-ai', 'zebra-medical'],
    'chatbots': ['copilot', 'gemini', 'perplexity', 'poe']
}

BASE_PATH = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/reviews"

sections_template = '''
            <section class="review-section" id="pricing">
                <h2>💰 Pricing</h2>
                <p>Flexible pricing options for different needs:</p>
                <div class="features-grid">
                    <div class="feature-card"><h4>Free Plan</h4><p>Basic features with limitations</p></div>
                    <div class="feature-card"><h4>Pro/Plus</h4><p>$10-25/month for individuals</p></div>
                    <div class="feature-card"><h4>Team/Business</h4><p>$15-40/user/month for teams</p></div>
                    <div class="feature-card"><h4>Enterprise</h4><p>Custom pricing for large organizations</p></div>
                    <div class="feature-card"><h4>Annual Savings</h4><p>20-40% discount on annual plans</p></div>
                    <div class="feature-card"><h4>Free Trial</h4><p>Test all features risk-free</p></div>
                </div>
            </section>

            <section class="review-section" id="use-cases">
                <h2>🎯 Best Use Cases</h2>
                <h3>Ideal For:</h3>
                <ul>
                    <li><strong>Professionals:</strong> Individuals seeking enhanced productivity and efficiency</li>
                    <li><strong>Teams:</strong> Collaborative environments requiring coordination</li>
                    <li><strong>Enterprises:</strong> Large organizations with complex workflows</li>
                    <li><strong>Remote Workers:</strong> Distributed teams needing communication tools</li>
                    <li><strong>Startups:</strong> Growing companies scaling operations</li>
                    <li><strong>Specific Industries:</strong> Healthcare, architecture, education, etc.</li>
                </ul>
                <h3>May Not Be Ideal For:</h3>
                <ul>
                    <li>Users with very basic requirements</li>
                    <li>Organizations with strict data residency needs</li>
                    <li>Teams unwilling to adopt new workflows</li>
                </ul>
            </section>

            <section class="review-section" id="comparison">
                <h2>📊 Comparison</h2>
                <h3>Platform Evaluation</h3>
                <div class="pros-cons-grid">
                    <div class="pros-card">
                        <h3>Key Strengths</h3>
                        <ul>
                            <li>Advanced AI capabilities</li>
                            <li>Intuitive user experience</li>
                            <li>Strong integration ecosystem</li>
                            <li>Regular feature updates</li>
                        </ul>
                    </div>
                    <div class="pros-card">
                        <h3>Competitive Edge</h3>
                        <ul>
                            <li>Market-leading position</li>
                            <li>Proven track record</li>
                            <li>Excellent support</li>
                            <li>Active community</li>
                        </ul>
                    </div>
                </div>
            </section>

            <section class="review-section" id="faq">
                <h2>❓ Frequently Asked Questions</h2>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>What are the main pricing tiers?</h4>
                    <p>Typical tiers include free (limited features), individual/pro ($10-25/month), team/business ($15-40/user/month), and enterprise (custom pricing).</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>Is there a free version available?</h4>
                    <p>Most platforms offer a free tier with basic features. Premium tiers unlock advanced capabilities, higher usage limits, and priority support.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>How does it integrate with other tools?</h4>
                    <p>Integrations typically include popular productivity tools, communication platforms, project management systems, and industry-specific software.</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>What kind of support is provided?</h4>
                    <p>Support ranges from community forums and documentation (free tier) to email support (paid), and dedicated account managers (enterprise).</p>
                </div>
                <div class="feature-card" style="margin-bottom: var(--space-md);">
                    <h4>Can I try before committing?</h4>
                    <p>Yes, free trials or freemium models allow testing features before purchasing. Trial periods typically range from 7-30 days.</p>
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
        insert_pos = re.search(r'(\s*</main>)', content)
        if not insert_pos:
            print(f"❌ No insertion point: {cat}/{filename}.html")
            return False
    
    new_content = content[:insert_pos.start()] + sections_template + content[insert_pos.start():]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ Completed {cat}/{filename}.html")
    return True

total = 0
completed = 0
for cat, files in CATEGORIES.items():
    print(f"\n=== {cat.upper()} ===")
    for f in files:
        total += 1
        if complete_file(cat, f):
            completed += 1

print(f"\n{'='*50}")
print(f"FINAL SUMMARY: {completed}/{total} files completed")
print(f"{'='*50}")
