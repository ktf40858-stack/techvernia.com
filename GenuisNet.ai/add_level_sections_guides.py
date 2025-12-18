#!/usr/bin/env python3
"""
Script pour ajouter les sections Beginner, Intermediate et Advanced
avec du contenu et des icônes high-tech
"""

import re

# Contenu pour la section Beginner
BEGINNER_SECTION = '''
            <!-- Section: Beginner Guides -->
            <div id="beginner"></div>
            <div class="section-divider" style="margin-top: var(--space-4xl);">
                <div style="display: flex; align-items: center; justify-content: center; gap: var(--space-md); margin-bottom: var(--space-md);">
                    <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-beginner-section)" stroke-width="2" width="40" height="40" style="filter: drop-shadow(0 0 10px rgba(34, 197, 94, 0.6));">
                        <circle cx="12" cy="12" r="10"/>
                        <path d="M12 16v-4"/>
                        <path d="M12 8h.01"/>
                    </svg>
                    <h2>Beginner Guides</h2>
                </div>
                <p style="color: var(--text-secondary);">Perfect starting point for AI newcomers - no experience required</p>
                <svg width="0" height="0" style="position: absolute;">
                    <defs>
                        <linearGradient id="grad-beginner-section" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" style="stop-color:#22C55E"/>
                            <stop offset="100%" style="stop-color:#10B981"/>
                        </linearGradient>
                    </defs>
                </svg>
            </div>

            <div class="guides-grid">
                <!-- Guide 1: AI Basics -->
                <div class="guide-card" style="cursor: default;">
                    <div class="guide-card-header">
                        <div class="guide-icon-container">
                            <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(16, 185, 129, 0.1)); border: 2px solid rgba(34, 197, 94, 0.3); --glow-rgb: 34, 197, 94; animation: glow 3s ease-in-out infinite;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-basics)" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba(34, 197, 94, 0.8));">
                                    <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                                    <path d="M2 17l10 5 10-5"/>
                                    <path d="M2 12l10 5 10-5"/>
                                </svg>
                                <svg width="0" height="0" style="position: absolute;">
                                    <defs>
                                        <linearGradient id="grad-basics" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:#22C55E"/>
                                            <stop offset="100%" style="stop-color:#10B981"/>
                                        </linearGradient>
                                    </defs>
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="guide-card-body">
                        <div style="text-align: center;">
                            <span class="guide-level level-beginner">Beginner</span>
                        </div>
                        <h3>AI Fundamentals</h3>
                        <p class="guide-description">
                            Understand what AI really is, how it works, and why it matters. Learn the basic concepts without technical jargon.
                        </p>
                        <div class="guide-meta">
                            <div class="guide-meta-item">
                                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="8" cy="8" r="6"/>
                                    <path d="M8 4v4l2 2"/>
                                </svg>
                                <span>20 min read</span>
                            </div>
                            <div class="guide-meta-item">
                                <span>5 lessons</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Guide 2: First Steps with ChatGPT -->
                <div class="guide-card" style="cursor: default;">
                    <div class="guide-card-header">
                        <div class="guide-icon-container">
                            <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(16, 185, 129, 0.1)); border: 2px solid rgba(34, 197, 94, 0.3); --glow-rgb: 34, 197, 94; animation: glow 3s ease-in-out infinite;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-chatgpt-start)" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba(34, 197, 94, 0.8));">
                                    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                                    <circle cx="9" cy="10" r="1" fill="#22C55E"/>
                                    <circle cx="12" cy="10" r="1" fill="#22C55E"/>
                                    <circle cx="15" cy="10" r="1" fill="#22C55E"/>
                                </svg>
                                <svg width="0" height="0" style="position: absolute;">
                                    <defs>
                                        <linearGradient id="grad-chatgpt-start" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:#22C55E"/>
                                            <stop offset="100%" style="stop-color:#10B981"/>
                                        </linearGradient>
                                    </defs>
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="guide-card-body">
                        <div style="text-align: center;">
                            <span class="guide-level level-beginner">Beginner</span>
                        </div>
                        <h3>Getting Started with ChatGPT</h3>
                        <p class="guide-description">
                            Your first steps with ChatGPT. Learn how to write effective prompts and get useful answers every time.
                        </p>
                        <div class="guide-meta">
                            <div class="guide-meta-item">
                                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="8" cy="8" r="6"/>
                                    <path d="M8 4v4l2 2"/>
                                </svg>
                                <span>30 min read</span>
                            </div>
                            <div class="guide-meta-item">
                                <span>7 lessons</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Guide 3: AI for Daily Tasks -->
                <div class="guide-card" style="cursor: default;">
                    <div class="guide-card-header">
                        <div class="guide-icon-container">
                            <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(16, 185, 129, 0.1)); border: 2px solid rgba(34, 197, 94, 0.3); --glow-rgb: 34, 197, 94; animation: glow 3s ease-in-out infinite;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-daily)" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba(34, 197, 94, 0.8));">
                                    <path d="M9 11l3 3L22 4"/>
                                    <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
                                </svg>
                                <svg width="0" height="0" style="position: absolute;">
                                    <defs>
                                        <linearGradient id="grad-daily" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:#22C55E"/>
                                            <stop offset="100%" style="stop-color:#10B981"/>
                                        </linearGradient>
                                    </defs>
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="guide-card-body">
                        <div style="text-align: center;">
                            <span class="guide-level level-beginner">Beginner</span>
                        </div>
                        <h3>AI for Everyday Productivity</h3>
                        <p class="guide-description">
                            Use AI to write emails, summarize documents, plan your day, and boost your productivity without technical skills.
                        </p>
                        <div class="guide-meta">
                            <div class="guide-meta-item">
                                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="8" cy="8" r="6"/>
                                    <path d="M8 4v4l2 2"/>
                                </svg>
                                <span>25 min read</span>
                            </div>
                            <div class="guide-meta-item">
                                <span>6 lessons</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
'''

