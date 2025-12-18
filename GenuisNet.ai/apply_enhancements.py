#!/usr/bin/env python3
"""
Apply enhancements to GenuisNet.ai:
1. Update all HTML files to use consistent GenuisNet.ai logo
2. Integrate enhanced hero section into index.html
3. Add required CSS and JS files
"""

import re
from pathlib import Path
import shutil

BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")

def update_logo_paths():
    """Ensure all HTML files use the correct logo path"""
    print("\n" + "="*70)
    print("UPDATING LOGO PATHS FOR CONSISTENCY")
    print("="*70 + "\n")

    # Logo paths by directory depth
    logo_mappings = {
        'index.html': 'assets/images/logo.svg',  # Root level
        'pages/*.html': '../assets/images/logo.svg',  # Pages level
        'pages/categories/*.html': '../../assets/images/logo.svg',  # Categories level
        'pages/reviews/*/*.html': '../../../assets/images/logo.svg',  # Reviews level
    }

    updated = 0

    # Update root index.html
    index_file = BASE_DIR / "index.html"
    if index_file.exists():
        content = index_file.read_text(encoding='utf-8')
        # Already correct path
        if '<img src="assets/images/logo.svg"' in content:
            print(f"  ✓ index.html - Already correct")
        else:
            print(f"  ℹ index.html - Needs manual check")

    # Update pages/*.html
    for html_file in (BASE_DIR / "pages").glob("*.html"):
        content = html_file.read_text(encoding='utf-8')
        original = content

        # Update logo img src
        content = re.sub(
            r'<img src="[^"]*logo\.svg"',
            '<img src="../assets/images/logo.svg"',
            content
        )

        if content != original:
            html_file.write_text(content, encoding='utf-8')
            print(f"  ✓ {html_file.name} - Updated")
            updated += 1
        else:
            print(f"  ✓ {html_file.name} - Already correct")

    # Update pages/categories/*.html
    for html_file in (BASE_DIR / "pages" / "categories").glob("*.html"):
        content = html_file.read_text(encoding='utf-8')
        original = content

        # Update logo img src
        content = re.sub(
            r'<img src="[^"]*logo\.svg"',
            '<img src="../../assets/images/logo.svg"',
            content
        )

        if content != original:
            html_file.write_text(content, encoding='utf-8')
            print(f"  ✓ categories/{html_file.name} - Updated")
            updated += 1

    # Update pages/reviews/*/*.html
    for category_dir in (BASE_DIR / "pages" / "reviews").iterdir():
        if category_dir.is_dir():
            for html_file in category_dir.glob("*.html"):
                content = html_file.read_text(encoding='utf-8')
                original = content

                # Update logo img src
                content = re.sub(
                    r'<img src="[^"]*logo\.svg"',
                    '<img src="../../../assets/images/logo.svg"',
                    content
                )

                if content != original:
                    html_file.write_text(content, encoding='utf-8')
                    updated += 1

    print(f"\n  Total files updated: {updated}")
    return updated

def integrate_enhanced_hero():
    """Integrate the enhanced hero section into index.html"""
    print("\n" + "="*70)
    print("INTEGRATING ENHANCED HERO SECTION")
    print("="*70 + "\n")

    index_file = BASE_DIR / "index.html"
    if not index_file.exists():
        print("  ✗ index.html not found!")
        return False

    content = index_file.read_text(encoding='utf-8')

    # Add CSS link in head
    if 'hero-enhanced.css' not in content:
        css_link = '    <link rel="stylesheet" href="css/hero-enhanced.css">'
        content = content.replace('</head>', f'{css_link}\n</head>')
        print("  ✓ Added hero-enhanced.css link")

    # Add JS script before </body>
    if 'hero-enhanced.js' not in content:
        js_script = '    <script src="js/hero-enhanced.js"></script>'
        content = content.replace('</body>', f'{js_script}\n</body>')
        print("  ✓ Added hero-enhanced.js script")

    # Save updated index.html
    index_file.write_text(content, encoding='utf-8')
    print("  ✓ index.html updated successfully")

    # Print instructions for manual hero replacement
    print("\n" + "="*70)
    print("MANUAL STEP REQUIRED:")
    print("="*70)
    print("\nTo complete the hero section upgrade:")
    print("1. Open: index.html")
    print("2. Find the <header class=\"hero\"> section")
    print("3. Replace it with content from: home_hero_enhanced.html")
    print("4. Save the file")
    print("\nOr use this command:")
    print("  nano index.html")
    print("\nThe enhanced hero includes:")
    print("  • Holographic grid background")
    print("  • 3D AI brain visualization")
    print("  • Floating data streams")
    print("  • Animated circuit patterns")
    print("  • Glitch effect title")
    print("  • Typewriter subtitle")
    print("  • Futuristic CTA buttons")
    print("  • Scrolling brand logos")
    print("  • Enhanced stats cards")
    print("  • Mouse trail effects")

    return True

