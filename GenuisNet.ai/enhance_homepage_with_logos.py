#!/usr/bin/env python3
"""
Enhance homepage with more AI logos and captivating artifacts
"""

import re
from pathlib import Path

BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")

def enhance_homepage():
    """Add logo showcase and visual artifacts"""

    print("="*70)
    print("ENHANCING HOMEPAGE WITH LOGOS & ARTIFACTS")
    print("="*70)

    index_file = BASE_DIR / "index.html"
    content = index_file.read_text(encoding='utf-8')

    # Backup
    backup_file = BASE_DIR / "index.html.backup3"
    backup_file.write_text(content, encoding='utf-8')
    print(f"\n✓ Backup created: index.html.backup3")

    # Find where to insert new sections (after value-section)
    insert_after = '</section>\n\n    <!-- Tool Spotlight -->'

    new_sections = '''</section>

    <!-- AI Logos Showcase -->
    <section class="section logos-showcase-section">
        <div class="container">
            <div class="section-header">
                <div class="showcase-badge">Featured AI Tools</div>
                <h2 class="section-title">The AI Revolution Starts Here</h2>
                <p class="section-subtitle">Discover the most powerful AI tools transforming industries worldwide</p>
            </div>

            <div class="logos-showcase-grid">
                <!-- Row 1 - Chatbots -->
                <div class="logo-showcase-item" data-category="Chatbot">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/chatbots/chatgpt.svg" alt="ChatGPT">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">ChatGPT</span>
                </div>

                <div class="logo-showcase-item" data-category="Chatbot">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/chatbots/claude.svg" alt="Claude">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">Claude</span>
                </div>

                <div class="logo-showcase-item" data-category="Chatbot">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/chatbots/gemini.svg" alt="Gemini">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">Gemini</span>
                </div>

                <div class="logo-showcase-item" data-category="Chatbot">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/chatbots/copilot.svg" alt="Copilot">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">Copilot</span>
                </div>

                <!-- Row 2 - Image & Coding -->
                <div class="logo-showcase-item" data-category="Image">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/image/midjourney.svg" alt="Midjourney">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">Midjourney</span>
                </div>

                <div class="logo-showcase-item" data-category="Image">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/image/dall-e-3.png" alt="DALL-E 3">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">DALL-E 3</span>
                </div>

                <div class="logo-showcase-item" data-category="Coding">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/coding/cursor.svg" alt="Cursor">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">Cursor</span>
                </div>

                <div class="logo-showcase-item" data-category="Coding">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/coding/github-copilot.png" alt="GitHub Copilot">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">GitHub Copilot</span>
                </div>

                <!-- Row 3 - Video & Writing -->
                <div class="logo-showcase-item" data-category="Video">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/video/runway.svg" alt="Runway">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">Runway</span>
                </div>

                <div class="logo-showcase-item" data-category="Video">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/video/synthesia.svg" alt="Synthesia">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">Synthesia</span>
                </div>

                <div class="logo-showcase-item" data-category="Writing">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/writing/grammarly.svg" alt="Grammarly">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">Grammarly</span>
                </div>

                <div class="logo-showcase-item" data-category="Writing">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/writing/jasper-ai.svg" alt="Jasper AI">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">Jasper AI</span>
                </div>

                <!-- Row 4 - Productivity & More -->
                <div class="logo-showcase-item" data-category="Productivity">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/productivity/notion-ai.png" alt="Notion AI">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">Notion AI</span>
                </div>

                <div class="logo-showcase-item" data-category="Audio">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/audio/elevenlabs.svg" alt="ElevenLabs">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">ElevenLabs</span>
                </div>

                <div class="logo-showcase-item" data-category="Image">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/image/stable-diffusion.svg" alt="Stable Diffusion">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">Stable Diffusion</span>
                </div>

                <div class="logo-showcase-item" data-category="Chatbot">
                    <div class="logo-showcase-wrapper">
                        <img src="assets/images/tools/chatbots/perplexity.png" alt="Perplexity">
                        <div class="logo-shine"></div>
                    </div>
                    <span class="logo-name">Perplexity</span>
                </div>
            </div>

            <div class="logos-cta">
                <p class="logos-cta-text">And 100+ more cutting-edge AI tools...</p>
                <a href="pages/categories/ai-chatbots.html" class="btn btn-outline">
                    Explore All Tools
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </a>
            </div>
        </div>
    </section>

    <!-- Live Stats Dashboard -->
    <section class="section live-stats-section">
        <div class="container">
            <div class="stats-dashboard">
                <div class="stat-dashboard-item">
                    <div class="stat-icon-lg">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                            <path d="M2 17l10 5 10-5"/>
                            <path d="M2 12l10 5 10-5"/>
                        </svg>
                    </div>
                    <div class="stat-content">
                        <div class="stat-number-lg counter" data-count="116">0</div>
                        <div class="stat-label-lg">AI Tools Reviewed</div>
                        <div class="stat-sublabel">Across 13 categories</div>
                    </div>
                    <div class="stat-pulse"></div>
                </div>

                <div class="stat-dashboard-item">
                    <div class="stat-icon-lg">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                            <circle cx="9" cy="7" r="4"/>
                            <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                            <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
                        </svg>
                    </div>
                    <div class="stat-content">
                        <div class="stat-number-lg counter" data-count="50000">0</div>
                        <div class="stat-label-lg">Community Members</div>
                        <div class="stat-sublabel">And growing daily</div>
                    </div>
                    <div class="stat-pulse"></div>
                </div>

                <div class="stat-dashboard-item">
                    <div class="stat-icon-lg">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
                        </svg>
                    </div>
                    <div class="stat-content">
                        <div class="stat-number-lg">24/7</div>
                        <div class="stat-label-lg">Updated Content</div>
                        <div class="stat-sublabel">Fresh reviews daily</div>
                    </div>
                    <div class="stat-pulse"></div>
                </div>
            </div>
        </div>
    </section>

    <!-- Tool Spotlight -->'''

    content = content.replace(insert_after, new_sections)

    print("✓ Added logos showcase (16 AI tools)")
    print("✓ Added live stats dashboard")

    # Save
    index_file.write_text(content, encoding='utf-8')

    print("\n✅ Homepage enhanced!")
    print("\n" + "="*70)
    print("NOUVELLES SECTIONS AJOUTÉES:")
    print("="*70)
    print("✓ Logos Showcase - 16 AI tools majeurs avec effets shine")
    print("✓ Live Stats Dashboard - 3 statistiques animées")
    print("\n🌐 Test: http://localhost:8000")
    print("="*70)

    return True

if __name__ == "__main__":
    enhance_homepage()