# Contenu pour la section Intermediate
INTERMEDIATE_SECTION = '''
            <!-- Section: Intermediate Guides -->
            <div id="intermediate"></div>
            <div class="section-divider" style="margin-top: var(--space-4xl);">
                <div style="display: flex; align-items: center; justify-content: center; gap: var(--space-md); margin-bottom: var(--space-md);">
                    <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-intermediate-section)" stroke-width="2" width="40" height="40" style="filter: drop-shadow(0 0 10px rgba(59, 130, 246, 0.6));">
                        <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/>
                        <polyline points="17 6 23 6 23 12"/>
                    </svg>
                    <h2>Intermediate Guides</h2>
                </div>
                <p style="color: var(--text-secondary);">Level up your AI skills with advanced techniques and workflows</p>
                <svg width="0" height="0" style="position: absolute;">
                    <defs>
                        <linearGradient id="grad-intermediate-section" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" style="stop-color:#3B82F6"/>
                            <stop offset="100%" style="stop-color:#2563EB"/>
                        </linearGradient>
                    </defs>
                </svg>
            </div>

            <div class="guides-grid">
                <!-- Guide 1: Advanced Prompting -->
                <div class="guide-card" style="cursor: default;">
                    <div class="guide-card-header">
                        <div class="guide-icon-container">
                            <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(37, 99, 235, 0.1)); border: 2px solid rgba(59, 130, 246, 0.3); --glow-rgb: 59, 130, 246; animation: glow 3s ease-in-out infinite;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-prompt)" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba(59, 130, 246, 0.8));">
                                    <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
                                </svg>
                                <svg width="0" height="0" style="position: absolute;">
                                    <defs>
                                        <linearGradient id="grad-prompt" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:#3B82F6"/>
                                            <stop offset="100%" style="stop-color:#2563EB"/>
                                        </linearGradient>
                                    </defs>
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="guide-card-body">
                        <div style="text-align: center;">
                            <span class="guide-level level-intermediate">Intermediate</span>
                        </div>
                        <h3>Advanced Prompt Engineering</h3>
                        <p class="guide-description">
                            Master prompt engineering techniques: chain-of-thought, few-shot learning, role prompting, and structured outputs.
                        </p>
                        <div class="guide-meta">
                            <div class="guide-meta-item">
                                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="8" cy="8" r="6"/>
                                    <path d="M8 4v4l2 2"/>
                                </svg>
                                <span>50 min read</span>
                            </div>
                            <div class="guide-meta-item">
                                <span>10 lessons</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Guide 2: AI Workflow Automation -->
                <div class="guide-card" style="cursor: default;">
                    <div class="guide-card-header">
                        <div class="guide-icon-container">
                            <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(37, 99, 235, 0.1)); border: 2px solid rgba(59, 130, 246, 0.3); --glow-rgb: 59, 130, 246; animation: glow 3s ease-in-out infinite;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-workflow)" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba(59, 130, 246, 0.8));">
                                    <rect x="3" y="3" width="18" height="18" rx="2"/>
                                    <path d="M9 9h6v6H9z"/>
                                    <path d="M9 3v6M15 9h6M15 15h6M9 15v6"/>
                                </svg>
                                <svg width="0" height="0" style="position: absolute;">
                                    <defs>
                                        <linearGradient id="grad-workflow" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:#3B82F6"/>
                                            <stop offset="100%" style="stop-color:#2563EB"/>
                                        </linearGradient>
                                    </defs>
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="guide-card-body">
                        <div style="text-align: center;">
                            <span class="guide-level level-intermediate">Intermediate</span>
                        </div>
                        <h3>AI Workflow Automation</h3>
                        <p class="guide-description">
                            Build automated workflows combining multiple AI tools. Zapier, Make, and custom integrations for maximum efficiency.
                        </p>
                        <div class="guide-meta">
                            <div class="guide-meta-item">
                                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="8" cy="8" r="6"/>
                                    <path d="M8 4v4l2 2"/>
                                </svg>
                                <span>45 min read</span>
                            </div>
                            <div class="guide-meta-item">
                                <span>8 lessons</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Guide 3: Multi-Modal AI -->
                <div class="guide-card" style="cursor: default;">
                    <div class="guide-card-header">
                        <div class="guide-icon-container">
                            <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(37, 99, 235, 0.1)); border: 2px solid rgba(59, 130, 246, 0.3); --glow-rgb: 59, 130, 246; animation: glow 3s ease-in-out infinite;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-multimodal)" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba(59, 130, 246, 0.8));">
                                    <rect x="3" y="3" width="7" height="7" rx="1"/>
                                    <rect x="14" y="3" width="7" height="7" rx="1"/>
                                    <rect x="14" y="14" width="7" height="7" rx="1"/>
                                    <rect x="3" y="14" width="7" height="7" rx="1"/>
                                </svg>
                                <svg width="0" height="0" style="position: absolute;">
                                    <defs>
                                        <linearGradient id="grad-multimodal" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:#3B82F6"/>
                                            <stop offset="100%" style="stop-color:#2563EB"/>
                                        </linearGradient>
                                    </defs>
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="guide-card-body">
                        <div style="text-align: center;">
                            <span class="guide-level level-intermediate">Intermediate</span>
                        </div>
                        <h3>Multi-Modal AI Mastery</h3>
                        <p class="guide-description">
                            Work with text, images, audio, and video together. Create complete projects using GPT-4V, DALL-E, and more.
                        </p>
                        <div class="guide-meta">
                            <div class="guide-meta-item">
                                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="8" cy="8" r="6"/>
                                    <path d="M8 4v4l2 2"/>
                                </svg>
                                <span>55 min read</span>
                            </div>
                            <div class="guide-meta-item">
                                <span>9 lessons</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
'''

