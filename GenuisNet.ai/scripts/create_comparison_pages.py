#!/usr/bin/env python3
"""
Génère des pages de comparaison détaillées pour les catégories d'outils IA
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
COMPARE_DIR = BASE_DIR / "pages" / "compare"
COMPARE_DIR.mkdir(exist_ok=True)

# Template HTML pour les comparaisons
COMPARE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | GenuisNet.ai</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">

    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/guides-reviews.css">
    <link rel="stylesheet" href="../css/animations.css">
    <link rel="stylesheet" href="../css/neon-icons.css">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container nav-container">
            <a href="../index.html" class="logo">
                <img src="../assets/images/logo-neon.svg" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">
            </a>
            <ul class="nav-menu">
                <li><a href="../index.html" class="nav-link">Home</a></li>
                <li><a href="../pages/guides.html" class="nav-link">Guides</a></li>
                <li><a href="../pages/about.html" class="nav-link">About</a></li>
            </ul>
        </div>
    </nav>

    <!-- Comparison Hero -->
    <section class="guide-hero">
        <div class="container">
            <div class="breadcrumb">
                <a href="../index.html">Home</a>
                <span>/</span>
                <a href="../pages/compare.html">Compare</a>
                <span>/</span>
                <span>{category_name}</span>
            </div>

            <div class="guide-hero-content">
                <div class="guide-badge">Comparison</div>
                <h1>{title}</h1>
                <p class="guide-subtitle">{subtitle}</p>

                <div class="guide-meta">
                    <div class="meta-item">
                        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                            <circle cx="12" cy="12" r="10"/>
                            <polyline points="12 6 12 12 16 14"/>
                        </svg>
                        <span>{read_time}</span>
                    </div>
                    <div class="meta-item">
                        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                            <path d="M9 11l3 3L22 4"/>
                            <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
                        </svg>
                        <span>{tools_count} Tools Compared</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Comparison Content -->
    <div class="container guide-container">
        <div class="guide-sidebar">
            <div class="toc-card">
                <h3>Quick Navigation</h3>
                <nav class="toc">
                    <a href="#overview" class="toc-link">Overview</a>
                    <a href="#comparison-table" class="toc-link">Comparison Table</a>
                    <a href="#detailed-reviews" class="toc-link">Detailed Reviews</a>
                    <a href="#verdict" class="toc-link">Final Verdict</a>
                </nav>
            </div>

            <div class="guide-tools-card">
                <h4>Tools in This Comparison</h4>
                {tools_list}
            </div>
        </div>

        <article class="guide-content">
            {content}

            <!-- Related Comparisons -->
            <section class="related-guides">
                <h2>Related Comparisons</h2>
                <div class="guides-grid">
                    {related_comparisons}
                </div>
            </section>
        </article>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 GenuisNet.ai. All rights reserved.</p>
        </div>
    </footer>

    <script src="../js/i18n.js"></script>
    <script src="../js/main.js"></script>
</body>
</html>'''

# Comparaisons détaillées
COMPARISONS = {
    'chatbots': {
        'title': 'ChatGPT vs Claude vs Gemini vs Grok: Complete AI Chatbot Comparison 2025',
        'subtitle': 'Which AI chatbot is right for you? In-depth comparison of features, pricing, and capabilities',
        'description': 'Comprehensive comparison of ChatGPT, Claude, Google Gemini, and Grok. Compare features, pricing, capabilities, and use cases to choose the best AI chatbot.',
        'keywords': 'ChatGPT vs Claude, AI chatbot comparison, Gemini vs ChatGPT, best AI assistant 2025',
        'category_name': 'AI Chatbots',
        'read_time': '15 min read',
        'tools': [
            {'name': 'ChatGPT', 'icon': '🤖'},
            {'name': 'Claude', 'icon': '🧠'},
            {'name': 'Google Gemini', 'icon': '✨'},
            {'name': 'Grok', 'icon': '🚀'},
            {'name': 'Perplexity', 'icon': '🔍'}
        ],
        'sections': [
            {
                'id': 'overview',
                'title': 'Overview: The AI Chatbot Landscape 2025',
                'content': '''
                    <p>The AI chatbot market has exploded in 2023-2025 with major players competing for dominance. Here's what you need to know about each platform:</p>

                    <div class="callout callout-info">
                        <h4>Market Leaders (January 2025)</h4>
                        <ul>
                            <li><strong>ChatGPT</strong>: 180M+ users, market leader, GPT-4 Turbo/4o</li>
                            <li><strong>Claude</strong>: 10M+ users, best for long documents, Claude 3.5 Sonnet</li>
                            <li><strong>Gemini</strong>: Integrated with Google Workspace, Gemini 1.5 Pro</li>
                            <li><strong>Grok</strong>: X.ai's chatbot, real-time X data, Grok-2</li>
                            <li><strong>Perplexity</strong>: Research-focused, real-time web search</li>
                        </ul>
                    </div>

                    <h3>Quick Verdict (TL;DR)</h3>
                    <ul>
                        <li><strong>Best Overall</strong>: ChatGPT (GPT-4o) - Most versatile, best ecosystem</li>
                        <li><strong>Best for Writing</strong>: Claude 3.5 Sonnet - Superior long-form content</li>
                        <li><strong>Best for Research</strong>: Perplexity - Citations and sources</li>
                        <li><strong>Best Free Tier</strong>: ChatGPT (GPT-4o mini) - Generous free access</li>
                        <li><strong>Best for Google Users</strong>: Gemini - Workspace integration</li>
                    </ul>
                '''
            },
            {
                'id': 'comparison-table',
                'title': 'Feature-by-Feature Comparison',
                'content': '''
                    <h3>Core Features Comparison</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Feature</th>
                                <th>ChatGPT</th>
                                <th>Claude</th>
                                <th>Gemini</th>
                                <th>Grok</th>
                                <th>Perplexity</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Model</strong></td>
                                <td>GPT-4o, GPT-4 Turbo</td>
                                <td>Claude 3.5 Sonnet</td>
                                <td>Gemini 1.5 Pro</td>
                                <td>Grok-2</td>
                                <td>GPT-4 + others</td>
                            </tr>
                            <tr>
                                <td><strong>Context Window</strong></td>
                                <td>128K tokens</td>
                                <td>200K tokens</td>
                                <td>1M tokens</td>
                                <td>32K tokens</td>
                                <td>Varies by model</td>
                            </tr>
                            <tr>
                                <td><strong>Free Tier</strong></td>
                                <td>✅ GPT-4o mini</td>
                                <td>✅ Limited</td>
                                <td>✅ Gemini 1.5 Flash</td>
                                <td>❌ X Premium only</td>
                                <td>✅ 5 searches/day</td>
                            </tr>
                            <tr>
                                <td><strong>Paid Tier Price</strong></td>
                                <td>$20/mo (Plus)</td>
                                <td>$20/mo (Pro)</td>
                                <td>$20/mo (Advanced)</td>
                                <td>$16/mo (X Premium+)</td>
                                <td>$20/mo (Pro)</td>
                            </tr>
                            <tr>
                                <td><strong>Image Generation</strong></td>
                                <td>✅ DALL-E 3</td>
                                <td>❌</td>
                                <td>✅ Imagen 3</td>
                                <td>✅ Flux</td>
                                <td>❌</td>
                            </tr>
                            <tr>
                                <td><strong>Image Upload</strong></td>
                                <td>✅ Vision</td>
                                <td>✅ Vision</td>
                                <td>✅ Vision</td>
                                <td>✅ Vision</td>
                                <td>✅</td>
                            </tr>
                            <tr>
                                <td><strong>File Upload</strong></td>
                                <td>✅ PDF, DOCX, etc.</td>
                                <td>✅ PDF, text, code</td>
                                <td>✅ Google Drive</td>
                                <td>✅ Limited</td>
                                <td>✅ PDF</td>
                            </tr>
                            <tr>
                                <td><strong>Web Search</strong></td>
                                <td>✅ Browse with Bing</td>
                                <td>❌</td>
                                <td>✅ Real-time Google</td>
                                <td>✅ Real-time X</td>
                                <td>✅ Multiple sources</td>
                            </tr>
                            <tr>
                                <td><strong>Code Execution</strong></td>
                                <td>✅ Advanced Data Analysis</td>
                                <td>✅ Artifacts</td>
                                <td>✅ Code execution</td>
                                <td>❌</td>
                                <td>❌</td>
                            </tr>
                            <tr>
                                <td><strong>API Access</strong></td>
                                <td>✅ $0.01-0.10/1K tokens</td>
                                <td>✅ $3-15/1M tokens</td>
                                <td>✅ Free tier available</td>
                                <td>✅ Enterprise only</td>
                                <td>✅ $20/1K queries</td>
                            </tr>
                            <tr>
                                <td><strong>Mobile App</strong></td>
                                <td>✅ iOS, Android</td>
                                <td>✅ iOS, Android</td>
                                <td>✅ iOS, Android</td>
                                <td>✅ In X app</td>
                                <td>✅ iOS, Android</td>
                            </tr>
                            <tr>
                                <td><strong>Voice Input</strong></td>
                                <td>✅ Voice mode</td>
                                <td>❌</td>
                                <td>✅ Voice typing</td>
                                <td>❌</td>
                                <td>✅</td>
                            </tr>
                        </tbody>
                    </table>

                    <h3>Pricing Comparison (January 2025)</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Plan</th>
                                <th>ChatGPT</th>
                                <th>Claude</th>
                                <th>Gemini</th>
                                <th>Grok</th>
                                <th>Perplexity</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Free</strong></td>
                                <td>GPT-4o mini unlimited</td>
                                <td>Limited messages</td>
                                <td>Gemini 1.5 Flash</td>
                                <td>Not available</td>
                                <td>5 searches/day</td>
                            </tr>
                            <tr>
                                <td><strong>Individual</strong></td>
                                <td>$20/mo (Plus)</td>
                                <td>$20/mo (Pro)</td>
                                <td>$20/mo (Advanced)</td>
                                <td>$16/mo (X Premium+)</td>
                                <td>$20/mo (Pro)</td>
                            </tr>
                            <tr>
                                <td><strong>Team</strong></td>
                                <td>$25-30/user/mo</td>
                                <td>$25/user/mo (Team)</td>
                                <td>Included in Workspace</td>
                                <td>N/A</td>
                                <td>$20/user/mo</td>
                            </tr>
                            <tr>
                                <td><strong>Enterprise</strong></td>
                                <td>Custom pricing</td>
                                <td>Custom pricing</td>
                                <td>Custom pricing</td>
                                <td>Custom pricing</td>
                                <td>Custom pricing</td>
                            </tr>
                        </tbody>
                    </table>

                    <div class="callout callout-success">
                        <h4>Best Value</h4>
                        <p>For most users, <strong>ChatGPT Plus ($20/mo)</strong> offers the best balance of features, performance, and ecosystem. The free tier is also the most generous.</p>
                    </div>
                '''
            },
            {
                'id': 'detailed-reviews',
                'title': 'Detailed Tool Reviews',
                'content': '''
                    <h3>ChatGPT (OpenAI)</h3>
                    <h4>Strengths</h4>
                    <ul>
                        <li>✅ <strong>Market Leader</strong>: Largest user base, most integrations</li>
                        <li>✅ <strong>GPT Store</strong>: 3M+ custom GPTs for specialized tasks</li>
                        <li>✅ <strong>DALL-E 3</strong>: Best-in-class image generation</li>
                        <li>✅ <strong>Voice Mode</strong>: Natural conversation with GPT-4o</li>
                        <li>✅ <strong>Code Interpreter</strong>: Run Python, analyze data, create charts</li>
                        <li>✅ <strong>Plugins</strong>: Zapier, Wolfram, browsing, and more</li>
                    </ul>
                    <h4>Weaknesses</h4>
                    <ul>
                        <li>❌ Shorter context window than competitors (128K vs 1M)</li>
                        <li>❌ Can be verbose and repetitive</li>
                        <li>❌ Knowledge cutoff (Oct 2023 for GPT-4, need web search for current info)</li>
                    </ul>
                    <h4>Best For</h4>
                    <ul>
                        <li>General-purpose AI assistant</li>
                        <li>Creative writing and brainstorming</li>
                        <li>Code generation and debugging</li>
                        <li>Image generation (DALL-E 3)</li>
                        <li>Users wanting the largest ecosystem</li>
                    </ul>

                    <hr>

                    <h3>Claude (Anthropic)</h3>
                    <h4>Strengths</h4>
                    <ul>
                        <li>✅ <strong>Best for Long Content</strong>: 200K context window, reads entire books</li>
                        <li>✅ <strong>Superior Writing Quality</strong>: More natural, less robotic prose</li>
                        <li>✅ <strong>Code Analysis</strong>: Excellent at reading and explaining complex codebases</li>
                        <li>✅ <strong>Artifacts</strong>: Interactive code execution and visualization</li>
                        <li>✅ <strong>Honesty</strong>: More likely to admit uncertainty vs. hallucinate</li>
                        <li>✅ <strong>Safety</strong>: Constitutional AI reduces harmful outputs</li>
                    </ul>
                    <h4>Weaknesses</h4>
                    <ul>
                        <li>❌ No web search (knowledge cutoff Aug 2024)</li>
                        <li>❌ No image generation</li>
                        <li>❌ Smaller ecosystem than ChatGPT</li>
                        <li>❌ More expensive API pricing</li>
                    </ul>
                    <h4>Best For</h4>
                    <ul>
                        <li>Long-form writing (articles, essays, reports)</li>
                        <li>Document analysis (legal, research papers)</li>
                        <li>Code review and refactoring</li>
                        <li>Users who value writing quality over speed</li>
                        <li>Sensitive content requiring safety</li>
                    </ul>

                    <hr>

                    <h3>Google Gemini</h3>
                    <h4>Strengths</h4>
                    <ul>
                        <li>✅ <strong>Massive Context Window</strong>: 1M tokens (can process entire codebases)</li>
                        <li>✅ <strong>Google Integration</strong>: Workspace, Gmail, Drive, Calendar</li>
                        <li>✅ <strong>Real-Time Web Search</strong>: Google search built-in</li>
                        <li>✅ <strong>Multimodal</strong>: Native audio, video, image understanding</li>
                        <li>✅ <strong>Fast</strong>: Gemini 1.5 Flash is incredibly quick</li>
                    </ul>
                    <h4>Weaknesses</h4>
                    <ul>
                        <li>❌ Less capable than GPT-4o/Claude 3.5 Sonnet for complex reasoning</li>
                        <li>❌ Imagen 3 not as good as DALL-E 3 for images</li>
                        <li>❌ More restrictive safety filters</li>
                        <li>❌ Limited third-party integrations</li>
                    </ul>
                    <h4>Best For</h4>
                    <ul>
                        <li>Google Workspace users</li>
                        <li>Long document processing (1M tokens!)</li>
                        <li>Research requiring current web data</li>
                        <li>Users who value speed (Flash model)</li>
                        <li>Multimodal tasks (video + audio + images)</li>
                    </ul>

                    <hr>

                    <h3>Grok (X.ai)</h3>
                    <h4>Strengths</h4>
                    <ul>
                        <li>✅ <strong>Real-Time X Data</strong>: Access to all posts on X (Twitter)</li>
                        <li>✅ <strong>Less Censored</strong>: More willing to engage with controversial topics</li>
                        <li>✅ <strong>Fun Personality</strong>: Witty, sarcastic, entertaining responses</li>
                        <li>✅ <strong>Image Generation</strong>: Flux model, fewer restrictions than competitors</li>
                    </ul>
                    <h4>Weaknesses</h4>
                    <ul>
                        <li>❌ Requires X Premium+ ($16/mo minimum)</li>
                        <li>❌ Smaller context window (32K tokens)</li>
                        <li>❌ Less capable than GPT-4o/Claude/Gemini for complex tasks</li>
                        <li>❌ Limited availability and integrations</li>
                    </ul>
                    <h4>Best For</h4>
                    <ul>
                        <li>X (Twitter) power users</li>
                        <li>Real-time social media insights</li>
                        <li>Users who want uncensored AI</li>
                        <li>Fun, casual conversations</li>
                    </ul>

                    <hr>

                    <h3>Perplexity</h3>
                    <h4>Strengths</h4>
                    <ul>
                        <li>✅ <strong>Best for Research</strong>: Cites sources, shows references</li>
                        <li>✅ <strong>Real-Time Web Search</strong>: Always up-to-date information</li>
                        <li>✅ <strong>Focus Mode</strong>: Academic, writing, video, etc.</li>
                        <li>✅ <strong>Copilot</strong>: Asks clarifying questions before searching</li>
                        <li>✅ <strong>Collections</strong>: Organize research into projects</li>
                    </ul>
                    <h4>Weaknesses</h4>
                    <ul>
                        <li>❌ Not as versatile as ChatGPT/Claude</li>
                        <li>❌ No image generation</li>
                        <li>❌ Limited creative writing capabilities</li>
                        <li>❌ Free tier very restrictive (5 searches/day)</li>
                    </ul>
                    <h4>Best For</h4>
                    <ul>
                        <li>Research and fact-finding</li>
                        <li>Academic work requiring citations</li>
                        <li>Current events and news</li>
                        <li>Users who need transparent sources</li>
                    </ul>
                '''
            },
            {
                'id': 'verdict',
                'title': 'Final Verdict & Recommendations',
                'content': '''
                    <h3>Choose Based on Your Primary Use Case</h3>

                    <div class="callout callout-success">
                        <h4>🏆 Best Overall: ChatGPT Plus ($20/mo)</h4>
                        <p>For 90% of users, ChatGPT Plus is the best choice. It's the most versatile, has the largest ecosystem (GPT Store with 3M+ custom GPTs), and balances capability with ease of use. GPT-4o is excellent for code, writing, analysis, and image generation (DALL-E 3).</p>
                    </div>

                    <div class="callout callout-info">
                        <h4>✍️ Best for Writers: Claude Pro ($20/mo)</h4>
                        <p>If you're writing long-form content (articles, books, reports), Claude 3.5 Sonnet produces the most natural, well-structured prose. The 200K context window lets you upload entire manuscripts for editing.</p>
                    </div>

                    <div class="callout callout-info">
                        <h4>🔬 Best for Research: Perplexity Pro ($20/mo)</h4>
                        <p>For research, fact-checking, and current information, Perplexity is unmatched. It cites sources, provides references, and searches the web in real-time. The Copilot feature asks clarifying questions to improve results.</p>
                    </div>

                    <div class="callout callout-info">
                        <h4>📊 Best for Google Users: Gemini Advanced ($20/mo)</h4>
                        <p>If you live in Google Workspace (Gmail, Docs, Drive), Gemini Advanced's integration is seamless. The 1M token context window is perfect for processing entire codebases or long documents.</p>
                    </div>

                    <h3>Use Case Recommendations</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Use Case</th>
                                <th>Recommended Tool</th>
                                <th>Alternative</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>General productivity</td>
                                <td>ChatGPT Plus</td>
                                <td>Claude Pro</td>
                            </tr>
                            <tr>
                                <td>Long-form writing</td>
                                <td>Claude Pro</td>
                                <td>ChatGPT Plus</td>
                            </tr>
                            <tr>
                                <td>Code generation</td>
                                <td>ChatGPT Plus</td>
                                <td>Claude Pro</td>
                            </tr>
                            <tr>
                                <td>Research & citations</td>
                                <td>Perplexity Pro</td>
                                <td>Gemini Advanced</td>
                            </tr>
                            <tr>
                                <td>Image generation</td>
                                <td>ChatGPT Plus (DALL-E 3)</td>
                                <td>Grok (Flux)</td>
                            </tr>
                            <tr>
                                <td>Document analysis</td>
                                <td>Claude Pro (200K context)</td>
                                <td>Gemini (1M context)</td>
                            </tr>
                            <tr>
                                <td>Real-time info</td>
                                <td>Perplexity Pro</td>
                                <td>Gemini Advanced</td>
                            </tr>
                            <tr>
                                <td>Google Workspace</td>
                                <td>Gemini Advanced</td>
                                <td>ChatGPT Plus</td>
                            </tr>
                            <tr>
                                <td>Social media insights</td>
                                <td>Grok</td>
                                <td>Perplexity Pro</td>
                            </tr>
                        </tbody>
                    </table>

                    <h3>Can You Use Multiple?</h3>
                    <p>Many power users subscribe to 2-3 tools for different purposes:</p>
                    <ul>
                        <li><strong>ChatGPT + Claude</strong>: $40/mo - Best combo for general use + long writing</li>
                        <li><strong>ChatGPT + Perplexity</strong>: $40/mo - Productivity + research</li>
                        <li><strong>Claude + Gemini</strong>: $40/mo - Writing + Google integration</li>
                        <li><strong>All Three</strong>: $60/mo - Maximum flexibility (ChatGPT + Claude + Perplexity)</li>
                    </ul>

                    <h3>Free Tier Recommendation</h3>
                    <p>If you're not ready to pay, <strong>ChatGPT Free (GPT-4o mini)</strong> is the best free option. It's more capable than most paid tools from 2023 and has unlimited usage.</p>

                    <div class="callout callout-warning">
                        <h4>Update Frequency</h4>
                        <p>This comparison is accurate as of January 2025. AI models update frequently—check official websites for the latest features and pricing.</p>
                    </div>
                '''
            }
        ]
    },

    'image-generators': {
        'title': 'Midjourney vs DALL-E 3 vs Stable Diffusion: AI Image Generator Comparison 2025',
        'subtitle': 'Which AI image generator creates the best images? Compare features, pricing, and quality',
        'description': 'Detailed comparison of Midjourney, DALL-E 3, Stable Diffusion, and other AI image generators. Compare quality, pricing, features, and use cases.',
        'keywords': 'Midjourney vs DALL-E, AI image generator comparison, Stable Diffusion vs Midjourney, best AI art generator',
        'category_name': 'AI Image Generators',
        'read_time': '12 min read',
        'tools': [
            {'name': 'Midjourney', 'icon': '🎨'},
            {'name': 'DALL-E 3', 'icon': '🖼️'},
            {'name': 'Stable Diffusion', 'icon': '⚡'},
            {'name': 'Leonardo AI', 'icon': '🎭'},
            {'name': 'Ideogram', 'icon': '📝'}
        ],
        'sections': [
            {
                'id': 'overview',
                'title': 'AI Image Generator Landscape 2025',
                'content': '''
                    <p>AI image generation has matured dramatically. Here are the top platforms and their strengths:</p>

                    <div class="callout callout-info">
                        <h4>Market Leaders</h4>
                        <ul>
                            <li><strong>Midjourney v6</strong>: Best overall quality, artistic style</li>
                            <li><strong>DALL-E 3</strong>: Best prompt understanding, integrated in ChatGPT</li>
                            <li><strong>Stable Diffusion XL</strong>: Open-source, unlimited generations</li>
                            <li><strong>Leonardo AI</strong>: Game assets, consistent characters</li>
                            <li><strong>Ideogram 2.0</strong>: Best text rendering in images</li>
                        </ul>
                    </div>

                    <h3>Quick Verdict</h3>
                    <ul>
                        <li><strong>Best Quality</strong>: Midjourney v6 - Stunning, artistic images</li>
                        <li><strong>Easiest to Use</strong>: DALL-E 3 (ChatGPT) - Natural language prompts</li>
                        <li><strong>Best Value</strong>: Stable Diffusion - Free, unlimited, open-source</li>
                        <li><strong>Best for Text</strong>: Ideogram 2.0 - Perfect typography in images</li>
                        <li><strong>Best for Consistency</strong>: Leonardo AI - Character sheets, game art</li>
                    </ul>
                '''
            }
        ]
    }
}

def generate_comparison(category_slug, comparison_data):
    """Génère une page de comparaison HTML"""

    # Tools list
    tools_html = ""
    for tool in comparison_data['tools']:
        tools_html += f'''
    <div class="tool-item">
        <span class="tool-icon">{tool['icon']}</span>
        <span class="tool-name">{tool['name']}</span>
    </div>
    '''

    # Sections content
    content_html = ""
    for section in comparison_data['sections']:
        content_html += f'''
        <section id="{section['id']}" class="guide-section">
            <h2>{section['title']}</h2>
            {section['content']}
        </section>
        '''

    # Related comparisons (placeholder)
    related_html = '''
    <div class="guide-card">
        <h4>More Comparisons Coming Soon</h4>
        <p>Check back for more AI tool comparisons</p>
    </div>
    '''

    # Generate HTML
    html = COMPARE_TEMPLATE.format(
        title=comparison_data['title'],
        description=comparison_data['description'],
        keywords=comparison_data['keywords'],
        category_name=comparison_data['category_name'],
        subtitle=comparison_data['subtitle'],
        read_time=comparison_data['read_time'],
        tools_count=len(comparison_data['tools']),
        tools_list=tools_html,
        content=content_html,
        related_comparisons=related_html
    )

    return html

def main():
    """Génère toutes les pages de comparaison"""
    print("=" * 70)
    print("Generating AI Tool Comparison Pages")
    print("=" * 70)

    for category_slug, comparison_data in COMPARISONS.items():
        output_file = COMPARE_DIR / f"{category_slug}-comparison.html"

        print(f"\n📝 Generating {category_slug} comparison...")
        html = generate_comparison(category_slug, comparison_data)

        output_file.write_text(html, encoding='utf-8')
        size_kb = output_file.stat().st_size / 1024

        print(f"   ✅ Created: {output_file.name}")
        print(f"   📊 Size: {size_kb:.1f} KB")
        print(f"   🔧 Tools: {len(comparison_data['tools'])}")

    print("\n" + "=" * 70)
    print(f"✅ Successfully generated {len(COMPARISONS)} comparison pages!")
    print("=" * 70)

if __name__ == "__main__":
    main()
