#!/usr/bin/env python3
"""
Ajoute des AI du monde entier avec structure simplifiée (pas de full review)
"""

from pathlib import Path
import re

# Données des AI supplémentaires par catégorie (structure simple)
SIMPLE_AI_DATA = {
    'ai-chatbots': [
        {
            'name': 'Gemini', 'company': 'Google', 'country': '🇺🇸',
            'description': 'Google\'s multimodal AI assistant with real-time search integration, image generation, and deep Google Workspace integration.',
            'tags': ['Multimodal', 'Real-time Search', 'Google Integration', 'Free Tier']
        },
        {
            'name': 'Microsoft Copilot', 'company': 'Microsoft', 'country': '🇺🇸',
            'description': 'AI assistant integrated across Windows, Edge, Office 365. Powered by GPT-4 with DALL-E 3 image generation.',
            'tags': ['GPT-4', 'DALL-E 3', 'Office Integration', 'Free']
        },
        {
            'name': 'Perplexity AI', 'company': 'Perplexity', 'country': '🇺🇸',
            'description': 'AI search engine combining GPT-4 and web search for accurate, cited answers with real-time information.',
            'tags': ['Real-time Search', 'Citations', 'Research', 'Free Tier']
        },
        {
            'name': 'Poe', 'company': 'Quora', 'country': '🇺🇸',
            'description': 'Multi-model platform accessing ChatGPT, Claude, Gemini, and more models in one interface.',
            'tags': ['Multi-Model', 'GPT-4', 'Claude', 'Free Access']
        },
        {
            'name': 'Character.AI', 'company': 'Character Technologies', 'country': '🇺🇸',
            'description': 'Create and chat with custom AI characters. Popular for role-play, learning, and entertainment.',
            'tags': ['Character Creation', 'Role-play', 'Free', 'Community']
        },
        {
            'name': 'Pi', 'company': 'Inflection AI', 'country': '🇺🇸',
            'description': 'Personal AI assistant focused on supportive, conversational interaction. Empathetic and personable.',
            'tags': ['Personal AI', 'Empathetic', 'Voice Chat', 'Free']
        },
        {
            'name': 'HuggingChat', 'company': 'Hugging Face', 'country': '🇺🇸',
            'description': 'Open-source ChatGPT alternative. Multiple open models including Llama 2, Mistral, and more.',
            'tags': ['Open Source', 'Multiple Models', 'Free', 'Privacy-focused']
        },
        {
            'name': 'YouChat', 'company': 'You.com', 'country': '🇺🇸',
            'description': 'AI chat integrated with web search. Real-time answers with source citations and multimodal capabilities.',
            'tags': ['Search Integration', 'Citations', 'Multimodal', 'Free']
        },
        {
            'name': 'Mistral Chat', 'company': 'Mistral AI', 'country': '🇫🇷',
            'description': 'European AI chatbot with strong performance. Focus on privacy and European values.',
            'tags': ['European', 'Privacy', 'Open Source', 'Multilingual']
        },
        {
            'name': 'DeepSeek', 'company': 'DeepSeek AI', 'country': '🇨🇳',
            'description': 'Chinese AI with strong coding and reasoning capabilities. Competitive with GPT-4.',
            'tags': ['Coding', 'Reasoning', 'Multilingual', 'Free Tier']
        },
        {
            'name': 'Grok', 'company': 'xAI', 'country': '🇺🇸',
            'description': 'Elon Musk\'s AI with real-time X (Twitter) integration and rebellious personality.',
            'tags': ['Real-time X Data', 'Humor', 'Uncensored', 'X Premium']
        },
        {
            'name': 'Cohere', 'company': 'Cohere', 'country': '🇨🇦',
            'description': 'Enterprise-focused AI for businesses. Strong RAG capabilities and multilingual support.',
            'tags': ['Enterprise', 'RAG', 'Multilingual', 'API']
        },
    ],

    'ai-writing': [
        {
            'name': 'Jasper', 'company': 'Jasper AI', 'country': '🇺🇸',
            'description': 'Leading AI writing platform for marketing content, blog posts, and social media. 50+ templates.',
            'tags': ['Marketing', 'SEO', 'Templates', 'Team Collaboration']
        },
        {
            'name': 'Copy.ai', 'company': 'Copy.ai', 'country': '🇺🇸',
            'description': 'AI copywriting tool for ads, emails, and social media. Over 90 templates and workflows.',
            'tags': ['Copywriting', 'Templates', 'Workflows', 'Free Trial']
        },
        {
            'name': 'Writesonic', 'company': 'Writesonic', 'country': '🇺🇸',
            'description': 'All-in-one AI writing platform with article writer, Chatsonic chatbot, and image generation.',
            'tags': ['Article Writer', 'Chatbot', 'SEO', 'Images']
        },
        {
            'name': 'Rytr', 'company': 'Rytr', 'country': '🇺🇸',
            'description': 'Affordable AI writing assistant. 40+ use cases and 30+ languages. Great for small businesses.',
            'tags': ['Affordable', '40+ Templates', '30+ Languages', 'Free Plan']
        },
        {
            'name': 'Grammarly', 'company': 'Grammarly', 'country': '🇺🇸',
            'description': 'AI writing assistant focused on grammar, clarity, and tone. Now with generative AI features.',
            'tags': ['Grammar Check', 'Clarity', 'Tone Detection', 'Browser Extension']
        },
        {
            'name': 'QuillBot', 'company': 'QuillBot', 'country': '🇺🇸',
            'description': 'AI paraphrasing tool with grammar checker, summarizer, and citation generator.',
            'tags': ['Paraphrasing', 'Summarizer', 'Grammar', 'Free']
        },
        {
            'name': 'Wordtune', 'company': 'AI21 Labs', 'country': '🇮🇱',
            'description': 'AI writing companion for rewriting and rephrasing. Makes writing clearer and more engaging.',
            'tags': ['Rewriting', 'Tone Adjustment', 'Chrome Extension', 'Free Tier']
        },
        {
            'name': 'Sudowrite', 'company': 'Sudowrite', 'country': '🇺🇸',
            'description': 'AI writing tool specifically for fiction authors. Story generation and creative assistance.',
            'tags': ['Fiction Writing', 'Story Generation', 'Character Development', 'Creative']
        },
        {
            'name': 'ProWritingAid', 'company': 'Orpheus Technology', 'country': '🇬🇧',
            'description': 'Comprehensive writing assistant for authors. Deep editing reports and style suggestions.',
            'tags': ['Editing', 'Style Analysis', 'Author Tools', 'Reports']
        },
        {
            'name': 'Notion AI', 'company': 'Notion', 'country': '🇺🇸',
            'description': 'AI writing assistant integrated into Notion workspace. Summarize, write, and brainstorm.',
            'tags': ['Workspace Integration', 'Summarization', 'Brainstorming', 'Free Trial']
        },
        {
            'name': 'Scalenut', 'company': 'Scalenut', 'country': '🇮🇳',
            'description': 'AI-powered SEO and content marketing platform. Keyword research and content optimization.',
            'tags': ['SEO', 'Content Marketing', 'Keyword Research', 'AI Writer']
        },
        {
            'name': 'Frase', 'company': 'Frase', 'country': '🇺🇸',
            'description': 'SEO content optimization tool with AI writing. Research, outline, and write SEO content.',
            'tags': ['SEO', 'Content Briefs', 'Research', 'Optimization']
        },
    ],

    'ai-coding': [
        {
            'name': 'GitHub Copilot', 'company': 'GitHub/Microsoft', 'country': '🇺🇸',
            'description': 'AI pair programmer powered by GPT-4. Autocomplete, chat, and code generation in your IDE.',
            'tags': ['GPT-4', 'IDE Integration', 'Autocomplete', 'Chat']
        },
        {
            'name': 'Cursor', 'company': 'Anysphere', 'country': '🇺🇸',
            'description': 'AI-first code editor built on VS Code. Natural language editing and codebase understanding.',
            'tags': ['AI Editor', 'Natural Language', 'VS Code', 'Codebase Chat']
        },
        {
            'name': 'Tabnine', 'company': 'Tabnine', 'country': '🇮🇱',
            'description': 'AI code completion trained on your codebase. Privacy-focused with on-premise option.',
            'tags': ['Autocomplete', 'Privacy', 'On-premise', 'Team Training']
        },
        {
            'name': 'Codeium', 'company': 'Exafunction', 'country': '🇺🇸',
            'description': 'Free GitHub Copilot alternative. Autocomplete, chat, and search across 70+ languages.',
            'tags': ['Free', '70+ Languages', 'Chat', 'Search']
        },
        {
            'name': 'Amazon CodeWhisperer', 'company': 'Amazon', 'country': '🇺🇸',
            'description': 'AI coding companion optimized for AWS. Code generation with security scanning.',
            'tags': ['AWS Optimized', 'Security Scan', 'Free for Individual', 'Python/Java']
        },
        {
            'name': 'Replit AI', 'company': 'Replit', 'country': '🇺🇸',
            'description': 'AI coding assistant in browser-based IDE. Generate, complete, and debug code online.',
            'tags': ['Browser IDE', 'Code Generation', 'Debugging', 'Collaboration']
        },
        {
            'name': 'Sourcegraph Cody', 'company': 'Sourcegraph', 'country': '🇺🇸',
            'description': 'AI assistant that understands your entire codebase. Context-aware code completion and chat.',
            'tags': ['Codebase Context', 'Code Search', 'Chat', 'Enterprise']
        },
        {
            'name': 'AskCodi', 'company': 'AskCodi', 'country': '🇺🇸',
            'description': 'AI coding assistant supporting multiple languages and frameworks. Docstring generation.',
            'tags': ['Multi-language', 'Docstrings', 'Test Generation', 'Free Tier']
        },
        {
            'name': 'Blackbox AI', 'company': 'Blackbox', 'country': '🇺🇸',
            'description': 'AI code search and generation. Extract code from videos and images.',
            'tags': ['Code Search', 'Image to Code', 'Chrome Extension', 'Free']
        },
        {
            'name': 'Phind', 'company': 'Phind', 'country': '🇺🇸',
            'description': 'AI search engine for developers. Get code answers with sources and explanations.',
            'tags': ['Developer Search', 'Code Answers', 'Real-time', 'Free']
        },
        {
            'name': 'Bito AI', 'company': 'Bito', 'country': '🇺🇸',
            'description': 'AI assistant for code review, documentation, and test generation. CLI and IDE support.',
            'tags': ['Code Review', 'Documentation', 'Tests', 'CLI']
        },
        {
            'name': 'AlphaCode', 'company': 'DeepMind', 'country': '🇬🇧',
            'description': 'Competitive programming AI. Solved problems at the level of average competitive programmer.',
            'tags': ['Competitive Programming', 'Research', 'Problem Solving', 'DeepMind']
        },
    ],

    'ai-image': [
        {
            'name': 'Midjourney', 'company': 'Midjourney', 'country': '🇺🇸',
            'description': 'Leading AI art generator. Photorealistic images with artistic style. Discord-based interface.',
            'tags': ['Photorealistic', 'Artistic', 'Discord', 'V6 Model']
        },
        {
            'name': 'DALL-E 3', 'company': 'OpenAI', 'country': '🇺🇸',
            'description': 'Advanced text-to-image AI with excellent text rendering and prompt following.',
            'tags': ['Text Accuracy', 'ChatGPT Integration', 'Safe', 'Creative']
        },
        {
            'name': 'Stable Diffusion', 'company': 'Stability AI', 'country': '🇬🇧',
            'description': 'Open-source image generation. Run locally or online. Customizable with LoRAs and ControlNet.',
            'tags': ['Open Source', 'Local', 'Customizable', 'Free']
        },
        {
            'name': 'Leonardo.ai', 'company': 'Leonardo', 'country': '🇦🇺',
            'description': 'AI art platform for game assets, concept art, and creative projects. Consistent characters.',
            'tags': ['Game Assets', 'Concept Art', 'Consistent Characters', 'Free Tier']
        },
        {
            'name': 'Ideogram', 'company': 'Ideogram', 'country': '🇺🇸',
            'description': 'AI image generator excelling at typography. Perfect text rendering in images.',
            'tags': ['Typography', 'Text in Images', 'Free', 'High Quality']
        },
        {
            'name': 'Adobe Firefly', 'company': 'Adobe', 'country': '🇺🇸',
            'description': 'Commercial-safe AI art generator. Trained only on licensed content. Adobe Creative Cloud integration.',
            'tags': ['Commercial Safe', 'Adobe Integration', 'Licensed Training', 'Generative Fill']
        },
        {
            'name': 'Canva AI', 'company': 'Canva', 'country': '🇦🇺',
            'description': 'AI image generation integrated into Canva design platform. Templates and Magic Edit.',
            'tags': ['Design Integration', 'Templates', 'Magic Edit', 'Easy to Use']
        },
        {
            'name': 'Runway ML', 'company': 'Runway', 'country': '🇺🇸',
            'description': 'Creative suite with AI image and video generation. Professional tools for creators.',
            'tags': ['Image & Video', 'Professional', 'Magic Tools', 'Gen-2']
        },
        {
            'name': 'DreamStudio', 'company': 'Stability AI', 'country': '🇬🇧',
            'description': 'Official Stable Diffusion interface. Advanced controls and SDXL model.',
            'tags': ['Stable Diffusion', 'SDXL', 'Advanced Controls', 'Credits']
        },
        {
            'name': 'Playground AI', 'company': 'Playground', 'country': '🇺🇸',
            'description': 'Free AI art generator with generous limits. Multiple models and canvas editing.',
            'tags': ['Generous Free Tier', 'Multiple Models', 'Canvas', 'Easy']
        },
        {
            'name': 'NightCafe', 'company': 'NightCafe', 'country': '🇦🇺',
            'description': 'AI art community platform. Multiple algorithms including Stable Diffusion and DALL-E.',
            'tags': ['Community', 'Multiple Algorithms', 'Daily Free Credits', 'Print Shop']
        },
        {
            'name': 'Artbreeder', 'company': 'Artbreeder', 'country': '🇺🇸',
            'description': 'Create images by mixing and evolving. Genetic algorithm approach to image generation.',
            'tags': ['Mixing Images', 'Evolution', 'Portraits', 'Collaborative']
        },
    ],

    'ai-video': [
        {
            'name': 'Runway Gen-2', 'company': 'Runway', 'country': '🇺🇸',
            'description': 'Leading text-to-video AI. Generate videos from text or images with motion controls.',
            'tags': ['Text-to-Video', 'Motion Brush', '4K', 'Professional']
        },
        {
            'name': 'Pika Labs', 'company': 'Pika', 'country': '🇺🇸',
            'description': 'AI video generation platform. Create and edit videos with natural language.',
            'tags': ['Video Generation', 'Editing', 'Effects', 'Community']
        },
        {
            'name': 'Synthesia', 'company': 'Synthesia', 'country': '🇬🇧',
            'description': 'AI avatar video platform. Create professional videos with AI presenters in 120+ languages.',
            'tags': ['AI Avatars', '120+ Languages', 'Professional', 'Enterprise']
        },
        {
            'name': 'HeyGen', 'company': 'HeyGen', 'country': '🇺🇸',
            'description': 'AI video platform with avatar creation and translation. Dub videos into multiple languages.',
            'tags': ['AI Avatars', 'Translation', 'Dubbing', 'Custom Avatars']
        },
        {
            'name': 'D-ID', 'company': 'D-ID', 'country': '🇮🇱',
            'description': 'Talking avatar videos from still images. Animate photos with AI voices.',
            'tags': ['Talking Photos', 'AI Voices', 'Real-time', 'API']
        },
        {
            'name': 'Descript', 'company': 'Descript', 'country': '🇺🇸',
            'description': 'All-in-one video editor with AI features. Edit video by editing text transcript.',
            'tags': ['Text-based Editing', 'Overdub', 'Studio Sound', 'Screen Recording']
        },
        {
            'name': 'Pictory', 'company': 'Pictory', 'country': '🇺🇸',
            'description': 'Transform text and blog posts into videos. Auto-captions and highlights.',
            'tags': ['Text to Video', 'Blog to Video', 'Auto-captions', 'Highlights']
        },
        {
            'name': 'InVideo AI', 'company': 'InVideo', 'country': '🇮🇳',
            'description': 'AI video creation from text prompts. Marketing and social media videos.',
            'tags': ['Text to Video', 'Marketing', 'Templates', 'Voiceover']
        },
        {
            'name': 'Fliki', 'company': 'Fliki', 'country': '🇮🇳',
            'description': 'Transform text into videos with AI voices. Support for 75+ languages.',
            'tags': ['Text to Video', 'AI Voices', '75+ Languages', 'Free Tier']
        },
        {
            'name': 'Lumen5', 'company': 'Lumen5', 'country': '🇨🇦',
            'description': 'Social media video creation. Transform blog posts into engaging videos.',
            'tags': ['Social Media', 'Blog to Video', 'Templates', 'Branded']
        },
        {
            'name': 'OpusClip', 'company': 'Opus', 'country': '🇺🇸',
            'description': 'AI video clipper for viral short content. Extract best moments from long videos.',
            'tags': ['Short Clips', 'Viral Content', 'Auto-captions', 'Scheduling']
        },
        {
            'name': 'CapCut', 'company': 'ByteDance', 'country': '🇨🇳',
            'description': 'Free video editor with AI features. Auto-captions, effects, and templates.',
            'tags': ['Free', 'Mobile & Desktop', 'AI Effects', 'TikTok Integration']
        },
    ],

    'ai-audio': [
        {
            'name': 'ElevenLabs', 'company': 'ElevenLabs', 'country': '🇺🇸',
            'description': 'Leading AI voice cloning and text-to-speech. Ultra-realistic voices in 29 languages.',
            'tags': ['Voice Cloning', '29 Languages', 'Ultra-realistic', 'API']
        },
        {
            'name': 'Murf AI', 'company': 'Murf', 'country': '🇺🇸',
            'description': 'Professional AI voiceover platform. 120+ voices for videos, podcasts, and presentations.',
            'tags': ['Voiceovers', '120+ Voices', 'Professional', 'Studio']
        },
        {
            'name': 'Play.ht', 'company': 'Play.ht', 'country': '🇺🇸',
            'description': 'Advanced text-to-speech with voice cloning. Ultra-realistic AI voices.',
            'tags': ['TTS', 'Voice Cloning', 'API', 'Wordpress Plugin']
        },
        {
            'name': 'Speechify', 'company': 'Speechify', 'country': '🇺🇸',
            'description': 'Text-to-speech reading app. Listen to documents, articles, and PDFs.',
            'tags': ['Reading Assistant', 'Mobile App', 'Chrome Extension', 'Natural Voices']
        },
        {
            'name': 'Descript Overdub', 'company': 'Descript', 'country': '🇺🇸',
            'description': 'Create ultra-realistic voice clone. Edit audio by editing text.',
            'tags': ['Voice Clone', 'Text-based Editing', 'Podcasts', 'Studio Sound']
        },
        {
            'name': 'Resemble AI', 'company': 'Resemble', 'country': '🇨🇦',
            'description': 'Real-time voice cloning and speech synthesis. Emotional control and localization.',
            'tags': ['Real-time', 'Emotion Control', 'Localization', 'API']
        },
        {
            'name': 'WellSaid Labs', 'company': 'WellSaid', 'country': '🇺🇸',
            'description': 'Enterprise text-to-speech platform. Studio-quality AI voices.',
            'tags': ['Enterprise', 'Studio Quality', 'Voice Avatars', 'Team Collaboration']
        },
        {
            'name': 'LOVO', 'company': 'LOVO AI', 'country': '🇺🇸',
            'description': 'AI voice generator and text-to-speech. 500+ voices in 100 languages.',
            'tags': ['500+ Voices', '100 Languages', 'Video Editing', 'Affordable']
        },
        {
            'name': 'Krisp', 'company': 'Krisp', 'country': '🇦🇲',
            'description': 'AI noise cancellation for calls and recordings. Remove background noise in real-time.',
            'tags': ['Noise Cancellation', 'Real-time', 'Meetings', 'Recording']
        },
        {
            'name': 'Otter.ai', 'company': 'Otter.ai', 'country': '🇺🇸',
            'description': 'AI meeting transcription and notes. Real-time transcription with speaker identification.',
            'tags': ['Transcription', 'Meeting Notes', 'Real-time', 'Collaboration']
        },
        {
            'name': 'AssemblyAI', 'company': 'AssemblyAI', 'country': '🇺🇸',
            'description': 'Speech-to-text API with advanced features. Sentiment analysis and topic detection.',
            'tags': ['Speech-to-text', 'API', 'Sentiment Analysis', 'Developer-friendly']
        },
        {
            'name': 'Suno AI', 'company': 'Suno', 'country': '🇺🇸',
            'description': 'AI music generation from text. Create complete songs with lyrics and music.',
            'tags': ['Music Generation', 'Lyrics', 'Text to Music', 'Creative']
        },
    ],

    'ai-productivity': [
        {
            'name': 'Notion AI', 'company': 'Notion', 'country': '🇺🇸',
            'description': 'AI assistant integrated into Notion workspace. Write, summarize, and brainstorm.',
            'tags': ['Workspace', 'Writing', 'Summarization', 'Brainstorming']
        },
        {
            'name': 'Motion', 'company': 'Motion', 'country': '🇺🇸',
            'description': 'AI calendar and project manager. Automatically schedules your tasks and meetings.',
            'tags': ['Calendar AI', 'Task Management', 'Auto-scheduling', 'Focus Time']
        },
        {
            'name': 'Reclaim AI', 'company': 'Reclaim', 'country': '🇺🇸',
            'description': 'Smart calendar assistant. Defends time for priorities, habits, and meetings.',
            'tags': ['Calendar Defense', 'Habits', 'Buffer Time', 'Google Calendar']
        },
        {
            'name': 'ClickUp AI', 'company': 'ClickUp', 'country': '🇺🇸',
            'description': 'AI features in project management platform. Generate tasks, summaries, and updates.',
            'tags': ['Project Management', 'Task Generation', 'Summaries', 'Automation']
        },
        {
            'name': 'Mem', 'company': 'Mem', 'country': '🇺🇸',
            'description': 'AI-powered note-taking. Self-organizing notes with smart search and connections.',
            'tags': ['Note-taking', 'Self-organizing', 'Smart Search', 'Knowledge Graph']
        },
        {
            'name': 'Fireflies.ai', 'company': 'Fireflies', 'country': '🇺🇸',
            'description': 'AI meeting assistant. Record, transcribe, and analyze meetings automatically.',
            'tags': ['Meeting Recorder', 'Transcription', 'Analysis', 'CRM Integration']
        },
        {
            'name': 'Tactiq', 'company': 'Tactiq', 'country': '🇦🇺',
            'description': 'Real-time meeting transcription for Google Meet, Zoom, and Teams. Speaker-identified.',
            'tags': ['Meeting Transcription', 'Chrome Extension', 'Speaker ID', 'Free']
        },
        {
            'name': 'Clockwise', 'company': 'Clockwise', 'country': '🇺🇸',
            'description': 'AI calendar optimizer. Creates focus time and flexible meetings.',
            'tags': ['Calendar Optimization', 'Focus Time', 'Team Scheduling', 'Analytics']
        },
        {
            'name': 'Sunsama', 'company': 'Sunsama', 'country': '🇺🇸',
            'description': 'Daily planner with AI features. Guided planning and time-boxing.',
            'tags': ['Daily Planning', 'Time-boxing', 'Calendar Integration', 'Mindful']
        },
        {
            'name': 'Taskade', 'company': 'Taskade', 'country': '🇺🇸',
            'description': 'AI-powered team workspace. Task lists, mind maps, and video chat in one.',
            'tags': ['Team Workspace', 'Mind Maps', 'AI Assistant', 'Real-time']
        },
        {
            'name': 'Superhuman', 'company': 'Superhuman', 'country': '🇺🇸',
            'description': 'AI-powered email client. Blazingly fast with AI writing and triage.',
            'tags': ['Email Client', 'AI Writing', 'Triage', 'Keyboard Shortcuts']
        },
        {
            'name': 'SaneBox', 'company': 'SaneBox', 'country': '🇺🇸',
            'description': 'AI email management. Automatically filters unimportant emails.',
            'tags': ['Email Filtering', 'Unsubscribe', 'Follow-up', 'Any Email Client']
        },
    ],

    'ai-seo': [
        {
            'name': 'Surfer SEO', 'company': 'Surfer', 'country': '🇵🇱',
            'description': 'Content optimization platform. Write and optimize SEO content with AI assistance.',
            'tags': ['Content Optimization', 'SERP Analysis', 'AI Writer', 'Audit']
        },
        {
            'name': 'Clearscope', 'company': 'Clearscope', 'country': '🇺🇸',
            'description': 'Content optimization tool. Data-driven SEO recommendations and grading.',
            'tags': ['Content Grading', 'Keyword Research', 'Google Docs', 'Competitor Analysis']
        },
        {
            'name': 'MarketMuse', 'company': 'MarketMuse', 'country': '🇺🇸',
            'description': 'AI content planning and optimization. Topic modeling and content briefs.',
            'tags': ['Content Strategy', 'Topic Modeling', 'Content Briefs', 'Enterprise']
        },
        {
            'name': 'Frase', 'company': 'Frase', 'country': '🇺🇸',
            'description': 'SEO content optimization with AI writing. Research competitors and create briefs.',
            'tags': ['SEO Writing', 'Content Briefs', 'Research', 'Optimization']
        },
        {
            'name': 'Scalenut', 'company': 'Scalenut', 'country': '🇮🇳',
            'description': 'AI SEO and content marketing platform. Keyword clustering and content planning.',
            'tags': ['SEO Platform', 'Keyword Clustering', 'AI Writer', 'Content Planning']
        },
        {
            'name': 'NeuronWriter', 'company': 'NeuronWriter', 'country': '🇵🇱',
            'description': 'Semantic SEO tool with AI writing. NLP-based content optimization.',
            'tags': ['Semantic SEO', 'NLP', 'Content Optimization', 'Affordable']
        },
        {
            'name': 'LongShot AI', 'company': 'LongShot', 'country': '🇮🇳',
            'description': 'Fact-checked AI content generator. Real-time fact verification and SEO.',
            'tags': ['Fact-checking', 'SEO Content', 'Research', 'Semantic SEO']
        },
        {
            'name': 'GrowthBar', 'company': 'GrowthBar', 'country': '🇺🇸',
            'description': 'SEO Chrome extension with AI writing. Keyword research and competitor analysis.',
            'tags': ['Chrome Extension', 'Keyword Research', 'AI Writing', 'Quick']
        },
        {
            'name': 'INK', 'company': 'INK', 'country': '🇺🇸',
            'description': 'AI SEO assistant and content writer. Real-time optimization and protection.',
            'tags': ['SEO Assistant', 'Content Protection', 'Real-time', 'AI Writer']
        },
        {
            'name': 'SEO.ai', 'company': 'SEO.ai', 'country': '🇺🇸',
            'description': 'AI SEO content automation. Keyword research to publishing automation.',
            'tags': ['Automation', 'Keyword Research', 'Content Generation', 'Publishing']
        },
        {
            'name': 'RankIQ', 'company': 'RankIQ', 'country': '🇺🇸',
            'description': 'SEO toolset for bloggers. AI-powered content briefs and optimization.',
            'tags': ['Blogging', 'Content Briefs', 'Keyword Library', 'Simple']
        },
        {
            'name': 'WordLift', 'company': 'WordLift', 'country': '🇮🇹',
            'description': 'Semantic SEO and knowledge graph. Structure data for better search visibility.',
            'tags': ['Semantic SEO', 'Knowledge Graph', 'Schema Markup', 'WordPress']
        },
    ],

    'ai-business': [
        {
            'name': 'Salesforce Einstein', 'company': 'Salesforce', 'country': '🇺🇸',
            'description': 'AI for CRM. Predictive analytics, lead scoring, and automated insights.',
            'tags': ['CRM AI', 'Predictive Analytics', 'Lead Scoring', 'Enterprise']
        },
        {
            'name': 'HubSpot AI', 'company': 'HubSpot', 'country': '🇺🇸',
            'description': 'AI-powered marketing, sales, and service platform. Content generation and automation.',
            'tags': ['Marketing Automation', 'CRM', 'Content AI', 'Sales']
        },
        {
            'name': 'Zoho Zia', 'company': 'Zoho', 'country': '🇮🇳',
            'description': 'AI assistant for Zoho suite. Predictions, recommendations, and automation.',
            'tags': ['Business Suite', 'Predictions', 'Automation', 'Affordable']
        },
        {
            'name': 'IBM Watson', 'company': 'IBM', 'country': '🇺🇸',
            'description': 'Enterprise AI platform. NLP, machine learning, and data analysis.',
            'tags': ['Enterprise AI', 'NLP', 'Machine Learning', 'Cloud']
        },
        {
            'name': 'Tableau AI', 'company': 'Salesforce', 'country': '🇺🇸',
            'description': 'AI-powered data visualization and analytics. Natural language queries.',
            'tags': ['Data Viz', 'Analytics', 'Natural Language', 'BI']
        },
        {
            'name': 'Power BI AI', 'company': 'Microsoft', 'country': '🇺🇸',
            'description': 'Business intelligence with AI insights. Automated analytics and visualizations.',
            'tags': ['Business Intelligence', 'AI Insights', 'Microsoft', 'Analytics']
        },
        {
            'name': 'DataRobot', 'company': 'DataRobot', 'country': '🇺🇸',
            'description': 'Automated machine learning platform. Build and deploy AI models.',
            'tags': ['AutoML', 'Model Building', 'Deployment', 'Enterprise']
        },
        {
            'name': 'H2O.ai', 'company': 'H2O.ai', 'country': '🇺🇸',
            'description': 'Open-source AI and machine learning platform. AutoML and model deployment.',
            'tags': ['Open Source', 'AutoML', 'ML Platform', 'Scalable']
        },
        {
            'name': 'UiPath', 'company': 'UiPath', 'country': '🇺🇸',
            'description': 'Robotic process automation with AI. Automate repetitive business tasks.',
            'tags': ['RPA', 'Automation', 'Document AI', 'Enterprise']
        },
        {
            'name': 'ThoughtSpot', 'company': 'ThoughtSpot', 'country': '🇺🇸',
            'description': 'AI-powered analytics. Search and AI-driven insights from business data.',
            'tags': ['Search Analytics', 'AI Insights', 'BI', 'Natural Language']
        },
        {
            'name': 'Workday AI', 'company': 'Workday', 'country': '🇺🇸',
            'description': 'AI for HR and finance. Intelligent automation and insights.',
            'tags': ['HR', 'Finance', 'Automation', 'Enterprise']
        },
        {
            'name': 'ServiceNow AI', 'company': 'ServiceNow', 'country': '🇺🇸',
            'description': 'AI-powered IT service management. Automated workflows and intelligent routing.',
            'tags': ['ITSM', 'Workflow Automation', 'Virtual Agent', 'Enterprise']
        },
    ],

    'ai-networking': [
        {
            'name': 'Cisco DNA Center', 'company': 'Cisco', 'country': '🇺🇸',
            'description': 'AI-powered network automation and assurance. Intent-based networking.',
            'tags': ['Network Automation', 'Intent-based', 'Assurance', 'Enterprise']
        },
        {
            'name': 'Juniper Mist AI', 'company': 'Juniper', 'country': '🇺🇸',
            'description': 'AI-driven wireless network optimization. Predictive troubleshooting.',
            'tags': ['Wireless AI', 'Predictive', 'AIOps', 'Cloud']
        },
        {
            'name': 'Aruba AI', 'company': 'HPE', 'country': '🇺🇸',
            'description': 'AI-powered network operations. Automated troubleshooting and optimization.',
            'tags': ['AIOps', 'Wireless', 'Automation', 'Analytics']
        },
        {
            'name': 'Fortinet FortiAI', 'company': 'Fortinet', 'country': '🇺🇸',
            'description': 'AI for network security and SD-WAN. Threat detection and prevention.',
            'tags': ['Security AI', 'SD-WAN', 'Threat Detection', 'FortiGate']
        },
        {
            'name': 'Dynatrace', 'company': 'Dynatrace', 'country': '🇺🇸',
            'description': 'AI-powered observability platform. Automated root cause analysis.',
            'tags': ['Observability', 'APM', 'Root Cause', 'Davis AI']
        },
        {
            'name': 'Datadog', 'company': 'Datadog', 'country': '🇺🇸',
            'description': 'Monitoring and analytics platform with AI. Anomaly detection and forecasting.',
            'tags': ['Monitoring', 'APM', 'Anomaly Detection', 'Cloud']
        },
        {
            'name': 'Splunk', 'company': 'Splunk', 'country': '🇺🇸',
            'description': 'Data analytics platform for IT operations. AI-powered insights and alerts.',
            'tags': ['SIEM', 'IT Ops', 'Analytics', 'Machine Learning']
        },
        {
            'name': 'New Relic AI', 'company': 'New Relic', 'country': '🇺🇸',
            'description': 'Observability platform with AI assistant. Automated analysis and recommendations.',
            'tags': ['Observability', 'APM', 'AI Assistant', 'Cloud']
        },
        {
            'name': 'ThousandEyes', 'company': 'Cisco', 'country': '🇺🇸',
            'description': 'Network intelligence platform. AI-powered visibility and troubleshooting.',
            'tags': ['Network Intelligence', 'Visibility', 'Cloud', 'Internet Insights']
        },
        {
            'name': 'NetBrain', 'company': 'NetBrain', 'country': '🇺🇸',
            'description': 'Network automation platform. Dynamic mapping and AI diagnostics.',
            'tags': ['Automation', 'Network Mapping', 'Diagnostics', 'Runbooks']
        },
        {
            'name': 'SolarWinds AI', 'company': 'SolarWinds', 'country': '🇺🇸',
            'description': 'Network management with AI insights. Performance monitoring and optimization.',
            'tags': ['Network Management', 'Monitoring', 'Performance', 'Alerts']
        },
        {
            'name': 'Auvik', 'company': 'Auvik', 'country': '🇨🇦',
            'description': 'Cloud-based network management. Automated discovery and mapping.',
            'tags': ['Cloud-based', 'Auto-discovery', 'Network Map', 'MSP']
        },
    ],

    'ai-cybersecurity': [
        {
            'name': 'CrowdStrike Falcon', 'company': 'CrowdStrike', 'country': '🇺🇸',
            'description': 'AI-powered endpoint protection. Real-time threat detection and response.',
            'tags': ['EDR', 'Threat Intelligence', 'Real-time', 'Cloud-native']
        },
        {
            'name': 'Darktrace', 'company': 'Darktrace', 'country': '🇬🇧',
            'description': 'Autonomous cyber AI. Self-learning threat detection and response.',
            'tags': ['Autonomous Response', 'Self-learning', 'Network AI', 'DETECT']
        },
        {
            'name': 'SentinelOne', 'company': 'SentinelOne', 'country': '🇺🇸',
            'description': 'AI-driven XDR platform. Automated threat hunting and response.',
            'tags': ['XDR', 'Automated Response', 'Threat Hunting', 'Cloud']
        },
        {
            'name': 'Palo Alto Cortex', 'company': 'Palo Alto Networks', 'country': '🇺🇸',
            'description': 'AI-powered security operations. XDR and SOAR automation.',
            'tags': ['XDR', 'SOAR', 'Threat Intel', 'Cloud Security']
        },
        {
            'name': 'Vectra AI', 'company': 'Vectra', 'country': '🇺🇸',
            'description': 'AI for threat detection and response. Network and cloud visibility.',
            'tags': ['NDR', 'Cloud Detection', 'AI Detection', 'Attack Signal']
        },
        {
            'name': 'Cybereason', 'company': 'Cybereason', 'country': '🇺🇸',
            'description': 'AI-driven endpoint protection. Malware defense and response.',
            'tags': ['EDR', 'Malware Defense', 'Threat Hunting', 'MalOp']
        },
        {
            'name': 'Cylance', 'company': 'BlackBerry', 'country': '🇨🇦',
            'description': 'AI prevention platform. Predictive threat prevention.',
            'tags': ['Prevention', 'Predictive AI', 'Endpoint', 'Zero-day']
        },
        {
            'name': 'Microsoft Defender AI', 'company': 'Microsoft', 'country': '🇺🇸',
            'description': 'Enterprise security with AI. XDR across endpoints, cloud, and identity.',
            'tags': ['XDR', 'Enterprise', 'Cloud Security', 'Integrated']
        },
        {
            'name': 'Splunk Enterprise Security', 'company': 'Splunk', 'country': '🇺🇸',
            'description': 'SIEM with AI analytics. Threat detection and investigation.',
            'tags': ['SIEM', 'Analytics', 'Threat Detection', 'UBA']
        },
        {
            'name': 'Abnormal Security', 'company': 'Abnormal Security', 'country': '🇺🇸',
            'description': 'AI email security. Behavioral AI for advanced email threats.',
            'tags': ['Email Security', 'Behavioral AI', 'Phishing', 'Cloud']
        },
        {
            'name': 'Recorded Future', 'company': 'Recorded Future', 'country': '🇺🇸',
            'description': 'Threat intelligence platform. Real-time threat intelligence with AI.',
            'tags': ['Threat Intel', 'Real-time', 'Risk Analysis', 'Integration']
        },
        {
            'name': 'ZeroFox', 'company': 'ZeroFox', 'country': '🇺🇸',
            'description': 'Digital risk protection. AI-powered social media and brand protection.',
            'tags': ['Digital Risk', 'Social Media', 'Brand Protection', 'Phishing']
        },
    ],

    'ai-medical': [
        {
            'name': 'IBM Watson Health', 'company': 'IBM', 'country': '🇺🇸',
            'description': 'AI for clinical decision support. Oncology, genomics, and drug discovery.',
            'tags': ['Clinical Decision', 'Oncology', 'Genomics', 'Enterprise']
        },
        {
            'name': 'PathAI', 'company': 'PathAI', 'country': '🇺🇸',
            'description': 'AI-powered pathology. Improve diagnosis accuracy with machine learning.',
            'tags': ['Pathology', 'Diagnosis', 'Accuracy', 'Research']
        },
        {
            'name': 'Zebra Medical Vision', 'company': 'Nanox', 'country': '🇮🇱',
            'description': 'AI for medical imaging. Automated detection of clinical findings.',
            'tags': ['Medical Imaging', 'Radiology', 'Detection', 'FDA-cleared']
        },
        {
            'name': 'Viz.ai', 'company': 'Viz.ai', 'country': '🇺🇸',
            'description': 'AI for stroke detection. Rapid triage and care coordination.',
            'tags': ['Stroke Detection', 'Triage', 'Care Coordination', 'FDA-cleared']
        },
        {
            'name': 'Tempus', 'company': 'Tempus', 'country': '🇺🇸',
            'description': 'Precision medicine platform. AI-driven cancer care and research.',
            'tags': ['Precision Medicine', 'Cancer', 'Genomics', 'Clinical Data']
        },
        {
            'name': 'Paige.AI', 'company': 'Paige', 'country': '🇺🇸',
            'description': 'Cancer detection AI. Computational pathology for oncology.',
            'tags': ['Cancer Detection', 'Pathology', 'FDA-approved', 'Oncology']
        },
        {
            'name': 'Aidoc', 'company': 'Aidoc', 'country': '🇮🇱',
            'description': 'AI radiology triage. Priority alerts for critical findings.',
            'tags': ['Radiology', 'Triage', 'Critical Findings', 'FDA-cleared']
        },
        {
            'name': 'HeartFlow', 'company': 'HeartFlow', 'country': '🇺🇸',
            'description': 'AI for cardiac analysis. Non-invasive coronary artery disease assessment.',
            'tags': ['Cardiac', 'Coronary Analysis', 'Non-invasive', 'FDA-cleared']
        },
        {
            'name': 'Qure.ai', 'company': 'Qure.ai', 'country': '🇮🇳',
            'description': 'AI medical imaging for emerging markets. Chest X-ray and CT analysis.',
            'tags': ['X-ray Analysis', 'CT Scan', 'Emerging Markets', 'TB Detection']
        },
        {
            'name': 'K Health', 'company': 'K Health', 'country': '🇺🇸',
            'description': 'AI symptom checker and virtual care. Primary care diagnosis assistance.',
            'tags': ['Symptom Checker', 'Virtual Care', 'Primary Care', 'Mobile']
        },
        {
            'name': 'Ada Health', 'company': 'Ada', 'country': '🇩🇪',
            'description': 'AI health assessment. Symptom analysis and medical guidance.',
            'tags': ['Symptom Assessment', 'Health Companion', 'Multilingual', 'Mobile']
        },
        {
            'name': 'Babylon Health', 'company': 'Babylon', 'country': '🇬🇧',
            'description': 'AI-powered healthcare platform. Virtual consultations and symptom checking.',
            'tags': ['Virtual Care', 'Symptom Checker', 'Triage', 'Mobile']
        },
    ],

    'ai-architecture': [
        {
            'name': 'Spacemaker', 'company': 'Autodesk', 'country': '🇳🇴',
            'description': 'AI for early-stage design. Optimize building layouts and site planning.',
            'tags': ['Site Planning', 'Design Optimization', 'Urban Design', 'Cloud']
        },
        {
            'name': 'TestFit', 'company': 'TestFit', 'country': '🇺🇸',
            'description': 'AI-powered site planning. Generate building configurations in real-time.',
            'tags': ['Site Planning', 'Real-time', 'Multi-family', 'Feasibility']
        },
        {
            'name': 'Finch3D', 'company': 'Finch', 'country': '🇩🇰',
            'description': 'AI for building optimization. Instant feedback on design decisions.',
            'tags': ['Building Optimization', 'Real-time Feedback', 'Grasshopper', 'Revit']
        },
        {
            'name': 'Hypar', 'company': 'Hypar', 'country': '🇺🇸',
            'description': 'Generative design platform. Automated space planning and design.',
            'tags': ['Generative Design', 'Space Planning', 'Cloud', 'API']
        },
        {
            'name': 'Autodesk Forma', 'company': 'Autodesk', 'country': '🇺🇸',
            'description': 'AI-driven early design software. Conceptual planning with environmental analysis.',
            'tags': ['Early Design', 'Environmental Analysis', 'Urban Planning', 'Cloud']
        },
        {
            'name': 'Archistar', 'company': 'Archistar', 'country': '🇦🇺',
            'description': 'AI-powered property development platform. Feasibility and design automation.',
            'tags': ['Property Development', 'Feasibility', 'Compliance', 'Cloud']
        },
        {
            'name': 'Augmenta', 'company': 'Augmenta', 'country': '🇫🇷',
            'description': 'AI for MEP automation. Automated building systems design.',
            'tags': ['MEP Automation', 'Building Systems', 'Revit Plugin', 'Time-saving']
        },
        {
            'name': 'Buildots', 'company': 'Buildots', 'country': '🇮🇱',
            'description': 'AI construction monitoring. Automated progress tracking with computer vision.',
            'tags': ['Construction Monitoring', 'Computer Vision', 'Progress Tracking', 'Analytics']
        },
        {
            'name': 'OpenSpace', 'company': 'OpenSpace', 'country': '🇺🇸',
            'description': 'AI-powered site documentation. 360° capture and progress tracking.',
            'tags': ['Site Documentation', '360° Capture', 'Progress Tracking', 'Mobile']
        },
        {
            'name': 'Doxel', 'company': 'Doxel', 'country': '🇺🇸',
            'description': 'AI for construction productivity. Automated progress monitoring and analytics.',
            'tags': ['Progress Monitoring', 'Productivity', 'Computer Vision', 'Analytics']
        },
        {
            'name': 'Reconstruct', 'company': 'Reconstruct', 'country': '🇺🇸',
            'description': 'AI construction analytics. Reality capture and project insights.',
            'tags': ['Construction Analytics', 'Reality Capture', 'BIM Compare', 'Cloud']
        },
        {
            'name': 'Join', 'company': 'Join', 'country': '🇦🇹',
            'description': 'AI for construction drawings. Automated detail and shop drawing generation.',
            'tags': ['Construction Drawings', 'Automation', 'Detailing', 'Timber']
        },
    ],
}