# Contenu pour la section Advanced
ADVANCED_SECTION = '''
            <!-- Section: Advanced Guides -->
            <div id="advanced"></div>
            <div class="section-divider" style="margin-top: var(--space-4xl);">
                <div style="display: flex; align-items: center; justify-content: center; gap: var(--space-md); margin-bottom: var(--space-md);">
                    <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-advanced-section)" stroke-width="2" width="40" height="40" style="filter: drop-shadow(0 0 10px rgba(168, 85, 247, 0.6));">
                        <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
                    </svg>
                    <h2>Advanced Guides</h2>
                </div>
                <p style="color: var(--text-secondary);">Expert-level techniques for AI professionals and power users</p>
                <svg width="0" height="0" style="position: absolute;">
                    <defs>
                        <linearGradient id="grad-advanced-section" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" style="stop-color:#A855F7"/>
                            <stop offset="100%" style="stop-color:#7C3AED"/>
                        </linearGradient>
                    </defs>
                </svg>
            </div>

            <div class="guides-grid">
                <!-- Guide 1: Fine-tuning & RAG -->
                <div class="guide-card" style="cursor: default;">
                    <div class="guide-card-header">
                        <div class="guide-icon-container">
                            <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(124, 58, 237, 0.1)); border: 2px solid rgba(168, 85, 247, 0.3); --glow-rgb: 168, 85, 247; animation: glow 3s ease-in-out infinite;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-finetune)" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba(168, 85, 247, 0.8));">
                                    <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
                                    <circle cx="12" cy="12" r="3"/>
                                </svg>
                                <svg width="0" height="0" style="position: absolute;">
                                    <defs>
                                        <linearGradient id="grad-finetune" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:#A855F7"/>
                                            <stop offset="100%" style="stop-color:#7C3AED"/>
                                        </linearGradient>
                                    </defs>
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="guide-card-body">
                        <div style="text-align: center;">
                            <span class="guide-level level-advanced">Advanced</span>
                        </div>
                        <h3>Fine-Tuning & RAG Systems</h3>
                        <p class="guide-description">
                            Build custom AI models with fine-tuning. Implement Retrieval-Augmented Generation for enterprise knowledge bases.
                        </p>
                        <div class="guide-meta">
                            <div class="guide-meta-item">
                                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="8" cy="8" r="6"/>
                                    <path d="M8 4v4l2 2"/>
                                </svg>
                                <span>90 min read</span>
                            </div>
                            <div class="guide-meta-item">
                                <span>12 lessons</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Guide 2: AI Agent Development -->
                <div class="guide-card" style="cursor: default;">
                    <div class="guide-card-header">
                        <div class="guide-icon-container">
                            <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(124, 58, 237, 0.1)); border: 2px solid rgba(168, 85, 247, 0.3); --glow-rgb: 168, 85, 247; animation: glow 3s ease-in-out infinite;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-agent)" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba(168, 85, 247, 0.8));">
                                    <circle cx="12" cy="12" r="3"/>
                                    <path d="M12 1v6m0 6v6M5.64 5.64l4.24 4.24m6.36 6.36l4.24 4.24M1 12h6m6 0h6M5.64 18.36l4.24-4.24m6.36-6.36l4.24-4.24"/>
                                </svg>
                                <svg width="0" height="0" style="position: absolute;">
                                    <defs>
                                        <linearGradient id="grad-agent" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:#A855F7"/>
                                            <stop offset="100%" style="stop-color:#7C3AED"/>
                                        </linearGradient>
                                    </defs>
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="guide-card-body">
                        <div style="text-align: center;">
                            <span class="guide-level level-advanced">Advanced</span>
                        </div>
                        <h3>AI Agent Development</h3>
                        <p class="guide-description">
                            Build autonomous AI agents with LangChain and AutoGPT. Create agents that can reason, plan, and execute complex tasks.
                        </p>
                        <div class="guide-meta">
                            <div class="guide-meta-item">
                                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="8" cy="8" r="6"/>
                                    <path d="M8 4v4l2 2"/>
                                </svg>
                                <span>120 min read</span>
                            </div>
                            <div class="guide-meta-item">
                                <span>15 lessons</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Guide 3: Enterprise AI Implementation -->
                <div class="guide-card" style="cursor: default;">
                    <div class="guide-card-header">
                        <div class="guide-icon-container">
                            <div class="guide-icon-neon" style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(124, 58, 237, 0.1)); border: 2px solid rgba(168, 85, 247, 0.3); --glow-rgb: 168, 85, 247; animation: glow 3s ease-in-out infinite;">
                                <svg viewBox="0 0 24 24" fill="none" stroke="url(#grad-enterprise)" stroke-width="1.5" width="60" height="60" style="filter: drop-shadow(0 0 12px rgba(168, 85, 247, 0.8));">
                                    <rect x="2" y="7" width="20" height="14" rx="2"/>
                                    <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
                                    <path d="M12 11h.01"/>
                                </svg>
                                <svg width="0" height="0" style="position: absolute;">
                                    <defs>
                                        <linearGradient id="grad-enterprise" x1="0%" y1="0%" x2="100%" y2="100%">
                                            <stop offset="0%" style="stop-color:#A855F7"/>
                                            <stop offset="100%" style="stop-color:#7C3AED"/>
                                        </linearGradient>
                                    </defs>
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="guide-card-body">
                        <div style="text-align: center;">
                            <span class="guide-level level-advanced">Advanced</span>
                        </div>
                        <h3>Enterprise AI Implementation</h3>
                        <p class="guide-description">
                            Deploy AI at scale: security, compliance, cost optimization, monitoring, and governance for enterprise environments.
                        </p>
                        <div class="guide-meta">
                            <div class="guide-meta-item">
                                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                                    <circle cx="8" cy="8" r="6"/>
                                    <path d="M8 4v4l2 2"/>
                                </svg>
                                <span>100 min read</span>
                            </div>
                            <div class="guide-meta-item">
                                <span>14 lessons</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
'''

def main():
    file_path = '/home/komet/Desktop/Projekt/AI Tools/GenuisNet.ai/pages/guides.html'

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver où insérer les sections (avant le CTA Section)
    cta_pattern = r'<!-- CTA Section -->'

    # Insérer les trois sections avant le CTA
    replacement = BEGINNER_SECTION + '\n' + INTERMEDIATE_SECTION + '\n' + ADVANCED_SECTION + '\n\n            <!-- CTA Section -->'

    content = re.sub(cta_pattern, replacement, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Sections ajoutées avec succès!")
    print("\n📊 Contenu ajouté:")
    print("  ✓ Section Beginner (3 guides)")
    print("  ✓ Section Intermediate (3 guides)")
    print("  ✓ Section Advanced (3 guides)")
    print("\n🎨 Icônes high-tech:")
    print("  ✓ Beginner: Vert (#22C55E) - Layers, Chat, Checklist")
    print("  ✓ Intermediate: Bleu (#3B82F6) - Wrench, Grid, Squares")
    print("  ✓ Advanced: Violet (#A855F7) - Lightning, Network, Briefcase")

if __name__ == '__main__':
    main()
