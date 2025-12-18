#!/usr/bin/env python3
"""
Create a clean homepage with ONLY hero + minimal teasing sections
Remove all category previews from homepage
"""

import re
from pathlib import Path

BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")

def create_clean_homepage():
    """Create a clean homepage with minimal content"""

    print("="*70)
    print("CREATING CLEAN HOMEPAGE")
    print("="*70)

    index_file = BASE_DIR / "index.html"
    hero_file = BASE_DIR / "home_hero_enhanced.html"

    if not index_file.exists():
        print("✗ index.html not found!")
        return False

    # Read content
    index_content = index_file.read_text(encoding='utf-8')
    hero_content = hero_file.read_text(encoding='utf-8')

    # Backup
    backup_file = BASE_DIR / "index.html.backup2"
    backup_file.write_text(index_content, encoding='utf-8')
    print(f"\n✓ Backup created: index.html.backup2")

    # Replace hero
    print("\n📝 Replacing hero section...")
    hero_pattern = r'<header class="hero[^"]*">.*?</header>'
    index_content = re.sub(hero_pattern, hero_content, index_content, flags=re.DOTALL)
    print("✓ Hero section replaced")

    # Remove ALL sections after hero (categories, popular tools, etc.)
    print("\n📝 Removing all sections after hero...")

    # Find everything between </header> and <footer>
    sections_pattern = r'(</header>)(.*?)(<footer)'

    # New minimal content - just value proposition and stats
    new_content = r'''
    <!-- Value Proposition -->
    <section class="section value-section">
        <div class="container">
            <div class="value-grid">
                <div class="value-card" data-aos="fade-up">
                    <div class="value-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                            <path d="M2 17l10 5 10-5"/>
                            <path d="M2 12l10 5 10-5"/>
                        </svg>
                    </div>
                    <h3>Curated Selection</h3>
                    <p>Handpicked AI tools across 13 categories, tested and reviewed by experts</p>
                </div>

                <div class="value-card" data-aos="fade-up" data-aos-delay="100">
                    <div class="value-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                            <path d="M22 4L12 14.01l-3-3"/>
                        </svg>
                    </div>
                    <h3>Always Updated</h3>
                    <p>Fresh reviews and comparisons to keep you ahead in the AI revolution</p>
                </div>

                <div class="value-card" data-aos="fade-up" data-aos-delay="200">
                    <div class="value-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                        </svg>
                    </div>
                    <h3>Expert Insights</h3>
                    <p>In-depth analysis from beginners to enterprise solutions</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Single Tool Spotlight -->
    <section class="section spotlight-section">
        <div class="container">
            <div class="spotlight-container">
                <div class="spotlight-badge">Featured Tool of the Week</div>

                <div class="spotlight-content">
                    <div class="spotlight-visual">
                        <div class="spotlight-logo-wrapper">
                            <img src="assets/images/tools/chatbots/claude.svg" alt="Claude" class="spotlight-logo">
                            <div class="spotlight-glow"></div>
                        </div>
                    </div>

                    <div class="spotlight-info">
                        <h2>Claude 3.5 Sonnet</h2>
                        <p class="spotlight-tagline">The AI assistant that thinks before it speaks</p>

                        <div class="spotlight-stats-mini">
                            <div class="mini-stat">
                                <span class="mini-stat-value">200K</span>
                                <span class="mini-stat-label">Context Window</span>
                            </div>
                            <div class="mini-stat">
                                <span class="mini-stat-value">#1</span>
                                <span class="mini-stat-label">Coding Benchmarks</span>
                            </div>
                            <div class="mini-stat">
                                <span class="mini-stat-value">4.9★</span>
                                <span class="mini-stat-label">Rating</span>
                            </div>
                        </div>

                        <p class="spotlight-description">
                            Claude by Anthropic represents the cutting edge of conversational AI. With its massive 200K token context window and exceptional coding abilities, it's revolutionizing how we interact with AI assistants.
                        </p>

                        <div class="spotlight-cta">
                            <a href="pages/reviews/chatbots/claude.html" class="btn btn-primary">
                                Read Full Review
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M5 12h14M12 5l7 7-7 7"/>
                                </svg>
                            </a>
                            <a href="https://claude.ai" class="btn btn-secondary" target="_blank" rel="nofollow">
                                Try Claude Free
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
                                    <path d="M15 3h6v6"/>
                                    <path d="M10 14L21 3"/>
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Choose Us -->
    <section class="section why-choose-section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Why GenuisNet.ai?</h2>
                <p class="section-subtitle">Your trusted companion in the AI journey</p>
            </div>

            <div class="why-grid">
                <div class="why-item" data-aos="zoom-in">
                    <div class="why-number">01</div>
                    <h4>Comprehensive Coverage</h4>
                    <p>From ChatGPT to specialized enterprise solutions, we cover every AI tool that matters</p>
                </div>

                <div class="why-item" data-aos="zoom-in" data-aos-delay="100">
                    <div class="why-number">02</div>
                    <h4>Real-World Testing</h4>
                    <p>Every tool is tested in actual workflows, not just theoretical benchmarks</p>
                </div>

                <div class="why-item" data-aos="zoom-in" data-aos-delay="200">
                    <div class="why-number">03</div>
                    <h4>Practical Guides</h4>
                    <p>Step-by-step tutorials and comparisons to help you make informed decisions</p>
                </div>

                <div class="why-item" data-aos="zoom-in" data-aos-delay="300">
                    <div class="why-number">04</div>
                    <h4>Community Driven</h4>
                    <p>Ratings and reviews from a global community of AI enthusiasts</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Call to Action -->
    <section class="section cta-section">
        <div class="container">
            <div class="cta-box">
                <div class="cta-content">
                    <h2>Ready to Discover Your Perfect AI Tool?</h2>
                    <p>Explore 116+ carefully curated tools across 13 categories</p>
                </div>
                <div class="cta-buttons">
                    <a href="pages/categories/ai-chatbots.html" class="btn btn-primary btn-lg">
                        Browse Categories
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M5 12h14M12 5l7 7-7 7"/>
                        </svg>
                    </a>
                    <a href="pages/guides.html" class="btn btn-outline btn-lg">
                        Read Guides
                    </a>
                </div>
            </div>
        </div>
    </section>

    '''

    index_content = re.sub(sections_pattern, r'\1' + new_content + r'\3', index_content, flags=re.DOTALL)

    print("✓ Removed all category/tool previews")
    print("✓ Added minimal value sections")

    # Save
    index_file.write_text(index_content, encoding='utf-8')

    print("\n✅ Clean homepage created!")
    print("\n" + "="*70)
    print("NOUVELLE STRUCTURE:")
    print("="*70)
    print("✓ Hero 3D impressionnant")
    print("✓ Value Proposition (3 cartes)")
    print("✓ Tool Spotlight (1 outil vedette)")
    print("✓ Why Choose Us (4 raisons)")
    print("✓ CTA Final")
    print("\n✗ PAS de liste de catégories")
    print("✗ PAS de liste d'outils populaires")
    print("\n→ Accès aux catégories: Menu en haut UNIQUEMENT")
    print("\n🌐 Test: http://localhost:8000")
    print("="*70)

    return True

if __name__ == "__main__":
    create_clean_homepage()
