#!/usr/bin/env python3
"""
Update homepage to show enhanced hero and remove categories section
"""

import re
from pathlib import Path

BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")

def update_homepage():
    """Replace hero and remove categories from index.html"""

    print("="*70)
    print("UPDATING HOMEPAGE")
    print("="*70)

    # Read files
    index_file = BASE_DIR / "index.html"
    hero_file = BASE_DIR / "home_hero_enhanced.html"

    if not index_file.exists():
        print("✗ index.html not found!")
        return False

    if not hero_file.exists():
        print("✗ home_hero_enhanced.html not found!")
        return False

    # Read content
    index_content = index_file.read_text(encoding='utf-8')
    hero_content = hero_file.read_text(encoding='utf-8')

    # Backup original
    backup_file = BASE_DIR / "index.html.backup"
    backup_file.write_text(index_content, encoding='utf-8')
    print(f"\n✓ Backup created: index.html.backup")

    # Step 1: Replace hero section
    print("\n📝 Replacing hero section...")

    # Find old hero
    hero_pattern = r'<header class="hero">.*?</header>'
    old_hero_match = re.search(hero_pattern, index_content, re.DOTALL)

    if old_hero_match:
        index_content = re.sub(hero_pattern, hero_content, index_content, flags=re.DOTALL)
        print("✓ Hero section replaced with enhanced version")
    else:
        print("✗ Could not find old hero section")
        return False

    # Step 2: Remove categories section from homepage
    print("\n📝 Removing categories section from homepage...")

    # Find categories section
    categories_pattern = r'<!-- Categories Section -->.*?(?=<!-- |<section class="section |<footer|$)'

    categories_match = re.search(categories_pattern, index_content, re.DOTALL)

    if categories_match:
        index_content = re.sub(categories_pattern, '', index_content, flags=re.DOTALL)
        print("✓ Categories section removed")
    else:
        print("⚠ Categories section not found (may already be removed)")

    # Step 3: Add new homepage sections after hero
    print("\n📝 Adding new homepage sections...")

    new_sections = '''
    <!-- Featured Categories Preview -->
    <section class="section featured-preview">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Discover</span>
                <h2 class="section-title">Explore by Category</h2>
                <p class="section-subtitle">
                    Browse our curated collection of AI tools organized by use case
                </p>
            </div>

            <div class="featured-categories-grid">
                <a href="pages/categories/ai-chatbots.html" class="featured-cat-card">
                    <div class="cat-card-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                        </svg>
                    </div>
                    <h3>AI Chatbots</h3>
                    <p>Conversational AI assistants</p>
                    <span class="cat-count">8 Tools</span>
                </a>

                <a href="pages/categories/ai-coding.html" class="featured-cat-card">
                    <div class="cat-card-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/>
                        </svg>
                    </div>
                    <h3>AI Coding</h3>
                    <p>Code generation & assistance</p>
                    <span class="cat-count">8 Tools</span>
                </a>

                <a href="pages/categories/ai-image.html" class="featured-cat-card">
                    <div class="cat-card-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                            <circle cx="8.5" cy="8.5" r="1.5"/>
                            <path d="M21 15l-5-5L5 21"/>
                        </svg>
                    </div>
                    <h3>AI Image</h3>
                    <p>Image generation & editing</p>
                    <span class="cat-count">8 Tools</span>
                </a>

                <a href="pages/categories/ai-video.html" class="featured-cat-card">
                    <div class="cat-card-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M23 7l-7 5 7 5V7z"/>
                            <rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>
                        </svg>
                    </div>
                    <h3>AI Video</h3>
                    <p>Video creation & editing</p>
                    <span class="cat-count">8 Tools</span>
                </a>

                <a href="pages/categories/ai-writing.html" class="featured-cat-card">
                    <div class="cat-card-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 20h9"/>
                            <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
                        </svg>
                    </div>
                    <h3>AI Writing</h3>
                    <p>Content creation tools</p>
                    <span class="cat-count">7 Tools</span>
                </a>

                <a href="pages/categories/ai-productivity.html" class="featured-cat-card">
                    <div class="cat-card-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                            <path d="M22 4L12 14.01l-3-3"/>
                        </svg>
                    </div>
                    <h3>AI Productivity</h3>
                    <p>Workflow automation</p>
                    <span class="cat-count">8 Tools</span>
                </a>
            </div>

            <div class="section-cta">
                <a href="pages/categories/ai-chatbots.html" class="btn btn-outline btn-lg">
                    View All Categories
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                </a>
            </div>
        </div>
    </section>

    <!-- Popular Tools -->
    <section class="section popular-tools">
        <div class="container">
            <div class="section-header">
                <span class="section-badge">Trending</span>
                <h2 class="section-title">Popular AI Tools</h2>
                <p class="section-subtitle">
                    Most reviewed and highly rated tools by our community
                </p>
            </div>

            <div class="popular-tools-grid">
                <a href="pages/reviews/chatbots/chatgpt.html" class="tool-preview-card">
                    <img src="assets/images/tools/chatbots/chatgpt.svg" alt="ChatGPT" class="tool-preview-logo">
                    <div class="tool-preview-info">
                        <h4>ChatGPT</h4>
                        <p>OpenAI's powerful conversational AI</p>
                        <div class="tool-preview-meta">
                            <span class="rating">★ 4.8</span>
                            <span class="badge">Popular</span>
                        </div>
                    </div>
                </a>

                <a href="pages/reviews/chatbots/claude.html" class="tool-preview-card">
                    <img src="assets/images/tools/chatbots/claude.svg" alt="Claude" class="tool-preview-logo">
                    <div class="tool-preview-info">
                        <h4>Claude</h4>
                        <p>Anthropic's advanced AI assistant</p>
                        <div class="tool-preview-meta">
                            <span class="rating">★ 4.9</span>
                            <span class="badge">Editor's Pick</span>
                        </div>
                    </div>
                </a>

                <a href="pages/reviews/image/midjourney.html" class="tool-preview-card">
                    <img src="assets/images/tools/image/midjourney.svg" alt="Midjourney" class="tool-preview-logo">
                    <div class="tool-preview-info">
                        <h4>Midjourney</h4>
                        <p>AI-powered image generation</p>
                        <div class="tool-preview-meta">
                            <span class="rating">★ 4.7</span>
                            <span class="badge">Trending</span>
                        </div>
                    </div>
                </a>

                <a href="pages/reviews/coding/cursor.html" class="tool-preview-card">
                    <img src="assets/images/tools/coding/cursor.svg" alt="Cursor" class="tool-preview-logo">
                    <div class="tool-preview-info">
                        <h4>Cursor</h4>
                        <p>AI-first code editor</p>
                        <div class="tool-preview-meta">
                            <span class="rating">★ 4.8</span>
                            <span class="badge">New</span>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </section>
'''

    # Insert new sections after hero
    hero_end = index_content.find('</header>')
    if hero_end != -1:
        insertion_point = index_content.find('\n', hero_end) + 1
        index_content = index_content[:insertion_point] + new_sections + index_content[insertion_point:]
        print("✓ Added featured categories and popular tools sections")

    # Save updated index.html
    index_file.write_text(index_content, encoding='utf-8')
    print("\n✅ Homepage updated successfully!")
    print("\n" + "="*70)
    print("CHANGES MADE:")
    print("="*70)
    print("✓ Replaced basic hero with enhanced 3D hero")
    print("✓ Removed full categories section")
    print("✓ Added featured categories preview (6 cards)")
    print("✓ Added popular tools section")
    print("✓ Created backup: index.html.backup")
    print("\n🌐 View at: http://localhost:8000")
    print("="*70)

    return True

if __name__ == "__main__":
    update_homepage()
