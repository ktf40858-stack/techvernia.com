#!/usr/bin/env python3
"""
Génère des guides spécialisés pour chaque catégorie d'outils IA
"""

from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
PAGES_DIR = BASE_DIR / "pages"
CATEGORIES_DIR = PAGES_DIR / "categories"
REVIEWS_DIR = PAGES_DIR / "reviews"

# Définition des guides par catégorie avec contenu détaillé
CATEGORY_GUIDES = {
    'chatbots': {
        'title': 'AI Chatbots Guide',
        'subtitle': 'Master Conversational AI Tools',
        'description': 'Complete guide to using AI chatbots like ChatGPT, Claude, and Gemini for productivity, creativity, and automation.',
        'icon': '💬',
        'guides': [
            {
                'title': 'Getting Started with AI Chatbots',
                'level': 'Beginner',
                'duration': '15 min',
                'description': 'Learn the basics of AI chatbots and how to start your first conversation',
                'topics': [
                    'What are AI chatbots?',
                    'Choosing the right chatbot for your needs',
                    'Creating your first account',
                    'Basic conversation techniques',
                    'Understanding chatbot capabilities and limitations'
                ]
            },
            {
                'title': 'Advanced Prompt Engineering',
                'level': 'Advanced',
                'duration': '30 min',
                'description': 'Master the art of crafting effective prompts for better AI responses',
                'topics': [
                    'Prompt structure and formatting',
                    'Context management techniques',
                    'Chain-of-thought prompting',
                    'Role-based prompts',
                    'Few-shot learning examples'
                ]
            },
            {
                'title': 'ChatGPT vs Claude vs Gemini',
                'level': 'Intermediate',
                'duration': '20 min',
                'description': 'Comprehensive comparison of major AI chatbots',
                'topics': [
                    'Feature comparison',
                    'Pricing and plans',
                    'Use case recommendations',
                    'Strengths and weaknesses',
                    'Integration capabilities'
                ]
            }
        ]
    },

    'image': {
        'title': 'AI Image Generation Guide',
        'subtitle': 'Create Stunning Visuals with AI',
        'description': 'Learn to use Midjourney, DALL-E, Stable Diffusion and other AI image generators.',
        'icon': '🎨',
        'guides': [
            {
                'title': 'AI Image Generation Basics',
                'level': 'Beginner',
                'duration': '20 min',
                'description': 'Introduction to AI image generation tools and techniques',
                'topics': [
                    'Understanding diffusion models',
                    'Choosing between Midjourney, DALL-E, and Stable Diffusion',
                    'Writing effective image prompts',
                    'Basic parameters and settings',
                    'Copyright and usage rights'
                ]
            },
            {
                'title': 'Advanced Image Prompting',
                'level': 'Advanced',
                'duration': '40 min',
                'description': 'Master complex prompts for professional-quality images',
                'topics': [
                    'Style modifiers and artistic references',
                    'Lighting and composition techniques',
                    'Negative prompts for refinement',
                    'Multi-prompt compositions',
                    'Aspect ratios and resolutions'
                ]
            }
        ]
    },

    'coding': {
        'title': 'AI Coding Assistants Guide',
        'subtitle': 'Boost Your Development Workflow',
        'description': 'Master GitHub Copilot, Cursor, and other AI coding tools.',
        'icon': '💻',
        'guides': [
            {
                'title': 'Getting Started with AI Code Completion',
                'level': 'Beginner',
                'duration': '15 min',
                'description': 'Set up and use your first AI coding assistant',
                'topics': [
                    'Installing GitHub Copilot or Cursor',
                    'IDE integration and setup',
                    'Basic code completion',
                    'Comment-to-code generation',
                    'Understanding AI suggestions'
                ]
            },
            {
                'title': 'AI-Assisted Debugging and Refactoring',
                'level': 'Intermediate',
                'duration': '25 min',
                'description': 'Use AI to find bugs and improve code quality',
                'topics': [
                    'AI-powered error detection',
                    'Automated refactoring suggestions',
                    'Code explanation and documentation',
                    'Test generation',
                    'Security vulnerability detection'
                ]
            }
        ]
    },

    'writing': {
        'title': 'AI Writing Tools Guide',
        'subtitle': 'Write Better Content Faster',
        'description': 'Learn to use Jasper, Copy.ai, Grammarly and other AI writing assistants.',
        'icon': '✍️',
        'guides': [
            {
                'title': 'AI Writing Fundamentals',
                'level': 'Beginner',
                'duration': '15 min',
                'description': 'Start using AI writing tools effectively',
                'topics': [
                    'Choosing the right writing AI',
                    'Content brief creation',
                    'Tone and style customization',
                    'Basic editing with AI',
                    'Plagiarism considerations'
                ]
            },
            {
                'title': 'SEO Content Creation with AI',
                'level': 'Intermediate',
                'duration': '30 min',
                'description': 'Create SEO-optimized content using AI tools',
                'topics': [
                    'Keyword integration techniques',
                    'Meta descriptions and titles',
                    'Content structure optimization',
                    'Long-form content generation',
                    'AI + human editing workflow'
                ]
            }
        ]
    },

    'research': {
        'title': 'AI Research Tools Guide',
        'subtitle': 'Accelerate Your Research',
        'description': 'Use Consensus, Elicit, SciSpace and other AI research assistants.',
        'icon': '📚',
        'guides': [
            {
                'title': 'AI-Powered Literature Review',
                'level': 'Intermediate',
                'duration': '25 min',
                'description': 'Conduct faster, more comprehensive literature reviews',
                'topics': [
                    'Using AI to find relevant papers',
                    'Automated summarization',
                    'Citation network analysis',
                    'Key insights extraction',
                    'Organizing research findings'
                ]
            },
            {
                'title': 'Research Question Answering with AI',
                'level': 'Advanced',
                'duration': '30 min',
                'description': 'Get evidence-based answers from academic literature',
                'topics': [
                    'Formulating effective research questions',
                    'Evaluating AI-generated evidence',
                    'Cross-referencing sources',
                    'Identifying research gaps',
                    'Export and citation management'
                ]
            }
        ]
    },

    'video': {
        'title': 'AI Video Creation Guide',
        'subtitle': 'Create Professional Videos with AI',
        'description': 'Master Runway, Synthesia, and other AI video generation tools.',
        'icon': '🎬',
        'guides': [
            {
                'title': 'AI Video Generation Basics',
                'level': 'Beginner',
                'duration': '20 min',
                'description': 'Create your first AI-generated video',
                'topics': [
                    'Text-to-video fundamentals',
                    'AI avatar creation',
                    'Script writing for AI video',
                    'Basic video editing',
                    'Export formats and quality settings'
                ]
            }
        ]
    },

    'productivity': {
        'title': 'AI Productivity Tools Guide',
        'subtitle': 'Work Smarter with AI',
        'description': 'Optimize your workflow with Notion AI, Motion, and other productivity tools.',
        'icon': '⚡',
        'guides': [
            {
                'title': 'AI-Powered Task Management',
                'level': 'Intermediate',
                'duration': '20 min',
                'description': 'Automate and optimize your task management',
                'topics': [
                    'AI task prioritization',
                    'Smart scheduling with Motion',
                    'Automated note-taking',
                    'Meeting summaries with AI',
                    'Workflow automation'
                ]
            }
        ]
    },

    'customer-service': {
        'title': 'AI Customer Service Guide',
        'subtitle': 'Transform Customer Support with AI',
        'description': 'Implement AI chatbots and support tools like Zendesk AI, Intercom Fin.',
        'icon': '📞',
        'guides': [
            {
                'title': 'Implementing AI Customer Support',
                'level': 'Intermediate',
                'duration': '30 min',
                'description': 'Set up and optimize AI customer service tools',
                'topics': [
                    'Chatbot implementation strategy',
                    'Knowledge base integration',
                    'Escalation workflows',
                    'Performance metrics',
                    'Customer satisfaction optimization'
                ]
            }
        ]
    },

    'sales': {
        'title': 'AI Sales Tools Guide',
        'subtitle': 'Close More Deals with AI',
        'description': 'Use Gong, Outreach, and AI sales tools to boost revenue.',
        'icon': '💼',
        'guides': [
            {
                'title': 'AI-Powered Sales Prospecting',
                'level': 'Intermediate',
                'duration': '25 min',
                'description': 'Find and engage prospects using AI',
                'topics': [
                    'Lead scoring with AI',
                    'Personalized outreach at scale',
                    'Conversation intelligence',
                    'Email optimization',
                    'Pipeline forecasting'
                ]
            }
        ]
    },

    'audio': {
        'title': 'AI Audio Tools Guide',
        'subtitle': 'Create Professional Audio with AI',
        'description': 'Master ElevenLabs, Murf AI and other voice generation tools.',
        'icon': '🎵',
        'guides': [
            {
                'title': 'AI Voice Generation Basics',
                'level': 'Beginner',
                'duration': '15 min',
                'description': 'Create realistic AI voices',
                'topics': [
                    'Text-to-speech fundamentals',
                    'Voice cloning basics',
                    'Emotion and tone control',
                    'Audio quality optimization',
                    'Use cases and applications'
                ]
            }
        ]
    }
}