def generate_simple_tool_card(ai, category, use_anchor=False):
    """Génère une carte simplifiée sans full review."""
    tags_html = ''.join([f'<span class="feature-tag">{tag}</span>' for tag in ai['tags']])

    # Pour certaines catégories, utiliser <a> au lieu de <article>
    tag = 'a href="#"' if use_anchor else 'article'
    closing_tag = 'a' if use_anchor else 'article'

    return f'''
                <{tag} class="tool-card">
                    <div class="tool-logo">
                        <span style="font-size: 32px;">🤖</span>
                    </div>
                    <h3>{ai['name']}</h3>
                    <p class="tool-company">by {ai['company']} <span class="country-flag" style="margin-left: 8px; opacity: 0.8;">{ai['country']}</span></p>
                    <p class="tool-description">{ai['description']}</p>
                    <div class="tool-features-list" style="margin-top: var(--space-md);">
                        {tags_html}
                    </div>
                </{closing_tag}>'''

def add_simple_tools_to_category(file_path, category_key):
    """Ajoute les AI simplifiées à une catégorie."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        ai_list = SIMPLE_AI_DATA.get(category_key, [])
        if not ai_list:
            return False, 0

        # Trouver la fin de la section tools-grid (avant la fermeture </div>)
        # Deux structures possibles:
        # 1. <article> tags: </article>\n        </div>\n\n        <!-- Comparison Table -->
        # 2. <a> tags: </a>\n            </div>\n    </section>

        pattern1 = r'(</article>\n\s*)(</div>\n\n\s*<!-- Comparison Table -->)'
        pattern2 = r'(</article>\n\s*)(</div>)'
        pattern3 = r'(</a>\n\s*)(</div>\n\s*</section>)'

        # Essayer les patterns dans l'ordre
        match = re.search(pattern1, content, re.MULTILINE)
        use_anchor = False
        if not match:
            match = re.search(pattern2, content, re.MULTILINE)
        if not match:
            match = re.search(pattern3, content, re.MULTILINE)
            use_anchor = True  # Pattern 3 utilise <a> tags

        # Générer les cartes simplifiées
        simple_cards_html = ''
        for ai in ai_list:
            simple_cards_html += generate_simple_tool_card(ai, category_key, use_anchor)

        # Insérer avant la fermeture
        if match:
            # Insérer entre le groupe 1 (</article> ou </a>) et le groupe 2 (</div>)
            content = content[:match.end(1)] + simple_cards_html + '\n' + content[match.start(2):]
        else:
            print(f"   ⚠️  Pattern de fermeture non trouvé")
            return False, 0

        # Sauvegarder
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return True, len(ai_list)

    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        return False, 0

def main():
    """Ajoute les AI simplifiées dans toutes les catégories."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories')

    print("🌍 Ajout d'AI du monde entier (structure simplifiée)...\n")

    total_added = 0
    categories_updated = 0

    for category_key in SIMPLE_AI_DATA.keys():
        file_path = base_dir / f'{category_key}.html'

        if file_path.exists():
            print(f"📁 {category_key}")
            success, count = add_simple_tools_to_category(file_path, category_key)
            if success:
                total_added += count
                categories_updated += 1
                print(f"   ✅ {count} AI ajoutées (structure simple)\n")
            else:
                print(f"   ⚠️  Échec\n")
        else:
            print(f"❌ {category_key}.html - Fichier non trouvé\n")

    print(f"{'='*50}")
    print(f"🎉 Terminé!")
    print(f"📊 {categories_updated} catégories enrichies")
    print(f"🌍 {total_added} AI ajoutées (sans full review)")
    print(f"✨ Structure simple: Logo + Nom + Pays + Description + Tags")

if __name__ == '__main__':
    main()
