#!/usr/bin/env python3
"""
Ajoute 20 AI par catégorie avec logo et pays d'origine
"""

from pathlib import Path
import re

# Données complètes des AI par catégorie
AI_DATA = {
    'ai-chatbots': [
        {'name': 'ChatGPT', 'company': 'OpenAI', 'country': '🇺🇸 USA', 'logo': '💬'},
        {'name': 'Claude', 'company': 'Anthropic', 'country': '🇺🇸 USA', 'logo': '🧠'},
        {'name': 'Gemini', 'company': 'Google', 'country': '🇺🇸 USA', 'logo': '✨'},
        {'name': 'Copilot', 'company': 'Microsoft', 'country': '🇺🇸 USA', 'logo': '🤖'},
        {'name': 'Perplexity AI', 'company': 'Perplexity', 'country': '🇺🇸 USA', 'logo': '🔍'},
        {'name': 'Poe', 'company': 'Quora', 'country': '🇺🇸 USA', 'logo': '🎭'},
        {'name': 'Character.AI', 'company': 'Character.AI', 'country': '🇺🇸 USA', 'logo': '🎪'},
        {'name': 'Pi', 'company': 'Inflection AI', 'country': '🇺🇸 USA', 'logo': '💭'},
        {'name': 'HuggingChat', 'company': 'Hugging Face', 'country': '🇺🇸 USA', 'logo': '🤗'},
        {'name': 'YouChat', 'company': 'You.com', 'country': '🇺🇸 USA', 'logo': '🔎'},
        {'name': 'Jasper Chat', 'company': 'Jasper', 'country': '🇺🇸 USA', 'logo': '📝'},
        {'name': 'Chatsonic', 'company': 'Writesonic', 'country': '🇺🇸 USA', 'logo': '⚡'},
        {'name': 'Replika', 'company': 'Luka Inc', 'country': '🇺🇸 USA', 'logo': '👤'},
        {'name': 'ChatSpot', 'company': 'HubSpot', 'country': '🇺🇸 USA', 'logo': '🎯'},
        {'name': 'LLaMA Chat', 'company': 'Meta', 'country': '🇺🇸 USA', 'logo': '🦙'},
        {'name': 'Mistral Chat', 'company': 'Mistral AI', 'country': '🇫🇷 France', 'logo': '🌬️'},
        {'name': 'DeepSeek', 'company': 'DeepSeek', 'country': '🇨🇳 China', 'logo': '🐉'},
        {'name': 'Grok', 'company': 'xAI', 'country': '🇺🇸 USA', 'logo': '𝕏'},
        {'name': 'Cohere', 'company': 'Cohere', 'country': '🇨🇦 Canada', 'logo': '🔗'},
        {'name': 'Anthropic Claude', 'company': 'Anthropic', 'country': '🇺🇸 USA', 'logo': '🎨'},
    ],

    'ai-writing': [
        {'name': 'Jasper', 'company': 'Jasper AI', 'country': '🇺🇸 USA', 'logo': '✍️'},
        {'name': 'Copy.ai', 'company': 'Copy.ai', 'country': '🇺🇸 USA', 'logo': '📋'},
        {'name': 'Writesonic', 'company': 'Writesonic', 'country': '🇺🇸 USA', 'logo': '⚡'},
        {'name': 'Rytr', 'company': 'Rytr', 'country': '🇺🇸 USA', 'logo': '📝'},
        {'name': 'Grammarly', 'company': 'Grammarly', 'country': '🇺🇸 USA', 'logo': '✅'},
        {'name': 'QuillBot', 'company': 'QuillBot', 'country': '🇺🇸 USA', 'logo': '🪶'},
        {'name': 'Wordtune', 'company': 'AI21 Labs', 'country': '🇮🇱 Israel', 'logo': '🎵'},
        {'name': 'Sudowrite', 'company': 'Sudowrite', 'country': '🇺🇸 USA', 'logo': '📚'},
        {'name': 'ProWritingAid', 'company': 'Orpheus Technology', 'country': '🇬🇧 UK', 'logo': '📖'},
        {'name': 'Hemingway Editor', 'company': 'Hemingway', 'country': '🇺🇸 USA', 'logo': '🖊️'},
        {'name': 'Notion AI', 'company': 'Notion', 'country': '🇺🇸 USA', 'logo': '📓'},
        {'name': 'Compose AI', 'company': 'Compose AI', 'country': '🇺🇸 USA', 'logo': '✉️'},
        {'name': 'Textio', 'company': 'Textio', 'country': '🇺🇸 USA', 'logo': '💼'},
        {'name': 'Anyword', 'company': 'Anyword', 'country': '🇮🇱 Israel', 'logo': '📊'},
        {'name': 'Scalenut', 'company': 'Scalenut', 'country': '🇮🇳 India', 'logo': '🌰'},
        {'name': 'Frase', 'company': 'Frase', 'country': '🇺🇸 USA', 'logo': '🔍'},
        {'name': 'LongShot AI', 'company': 'LongShot', 'country': '🇮🇳 India', 'logo': '🎯'},
        {'name': 'Hypotenuse AI', 'company': 'Hypotenuse', 'country': '🇸🇬 Singapore', 'logo': '🏪'},
        {'name': 'Pepper Content', 'company': 'Pepper Content', 'country': '🇮🇳 India', 'logo': '🌶️'},
        {'name': 'ContentBot', 'company': 'ContentBot', 'country': '🇺🇸 USA', 'logo': '🤖'},
    ],

    'ai-coding': [
        {'name': 'GitHub Copilot', 'company': 'GitHub/Microsoft', 'country': '🇺🇸 USA', 'logo': '🐙'},
        {'name': 'Cursor', 'company': 'Anysphere', 'country': '🇺🇸 USA', 'logo': '⚡'},
        {'name': 'Tabnine', 'company': 'Tabnine', 'country': '🇮🇱 Israel', 'logo': '🔮'},
        {'name': 'Codeium', 'company': 'Exafunction', 'country': '🇺🇸 USA', 'logo': '💫'},
        {'name': 'Amazon CodeWhisperer', 'company': 'Amazon', 'country': '🇺🇸 USA', 'logo': '🔮'},
        {'name': 'Replit AI', 'company': 'Replit', 'country': '🇺🇸 USA', 'logo': '🔁'},
        {'name': 'Sourcegraph Cody', 'company': 'Sourcegraph', 'country': '🇺🇸 USA', 'logo': '🔍'},
        {'name': 'AskCodi', 'company': 'AskCodi', 'country': '🇺🇸 USA', 'logo': '❓'},
        {'name': 'CodeGPT', 'company': 'CodeGPT', 'country': '🇺🇸 USA', 'logo': '💻'},
        {'name': 'Blackbox AI', 'company': 'Blackbox', 'country': '🇺🇸 USA', 'logo': '⬛'},
        {'name': 'Mutable AI', 'company': 'Mutable', 'country': '🇺🇸 USA', 'logo': '🧬'},
        {'name': 'Fig', 'company': 'Fig', 'country': '🇺🇸 USA', 'logo': '🌿'},
        {'name': 'Phind', 'company': 'Phind', 'country': '🇺🇸 USA', 'logo': '🔎'},
        {'name': 'Bito AI', 'company': 'Bito', 'country': '🇺🇸 USA', 'logo': '🎯'},
        {'name': 'Pieces', 'company': 'Pieces', 'country': '🇺🇸 USA', 'logo': '🧩'},
        {'name': 'Aider', 'company': 'Aider', 'country': '🇺🇸 USA', 'logo': '🛠️'},
        {'name': 'Codex', 'company': 'OpenAI', 'country': '🇺🇸 USA', 'logo': '📜'},
        {'name': 'AlphaCode', 'company': 'DeepMind', 'country': '🇬🇧 UK', 'logo': '🏆'},
        {'name': 'Polycoder', 'company': 'CMU', 'country': '🇺🇸 USA', 'logo': '🔬'},
        {'name': 'CodeT5', 'company': 'Salesforce', 'country': '🇺🇸 USA', 'logo': '5️⃣'},
    ],

    'ai-image': [
        {'name': 'Midjourney', 'company': 'Midjourney', 'country': '🇺🇸 USA', 'logo': '🎨'},
        {'name': 'DALL-E 3', 'company': 'OpenAI', 'country': '🇺🇸 USA', 'logo': '🖼️'},
        {'name': 'Stable Diffusion', 'company': 'Stability AI', 'country': '🇬🇧 UK', 'logo': '🌊'},
        {'name': 'Leonardo.ai', 'company': 'Leonardo', 'country': '🇦🇺 Australia', 'logo': '🎮'},
        {'name': 'Ideogram', 'company': 'Ideogram', 'country': '🇺🇸 USA', 'logo': '📝'},
        {'name': 'Adobe Firefly', 'company': 'Adobe', 'country': '🇺🇸 USA', 'logo': '🔥'},
        {'name': 'Canva AI', 'company': 'Canva', 'country': '🇦🇺 Australia', 'logo': '🎨'},
        {'name': 'Runway ML', 'company': 'Runway', 'country': '🇺🇸 USA', 'logo': '🛫'},
        {'name': 'DreamStudio', 'company': 'Stability AI', 'country': '🇬🇧 UK', 'logo': '💭'},
        {'name': 'Playground AI', 'company': 'Playground', 'country': '🇺🇸 USA', 'logo': '🎪'},
        {'name': 'BlueWillow', 'company': 'BlueWillow', 'country': '🇺🇸 USA', 'logo': '🌳'},
        {'name': 'Bing Image Creator', 'company': 'Microsoft', 'country': '🇺🇸 USA', 'logo': '🔷'},
        {'name': 'Craiyon', 'company': 'Craiyon', 'country': '🇺🇸 USA', 'logo': '🖍️'},
        {'name': 'NightCafe', 'company': 'NightCafe', 'country': '🇦🇺 Australia', 'logo': '☕'},
        {'name': 'Artbreeder', 'company': 'Artbreeder', 'country': '🇺🇸 USA', 'logo': '🧬'},
        {'name': 'Photosonic', 'company': 'Writesonic', 'country': '🇺🇸 USA', 'logo': '📸'},
        {'name': 'StarryAI', 'company': 'StarryAI', 'country': '🇨🇦 Canada', 'logo': '⭐'},
        {'name': 'Deep Dream Generator', 'company': 'Deep Dream', 'country': '🇺🇸 USA', 'logo': '🌈'},
        {'name': 'WOMBO Dream', 'company': 'WOMBO', 'country': '🇨🇦 Canada', 'logo': '🎭'},
        {'name': 'Fotor AI', 'company': 'Fotor', 'country': '🇨🇳 China', 'logo': '📷'},
    ],

    'ai-video': [
        {'name': 'Runway Gen-2', 'company': 'Runway', 'country': '🇺🇸 USA', 'logo': '🎬'},
        {'name': 'Pika Labs', 'company': 'Pika', 'country': '🇺🇸 USA', 'logo': '⚡'},
        {'name': 'Synthesia', 'company': 'Synthesia', 'country': '🇬🇧 UK', 'logo': '🎭'},
        {'name': 'HeyGen', 'company': 'HeyGen', 'country': '🇺🇸 USA', 'logo': '👋'},
        {'name': 'D-ID', 'company': 'D-ID', 'country': '🇮🇱 Israel', 'logo': '🎪'},
        {'name': 'Descript', 'company': 'Descript', 'country': '🇺🇸 USA', 'logo': '✂️'},
        {'name': 'Pictory', 'company': 'Pictory', 'country': '🇺🇸 USA', 'logo': '📖'},
        {'name': 'InVideo AI', 'company': 'InVideo', 'country': '🇮🇳 India', 'logo': '🎥'},
        {'name': 'Fliki', 'company': 'Fliki', 'country': '🇮🇳 India', 'logo': '🎬'},
        {'name': 'Lumen5', 'company': 'Lumen5', 'country': '🇨🇦 Canada', 'logo': '💡'},
        {'name': 'Elai.io', 'company': 'Elai', 'country': '🇺🇸 USA', 'logo': '📺'},
        {'name': 'Hour One', 'company': 'Hour One', 'country': '🇮🇱 Israel', 'logo': '⏰'},
        {'name': 'Colossyan', 'company': 'Colossyan', 'country': '🇬🇧 UK', 'logo': '🎓'},
        {'name': 'DeepBrain AI', 'company': 'DeepBrain', 'country': '🇰🇷 South Korea', 'logo': '🧠'},
        {'name': 'Steve.AI', 'company': 'Steve.AI', 'country': '🇮🇳 India', 'logo': '🎨'},
        {'name': 'Vidyo.ai', 'company': 'Vidyo', 'country': '🇺🇸 USA', 'logo': '📹'},
        {'name': 'OpusClip', 'company': 'Opus', 'country': '🇺🇸 USA', 'logo': '✂️'},
        {'name': 'Kapwing AI', 'company': 'Kapwing', 'country': '🇺🇸 USA', 'logo': '🎞️'},
        {'name': 'Wondershare Filmora', 'company': 'Wondershare', 'country': '🇨🇳 China', 'logo': '🎬'},
        {'name': 'CapCut', 'company': 'ByteDance', 'country': '🇨🇳 China', 'logo': '✨'},
    ],

    'ai-audio': [
        {'name': 'ElevenLabs', 'company': 'ElevenLabs', 'country': '🇺🇸 USA', 'logo': '🔊'},
        {'name': 'Murf AI', 'company': 'Murf', 'country': '🇺🇸 USA', 'logo': '🎤'},
        {'name': 'Play.ht', 'company': 'Play.ht', 'country': '🇺🇸 USA', 'logo': '▶️'},
        {'name': 'Speechify', 'company': 'Speechify', 'country': '🇺🇸 USA', 'logo': '📖'},
        {'name': 'Descript Overdub', 'company': 'Descript', 'country': '🇺🇸 USA', 'logo': '🎙️'},
        {'name': 'Resemble AI', 'company': 'Resemble', 'country': '🇨🇦 Canada', 'logo': '🔉'},
        {'name': 'WellSaid Labs', 'company': 'WellSaid', 'country': '🇺🇸 USA', 'logo': '💬'},
        {'name': 'Listnr', 'company': 'Listnr', 'country': '🇺🇸 USA', 'logo': '🎧'},
        {'name': 'LOVO', 'company': 'LOVO AI', 'country': '🇺🇸 USA', 'logo': '🗣️'},
        {'name': 'Synthesys', 'company': 'Synthesys', 'country': '🇺🇸 USA', 'logo': '🎵'},
        {'name': 'Voicemod', 'company': 'Voicemod', 'country': '🇪🇸 Spain', 'logo': '🎭'},
        {'name': 'Respeecher', 'company': 'Respeecher', 'country': '🇺🇦 Ukraine', 'logo': '🔄'},
        {'name': 'Adobe Podcast', 'company': 'Adobe', 'country': '🇺🇸 USA', 'logo': '🎙️'},
        {'name': 'Cleanvoice', 'company': 'Cleanvoice', 'country': '🇩🇪 Germany', 'logo': '🧹'},
        {'name': 'Krisp', 'company': 'Krisp', 'country': '🇦🇲 Armenia', 'logo': '🔇'},
        {'name': 'Otter.ai', 'company': 'Otter.ai', 'country': '🇺🇸 USA', 'logo': '🦦'},
        {'name': 'AssemblyAI', 'company': 'AssemblyAI', 'country': '🇺🇸 USA', 'logo': '🔧'},
        {'name': 'Sonix', 'company': 'Sonix', 'country': '🇺🇸 USA', 'logo': '📝'},
        {'name': 'Riverside.fm', 'company': 'Riverside', 'country': '🇮🇱 Israel', 'logo': '🎙️'},
        {'name': 'Suno AI', 'company': 'Suno', 'country': '🇺🇸 USA', 'logo': '🎵'},
    ],

    'ai-productivity': [
        {'name': 'Notion AI', 'company': 'Notion', 'country': '🇺🇸 USA', 'logo': '📓'},
        {'name': 'Motion', 'company': 'Motion', 'country': '🇺🇸 USA', 'logo': '⚡'},
        {'name': 'Reclaim AI', 'company': 'Reclaim', 'country': '🇺🇸 USA', 'logo': '📅'},
        {'name': 'Todoist AI', 'company': 'Doist', 'country': '🇨🇱 Chile', 'logo': '✅'},
        {'name': 'ClickUp AI', 'company': 'ClickUp', 'country': '🇺🇸 USA', 'logo': '⬆️'},
        {'name': 'Mem', 'company': 'Mem', 'country': '🇺🇸 USA', 'logo': '🧠'},
        {'name': 'Otter.ai', 'company': 'Otter.ai', 'country': '🇺🇸 USA', 'logo': '🦦'},
        {'name': 'Fireflies.ai', 'company': 'Fireflies', 'country': '🇺🇸 USA', 'logo': '🔥'},
        {'name': 'Tactiq', 'company': 'Tactiq', 'country': '🇦🇺 Australia', 'logo': '📝'},
        {'name': 'Sembly AI', 'company': 'Sembly', 'country': '🇺🇸 USA', 'logo': '👥'},
        {'name': 'Krisp', 'company': 'Krisp', 'country': '🇦🇲 Armenia', 'logo': '🔇'},
        {'name': 'Clockwise', 'company': 'Clockwise', 'country': '🇺🇸 USA', 'logo': '🕐'},
        {'name': 'Trevor AI', 'company': 'Trevor', 'country': '🇺🇸 USA', 'logo': '📋'},
        {'name': 'Akiflow', 'company': 'Akiflow', 'country': '🇮🇹 Italy', 'logo': '⚡'},
        {'name': 'Sunsama', 'company': 'Sunsama', 'country': '🇺🇸 USA', 'logo': '☀️'},
        {'name': 'BeforeSunset AI', 'company': 'BeforeSunset', 'country': '🇹🇷 Turkey', 'logo': '🌅'},
        {'name': 'Taskade', 'company': 'Taskade', 'country': '🇺🇸 USA', 'logo': '📝'},
        {'name': 'Superhuman', 'company': 'Superhuman', 'country': '🇺🇸 USA', 'logo': '⚡'},
        {'name': 'SaneBox', 'company': 'SaneBox', 'country': '🇺🇸 USA', 'logo': '📧'},
        {'name': 'Mailbutler', 'company': 'Mailbutler', 'country': '🇩🇪 Germany', 'logo': '✉️'},
    ],

    'ai-seo': [
        {'name': 'Surfer SEO', 'company': 'Surfer', 'country': '🇵🇱 Poland', 'logo': '🏄'},
        {'name': 'Clearscope', 'company': 'Clearscope', 'country': '🇺🇸 USA', 'logo': '🔭'},
        {'name': 'MarketMuse', 'company': 'MarketMuse', 'country': '🇺🇸 USA', 'logo': '🎯'},
        {'name': 'Frase', 'company': 'Frase', 'country': '🇺🇸 USA', 'logo': '📝'},
        {'name': 'SEMrush AI', 'company': 'SEMrush', 'country': '🇺🇸 USA', 'logo': '📊'},
        {'name': 'Ahrefs AI', 'company': 'Ahrefs', 'country': '🇸🇬 Singapore', 'logo': '🔗'},
        {'name': 'Scalenut', 'company': 'Scalenut', 'country': '🇮🇳 India', 'logo': '🌰'},
        {'name': 'NeuronWriter', 'company': 'NeuronWriter', 'country': '🇵🇱 Poland', 'logo': '🧠'},
        {'name': 'LongShot AI', 'company': 'LongShot', 'country': '🇮🇳 India', 'logo': '🎯'},
        {'name': 'Outranking', 'company': 'Outranking', 'country': '🇺🇸 USA', 'logo': '📈'},
        {'name': 'GrowthBar', 'company': 'GrowthBar', 'country': '🇺🇸 USA', 'logo': '📊'},
        {'name': 'PageOptimizer Pro', 'company': 'PageOptimizer', 'country': '🇺🇸 USA', 'logo': '⚡'},
        {'name': 'INK', 'company': 'INK', 'country': '🇺🇸 USA', 'logo': '🖋️'},
        {'name': 'Keyword Insights', 'company': 'Keyword Insights', 'country': '🇬🇧 UK', 'logo': '🔑'},
        {'name': 'Topic', 'company': 'Topic', 'country': '🇺🇸 USA', 'logo': '📋'},
        {'name': 'SEO.ai', 'company': 'SEO.ai', 'country': '🇺🇸 USA', 'logo': '🤖'},
        {'name': 'RankIQ', 'company': 'RankIQ', 'country': '🇺🇸 USA', 'logo': '📈'},
        {'name': 'ContentShake', 'company': 'SEMrush', 'country': '🇺🇸 USA', 'logo': '🎲'},
        {'name': 'Copy.ai SEO', 'company': 'Copy.ai', 'country': '🇺🇸 USA', 'logo': '📋'},
        {'name': 'WordLift', 'company': 'WordLift', 'country': '🇮🇹 Italy', 'logo': '🏋️'},
    ],

    'ai-business': [
        {'name': 'Salesforce Einstein', 'company': 'Salesforce', 'country': '🇺🇸 USA', 'logo': '☁️'},
        {'name': 'HubSpot AI', 'company': 'HubSpot', 'country': '🇺🇸 USA', 'logo': '🎯'},
        {'name': 'Zoho Zia', 'company': 'Zoho', 'country': '🇮🇳 India', 'logo': '🔮'},
        {'name': 'Microsoft Dynamics 365', 'company': 'Microsoft', 'country': '🇺🇸 USA', 'logo': '💼'},
        {'name': 'SAP Business AI', 'company': 'SAP', 'country': '🇩🇪 Germany', 'logo': '💼'},
        {'name': 'Oracle AI', 'company': 'Oracle', 'country': '🇺🇸 USA', 'logo': '🔴'},
        {'name': 'IBM Watson', 'company': 'IBM', 'country': '🇺🇸 USA', 'logo': '💙'},
        {'name': 'Tableau AI', 'company': 'Tableau', 'country': '🇺🇸 USA', 'logo': '📊'},
        {'name': 'Power BI AI', 'company': 'Microsoft', 'country': '🇺🇸 USA', 'logo': '⚡'},
        {'name': 'Looker AI', 'company': 'Google', 'country': '🇺🇸 USA', 'logo': '👀'},
        {'name': 'ThoughtSpot', 'company': 'ThoughtSpot', 'country': '🇺🇸 USA', 'logo': '💭'},
        {'name': 'Qlik AutoML', 'company': 'Qlik', 'country': '🇺🇸 USA', 'logo': '📈'},
        {'name': 'DataRobot', 'company': 'DataRobot', 'country': '🇺🇸 USA', 'logo': '🤖'},
        {'name': 'H2O.ai', 'company': 'H2O.ai', 'country': '🇺🇸 USA', 'logo': '💧'},
        {'name': 'Alteryx', 'company': 'Alteryx', 'country': '🇺🇸 USA', 'logo': '🔧'},
        {'name': 'Anaplan', 'company': 'Anaplan', 'country': '🇺🇸 USA', 'logo': '📋'},
        {'name': 'Workday AI', 'company': 'Workday', 'country': '🇺🇸 USA', 'logo': '💼'},
        {'name': 'ServiceNow AI', 'company': 'ServiceNow', 'country': '🇺🇸 USA', 'logo': '⚙️'},
        {'name': 'UiPath', 'company': 'UiPath', 'country': '🇺🇸 USA', 'logo': '🤖'},
        {'name': 'Automation Anywhere', 'company': 'Automation Anywhere', 'country': '🇺🇸 USA', 'logo': '⚡'},
    ],

    'ai-networking': [
        {'name': 'Cisco DNA Center', 'company': 'Cisco', 'country': '🇺🇸 USA', 'logo': '🔵'},
        {'name': 'Juniper Mist AI', 'company': 'Juniper', 'country': '🇺🇸 USA', 'logo': '🌿'},
        {'name': 'Aruba AI', 'company': 'HPE', 'country': '🇺🇸 USA', 'logo': '🏝️'},
        {'name': 'Fortinet FortiAI', 'company': 'Fortinet', 'country': '🇺🇸 USA', 'logo': '🛡️'},
        {'name': 'Extreme Networks AIQ', 'company': 'Extreme', 'country': '🇺🇸 USA', 'logo': '⚡'},
        {'name': 'Nokia AVA', 'company': 'Nokia', 'country': '🇫🇮 Finland', 'logo': '📱'},
        {'name': 'Huawei iMaster NCE', 'company': 'Huawei', 'country': '🇨🇳 China', 'logo': '🔴'},
        {'name': 'VMware NSX Intelligence', 'company': 'VMware', 'country': '🇺🇸 USA', 'logo': '☁️'},
        {'name': 'Riverbed SteelCentral', 'company': 'Riverbed', 'country': '🇺🇸 USA', 'logo': '🌊'},
        {'name': 'AppDynamics', 'company': 'Cisco', 'country': '🇺🇸 USA', 'logo': '📊'},
        {'name': 'Dynatrace', 'company': 'Dynatrace', 'country': '🇺🇸 USA', 'logo': '🔍'},
        {'name': 'New Relic AI', 'company': 'New Relic', 'country': '🇺🇸 USA', 'logo': '📈'},
        {'name': 'Splunk', 'company': 'Splunk', 'country': '🇺🇸 USA', 'logo': '🔎'},
        {'name': 'Datadog', 'company': 'Datadog', 'country': '🇺🇸 USA', 'logo': '🐕'},
        {'name': 'ThousandEyes', 'company': 'Cisco', 'country': '🇺🇸 USA', 'logo': '👁️'},
        {'name': 'NetBrain', 'company': 'NetBrain', 'country': '🇺🇸 USA', 'logo': '🧠'},
        {'name': 'SolarWinds AI', 'company': 'SolarWinds', 'country': '🇺🇸 USA', 'logo': '☀️'},
        {'name': 'ManageEngine AI', 'company': 'Zoho', 'country': '🇮🇳 India', 'logo': '⚙️'},
        {'name': 'Auvik', 'company': 'Auvik', 'country': '🇨🇦 Canada', 'logo': '🔧'},
        {'name': 'LogicMonitor', 'company': 'LogicMonitor', 'country': '🇺🇸 USA', 'logo': '📊'},
    ],

    'ai-cybersecurity': [
        {'name': 'CrowdStrike Falcon', 'company': 'CrowdStrike', 'country': '🇺🇸 USA', 'logo': '🦅'},
        {'name': 'Darktrace', 'company': 'Darktrace', 'country': '🇬🇧 UK', 'logo': '🕷️'},
        {'name': 'SentinelOne', 'company': 'SentinelOne', 'country': '🇺🇸 USA', 'logo': '🛡️'},
        {'name': 'Palo Alto Cortex', 'company': 'Palo Alto', 'country': '🇺🇸 USA', 'logo': '🔐'},
        {'name': 'Vectra AI', 'company': 'Vectra', 'country': '🇺🇸 USA', 'logo': '🎯'},
        {'name': 'Cybereason', 'company': 'Cybereason', 'country': '🇺🇸 USA', 'logo': '🔍'},
        {'name': 'Cylance', 'company': 'BlackBerry', 'country': '🇨🇦 Canada', 'logo': '⚫'},
        {'name': 'Fortinet FortiGuard', 'company': 'Fortinet', 'country': '🇺🇸 USA', 'logo': '🛡️'},
        {'name': 'McAfee MVISION', 'company': 'McAfee', 'country': '🇺🇸 USA', 'logo': '🔴'},
        {'name': 'Symantec AI', 'company': 'Broadcom', 'country': '🇺🇸 USA', 'logo': '🟡'},
        {'name': 'Trend Micro XDR', 'company': 'Trend Micro', 'country': '🇯🇵 Japan', 'logo': '🔵'},
        {'name': 'Check Point Infinity', 'company': 'Check Point', 'country': '🇮🇱 Israel', 'logo': '✅'},
        {'name': 'Sophos Intercept X', 'company': 'Sophos', 'country': '🇬🇧 UK', 'logo': '🔒'},
        {'name': 'Microsoft Defender AI', 'company': 'Microsoft', 'country': '🇺🇸 USA', 'logo': '🛡️'},
        {'name': 'IBM QRadar', 'company': 'IBM', 'country': '🇺🇸 USA', 'logo': '🔵'},
        {'name': 'Splunk Enterprise Security', 'company': 'Splunk', 'country': '🇺🇸 USA', 'logo': '🔎'},
        {'name': 'Exabeam', 'company': 'Exabeam', 'country': '🇺🇸 USA', 'logo': '📊'},
        {'name': 'Abnormal Security', 'company': 'Abnormal', 'country': '🇺🇸 USA', 'logo': '📧'},
        {'name': 'Recorded Future', 'company': 'Recorded Future', 'country': '🇺🇸 USA', 'logo': '🔮'},
        {'name': 'ZeroFox', 'company': 'ZeroFox', 'country': '🇺🇸 USA', 'logo': '🦊'},
    ],

    'ai-medical': [
        {'name': 'DeepMind AlphaFold', 'company': 'Google DeepMind', 'country': '🇬🇧 UK', 'logo': '🧬'},
        {'name': 'IBM Watson Health', 'company': 'IBM', 'country': '🇺🇸 USA', 'logo': '💙'},
        {'name': 'PathAI', 'company': 'PathAI', 'country': '🇺🇸 USA', 'logo': '🔬'},
        {'name': 'Zebra Medical Vision', 'company': 'Zebra Medical', 'country': '🇮🇱 Israel', 'logo': '🦓'},
        {'name': 'Butterfly iQ', 'company': 'Butterfly Network', 'country': '🇺🇸 USA', 'logo': '🦋'},
        {'name': 'Viz.ai', 'company': 'Viz.ai', 'country': '🇺🇸 USA', 'logo': '🧠'},
        {'name': 'Tempus', 'company': 'Tempus', 'country': '🇺🇸 USA', 'logo': '🔬'},
        {'name': 'Paige.AI', 'company': 'Paige', 'country': '🇺🇸 USA', 'logo': '🎗️'},
        {'name': 'Aidoc', 'company': 'Aidoc', 'country': '🇮🇱 Israel', 'logo': '📋'},
        {'name': 'Enlitic', 'company': 'Enlitic', 'country': '🇺🇸 USA', 'logo': '🏥'},
        {'name': 'iCAD', 'company': 'iCAD', 'country': '🇺🇸 USA', 'logo': '🎀'},
        {'name': 'HeartFlow', 'company': 'HeartFlow', 'country': '🇺🇸 USA', 'logo': '❤️'},
        {'name': 'Caption Health', 'company': 'Caption Health', 'country': '🇺🇸 USA', 'logo': '💓'},
        {'name': 'Qure.ai', 'company': 'Qure.ai', 'country': '🇮🇳 India', 'logo': '🩺'},
        {'name': 'Arterys', 'company': 'Arterys', 'country': '🇺🇸 USA', 'logo': '🫀'},
        {'name': 'Bay Labs', 'company': 'Bay Labs', 'country': '🇺🇸 USA', 'logo': '💙'},
        {'name': 'Gauss Surgical', 'company': 'Gauss Surgical', 'country': '🇺🇸 USA', 'logo': '🩸'},
        {'name': 'K Health', 'company': 'K Health', 'country': '🇺🇸 USA', 'logo': '📱'},
        {'name': 'Ada Health', 'company': 'Ada', 'country': '🇩🇪 Germany', 'logo': '🤖'},
        {'name': 'Babylon Health', 'company': 'Babylon', 'country': '🇬🇧 UK', 'logo': '🏥'},
    ],

    'ai-architecture': [
        {'name': 'TestFit', 'company': 'TestFit', 'country': '🇺🇸 USA', 'logo': '📐'},
        {'name': 'Spacemaker', 'company': 'Autodesk', 'country': '🇳🇴 Norway', 'logo': '🏗️'},
        {'name': 'Hypar', 'company': 'Hypar', 'country': '🇺🇸 USA', 'logo': '🎯'},
        {'name': 'Finch3D', 'company': 'Finch', 'country': '🇩🇰 Denmark', 'logo': '🐦'},
        {'name': 'Archistar', 'company': 'Archistar', 'country': '🇦🇺 Australia', 'logo': '⭐'},
        {'name': 'Digital Blue Foam', 'company': 'Digital Blue Foam', 'country': '🇨🇦 Canada', 'logo': '🌊'},
        {'name': 'Autodesk Forma', 'company': 'Autodesk', 'country': '🇺🇸 USA', 'logo': '🏢'},
        {'name': 'Revit AI', 'company': 'Autodesk', 'country': '🇺🇸 USA', 'logo': '🏗️'},
        {'name': 'SketchUp AI', 'company': 'Trimble', 'country': '🇺🇸 USA', 'logo': '✏️'},
        {'name': 'Rhino Grasshopper', 'company': 'Robert McNeel', 'country': '🇺🇸 USA', 'logo': '🦗'},
        {'name': 'Dynamo', 'company': 'Autodesk', 'country': '🇺🇸 USA', 'logo': '⚡'},
        {'name': 'ARCHIlogic', 'company': 'ARCHIlogic', 'country': '🇨🇭 Switzerland', 'logo': '📊'},
        {'name': 'Augmenta', 'company': 'Augmenta', 'country': '🇫🇷 France', 'logo': '⚙️'},
        {'name': 'MonographAI', 'company': 'Monograph', 'country': '🇺🇸 USA', 'logo': '📋'},
        {'name': 'Join', 'company': 'Join', 'country': '🇦🇹 Austria', 'logo': '📐'},
        {'name': 'Buildots', 'company': 'Buildots', 'country': '🇮🇱 Israel', 'logo': '👷'},
        {'name': 'OpenSpace', 'company': 'OpenSpace', 'country': '🇺🇸 USA', 'logo': '📸'},
        {'name': 'Reconstruct', 'company': 'Reconstruct', 'country': '🇺🇸 USA', 'logo': '📊'},
        {'name': 'Doxel', 'company': 'Doxel', 'country': '🇺🇸 USA', 'logo': '🤖'},
        {'name': 'Smartvid.io', 'company': 'Smartvid', 'country': '🇺🇸 USA', 'logo': '🎥'},
    ],
}

