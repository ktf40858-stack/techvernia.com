#!/usr/bin/env python3
"""
Script to create new AI category pages
"""

from pathlib import Path

BASE_DIR = Path("/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai")
CATEGORIES_DIR = BASE_DIR / "pages" / "categories"

# Category configurations
CATEGORIES = {
    "ai-legal": {
        "title": "⚖️ AI Legal & Compliance",
        "description": "AI-powered legal research, contract analysis, and compliance automation. Transform legal workflows with intelligent document review and case law analysis.",
        "gradient": "rgba(245, 158, 11, 0.1), rgba(217, 119, 6, 0.1)",
        "gradient_colors": "#F59E0B, #D97706",
        "icon": "⚖️",
        "stats": {"tools": "12", "market": "Legal AI"},
        "tools": [
            ("Harvey AI", "🇺🇸", "United States", "Legal Research & Drafting"),
            ("CoCounsel", "🇺🇸", "United States", "Thomson Reuters AI"),
            ("LawGeex", "🇮🇱", "Israel", "Contract Review"),
            ("Luminance", "🇬🇧", "UK", "AI Due Diligence"),
            ("Kira Systems", "🇨🇦", "Canada", "Contract Analysis"),
            ("ROSS Intelligence", "🇺🇸", "United States", "Legal Research"),
            ("Casetext", "🇺🇸", "United States", "Legal AI Assistant"),
            ("Lex Machina", "🇺🇸", "United States", "Legal Analytics"),
            ("Blue J Legal", "🇨🇦", "Canada", "Tax & Employment Law"),
            ("Everlaw", "🇺🇸", "United States", "eDiscovery AI"),
            ("Primer", "🇺🇸", "United States", "Contract Intelligence"),
            ("Ravel Law", "🇺🇸", "United States", "Legal Analytics")
        ]
    },
    "ai-customer-service": {
        "title": "💬 AI Customer Service & Support",
        "description": "Intelligent chatbots, automated support, and AI-powered customer engagement. Deliver 24/7 support with natural language understanding and sentiment analysis.",
        "gradient": "rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.1)",
        "gradient_colors": "#10B981, #059669",
        "icon": "💬",
        "stats": {"tools": "15", "market": "$8B Savings"},
        "tools": [
            ("Intercom Fin", "🇺🇸", "United States", "AI Customer Support"),
            ("Zendesk AI", "🇺🇸", "United States", "Support Automation"),
            ("Ada", "🇨🇦", "Canada", "AI Chatbot Platform"),
            ("Drift", "🇺🇸", "United States", "Conversational AI"),
            ("LivePerson", "🇺🇸", "United States", "Messaging AI"),
            ("Freshdesk AI", "🇺🇸", "United States", "Helpdesk Automation"),
            ("Kustomer", "🇺🇸", "United States", "CRM AI"),
            ("Ultimate.ai", "🇩🇪", "Germany", "Automation Platform"),
            ("PolyAI", "🇬🇧", "UK", "Voice AI"),
            ("Forethought", "🇺🇸", "United States", "Support Automation"),
            ("Helpshift", "🇺🇸", "United States", "In-App Support"),
            ("Yellow.ai", "🇺🇸", "United States", "Enterprise Automation"),
            ("Netomi", "🇺🇸", "United States", "AI Customer Service"),
            ("Certainly", "🇩🇰", "Denmark", "Conversational AI"),
            ("Cognigy", "🇩🇪", "Germany", "Enterprise AI")
        ]
    },
    "ai-education": {
        "title": "🎓 AI Education & E-Learning",
        "description": "Personalized learning with AI tutors, adaptive assessments, and intelligent course recommendations. Transform education with AI-powered teaching assistants.",
        "gradient": "rgba(139, 92, 246, 0.1), rgba(124, 58, 237, 0.1)",
        "gradient_colors": "#8B5CF6, #7C3AED",
        "icon": "🎓",
        "stats": {"tools": "14", "market": "$30B by 2032"},
        "tools": [
            ("Khan Academy AI", "🇺🇸", "United States", "Khanmigo Tutor"),
            ("Duolingo Max", "🇺🇸", "United States", "AI Language Learning"),
            ("Coursera Coach", "🇺🇸", "United States", "Learning Assistant"),
            ("Century Tech", "🇬🇧", "UK", "Adaptive Learning"),
            ("Squirrel AI", "🇨🇳", "China", "Personalized Education"),
            ("Carnegie Learning", "🇺🇸", "United States", "Math AI Tutor"),
            ("Gradescope", "🇺🇸", "United States", "AI Grading"),
            ("Socratic by Google", "🇺🇸", "United States", "Homework Help"),
            ("Quizlet AI", "🇺🇸", "United States", "Study Assistant"),
            ("Cognii", "🇺🇸", "United States", "Virtual Tutor"),
            ("Thinkster Math", "🇺🇸", "United States", "AI Math Tutoring"),
            ("ALEKS", "🇺🇸", "United States", "Assessment Platform"),
            ("Knewton Alta", "🇺🇸", "United States", "Adaptive Courseware"),
            ("Querium", "🇺🇸", "United States", "STEM Tutoring")
        ]
    },
    "ai-sales": {
        "title": "💼 AI Sales & CRM",
        "description": "Automate prospecting, lead scoring, and sales forecasting with AI. Intelligent CRM, conversation intelligence, and revenue optimization.",
        "gradient": "rgba(239, 68, 68, 0.1), rgba(220, 38, 38, 0.1)",
        "gradient_colors": "#EF4444, #DC2626",
        "icon": "💼",
        "stats": {"tools": "16", "market": "30% Growth"},
        "tools": [
            ("Salesforce Einstein GPT", "🇺🇸", "United States", "AI CRM"),
            ("HubSpot AI", "🇺🇸", "United States", "Sales Automation"),
            ("Gong", "🇺🇸", "United States", "Revenue Intelligence"),
            ("Outreach", "🇺🇸", "United States", "Sales Engagement"),
            ("Apollo.io", "🇺🇸", "United States", "Sales Intelligence"),
            ("People.ai", "🇺🇸", "United States", "Revenue Operations"),
            ("Clari", "🇺🇸", "United States", "Revenue Platform"),
            ("Chorus.ai", "🇺🇸", "United States", "Conversation Intelligence"),
            ("Conversica", "🇺🇸", "United States", "AI Sales Assistant"),
            ("Exceed.ai", "🇺🇸", "United States", "Lead Qualification"),
            ("6sense", "🇺🇸", "United States", "Predictive Intelligence"),
            ("InsideSales", "🇺🇸", "United States", "AI Acceleration"),
            ("Troops.ai", "🇺🇸", "United States", "Slack CRM"),
            ("Attention", "🇺🇸", "United States", "Sales Copilot"),
            ("Lavender", "🇺🇸", "United States", "Email AI"),
            ("Regie.ai", "🇺🇸", "United States", "Prospecting AI")
        ]
    },
    "ai-research": {
        "title": "🔬 AI Research & Academia",
        "description": "Accelerate scientific discovery with AI-powered literature review, data analysis, and hypothesis generation. Research assistants for scholars and scientists.",
        "gradient": "rgba(6, 182, 212, 0.1), rgba(8, 145, 178, 0.1)",
        "gradient_colors": "#06B6D4, #0891B2",
        "icon": "🔬",
        "stats": {"tools": "12", "market": "2M+ Researchers"},
        "tools": [
            ("Consensus", "🇺🇸", "United States", "AI Research Engine"),
            ("Elicit", "🇺🇸", "United States", "Research Assistant"),
            ("Scite", "🇺🇸", "United States", "Citation Analysis"),
            ("SciSpace", "🇮🇳", "India", "Research Copilot"),
            ("ResearchRabbit", "🇺🇸", "United States", "Literature Discovery"),
            ("Semantic Scholar", "🇺🇸", "United States", "AI Search"),
            ("Iris.ai", "🇳🇴", "Norway", "Research Workspace"),
            ("Scholarcy", "🇬🇧", "UK", "Article Summarizer"),
            ("Litmaps", "🇦🇺", "Australia", "Citation Network"),
            ("Connected Papers", "🇮🇱", "Israel", "Visual Graph"),
            ("Perplexity Research", "🇺🇸", "United States", "AI Search"),
            ("Undermind", "🇺🇸", "United States", "Deep Research")
        ]
    },
    "ai-hr": {
        "title": "👥 AI HR & Recruiting",
        "description": "Transform hiring with AI-powered resume screening, candidate matching, and interview intelligence. Automate onboarding and employee engagement.",
        "gradient": "rgba(236, 72, 153, 0.1), rgba(219, 39, 119, 0.1)",
        "gradient_colors": "#EC4899, #DB2777",
        "icon": "👥",
        "stats": {"tools": "14", "market": "79% Adoption"},
        "tools": [
            ("Paradox (Olivia)", "🇺🇸", "United States", "AI Recruiting Assistant"),
            ("HireVue", "🇺🇸", "United States", "Video Interview AI"),
            ("Pymetrics", "🇺🇸", "United States", "Behavioral Assessment"),
            ("Eightfold AI", "🇺🇸", "United States", "Talent Intelligence"),
            ("Beamery", "🇬🇧", "UK", "Talent Lifecycle"),
            ("Phenom", "🇺🇸", "United States", "Talent Experience"),
            ("Seekout", "🇺🇸", "United States", "Talent Search"),
            ("Harver", "🇳🇱", "Netherlands", "Hiring Assessment"),
            ("Textio", "🇺🇸", "United States", "Job Description AI"),
            ("Fetcher", "🇺🇸", "United States", "Automated Sourcing"),
            ("Humanly", "🇺🇸", "United States", "Conversational AI"),
            ("Sense", "🇺🇸", "United States", "Talent Engagement"),
            ("Findem", "🇺🇸", "United States", "Talent Discovery"),
            ("Workable AI", "🇬🇷", "Greece", "ATS with AI")
        ]
    },
    "ai-translation": {
        "title": "🌍 AI Translation & Localization",
        "description": "Break language barriers with neural machine translation, real-time interpretation, and content localization. Support 100+ languages with AI accuracy.",
        "gradient": "rgba(34, 197, 94, 0.1), rgba(22, 163, 74, 0.1)",
        "gradient_colors": "#22C55E, #16A34A",
        "icon": "🌍",
        "stats": {"tools": "10", "market": "$1.5B in 2024"},
        "tools": [
            ("DeepL Pro", "🇩🇪", "Germany", "Neural Translation"),
            ("Google Translate AI", "🇺🇸", "United States", "100+ Languages"),
            ("Microsoft Translator", "🇺🇸", "United States", "Enterprise Translation"),
            ("Phrase", "🇩🇪", "Germany", "Localization Platform"),
            ("Smartling", "🇺🇸", "United States", "Translation Management"),
            ("Lokalise", "🇱🇻", "Latvia", "Localization AI"),
            ("SYSTRAN", "🇫🇷", "France", "Enterprise Translation"),
            ("Unbabel", "🇵🇹", "Portugal", "Human + AI Translation"),
            ("Lilt", "🇺🇸", "United States", "Adaptive MT"),
            ("ModernMT", "🇮🇹", "Italy", "Context-Aware Translation")
        ]
    },
    "ai-gaming": {
        "title": "🎮 AI Gaming & Entertainment",
        "description": "Create intelligent NPCs, generate game content, and build immersive experiences. AI-powered game design, procedural generation, and dynamic storytelling.",
        "gradient": "rgba(168, 85, 247, 0.1), rgba(147, 51, 234, 0.1)",
        "gradient_colors": "#A855F7, #9333EA",
        "icon": "🎮",
        "stats": {"tools": "11", "market": "$3.5B by 2030"},
        "tools": [
            ("Inworld AI", "🇺🇸", "United States", "NPC Intelligence"),
            ("Scenario", "🇫🇷", "France", "Game Asset Generation"),
            ("Ludo.ai", "🇳🇱", "Netherlands", "Game Design AI"),
            ("Latitude (AI Dungeon)", "🇺🇸", "United States", "Interactive Stories"),
            ("Promethean AI", "🇺🇸", "United States", "World Building"),
            ("Rosebud AI", "🇺🇸", "United States", "Game Generation"),
            ("Hidden Door", "🇺🇸", "United States", "Narrative Games"),
            ("Charisma.ai", "🇬🇧", "UK", "Interactive Stories"),
            ("Rct AI", "🇺🇸", "United States", "Procedural Content"),
            ("Artomatix", "🇮🇪", "Ireland", "3D Asset Creation"),
            ("Replika", "🇺🇸", "United States", "AI Companion")
        ]
    },
    "ai-quantum": {
        "title": "⚛️ AI Quantum Computing",
        "description": "Quantum-enhanced machine learning and optimization. Explore quantum algorithms, simulators, and cloud quantum computing platforms for next-gen AI.",
        "gradient": "rgba(99, 102, 241, 0.1), rgba(79, 70, 229, 0.1)",
        "gradient_colors": "#6366F1, #4F46E5",
        "icon": "⚛️",
        "stats": {"tools": "8", "market": "Emerging Tech"},
        "tools": [
            ("IBM Quantum", "🇺🇸", "United States", "Quantum Cloud Platform"),
            ("Google Cirq", "🇺🇸", "United States", "Quantum Framework"),
            ("Amazon Braket", "🇺🇸", "United States", "AWS Quantum"),
            ("Azure Quantum", "🇺🇸", "United States", "Microsoft Quantum"),
            ("D-Wave Leap", "🇨🇦", "Canada", "Quantum Annealing"),
            ("Rigetti QCS", "🇺🇸", "United States", "Quantum Cloud Services"),
            ("Xanadu PennyLane", "🇨🇦", "Canada", "Quantum ML"),
            ("IonQ", "🇺🇸", "United States", "Trapped Ion Quantum")
        ]
    }
}

