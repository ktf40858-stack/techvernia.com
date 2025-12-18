#!/usr/bin/env python3
"""
Générateur de pages de certification individuelles pour Cybersecurity
Crée des pages HTML détaillées pour chaque certification (format identique à CCNA)
"""

import os
import re

# Template HTML pour une page de certification
CERT_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>{cert_name} - Complete Guide & Review | GenuisNet.ai</title>
    <meta content="{meta_description}" name="description"/>
    <link href="../../assets/css/styles.css" rel="stylesheet"/>
    <link href="../../assets/images/favicon.png" rel="icon" type="image/png"/>
    <style>
        :root {{
            --bg-primary: #0a0e27;
            --bg-secondary: #111530;
            --bg-card: #1a1f3a;
            --text-primary: #e2e8f0;
            --text-secondary: #94a3b8;
            --text-tertiary: #64748b;
            --accent-color: {brand_color};
            --accent-hover: {brand_color_dark};
            --border-color: rgba(148, 163, 184, 0.1);
            --space-xs: 0.25rem;
            --space-sm: 0.5rem;
            --space-md: 1rem;
            --space-lg: 1.5rem;
            --space-xl: 2rem;
            --space-2xl: 3rem;
            --space-3xl: 4rem;
            --space-4xl: 6rem;
            --text-xs: 0.75rem;
            --text-sm: 0.875rem;
            --text-base: 1rem;
            --text-lg: 1.125rem;
            --text-xl: 1.25rem;
            --text-2xl: 1.5rem;
            --text-3xl: 1.875rem;
            --text-4xl: 2.25rem;
            --radius-sm: 0.25rem;
            --radius-md: 0.5rem;
            --radius-lg: 0.75rem;
            --radius-xl: 1rem;
        }}

        [data-theme="light"] {{
            --bg-primary: #f8fafc;
            --bg-secondary: #f1f5f9;
            --bg-card: #ffffff;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --text-tertiary: #64748b;
            --border-color: rgba(15, 23, 42, 0.1);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
            overflow-x: hidden;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 var(--space-lg);
        }}

        .cert-hero {{
            padding: calc(80px + var(--space-4xl)) var(--space-lg) var(--space-3xl);
            background: linear-gradient(135deg, rgba({brand_rgb}, 0.1) 0%, rgba({brand_rgb}, 0.05) 100%);
            text-align: center;
        }}

        .cert-badge {{
            width: 180px;
            height: 180px;
            margin: 0 auto var(--space-xl);
        }}

        .cert-badge img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
        }}

        .cert-hero h1 {{
            font-size: clamp(var(--text-2xl), 5vw, var(--text-4xl));
            font-weight: 800;
            margin-bottom: var(--space-sm);
        }}

        .cert-level {{
            color: var(--accent-color);
            font-size: var(--text-xl);
            font-weight: 600;
            margin-bottom: var(--space-lg);
        }}

        .cert-meta {{
            display: flex;
            gap: var(--space-xl);
            justify-content: center;
            flex-wrap: wrap;
            margin-top: var(--space-lg);
        }}

        .meta-item {{
            display: flex;
            align-items: center;
            gap: var(--space-xs);
            color: var(--text-secondary);
            font-size: var(--text-sm);
        }}

        .review-section {{
            padding: var(--space-3xl) 0;
            border-bottom: 1px solid var(--border-color);
        }}

        .review-section h2 {{
            display: flex;
            align-items: center;
            gap: var(--space-md);
            font-size: var(--text-2xl);
            margin-bottom: var(--space-xl);
            color: var(--text-primary);
        }}

        .review-section h3 {{
            font-size: var(--text-xl);
            margin: var(--space-xl) 0 var(--space-md);
            color: var(--text-primary);
        }}

        .review-section p {{
            color: var(--text-secondary);
            line-height: 1.8;
            margin-bottom: var(--space-md);
        }}

        .review-section ul {{
            list-style: none;
            padding: 0;
        }}

        .review-section ul li {{
            padding: var(--space-sm) 0;
            padding-left: var(--space-lg);
            color: var(--text-secondary);
            position: relative;
        }}

        .review-section ul li:before {{
            content: "▹";
            position: absolute;
            left: 0;
            color: var(--accent-color);
            font-weight: bold;
        }}

        .info-box {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: var(--space-xl);
            margin: var(--space-xl) 0;
        }}

        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: var(--space-lg);
            margin: var(--space-xl) 0;
        }}

        .info-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: var(--space-lg);
        }}

        .info-card h4 {{
            color: var(--accent-color);
            font-size: var(--text-sm);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: var(--space-sm);
        }}

        .info-card .value {{
            color: var(--text-primary);
            font-size: var(--text-xl);
            font-weight: 700;
        }}

        .highlight-box {{
            background: linear-gradient(135deg, rgba({brand_rgb}, 0.05) 0%, rgba({brand_rgb}, 0.02) 100%);
            border-radius: var(--radius-lg);
            border-left: 4px solid var(--accent-color);
            padding: var(--space-xl);
            margin: var(--space-xl) 0;
        }}

        .neon-icon {{
            width: 24px;
            height: 24px;
            stroke: var(--accent-color);
        }}

        .navbar {{
            position: fixed;
            top: 0;
            width: 100%;
            background: var(--bg-secondary);
            z-index: 1000;
            padding: var(--space-md) 0;
            border-bottom: 1px solid var(--border-color);
        }}

        @media (max-width: 768px) {{
            .cert-meta {{
                flex-direction: column;
                gap: var(--space-md);
            }}

            .info-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
<nav class="navbar">
    <div class="container">
        <a href="../../index.html" style="color: var(--accent-color); text-decoration: none; font-weight: 700; font-size: var(--text-lg);">← Back to GenuisNet.ai</a>
    </div>
</nav>

<header class="cert-hero">
    <div class="container">
        <div class="cert-badge">
            <img src="../../assets/images/certifications/{badge_image}" alt="{cert_name} Badge"/>
        </div>
        <h1>{cert_full_name}</h1>
        <div class="cert-level">{level}</div>
        <p style="max-width: 800px; margin: 0 auto; color: var(--text-secondary); font-size: var(--text-lg);">{hero_description}</p>

        <div class="cert-meta">
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <span>Exam: {exam_code}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
                </svg>
                <span>{duration}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <line x1="12" x2="12" y1="1" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"></path>
                </svg>
                <span>{cost}</span>
            </div>
            <div class="meta-item">
                <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                </svg>
                <span>4.{rating}/5 Rating</span>
            </div>
        </div>
    </div>
</header>

<main class="container">
    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                <rect height="4" rx="1" ry="1" width="8" x="8" y="2"></rect>
            </svg>
            Overview
        </h2>
        {overview_paragraphs}
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
            </svg>
            Key Topics Covered
        </h2>
        <p>{topics_intro}</p>
        <ul>
            {topics_list}
        </ul>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <circle cx="12" cy="12" r="10"></circle>
                <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path>
                <line x1="12" x2="12.01" y1="17" y2="17"></line>
            </svg>
            Why This Certification Matters for {tool_name}
        </h2>
        <div class="highlight-box">
            <p>{relevance_text}</p>
        </div>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            Exam Information
        </h2>

        <div class="info-grid">
            <div class="info-card">
                <h4>Exam Code</h4>
                <div class="value">{exam_code}</div>
            </div>
            <div class="info-card">
                <h4>Duration</h4>
                <div class="value">{duration}</div>
            </div>
            <div class="info-card">
                <h4>Exam Cost</h4>
                <div class="value">{cost}</div>
            </div>
            <div class="info-card">
                <h4>Validity Period</h4>
                <div class="value">{validity}</div>
            </div>
        </div>

        <div class="info-box">
            <h3>Exam Format</h3>
            <p>{exam_format}</p>

            <h3>Prerequisites</h3>
            <p>{prerequisites}</p>
        </div>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
            </svg>
            Study Resources
        </h2>
        <p>Recommended resources for preparing for this certification:</p>
        <ul>
            {study_resources}
        </ul>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
            </svg>
            Career Opportunities
        </h2>
        <p>This certification opens doors to the following career paths:</p>
        <ul>
            {career_paths}
        </ul>

        <div class="info-box">
            <h3>Expected Salary Range</h3>
            <p style="font-size: var(--text-xl); color: var(--accent-color); font-weight: 700; margin-top: var(--space-sm);">{salary_range}</p>
            <p style="margin-top: var(--space-md); font-size: var(--text-sm);">Salary ranges vary by location, experience, and company size. These figures represent typical ranges in the United States market.</p>
        </div>
    </section>

    <section class="review-section">
        <h2>
            <svg class="neon-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M9 5l7 7-7 7"></path>
            </svg>
            Next Steps
        </h2>
        <div class="highlight-box">
            <p>{next_steps}</p>
        </div>

        <p style="margin-top: var(--space-xl);">Ready to get started? Visit the <a href="{vendor_url}" style="color: var(--accent-color);">{vendor_name} Training Portal</a> for official training materials and exam registration.</p>

        <p style="margin-top: var(--space-md);">Download your digital badge from <a href="https://www.credly.com" style="color: var(--accent-color);">Credly</a> (if available) after passing the exam to showcase your achievement on LinkedIn and other professional platforms.</p>
    </section>
</main>

<footer style="background: var(--bg-secondary); padding: var(--space-xl) 0; margin-top: var(--space-4xl); border-top: 1px solid var(--border-color); text-align: center; color: var(--text-tertiary);">
    <div class="container">
        <p>&copy; 2025 GenuisNet.ai. All rights reserved.</p>
        <p style="margin-top: var(--space-sm); font-size: var(--text-sm);">{trademark_text}</p>
    </div>
</footer>

</body>
</html>"""

def hex_to_rgb(hex_color):
    """Convert hex color to RGB values"""
    hex_color = hex_color.lstrip('#')
    return ', '.join(str(int(hex_color[i:i+2], 16)) for i in (0, 2, 4))

def darken_color(hex_color):
    """Darken a hex color by 20%"""
    hex_color = hex_color.lstrip('#')
    rgb = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
    rgb = [max(0, int(c * 0.8)) for c in rgb]
    return '#' + ''.join(f'{c:02x}' for c in rgb)

# Suite du fichier dans le prochain message car trop long...
print("Script de génération chargé (partie 1/2)...")
