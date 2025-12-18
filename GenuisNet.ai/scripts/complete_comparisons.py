#!/usr/bin/env python3
"""
Complète les comparaisons existantes et en crée de nouvelles
"""

# Contenu complet pour Image Generators Comparison
IMAGE_GENERATORS_CONTENT = {
    'comparison-table': '''
        <h3>Feature Comparison Table</h3>
        <table>
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>Midjourney v6</th>
                    <th>DALL-E 3</th>
                    <th>Stable Diffusion XL</th>
                    <th>Leonardo AI</th>
                    <th>Ideogram 2.0</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Image Quality</strong></td>
                    <td>⭐⭐⭐⭐⭐ Best</td>
                    <td>⭐⭐⭐⭐ Excellent</td>
                    <td>⭐⭐⭐⭐ Very Good</td>
                    <td>⭐⭐⭐⭐ Excellent</td>
                    <td>⭐⭐⭐⭐ Excellent</td>
                </tr>
                <tr>
                    <td><strong>Ease of Use</strong></td>
                    <td>⭐⭐⭐ Discord-based</td>
                    <td>⭐⭐⭐⭐⭐ Easiest (ChatGPT)</td>
                    <td>⭐⭐ Technical</td>
                    <td>⭐⭐⭐⭐ User-friendly</td>
                    <td>⭐⭐⭐⭐ Simple</td>
                </tr>
                <tr>
                    <td><strong>Prompt Understanding</strong></td>
                    <td>⭐⭐⭐⭐ Excellent</td>
                    <td>⭐⭐⭐⭐⭐ Best (GPT-4)</td>
                    <td>⭐⭐⭐ Good</td>
                    <td>⭐⭐⭐⭐ Very Good</td>
                    <td>⭐⭐⭐⭐ Very Good</td>
                </tr>
                <tr>
                    <td><strong>Text in Images</strong></td>
                    <td>⭐⭐⭐ Improving</td>
                    <td>⭐⭐⭐⭐ Good</td>
                    <td>⭐⭐ Poor</td>
                    <td>⭐⭐⭐ Good</td>
                    <td>⭐⭐⭐⭐⭐ Perfect</td>
                </tr>
                <tr>
                    <td><strong>Artistic Style</strong></td>
                    <td>⭐⭐⭐⭐⭐ Most artistic</td>
                    <td>⭐⭐⭐⭐ Polished</td>
                    <td>⭐⭐⭐⭐ Customizable</td>
                    <td>⭐⭐⭐⭐ Game-focused</td>
                    <td>⭐⭐⭐⭐ Clean</td>
                </tr>
                <tr>
                    <td><strong>Free Tier</strong></td>
                    <td>❌ No free tier</td>
                    <td>✅ Limited (ChatGPT Free)</td>
                    <td>✅ Unlimited (open source)</td>
                    <td>✅ 150 tokens/day</td>
                    <td>✅ 25 images/day</td>
                </tr>
                <tr>
                    <td><strong>Pricing (Paid)</strong></td>
                    <td>$10-60/mo</td>
                    <td>$20/mo (ChatGPT Plus)</td>
                    <td>Free (or $10-50 for cloud)</td>
                    <td>$12-48/mo</td>
                    <td>$7-20/mo</td>
                </tr>
                <tr>
                    <td><strong>Image Resolution</strong></td>
                    <td>Up to 2048x2048</td>
                    <td>1024x1024 to 1792x1024</td>
                    <td>1024x1024 (customizable)</td>
                    <td>Up to 1024x1536</td>
                    <td>Up to 2048x2048</td>
                </tr>
                <tr>
                    <td><strong>Generation Speed</strong></td>
                    <td>~60 sec</td>
                    <td>~20 sec</td>
                    <td>~10 sec (local) ~30 sec (cloud)</td>
                    <td>~15 sec</td>
                    <td>~15 sec</td>
                </tr>
                <tr>
                    <td><strong>Batch Generation</strong></td>
                    <td>4 images per prompt</td>
                    <td>1 image per prompt</td>
                    <td>Unlimited</td>
                    <td>Up to 8 images</td>
                    <td>1-4 images</td>
                </tr>
                <tr>
                    <td><strong>Image Editing</strong></td>
                    <td>✅ Vary, Zoom, Pan</td>
                    <td>✅ Edit mode</td>
                    <td>✅ Img2img, Inpainting</td>
                    <td>✅ Canvas editor</td>
                    <td>✅ Magic Edit</td>
                </tr>
                <tr>
                    <td><strong>Style Consistency</strong></td>
                    <td>⭐⭐⭐ Varies</td>
                    <td>⭐⭐⭐ Decent</td>
                    <td>⭐⭐⭐⭐ LoRA models</td>
                    <td>⭐⭐⭐⭐⭐ Best (character sheets)</td>
                    <td>⭐⭐⭐ Good</td>
                </tr>
                <tr>
                    <td><strong>Commercial Use</strong></td>
                    <td>✅ Yes (paid plans)</td>
                    <td>✅ Yes</td>
                    <td>✅ Yes (depends on model)</td>
                    <td>✅ Yes</td>
                    <td>✅ Yes</td>
                </tr>
                <tr>
                    <td><strong>API Access</strong></td>
                    <td>❌ Not yet</td>
                    <td>✅ OpenAI API</td>
                    <td>✅ Many providers</td>
                    <td>✅ API available</td>
                    <td>✅ API available</td>
                </tr>
                <tr>
                    <td><strong>Mobile App</strong></td>
                    <td>✅ iOS, Android (via Discord)</td>
                    <td>✅ ChatGPT app</td>
                    <td>✅ Third-party apps</td>
                    <td>✅ iOS, Android</td>
                    <td>✅ iOS, Android</td>
                </tr>
            </tbody>
        </table>

        <h3>Pricing Detailed Comparison</h3>
        <table>
            <thead>
                <tr>
                    <th>Plan</th>
                    <th>Midjourney</th>
                    <th>DALL-E 3</th>
                    <th>Stable Diffusion</th>
                    <th>Leonardo AI</th>
                    <th>Ideogram</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Free</strong></td>
                    <td>None</td>
                    <td>Limited via ChatGPT</td>
                    <td>Unlimited (local)</td>
                    <td>150 tokens/day</td>
                    <td>25 images/day</td>
                </tr>
                <tr>
                    <td><strong>Basic</strong></td>
                    <td>$10/mo (200 images)</td>
                    <td>$20/mo (ChatGPT Plus)</td>
                    <td>Free (or cloud $10/mo)</td>
                    <td>$12/mo (8,500 tokens)</td>
                    <td>$7/mo (400 images)</td>
                </tr>
                <tr>
                    <td><strong>Standard</strong></td>
                    <td>$30/mo (unlimited relax, 15h fast)</td>
                    <td>N/A</td>
                    <td>Various cloud: $25-50/mo</td>
                    <td>$24/mo (25K tokens)</td>
                    <td>$16/mo (1,000 images)</td>
                </tr>
                <tr>
                    <td><strong>Pro</strong></td>
                    <td>$60/mo (unlimited relax, 30h fast)</td>
                    <td>N/A</td>
                    <td>Dedicated GPU: $100+/mo</td>
                    <td>$48/mo (60K tokens)</td>
                    <td>$20/mo (3,000 images)</td>
                </tr>
            </tbody>
        </table>

        <div class="callout callout-success">
            <h4>Best Value by Use Case</h4>
            <ul>
                <li><strong>Hobbyist/Learning</strong>: Ideogram Free (25/day) or Leonardo Free (150 tokens)</li>
                <li><strong>Content Creator</strong>: Midjourney Standard ($30/mo, unlimited relax)</li>
                <li><strong>Professional Artist</strong>: Midjourney Pro ($60/mo) or Stable Diffusion (one-time GPU cost)</li>
                <li><strong>ChatGPT User</strong>: DALL-E 3 ($20/mo, bundled with ChatGPT Plus)</li>
                <li><strong>Game Developer</strong>: Leonardo AI ($24-48/mo for consistency)</li>
            </ul>
        </div>
    ''',

    'detailed-reviews': '''
        <h3>Midjourney v6</h3>
        <h4>Strengths</h4>
        <ul>
            <li>✅ <strong>Best Image Quality</strong>: Most photorealistic and artistic results</li>
            <li>✅ <strong>Artistic Consistency</strong>: Distinctive "Midjourney aesthetic"</li>
            <li>✅ <strong>Advanced Features</strong>: --style, --chaos, --weird parameters</li>
            <li>✅ <strong>Active Community</strong>: Discord with millions of users sharing prompts</li>
            <li>✅ <strong>Regular Updates</strong>: v6 released Dec 2023, continuous improvements</li>
            <li>✅ <strong>Commercial Rights</strong>: Full ownership on paid plans</li>
        </ul>

        <h4>Weaknesses</h4>
        <ul>
            <li>❌ <strong>Discord-Only</strong>: No web UI yet (in beta), Discord can be overwhelming</li>
            <li>❌ <strong>No Free Tier</strong>: $10/mo minimum</li>
            <li>❌ <strong>Learning Curve</strong>: Complex parameter system</li>
            <li>❌ <strong>Slow Generation</strong>: ~60 seconds per batch</li>
            <li>❌ <strong>Limited Text</strong>: Still struggles with text in images</li>
        </ul>

        <h4>Best For</h4>
        <ul>
            <li>Professional artists and designers</li>
            <li>Marketing and advertising creatives</li>
            <li>Concept art and illustration</li>
            <li>Photography-style images</li>
            <li>Users who value quality over speed</li>
        </ul>

        <h4>Sample Prompts</h4>
        <pre><code>a serene japanese zen garden at sunset, cherry blossoms, stone lanterns, koi pond, photorealistic, 8k, cinematic lighting --ar 16:9 --v 6

cyberpunk street scene, neon lights, rain-soaked pavement, flying cars, blade runner aesthetic, hyper-detailed --style raw --chaos 20
        </code></pre>

        <hr>

        <h3>DALL-E 3 (OpenAI)</h3>
        <h4>Strengths</h4>
        <ul>
            <li>✅ <strong>Best Prompt Understanding</strong>: GPT-4 interprets and enhances your prompts</li>
            <li>✅ <strong>Easiest to Use</strong>: Natural language, no complex parameters</li>
            <li>✅ <strong>ChatGPT Integration</strong>: Generate images while chatting</li>
            <li>✅ <strong>Improved Text Rendering</strong>: Better than v2, readable text in images</li>
            <li>✅ <strong>Ethical Safeguards</strong>: Strong content policy, reduced bias</li>
            <li>✅ <strong>Edit Mode</strong>: Modify specific parts of images</li>
        </ul>

        <h4>Weaknesses</h4>
        <ul>
            <li>❌ <strong>Aggressive Filtering</strong>: Rejects many creative prompts</li>
            <li>❌ <strong>Limited Customization</strong>: Few parameters (no aspect ratio control)</li>
            <li>❌ <strong>No Batch Generation</strong>: 1 image per prompt</li>
            <li>❌ <strong>Resolution Limits</strong>: Max 1792x1024</li>
            <li>❌ <strong>Style Consistency</strong>: Hard to maintain style across images</li>
        </ul>

        <h4>Best For</h4>
        <ul>
            <li>ChatGPT users who want integrated image generation</li>
            <li>Beginners with no AI art experience</li>
            <li>Content creators needing quick illustrations</li>
            <li>Users who want text in images (logos, posters)</li>
            <li>Educational and safe-for-work content</li>
        </ul>

        <h4>Sample Prompts</h4>
        <pre><code>Create a vintage travel poster for Mars colonization, 1950s retro-futuristic style, with bold text "MARS AWAITS" at the top

A cozy coffee shop interior on a rainy day, warm lighting, customers reading books, steaming cups, plants on windowsill, watercolor painting style
        </code></pre>

        <hr>

        <h3>Stable Diffusion XL</h3>
        <h4>Strengths</h4>
        <ul>
            <li>✅ <strong>Open Source</strong>: Free, unlimited generations</li>
            <li>✅ <strong>Full Control</strong>: 100+ parameters, LoRA, ControlNet, etc.</li>
            <li>✅ <strong>Community Models</strong>: 1000s of custom models on Civitai</li>
            <li>✅ <strong>Local or Cloud</strong>: Run on your GPU or use cloud services</li>
            <li>✅ <strong>Consistent Characters</strong>: Use LoRA for character training</li>
            <li>✅ <strong>Advanced Techniques</strong>: Img2img, inpainting, outpainting, upscaling</li>
            <li>✅ <strong>API Ecosystem</strong>: Replicate, RunPod, HuggingFace, etc.</li>
        </ul>

        <h4>Weaknesses</h4>
        <ul>
            <li>❌ <strong>Technical Setup</strong>: Requires GPU, Python, dependencies</li>
            <li>❌ <strong>Steep Learning Curve</strong>: Overwhelming for beginners</li>
            <li>❌ <strong>Quality Variance</strong>: Depends heavily on model and prompt</li>
            <li>❌ <strong>No Built-in Safety</strong>: Can generate NSFW content (requires self-moderation)</li>
            <li>❌ <strong>Hardware Requirements</strong>: Need 8GB+ VRAM for local generation</li>
        </ul>

        <h4>Best For</h4>
        <ul>
            <li>Tech-savvy users comfortable with command line</li>
            <li>Users who need unlimited generations</li>
            <li>Developers building AI art applications</li>
            <li>Artists wanting full creative control</li>
            <li>NSFW content creators (responsibly)</li>
        </ul>

        <h4>Popular Models & Use Cases</h4>
        <ul>
            <li><strong>SDXL Base</strong>: General purpose, photorealism</li>
            <li><strong>Dreamshaper XL</strong>: Vibrant colors, fantasy art</li>
            <li><strong>Realistic Vision XL</strong>: Photorealistic portraits</li>
            <li><strong>Anime XL</strong>: Anime and manga style</li>
            <li><strong>JuggernautXL</strong>: Versatile, high quality</li>
        </ul>

        <hr>

        <h3>Leonardo AI</h3>
        <h4>Strengths</h4>
        <ul>
            <li>✅ <strong>Best for Game Assets</strong>: Texture generation, sprites, environments</li>
            <li>✅ <strong>Character Consistency</strong>: Character reference feature for consistent designs</li>
            <li>✅ <strong>Canvas Editor</strong>: Advanced editing with inpainting and masking</li>
            <li>✅ <strong>Multiple Models</strong>: Leonardo Diffusion, Anime, PhotoReal, etc.</li>
            <li>✅ <strong>Fast Generation</strong>: ~15 seconds</li>
            <li>✅ <strong>Generous Free Tier</strong>: 150 tokens/day</li>
            <li>✅ <strong>Motion</strong>: Animate images with AI</li>
        </ul>

        <h4>Weaknesses</h4>
        <ul>
            <li>❌ <strong>Token System</strong>: Complex pricing (not per image)</li>
            <li>❌ <strong>Limited Prompt Understanding</strong>: Not as smart as GPT-4</li>
            <li>❌ <strong>Web UI Only</strong>: No desktop app</li>
            <li>❌ <strong>Smaller Community</strong>: Fewer shared prompts than Midjourney</li>
        </ul>

        <h4>Best For</h4>
        <ul>
            <li>Game developers (characters, environments, UI)</li>
            <li>Indie game studios on a budget</li>
            <li>Comic and manga artists (consistent characters)</li>
            <li>Users who need specific art styles (anime, realistic, etc.)</li>
            <li>Animation and motion graphics</li>
        </ul>

        <hr>

        <h3>Ideogram 2.0</h3>
        <h4>Strengths</h4>
        <ul>
            <li>✅ <strong>Perfect Text Rendering</strong>: Best text-in-images of any AI tool</li>
            <li>✅ <strong>Clean Aesthetic</strong>: Polished, professional-looking results</li>
            <li>✅ <strong>Magic Prompt</strong>: AI enhances your prompt automatically</li>
            <li>✅ <strong>Generous Free Tier</strong>: 25 images/day</li>
            <li>✅ <strong>Fast</strong>: ~15 seconds</li>
            <li>✅ <strong>Magic Edit</strong>: Select and change parts of image</li>
        </ul>

        <h4>Weaknesses</h4>
        <ul>
            <li>❌ <strong>Limited Artistic Range</strong>: Less versatile than Midjourney</li>
            <li>❌ <strong>Newer Platform</strong>: Smaller community</li>
            <li>❌ <strong>Fewer Features</strong>: No advanced parameters</li>
        </ul>

        <h4>Best For</h4>
        <ul>
            <li>Posters and flyers with text</li>
            <li>Logos and branding</li>
            <li>Social media graphics</li>
            <li>Memes and typography art</li>
            <li>Users who need readable text in images</li>
        </ul>

        <div class="callout callout-info">
            <h4>Pro Tip: Combine Tools</h4>
            <p>Many professionals use multiple tools:</p>
            <ul>
                <li><strong>Concept</strong>: Midjourney for initial ideas</li>
                <li><strong>Refinement</strong>: Stable Diffusion with img2img</li>
                <li><strong>Text overlay</strong>: Ideogram for adding text</li>
                <li><strong>Quick iterations</strong>: DALL-E 3 in ChatGPT</li>
            </ul>
        </div>
    ''',

    'verdict': '''
        <h3>Which AI Image Generator Should You Choose?</h3>

        <div class="callout callout-success">
            <h4>🏆 Overall Winner: Midjourney v6</h4>
            <p>For pure image quality and artistic results, Midjourney is unmatched. If you're serious about AI art and can afford $30-60/mo, it's the best choice. The Discord interface is quirky but the results speak for themselves.</p>
        </div>

        <div class="callout callout-info">
            <h4>💡 Best for Beginners: DALL-E 3 (ChatGPT Plus)</h4>
            <p>If you're already using ChatGPT, DALL-E 3 is a no-brainer at $20/mo. It's the easiest to use—just describe what you want in natural language. Perfect for casual users who don't need advanced features.</p>
        </div>

        <div class="callout callout-info">
            <h4>💰 Best Value: Stable Diffusion XL</h4>
            <p>For unlimited free generations, Stable Diffusion can't be beat. Yes, it's technical to set up, but once running, you have complete control and zero usage limits. Cloud options like RunPod start at $10/mo.</p>
        </div>

        <div class="callout callout-info">
            <h4>🎮 Best for Consistency: Leonardo AI</h4>
            <p>Game developers and artists needing consistent characters across images should use Leonardo AI. The character reference feature is killer, and the free tier (150 tokens/day) is generous enough for daily use.</p>
        </div>

        <div class="callout callout-info">
            <h4>📝 Best for Text: Ideogram 2.0</h4>
            <p>If you need text in your images (posters, logos, memes), Ideogram is the only choice. It renders text perfectly while others fail. The free tier (25 images/day) covers most casual users.</p>
        </div>

        <h3>Decision Tree: Which Tool for Your Needs?</h3>

        <table>
            <thead>
                <tr>
                    <th>Your Need</th>
                    <th>Recommended Tool</th>
                    <th>Alternative</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Professional marketing/advertising</td>
                    <td>Midjourney Pro ($60/mo)</td>
                    <td>Leonardo AI ($24/mo)</td>
                </tr>
                <tr>
                    <td>Casual/personal use</td>
                    <td>Ideogram Free (25/day)</td>
                    <td>Leonardo Free (150 tokens)</td>
                </tr>
                <tr>
                    <td>Unlimited generations</td>
                    <td>Stable Diffusion (local)</td>
                    <td>Midjourney Standard ($30 unlimited relax)</td>
                </tr>
                <tr>
                    <td>Text in images (logos, posters)</td>
                    <td>Ideogram 2.0</td>
                    <td>DALL-E 3</td>
                </tr>
                <tr>
                    <td>Game asset creation</td>
                    <td>Leonardo AI</td>
                    <td>Stable Diffusion + LoRA</td>
                </tr>
                <tr>
                    <td>Photorealistic portraits</td>
                    <td>Midjourney v6</td>
                    <td>SD XL (Realistic Vision)</td>
                </tr>
                <tr>
                    <td>Anime/manga style</td>
                    <td>Leonardo AI (Anime model)</td>
                    <td>SD XL (Anime models)</td>
                </tr>
                <tr>
                    <td>Quick iterations/brainstorming</td>
                    <td>DALL-E 3 (ChatGPT)</td>
                    <td>Ideogram</td>
                </tr>
                <tr>
                    <td>API integration</td>
                    <td>Stable Diffusion (Replicate)</td>
                    <td>DALL-E 3 API</td>
                </tr>
                <tr>
                    <td>Learning AI art</td>
                    <td>Stable Diffusion (free)</td>
                    <td>Ideogram Free</td>
                </tr>
            </tbody>
        </table>

        <h3>Can You Use Multiple Tools?</h3>
        <p>Many professionals use 2-3 tools depending on the project:</p>
        <ul>
            <li><strong>Hobbyist Combo</strong>: Ideogram Free + Leonardo Free ($0/mo)</li>
            <li><strong>Creator Combo</strong>: DALL-E 3 + Ideogram Pro ($20 + $7 = $27/mo)</li>
            <li><strong>Professional Combo</strong>: Midjourney Standard + Stable Diffusion ($30 + local = $30/mo)</li>
            <li><strong>Studio Combo</strong>: Midjourney Pro + Leonardo Pro + SD ($60 + $48 + local = $108/mo)</li>
        </ul>

        <h3>Final Recommendations by Budget</h3>

        <h4>$0/month (Free)</h4>
        <ul>
            <li><strong>Primary</strong>: Ideogram (25 images/day)</li>
            <li><strong>Secondary</strong>: Leonardo AI (150 tokens/day)</li>
            <li><strong>Learning</strong>: Stable Diffusion (unlimited, but requires setup)</li>
        </ul>

        <h4>$10-20/month</h4>
        <ul>
            <li><strong>Best Value</strong>: DALL-E 3 via ChatGPT Plus ($20/mo) - also get GPT-4</li>
            <li><strong>Alternative</strong>: Ideogram Basic ($7/mo) + Leonardo Apprentice ($12/mo) = $19/mo</li>
            <li><strong>Cloud SD</strong>: RunPod or Replicate ($10-15/mo for ~500-1000 images)</li>
        </ul>

        <h4>$30-50/month</h4>
        <ul>
            <li><strong>Best Quality</strong>: Midjourney Standard ($30/mo)</li>
            <li><strong>Most Versatile</strong>: ChatGPT Plus + Leonardo Artisan ($20 + $24 = $44/mo)</li>
            <li><strong>Game Dev</strong>: Leonardo Maestro ($48/mo)</li>
        </ul>

        <h4>$60+/month (Professional)</h4>
        <ul>
            <li><strong>Premium</strong>: Midjourney Pro ($60/mo)</li>
            <li><strong>Ultimate Combo</strong>: Midjourney Pro + ChatGPT Plus + Ideogram ($60 + $20 + $16 = $96/mo)</li>
            <li><strong>Studio Setup</strong>: All tools + dedicated SD GPU ($150-300/mo)</li>
        </ul>

        <div class="callout callout-warning">
            <h4>Keep in Mind</h4>
            <ul>
                <li><strong>Quality vs. Speed</strong>: Midjourney is slow but beautiful. DALL-E is fast but less control.</li>
                <li><strong>Learning Curve</strong>: Stable Diffusion rewards patience. DALL-E requires no learning.</li>
                <li><strong>Commercial Use</strong>: Check each tool's terms. Most allow commercial use on paid plans.</li>
                <li><strong>Updates</strong>: This comparison is accurate as of January 2025. AI tools update frequently!</li>
            </ul>
        </div>

        <h3>What's Coming in 2025?</h3>
        <ul>
            <li><strong>Midjourney v7</strong>: Expected Q2 2025, rumored web UI and 3D generation</li>
            <li><strong>DALL-E 4</strong>: Higher resolution, better consistency</li>
            <li><strong>Stable Diffusion 3</strong>: Already in beta, major quality improvements</li>
            <li><strong>Video Generation</strong>: All tools adding text-to-video (Runway, Pika leading)</li>
            <li><strong>Real-Time Generation</strong>: Sub-second image generation</li>
        </ul>
    '''
}

print("Contenu pour Image Generators créé!")
print(f"- Comparison Table: {len(IMAGE_GENERATORS_CONTENT['comparison-table'])} caractères")
print(f"- Detailed Reviews: {len(IMAGE_GENERATORS_CONTENT['detailed-reviews'])} caractères")
print(f"- Verdict: {len(IMAGE_GENERATORS_CONTENT['verdict'])} caractères")
print(f"Total: {sum(len(v) for v in IMAGE_GENERATORS_CONTENT.values())} caractères")
