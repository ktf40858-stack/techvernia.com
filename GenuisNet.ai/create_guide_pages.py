#!/usr/bin/env python3
"""
Script pour créer des pages individuelles pour chaque guide et corriger les cartes
"""

import os
from pathlib import Path

# Données des guides avec leurs slugs et contenu
guides_data = {
    'beginner': [
        {
            'slug': 'ai-fundamentals',
            'title': 'AI Fundamentals',
            'description': 'Master the core concepts of artificial intelligence, machine learning, and neural networks',
            'time': '20 min',
            'lessons': '5 lessons',
            'icon': '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
            'gradient_id': 'grad-beginner-1',
            'color_start': '#22C55E',
            'color_end': '#10B981',
            'glow_rgb': '34, 197, 94'
        },
        {
            'slug': 'getting-started-chatgpt',
            'title': 'Getting Started with ChatGPT',
            'description': 'Learn how to use ChatGPT effectively for writing, coding, and problem-solving',
            'time': '25 min',
            'lessons': '6 lessons',
            'icon': '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
            'gradient_id': 'grad-beginner-2',
            'color_start': '#22C55E',
            'color_end': '#10B981',
            'glow_rgb': '34, 197, 94'
        },
        {
            'slug': 'introduction-image-ai',
            'title': 'Introduction to Image AI',
            'description': 'Discover how to create stunning visuals with DALL-E, Midjourney, and Stable Diffusion',
            'time': '30 min',
            'lessons': '7 lessons',
            'icon': '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/>',
            'gradient_id': 'grad-beginner-3',
            'color_start': '#22C55E',
            'color_end': '#10B981',
            'glow_rgb': '34, 197, 94'
        },
        {
            'slug': 'ai-writing-tools-basics',
            'title': 'AI Writing Tools Basics',
            'description': 'Master AI-powered writing assistants for content creation and editing',
            'time': '18 min',
            'lessons': '4 lessons',
            'icon': '<path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/><path d="M2 2l7.586 7.586"/>',
            'gradient_id': 'grad-beginner-4',
            'color_start': '#22C55E',
            'color_end': '#10B981',
            'glow_rgb': '34, 197, 94'
        },
        {
            'slug': 'understanding-ai-models',
            'title': 'Understanding AI Models',
            'description': 'Learn about different types of AI models and their applications',
            'time': '22 min',
            'lessons': '5 lessons',
            'icon': '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
            'gradient_id': 'grad-beginner-5',
            'color_start': '#22C55E',
            'color_end': '#10B981',
            'glow_rgb': '34, 197, 94'
        },
        {
            'slug': 'ai-safety-ethics-101',
            'title': 'AI Safety & Ethics 101',
            'description': 'Explore responsible AI use and ethical considerations',
            'time': '15 min',
            'lessons': '4 lessons',
            'icon': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
            'gradient_id': 'grad-beginner-6',
            'color_start': '#22C55E',
            'color_end': '#10B981',
            'glow_rgb': '34, 197, 94'
        },
        {
            'slug': 'prompt-engineering-basics',
            'title': 'Prompt Engineering Basics',
            'description': 'Learn to write effective prompts for better AI outputs',
            'time': '28 min',
            'lessons': '6 lessons',
            'icon': '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
            'gradient_id': 'grad-beginner-7',
            'color_start': '#22C55E',
            'color_end': '#10B981',
            'glow_rgb': '34, 197, 94'
        },
        {
            'slug': 'ai-personal-productivity',
            'title': 'AI for Personal Productivity',
            'description': 'Boost your daily efficiency with AI tools and techniques',
            'time': '20 min',
            'lessons': '5 lessons',
            'icon': '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="M22 4L12 14.01l-3-3"/>',
            'gradient_id': 'grad-beginner-8',
            'color_start': '#22C55E',
            'color_end': '#10B981',
            'glow_rgb': '34, 197, 94'
        },
        {
            'slug': 'voice-audio-ai-intro',
            'title': 'Voice & Audio AI Intro',
            'description': 'Get started with AI voice generation and audio processing',
            'time': '25 min',
            'lessons': '6 lessons',
            'icon': '<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2M12 19v4M8 23h8"/>',
            'gradient_id': 'grad-beginner-9',
            'color_start': '#22C55E',
            'color_end': '#10B981',
            'glow_rgb': '34, 197, 94'
        },
        {
            'slug': 'ai-tools-comparison',
            'title': 'AI Tools Comparison Guide',
            'description': 'Compare popular AI tools to find the best fit for your needs',
            'time': '30 min',
            'lessons': '7 lessons',
            'icon': '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>',
            'gradient_id': 'grad-beginner-10',
            'color_start': '#22C55E',
            'color_end': '#10B981',
            'glow_rgb': '34, 197, 94'
        }
    ],
    'intermediate': [
        {
            'slug': 'advanced-prompt-engineering',
            'title': 'Advanced Prompt Engineering',
            'description': 'Master complex prompting techniques for sophisticated AI interactions',
            'time': '35 min',
            'lessons': '8 lessons',
            'icon': '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
            'gradient_id': 'grad-inter-1',
            'color_start': '#3B82F6',
            'color_end': '#2563EB',
            'glow_rgb': '59, 130, 246'
        },
        {
            'slug': 'api-integration-mastery',
            'title': 'API Integration Mastery',
            'description': 'Connect AI capabilities to your applications via APIs',
            'time': '38 min',
            'lessons': '9 lessons',
            'icon': '<path d="M16 18l2-2-2-2M8 6L6 8l2 2"/><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>',
            'gradient_id': 'grad-inter-2',
            'color_start': '#3B82F6',
            'color_end': '#2563EB',
            'glow_rgb': '59, 130, 246'
        },
        {
            'slug': 'multimodal-ai-applications',
            'title': 'Multimodal AI Applications',
            'description': 'Combine text, image, and audio AI for powerful solutions',
            'time': '42 min',
            'lessons': '10 lessons',
            'icon': '<path d="M3 3v18h18M7 16l4-4 4 4 6-6"/>',
            'gradient_id': 'grad-inter-3',
            'color_start': '#3B82F6',
            'color_end': '#2563EB',
            'glow_rgb': '59, 130, 246'
        },
        {
            'slug': 'ai-content-strategy',
            'title': 'AI Content Strategy',
            'description': 'Develop professional content workflows using AI tools',
            'time': '35 min',
            'lessons': '8 lessons',
            'icon': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/>',
            'gradient_id': 'grad-inter-4',
            'color_start': '#3B82F6',
            'color_end': '#2563EB',
            'glow_rgb': '59, 130, 246'
        },
        {
            'slug': 'ai-data-analysis',
            'title': 'AI Data Analysis',
            'description': 'Leverage AI for advanced data processing and insights',
            'time': '40 min',
            'lessons': '9 lessons',
            'icon': '<path d="M3 3v18h18"/><path d="M18 17V9M13 17V5M8 17v-3"/>',
            'gradient_id': 'grad-inter-5',
            'color_start': '#3B82F6',
            'color_end': '#2563EB',
            'glow_rgb': '59, 130, 246'
        },
        {
            'slug': 'building-ai-chatbots',
            'title': 'Building AI Chatbots',
            'description': 'Create custom chatbots for business and personal use',
            'time': '45 min',
            'lessons': '10 lessons',
            'icon': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M9 10h.01M15 10h.01M12 14h.01"/>',
            'gradient_id': 'grad-inter-6',
            'color_start': '#3B82F6',
            'color_end': '#2563EB',
            'glow_rgb': '59, 130, 246'
        },
        {
            'slug': 'ai-video-animation',
            'title': 'AI Video & Animation',
            'description': 'Master AI tools for video creation and editing',
            'time': '38 min',
            'lessons': '9 lessons',
            'icon': '<path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/>',
            'gradient_id': 'grad-inter-7',
            'color_start': '#3B82F6',
            'color_end': '#2563EB',
            'glow_rgb': '59, 130, 246'
        },
        {
            'slug': 'ai-testing-optimization',
            'title': 'AI Testing & Optimization',
            'description': 'Learn to test, benchmark, and improve AI outputs',
            'time': '35 min',
            'lessons': '8 lessons',
            'icon': '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="M22 4L12 14.01l-3-3"/>',
            'gradient_id': 'grad-inter-8',
            'color_start': '#3B82F6',
            'color_end': '#2563EB',
            'glow_rgb': '59, 130, 246'
        },
        {
            'slug': 'custom-ai-training',
            'title': 'Custom AI Training Basics',
            'description': 'Learn to fine-tune AI models for specialized tasks',
            'time': '45 min',
            'lessons': '10 lessons',
            'icon': '<rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
            'gradient_id': 'grad-inter-9',
            'color_start': '#3B82F6',
            'color_end': '#2563EB',
            'glow_rgb': '59, 130, 246'
        },
        {
            'slug': 'ai-workflow-automation',
            'title': 'AI Workflow Automation',
            'description': 'Build automated workflows combining multiple AI tools',
            'time': '40 min',
            'lessons': '9 lessons',
            'icon': '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M12 22V12M22 8.5l-10 5.75M2 8.5l10 5.75"/>',
            'gradient_id': 'grad-inter-10',
            'color_start': '#3B82F6',
            'color_end': '#2563EB',
            'glow_rgb': '59, 130, 246'
        }
    ],
    'advanced': [
        {
            'slug': 'enterprise-ai-architecture',
            'title': 'Enterprise AI Architecture',
            'description': 'Design scalable AI systems for large organizations',
            'time': '50 min',
            'lessons': '12 lessons',
            'icon': '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>',
            'gradient_id': 'grad-adv-1',
            'color_start': '#A855F7',
            'color_end': '#7C3AED',
            'glow_rgb': '168, 85, 247'
        },
        {
            'slug': 'ai-model-development',
            'title': 'AI Model Development',
            'description': 'Build and deploy custom AI models from scratch',
            'time': '60 min',
            'lessons': '14 lessons',
            'icon': '<rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
            'gradient_id': 'grad-adv-2',
            'color_start': '#A855F7',
            'color_end': '#7C3AED',
            'glow_rgb': '168, 85, 247'
        },
        {
            'slug': 'advanced-neural-networks',
            'title': 'Advanced Neural Networks',
            'description': 'Deep dive into transformer models and neural architecture',
            'time': '55 min',
            'lessons': '13 lessons',
            'icon': '<circle cx="12" cy="12" r="3"/><path d="M12 1v6M12 17v6M4.22 4.22l4.24 4.24M15.54 15.54l4.24 4.24M1 12h6M17 12h6M4.22 19.78l4.24-4.24M15.54 8.46l4.24-4.24"/>',
            'gradient_id': 'grad-adv-3',
            'color_start': '#A855F7',
            'color_end': '#7C3AED',
            'glow_rgb': '168, 85, 247'
        },
        {
            'slug': 'ai-security-privacy',
            'title': 'AI Security & Privacy',
            'description': 'Implement robust security measures for AI systems',
            'time': '45 min',
            'lessons': '11 lessons',
            'icon': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M12 9v4M12 17h.01"/>',
            'gradient_id': 'grad-adv-4',
            'color_start': '#A855F7',
            'color_end': '#7C3AED',
            'glow_rgb': '168, 85, 247'
        },
        {
            'slug': 'production-ai-deployment',
            'title': 'Production AI Deployment',
            'description': 'Deploy and monitor AI models in production environments',
            'time': '50 min',
            'lessons': '12 lessons',
            'icon': '<path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/>',
            'gradient_id': 'grad-adv-5',
            'color_start': '#A855F7',
            'color_end': '#7C3AED',
            'glow_rgb': '168, 85, 247'
        },
        {
            'slug': 'ai-performance-tuning',
            'title': 'AI Performance Tuning',
            'description': 'Optimize AI models for speed, cost, and accuracy',
            'time': '48 min',
            'lessons': '11 lessons',
            'icon': '<path d="M12 20v-6M6 20V10M18 20V4"/>',
            'gradient_id': 'grad-adv-6',
            'color_start': '#A855F7',
            'color_end': '#7C3AED',
            'glow_rgb': '168, 85, 247'
        },
        {
            'slug': 'custom-llm-finetuning',
            'title': 'Custom LLM Fine-tuning',
            'description': 'Train specialized language models for domain expertise',
            'time': '58 min',
            'lessons': '13 lessons',
            'icon': '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
            'gradient_id': 'grad-adv-7',
            'color_start': '#A855F7',
            'color_end': '#7C3AED',
            'glow_rgb': '168, 85, 247'
        },
        {
            'slug': 'ai-ethics-implementation',
            'title': 'AI Ethics Implementation',
            'description': 'Build ethical frameworks into AI systems and workflows',
            'time': '42 min',
            'lessons': '10 lessons',
            'icon': '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/>',
            'gradient_id': 'grad-adv-8',
            'color_start': '#A855F7',
            'color_end': '#7C3AED',
            'glow_rgb': '168, 85, 247'
        },
        {
            'slug': 'multi-agent-ai-systems',
            'title': 'Multi-Agent AI Systems',
            'description': 'Orchestrate multiple AI agents for complex tasks',
            'time': '52 min',
            'lessons': '12 lessons',
            'icon': '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
            'gradient_id': 'grad-adv-9',
            'color_start': '#A855F7',
            'color_end': '#7C3AED',
            'glow_rgb': '168, 85, 247'
        },
        {
            'slug': 'ai-research-innovation',
            'title': 'AI Research & Innovation',
            'description': 'Explore cutting-edge AI research and experimental techniques',
            'time': '55 min',
            'lessons': '13 lessons',
            'icon': '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
            'gradient_id': 'grad-adv-10',
            'color_start': '#A855F7',
            'color_end': '#7C3AED',
            'glow_rgb': '168, 85, 247'
        }
    ]
}