def create_category_page(filename, config):
    """Create a category page HTML file"""

    tools_html = "\n                ".join([
        f'''<a href="#" class="tool-card">
                    <div class="tool-logo"><span style="font-size: 48px;">{config["icon"]}</span></div>
                    <h3>{name}</h3>
                    <div class="tool-country"><span class="country-flag">{flag}</span><span class="country-name">{country}</span></div>
                    <div class="tool-meta"><span>{category}</span></div>
                </a>'''
        for name, flag, country, category in config["tools"]
    ])

    html = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{config["description"]}">
    <meta name="keywords" content="AI tools, {config['title']}, artificial intelligence">
    <meta name="author" content="GenuisNet.ai">
    <title>{config["title"]} | GenuisNet.ai</title>
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="../../css/animations.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        .category-hero {{
            padding: calc(80px + var(--space-4xl)) 0 var(--space-3xl);
            background: linear-gradient(135deg, {config["gradient"]});
            border-bottom: 1px solid var(--border-color);
        }}
        .category-hero-content {{ display: grid; grid-template-columns: 1fr auto; gap: var(--space-3xl); align-items: center; }}
        .category-icon-large {{ width: 120px; height: 120px; display: flex; align-items: center; justify-content: center; font-size: 4rem; }}
        .category-hero h1 {{ font-size: clamp(2.5rem, 5vw, 3.5rem); font-weight: 800; margin-bottom: var(--space-md); }}
        .category-hero p {{ font-size: var(--text-lg); color: var(--text-secondary); max-width: 600px; line-height: 1.7; }}
        .category-stats {{ display: flex; gap: var(--space-2xl); margin-top: var(--space-xl); }}
        .category-stat {{ text-align: center; }}
        .category-stat-number {{ font-size: var(--text-3xl); font-weight: 800; background: linear-gradient(135deg, {config["gradient_colors"]}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .category-stat-label {{ font-size: var(--text-sm); color: var(--text-tertiary); }}
        .tools-section {{ padding: var(--space-4xl) 0; }}
        .tools-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: var(--space-xl); }}
        .tool-card {{ background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: var(--space-xl); text-align: center; transition: all var(--transition-normal); text-decoration: none; color: inherit; display: flex; flex-direction: column; align-items: center; }}
        .tool-card:hover {{ transform: translateY(-5px); border-color: var(--border-color-hover); box-shadow: var(--shadow-glow); }}
        .tool-logo {{ width: 80px; height: 80px; margin-bottom: var(--space-md); display: flex; align-items: center; justify-content: center; }}
        .tool-logo img {{ width: 100%; height: 100%; object-fit: contain; }}
        .tool-card h3 {{ font-size: var(--text-lg); font-weight: 700; margin-bottom: var(--space-sm); }}
        .tool-country {{ display: flex; align-items: center; gap: var(--space-xs); margin-bottom: var(--space-sm); font-size: var(--text-sm); color: var(--text-secondary); }}
        .tool-meta {{ display: flex; gap: var(--space-sm); font-size: var(--text-xs); color: var(--text-tertiary); margin-top: auto; }}
        @media (max-width: 768px) {{ .category-hero-content {{ grid-template-columns: 1fr; text-align: center; }} .category-icon-large {{ margin: 0 auto; }} }}
    </style>
</head>
<body>
    <canvas id="neural-bg"></canvas>

    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="../../index.html" class="logo">
                <img src="../../assets/images/logo-neon.svg" alt="GenuisNet.ai" style="height: 50px; width: auto;">
            </a>
            <ul class="nav-menu" id="nav-menu">
                <li class="nav-item"><a href="../../index.html" class="nav-link">Home</a></li>
                <li class="nav-item"><a href="../guides.html" class="nav-link">Guides</a></li>
                <li class="nav-item"><a href="../comparisons.html" class="nav-link">Compare</a></li>
                <li class="nav-item"><a href="../about.html" class="nav-link">About</a></li>
            </ul>
            <div class="nav-actions">
                <button class="theme-toggle" id="theme-toggle" aria-label="Toggle Theme">
                    <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>
                    </svg>
                    <svg class="moon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
                    </svg>
                </button>
            </div>
        </div>
    </nav>

    <header class="category-hero">
        <div class="container">
            <div class="category-hero-content">
                <div>
                    <h1>{config["title"]}</h1>
                    <p>{config["description"]}</p>
                    <div class="category-stats">
                        <div class="category-stat">
                            <div class="category-stat-number">{config["stats"]["tools"]}</div>
                            <div class="category-stat-label">Tools</div>
                        </div>
                        <div class="category-stat">
                            <div class="category-stat-number">{config["stats"]["market"]}</div>
                            <div class="category-stat-label">Market Size</div>
                        </div>
                    </div>
                </div>
                <div class="category-icon-large">{config["icon"]}</div>
            </div>
        </div>
    </header>

    <main class="tools-section">
        <div class="container">
            <div class="tools-grid">
                {tools_html}
            </div>
        </div>
    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="../../index.html" class="footer-logo">
                        <img src="../../assets/images/logo-neon.svg" alt="GenuisNet.ai Logo" style="height: 40px; width: auto;">
                    </a>
                    <p class="footer-desc">Your trusted source for AI tool reviews, comparisons, and guides.</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p class="copyright">© 2024 GenuisNet.ai. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="../../js/animations.js"></script>
    <script src="../../js/main.js"></script>
</body>
</html>'''

    return html

def main():
    print("🚀 Creating new AI category pages...\n")

    created_count = 0

    for filename, config in CATEGORIES.items():
        filepath = CATEGORIES_DIR / f"{filename}.html"

        # Create the HTML content
        html_content = create_category_page(filename, config)

        # Write the file
        filepath.write_text(html_content, encoding='utf-8')

        print(f"✅ Created: {filename}.html - {config['title']}")
        created_count += 1

    print(f"\n{'='*60}")
    print(f"✅ Successfully created {created_count} category pages!")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