def count_tools_in_category(category):
    """Compte le nombre d'outils dans une catégorie"""
    category_dir = REVIEWS_DIR / category
    if category_dir.exists():
        return len(list(category_dir.glob("*.html")))
    return 0

def generate_guide_recommendations():
    """Génère un rapport avec des recommandations de guides"""

    print("=" * 70)
    print("AI Tools Guide Opportunities Analysis")
    print("=" * 70)

    # Analyser toutes les catégories
    all_categories = []
    for category_dir in sorted(REVIEWS_DIR.iterdir()):
        if category_dir.is_dir():
            category = category_dir.name
            tool_count = count_tools_in_category(category)
            has_guide = category in CATEGORY_GUIDES

            all_categories.append({
                'name': category,
                'tools': tool_count,
                'has_guide': has_guide,
                'priority': tool_count * (2 if not has_guide else 1)
            })

    # Trier par priorité
    all_categories.sort(key=lambda x: x['priority'], reverse=True)

    # Afficher le rapport
    print(f"\n📊 Category Analysis (23 categories, {sum(c['tools'] for c in all_categories)} tools total)\n")

    print("✅ Categories WITH Guides ({}):\n".format(sum(1 for c in all_categories if c['has_guide'])))
    for cat in all_categories:
        if cat['has_guide']:
            guide_count = len(CATEGORY_GUIDES[cat['name']]['guides'])
            print(f"   {CATEGORY_GUIDES[cat['name']]['icon']} {cat['name']:20s}: {cat['tools']:2d} tools, {guide_count} guides")

    print(f"\n❌ Categories WITHOUT Guides ({sum(1 for c in all_categories if not c['has_guide'])}):\n")
    for cat in all_categories:
        if not cat['has_guide']:
            print(f"   📝 {cat['name']:20s}: {cat['tools']:2d} tools - Priority: {cat['priority']}")

    # Recommandations
    print("\n" + "=" * 70)
    print("🎯 Guide Recommendations (Priority Order)")
    print("=" * 70)

    high_priority = [c for c in all_categories if not c['has_guide'] and c['tools'] >= 10]
    medium_priority = [c for c in all_categories if not c['has_guide'] and 5 <= c['tools'] < 10]
    low_priority = [c for c in all_categories if not c['has_guide'] and c['tools'] < 5]

    if high_priority:
        print("\n🔥 HIGH PRIORITY (10+ tools):")
        for cat in high_priority:
            print(f"   • {cat['name']:20s}: {cat['tools']} tools")

    if medium_priority:
        print("\n⭐ MEDIUM PRIORITY (5-9 tools):")
        for cat in medium_priority:
            print(f"   • {cat['name']:20s}: {cat['tools']} tools")

    if low_priority:
        print("\n💡 LOW PRIORITY (<5 tools):")
        for cat in low_priority:
            print(f"   • {cat['name']:20s}: {cat['tools']} tools")

    # Statistiques
    existing_guides = sum(1 for c in all_categories if c['has_guide'])
    total_guides_content = sum(len(CATEGORY_GUIDES[c['name']]['guides'])
                               for c in all_categories if c['has_guide'])

    print("\n" + "=" * 70)
    print("📈 Summary")
    print("=" * 70)
    print(f"Current guides: {existing_guides}/23 categories ({existing_guides/23*100:.1f}%)")
    print(f"Total guide pages: {total_guides_content}")
    print(f"Potential new guides: {23 - existing_guides} categories")
    print(f"Estimated new guide pages: {(23 - existing_guides) * 2} (assuming 2 guides/category)")
    print("=" * 70)

def main():
    generate_guide_recommendations()

    print("\n📝 Guide content is ready for implementation!")
    print("   Run the implementation script to create guide pages.")

if __name__ == "__main__":
    main()