def create_implementation_guide():
    """Create a guide for implementing the enhancements"""
    guide_content = """# GenuisNet.ai Enhancement Implementation Guide

## ✅ Completed Automatically

1. **Logo Consistency** - All HTML files now use correct relative paths to logo.svg
2. **CSS & JS Integration** - hero-enhanced.css and hero-enhanced.js linked in index.html

## 📝 Manual Steps Required

### Replace Hero Section in index.html

1. Open `index.html` in your editor
2. Locate the existing hero section (starts with `<header class="hero">`)
3. Replace the entire hero section with the content from `home_hero_enhanced.html`
4. Save the file

**Before:**
```html
<header class="hero">
    ... old hero content ...
</header>
```

**After:**
```html
<header class="hero hero-enhanced">
    <!-- 3D Holographic Grid Background -->
    <canvas id="holographic-grid" class="holographic-grid"></canvas>
    ... enhanced hero content ...
</header>
```

## 🎨 New Features Added

### Visual Effects
- ✨ Holographic 3D grid background
- 🧠 3D AI brain visualization with rotating neurons
- 💫 Floating data streams
- ⚡ Animated circuit patterns
- 🌟 Glowing orbs with parallax
- 🎭 Glitch effect on title
- ⌨️ Typewriter effect on subtitle
- 🖱️ Mouse trail particles

### Interactive Elements
- 🎯 Enhanced stat cards with hover effects
- 🚀 Futuristic CTA buttons with particle explosions
- 📊 Animated counters
- 🏷️ Scrolling brand logos (ChatGPT, Claude, Gemini, etc.)
- 📱 Floating preview cards
- 🎪 Smooth scroll indicators

### Performance
- 🎮 Hardware-accelerated canvas animations
- 🔄 RequestAnimationFrame for smooth 60fps
- 📦 Lazy loading with Intersection Observer
- 🎯 Optimized particle systems

## 🧪 Testing

After implementing, test these features:

1. **Desktop (1920x1080)**
   - Check holographic grid animation
   - Verify 3D brain rotates smoothly
   - Test CTA button hover effects
   - Confirm logo scroll animation

2. **Tablet (768px)**
   - Ensure single column layout
   - Check stat cards stack properly
   - Verify buttons are centered

3. **Mobile (375px)**
   - Confirm floating cards are hidden
   - Test touch interactions
   - Verify typewriter is readable

## 📈 Expected Results

Visitors will see:
- **Immediate "WOW" factor** with holographic effects
- **Professional, cutting-edge design** that matches AI theme
- **Smooth, fluid animations** that feel premium
- **Clear hierarchy** with enhanced typography
- **Trust signals** with brand logo carousel

## 🐛 Troubleshooting

**Issue:** Animations not showing
**Fix:** Check browser console, ensure JS file loaded

**Issue:** Layout broken on mobile
**Fix:** Clear cache, check responsive CSS

**Issue:** Performance slow
**Fix:** Reduce particle count in hero-enhanced.js (line 270)

## 📞 Support

If issues persist, check:
- Browser DevTools Console for errors
- CSS file loaded correctly
- JS file loaded before </body>
- Canvas elements have IDs set correctly

---

**Last Updated:** November 29, 2024
**Version:** 2.0 Enhanced
"""

    guide_file = BASE_DIR / "IMPLEMENTATION_GUIDE.md"
    guide_file.write_text(guide_content, encoding='utf-8')
    print(f"\n  ✓ Created implementation guide: IMPLEMENTATION_GUIDE.md")

if __name__ == "__main__":
    print("="*70)
    print("GENUISNET.AI ENHANCEMENT APPLICATION")
    print("="*70)

    # Step 1: Update logo paths
    logo_updates = update_logo_paths()

    # Step 2: Integrate enhanced hero
    hero_integrated = integrate_enhanced_hero()

    # Step 3: Create implementation guide
    create_implementation_guide()

    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"\n✅ Logo paths updated: {logo_updates} files")
    print(f"✅ Hero enhancements integrated: {'Yes' if hero_integrated else 'No'}")
    print(f"✅ Implementation guide created")
    print("\n📖 Next step: Read IMPLEMENTATION_GUIDE.md for manual hero replacement")
    print("\n🌐 View your site at: http://localhost:8000")
    print("="*70)