def create_guide_page_html(guide, level):
    """Crée le HTML pour une page de guide individuelle."""
    level_colors = {
        'beginner': {'name': 'Beginner', 'color': '#22C55E', 'bg': 'rgba(34, 197, 94, 0.1)'},
        'intermediate': {'name': 'Intermediate', 'color': '#3B82F6', 'bg': 'rgba(59, 130, 246, 0.1)'},
        'advanced': {'name': 'Advanced', 'color': '#A855F7', 'bg': 'rgba(168, 85, 247, 0.1)'}
    }

    level_info = level_colors[level]

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{guide['title']} - GenuisNet.ai</title>
    <link rel="stylesheet" href="../../css/style.css">
    <link rel="stylesheet" href="../../css/guides-reviews.css">
    <link rel="icon" type="image/svg+xml" href="../../assets/images/logo.svg">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container">
            <div class="nav-container">
                <a href="../../index.html" class="logo">
                    <img src="../../assets/images/logo.svg" alt="GenuisNet.ai" class="logo-image">
                </a>
            </div>
        </div>
    </nav>

    <!-- Guide Content -->
    <main class="guide-content">
        <div class="container" style="max-width: 900px; margin-top: var(--space-4xl);">
            <!-- Breadcrumb -->
            <div style="margin-bottom: var(--space-xl);">
                <a href="../guides.html" style="color: var(--text-secondary); text-decoration: none;">
                    ← Back to Guides
                </a>
            </div>

            <!-- Header -->
            <header style="margin-bottom: var(--space-3xl);">
                <div style="display: inline-block; padding: var(--space-xs) var(--space-md); background: {level_info['bg']}; border: 1px solid {level_info['color']}; border-radius: var(--radius-full); color: {level_info['color']}; font-size: var(--text-sm); font-weight: 600; margin-bottom: var(--space-md);">
                    {level_info['name']} Level
                </div>
                <h1 style="font-size: var(--text-4xl); font-weight: 800; margin-bottom: var(--space-md); background: linear-gradient(135deg, {guide['color_start']}, {guide['color_end']}); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                    {guide['title']}
                </h1>
                <p style="font-size: var(--text-xl); color: var(--text-secondary); margin-bottom: var(--space-lg);">
                    {guide['description']}
                </p>
                <div style="display: flex; gap: var(--space-lg); color: var(--text-secondary); font-size: var(--text-sm);">
                    <span>
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px; display: inline-block; vertical-align: middle; margin-right: 6px;">
                            <circle cx="12" cy="12" r="10"/>
                            <path d="M12 6v6l4 2"/>
                        </svg>
                        {guide['time']} read
                    </span>
                    <span>
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px; display: inline-block; vertical-align: middle; margin-right: 6px;">
                            <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
                            <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
                        </svg>
                        {guide['lessons']}
                    </span>
                </div>
            </header>

            <!-- Table of Contents -->
            <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: var(--space-xl); margin-bottom: var(--space-3xl);">
                <h2 style="font-size: var(--text-xl); font-weight: 700; margin-bottom: var(--space-md);">
                    What You'll Learn
                </h2>
                <ul style="list-style: none; padding: 0; margin: 0;">
                    <li style="padding: var(--space-sm) 0; display: flex; align-items: start;">
                        <svg viewBox="0 0 24 24" fill="none" stroke="{guide['color_start']}" stroke-width="2" style="width: 20px; height: 20px; margin-right: var(--space-sm); flex-shrink: 0; margin-top: 2px;">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                            <path d="M22 4L12 14.01l-3-3"/>
                        </svg>
                        <span>Core concepts and fundamental principles</span>
                    </li>
                    <li style="padding: var(--space-sm) 0; display: flex; align-items: start;">
                        <svg viewBox="0 0 24 24" fill="none" stroke="{guide['color_start']}" stroke-width="2" style="width: 20px; height: 20px; margin-right: var(--space-sm); flex-shrink: 0; margin-top: 2px;">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                            <path d="M22 4L12 14.01l-3-3"/>
                        </svg>
                        <span>Practical techniques and best practices</span>
                    </li>
                    <li style="padding: var(--space-sm) 0; display: flex; align-items: start;">
                        <svg viewBox="0 0 24 24" fill="none" stroke="{guide['color_start']}" stroke-width="2" style="width: 20px; height: 20px; margin-right: var(--space-sm); flex-shrink: 0; margin-top: 2px;">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                            <path d="M22 4L12 14.01l-3-3"/>
                        </svg>
                        <span>Real-world examples and use cases</span>
                    </li>
                    <li style="padding: var(--space-sm) 0; display: flex; align-items: start;">
                        <svg viewBox="0 0 24 24" fill="none" stroke="{guide['color_start']}" stroke-width="2" style="width: 20px; height: 20px; margin-right: var(--space-sm); flex-shrink: 0; margin-top: 2px;">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
                            <path d="M22 4L12 14.01l-3-3"/>
                        </svg>
                        <span>Tips for optimizing your workflow</span>
                    </li>
                </ul>
            </div>

            <!-- Main Content -->
            <article class="guide-section">
                <section style="margin-bottom: var(--space-3xl);">
                    <h2 style="font-size: var(--text-2xl); font-weight: 700; margin-bottom: var(--space-lg); color: var(--text-primary);">
                        Introduction
                    </h2>
                    <p style="line-height: 1.8; margin-bottom: var(--space-md); color: var(--text-secondary);">
                        Welcome to this comprehensive guide on {guide['title'].lower()}. In this guide, you'll discover everything you need to know to master this essential aspect of AI technology.
                    </p>
                    <p style="line-height: 1.8; color: var(--text-secondary);">
                        Whether you're just getting started or looking to expand your knowledge, this guide will provide you with practical insights, actionable strategies, and expert tips to help you succeed.
                    </p>
                </section>

                <section style="margin-bottom: var(--space-3xl);">
                    <h2 style="font-size: var(--text-2xl); font-weight: 700; margin-bottom: var(--space-lg); color: var(--text-primary);">
                        Getting Started
                    </h2>
                    <p style="line-height: 1.8; margin-bottom: var(--space-md); color: var(--text-secondary);">
                        Before diving into the details, let's establish a solid foundation. Understanding the basics is crucial for making the most of AI technology in this area.
                    </p>
                    <div style="background: {level_info['bg']}; border-left: 4px solid {level_info['color']}; padding: var(--space-lg); border-radius: var(--radius-md); margin: var(--space-lg) 0;">
                        <p style="margin: 0; line-height: 1.8; color: var(--text-secondary);">
                            <strong style="color: var(--text-primary);">Pro Tip:</strong> Take your time with each section. Practical experience combined with theoretical knowledge will give you the best results.
                        </p>
                    </div>
                </section>

                <section style="margin-bottom: var(--space-3xl);">
                    <h2 style="font-size: var(--text-2xl); font-weight: 700; margin-bottom: var(--space-lg); color: var(--text-primary);">
                        Key Concepts
                    </h2>
                    <p style="line-height: 1.8; margin-bottom: var(--space-lg); color: var(--text-secondary);">
                        Let's explore the fundamental concepts that form the backbone of this topic. These principles will guide your understanding and implementation.
                    </p>
                    <div style="display: grid; gap: var(--space-md); margin-bottom: var(--space-lg);">
                        <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: var(--space-lg);">
                            <h3 style="font-size: var(--text-lg); font-weight: 600; margin-bottom: var(--space-sm); color: var(--text-primary);">
                                Core Principles
                            </h3>
                            <p style="margin: 0; line-height: 1.8; color: var(--text-secondary);">
                                Understanding the underlying principles helps you make better decisions and achieve more effective results in your AI projects.
                            </p>
                        </div>
                        <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: var(--space-lg);">
                            <h3 style="font-size: var(--text-lg); font-weight: 600; margin-bottom: var(--space-sm); color: var(--text-primary);">
                                Best Practices
                            </h3>
                            <p style="margin: 0; line-height: 1.8; color: var(--text-secondary);">
                                Follow industry-standard best practices to ensure your work is efficient, scalable, and maintainable over time.
                            </p>
                        </div>
                    </div>
                </section>

                <section style="margin-bottom: var(--space-3xl);">
                    <h2 style="font-size: var(--text-2xl); font-weight: 700; margin-bottom: var(--space-lg); color: var(--text-primary);">
                        Practical Applications
                    </h2>
                    <p style="line-height: 1.8; margin-bottom: var(--space-md); color: var(--text-secondary);">
                        Now that you understand the fundamentals, let's look at how to apply these concepts in real-world scenarios.
                    </p>
                    <p style="line-height: 1.8; color: var(--text-secondary);">
                        These practical examples will help you translate theory into action and start seeing results immediately.
                    </p>
                </section>

                <section style="margin-bottom: var(--space-3xl);">
                    <h2 style="font-size: var(--text-2xl); font-weight: 700; margin-bottom: var(--space-lg); color: var(--text-primary);">
                        Common Challenges & Solutions
                    </h2>
                    <p style="line-height: 1.8; margin-bottom: var(--space-lg); color: var(--text-secondary);">
                        Every journey has its obstacles. Here are some common challenges you might face and proven solutions to overcome them.
                    </p>
                    <ul style="list-style: none; padding: 0; margin: 0;">
                        <li style="padding: var(--space-md) 0; border-bottom: 1px solid var(--border-color);">
                            <strong style="color: var(--text-primary);">Challenge:</strong>
                            <span style="color: var(--text-secondary);"> Getting started with complex AI tools</span><br>
                            <strong style="color: {level_info['color']};">Solution:</strong>
                            <span style="color: var(--text-secondary);"> Start with simpler tools and gradually build your expertise</span>
                        </li>
                        <li style="padding: var(--space-md) 0; border-bottom: 1px solid var(--border-color);">
                            <strong style="color: var(--text-primary);">Challenge:</strong>
                            <span style="color: var(--text-secondary);"> Optimizing AI outputs for your specific needs</span><br>
                            <strong style="color: {level_info['color']};">Solution:</strong>
                            <span style="color: var(--text-secondary);"> Experiment with different approaches and track what works best</span>
                        </li>
                        <li style="padding: var(--space-md) 0;">
                            <strong style="color: var(--text-primary);">Challenge:</strong>
                            <span style="color: var(--text-secondary);"> Staying updated with rapidly evolving AI technology</span><br>
                            <strong style="color: {level_info['color']};">Solution:</strong>
                            <span style="color: var(--text-secondary);"> Follow industry leaders and regularly check GenuisNet.ai for updates</span>
                        </li>
                    </ul>
                </section>

                <section style="margin-bottom: var(--space-3xl);">
                    <h2 style="font-size: var(--text-2xl); font-weight: 700; margin-bottom: var(--space-lg); color: var(--text-primary);">
                        Next Steps
                    </h2>
                    <p style="line-height: 1.8; margin-bottom: var(--space-md); color: var(--text-secondary);">
                        Congratulations on completing this guide! Here's what you can do next to continue your AI journey:
                    </p>
                    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: var(--space-xl);">
                        <ol style="margin: 0; padding-left: var(--space-lg); color: var(--text-secondary); line-height: 2;">
                            <li>Practice what you've learned with real projects</li>
                            <li>Explore related guides on GenuisNet.ai</li>
                            <li>Join AI communities to share your experiences</li>
                            <li>Stay updated with the latest AI tools and trends</li>
                        </ol>
                    </div>
                </section>
            </article>

            <!-- Related Guides -->
            <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-xl); padding: var(--space-2xl); margin-top: var(--space-4xl);">
                <h2 style="font-size: var(--text-xl); font-weight: 700; margin-bottom: var(--space-lg); text-align: center;">
                    Continue Learning
                </h2>
                <div style="display: flex; gap: var(--space-md); justify-content: center; flex-wrap: wrap;">
                    <a href="../guides.html#beginner" class="btn btn-outline">More Beginner Guides</a>
                    <a href="../guides.html#intermediate" class="btn btn-outline">Intermediate Guides</a>
                    <a href="../guides.html#advanced" class="btn btn-outline">Advanced Guides</a>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <a href="../../index.html" class="footer-logo">
                        <img src="../../assets/images/logo.svg" alt="GenuisNet.ai Logo" class="footer-logo-image">
                    </a>
                    <p class="footer-description">Your trusted source for AI tool reviews and comparisons.</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 GenuisNet.ai. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        // Logo scroll behavior
        const navbar = document.querySelector('.navbar');
        const logo = document.querySelector('.logo');

        window.addEventListener('scroll', () => {{
            const currentScroll = window.pageYOffset;

            if (currentScroll > 100) {{
                logo.style.opacity = '0';
                logo.style.pointerEvents = 'none';
            }} else {{
                logo.style.opacity = '1';
                logo.style.pointerEvents = 'auto';
            }}
        }});
    </script>
</body>
</html>'''

def main():
    """Crée toutes les pages de guides."""
    base_dir = Path('/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides')
    base_dir.mkdir(exist_ok=True)

    total_created = 0

    for level, guides in guides_data.items():
        print(f"\n📝 Création des guides {level}...")
        for guide in guides:
            file_path = base_dir / f"{guide['slug']}.html"
            html_content = create_guide_page_html(guide, level)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)

            total_created += 1
            print(f"   ✅ {guide['title']}")

    print(f"\n🎉 {total_created} pages de guides créées avec succès!")

if __name__ == '__main__':
    main()
