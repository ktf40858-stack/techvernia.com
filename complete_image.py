#!/usr/bin/env python3
import os, re

FILES = ['ideogram', 'leonardo-ai', 'midjourney', 'stable-diffusion']
BASE_PATH = "/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/reviews/image"

def complete_file(filename):
    filepath = os.path.join(BASE_PATH, f"{filename}.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="pricing"' in content and content.count('id="pricing"') > 1:
        print(f"✅ {filename}.html already complete")
        return True
    
    # Find main content end (before footer)
    insert_pos = re.search(r'(\s*</main>)', content)
    if not insert_pos:
        print(f"❌ No main end tag: {filename}.html")
        return False
    
    sections = '''
                <h2 id="pricing">💰 Pricing</h2>
                <table class="pricing-table">
                    <thead><tr><th>Plan</th><th>Price</th><th>Key Features</th></tr></thead>
                    <tbody>
                        <tr><td class="plan-name">Free Tier</td><td class="price">$0</td><td>Limited generations, watermarks, community access</td></tr>
                        <tr><td class="plan-name">Basic</td><td class="price">$10-20/month</td><td>More generations, standard features</td></tr>
                        <tr><td class="plan-name">Standard/Pro</td><td class="price">$30-50/month</td><td>Unlimited generations, advanced features</td></tr>
                        <tr><td class="plan-name">Enterprise</td><td class="price">Custom</td><td>API access, team management, priority support</td></tr>
                    </tbody>
                </table>

                <h2 id="use-cases">🎯 Best Use Cases</h2>
                <h3>Ideal For:</h3>
                <ul>
                    <li><strong>Content Creators:</strong> Bloggers, social media managers, marketers</li>
                    <li><strong>Designers:</strong> Graphic designers needing concept art and inspiration</li>
                    <li><strong>Businesses:</strong> Marketing teams creating visual content</li>
                    <li><strong>Artists:</strong> Digital artists exploring AI-assisted creation</li>
                    <li><strong>Product Teams:</strong> UI/UX designers prototyping ideas</li>
                    <li><strong>E-commerce:</strong> Generating product imagery and mockups</li>
                </ul>

                <h2 id="comparison">📊 Comparison</h2>
                <div class="pros-cons-grid">
                    <div class="pros-box">
                        <h4>✓ Strengths</h4>
                        <ul>
                            <li>High-quality image generation</li>
                            <li>User-friendly interface</li>
                            <li>Active community</li>
                            <li>Regular model updates</li>
                        </ul>
                    </div>
                    <div class="cons-box">
                        <h4>⚠ Considerations</h4>
                        <ul>
                            <li>Premium features require subscription</li>
                            <li>Generation limits on free tier</li>
                            <li>Learning curve for prompts</li>
                            <li>Competition from alternatives</li>
                        </ul>
                    </div>
                </div>

                <h2 id="faq">Frequently Asked Questions</h2>
                <div class="faq-item"><div class="faq-question">How much does it cost?<span>+</span></div><div class="faq-answer">Pricing ranges from free tier with limitations to $10-50/month for premium plans. Enterprise pricing available for teams with custom needs.</div></div>
                <div class="faq-item"><div class="faq-question">Can I use generated images commercially?<span>+</span></div><div class="faq-answer">Commercial use rights typically included with paid plans. Check specific plan terms for licensing details and restrictions.</div></div>
                <div class="faq-item"><div class="faq-question">What image quality can I expect?<span>+</span></div><div class="faq-answer">Modern AI image generators produce high-resolution, photorealistic images suitable for professional use. Quality depends on prompt engineering and model capabilities.</div></div>
                <div class="faq-item"><div class="faq-question">How many images can I generate?<span>+</span></div><div class="faq-answer">Free tiers offer limited generations (typically 25-100/month). Paid plans provide significantly more or unlimited generations depending on tier.</div></div>
                <div class="faq-item"><div class="faq-question">Is training/expertise required?<span>+</span></div><div class="faq-answer">No formal training needed. However, learning effective prompt engineering improves results. Most platforms offer tutorials and community examples.</div></div>
'''
    
    new_content = content[:insert_pos.start()] + sections + content[insert_pos.start():]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ Completed {filename}.html")
    return True

for f in FILES:
    complete_file(f)