def generate_tool_card_html(ai, category):
    """Génère le HTML pour une carte d'outil AI."""
    return f'''
                <a href="#" class="tool-card">
                    <div class="tool-logo">
                        <span style="font-size: 32px;">{ai['logo']}</span>
                    </div>
                    <h3>{ai['name']}</h3>
                    <p class="tool-company">{ai['company']}</p>
                    <div class="tool-meta">
                        <span class="meta-item">
                            <span>{ai['country']}</span>
                        </span>
                    </div>
                </a>'''

def add_ai_to_category(file_path, category_key):
    """Ajoute 20 AI à une catégorie."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        ai_list = AI_DATA.get(category_key, [])
        if not ai_list:
            return False, 0

        # Trouver la section tools-grid
        pattern = r'(<div class="tools-grid">)(.*?)(</div>\s*</section>)'

        match = re.search(pattern, content, re.DOTALL)
        if not match:
            print(f"   ⚠️  Pattern tools-grid non trouvé")
            return False, 0

        # Générer toutes les cartes
        cards_html = ''
        for ai in ai_list:
            cards_html += generate_tool_card_html(ai, category_key)

        # Remplacer le contenu
        new_content = match.group(1) + cards_html + '\n            ' + match.group(3)
        content = content[:match.start()] + new_content + content[match.end():]

        # Sauvegarder
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return True, len(ai_list)

    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        return False, 0

def main():
    """Ajoute les AI dans toutes les catégories."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/categories')

    print("🤖 Ajout de 20 AI par catégorie...\n")

    total_added = 0
    categories_updated = 0

    for category_key in AI_DATA.keys():
        file_path = base_dir / f'{category_key}.html'

        if file_path.exists():
            print(f"📁 {category_key}")
            success, count = add_ai_to_category(file_path, category_key)
            if success:
                total_added += count
                categories_updated += 1
                print(f"   ✅ {count} AI ajoutées\n")
            else:
                print(f"   ⚠️  Échec\n")
        else:
            print(f"❌ {category_key}.html - Fichier non trouvé\n")

    print(f"{'='*50}")
    print(f"🎉 Terminé!")
    print(f"📊 {categories_updated} catégories mises à jour")
    print(f"🤖 {total_added} AI ajoutées au total")
    print(f"✨ Chaque catégorie a maintenant 20 AI!")

if __name__ == '__main__':
    main()
