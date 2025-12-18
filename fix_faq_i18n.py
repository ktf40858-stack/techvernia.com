#!/usr/bin/env python3
"""
Script pour corriger les FAQ et ajouter data-i18n
"""

def fix_faq_i18n():
    file_path = "GenuisNet.ai/pages/reviews/chatbots/chatgpt.html"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # FAQ replacements - exact text avec les espaces
    faq_replacements = [
        # FAQ 1
        (
            '<div class="faq-question">\n                        Is ChatGPT free to use?\n                        <span>+</span>',
            '<div class="faq-question">\n                        <span data-i18n="review.chatgpt.faq1.question">Is ChatGPT free to use?</span>\n                        <span>+</span>'
        ),
        (
            '<div class="faq-answer">\n                        Yes, ChatGPT offers a free tier that includes access to GPT-4o mini and limited GPT-4 usage. For full access to GPT-4, DALL-E, Code Interpreter, and other premium features, you\'ll need ChatGPT Plus at $20/month.\n                    </div>',
            '<div class="faq-answer">\n                        <span data-i18n="review.chatgpt.faq1.answer">Yes, ChatGPT offers a free tier that includes access to GPT-4o mini and limited GPT-4 usage. For full access to GPT-4, DALL-E, Code Interpreter, and other premium features, you\'ll need ChatGPT Plus at $20/month.</span>\n                    </div>'
        ),

        # FAQ 2
        (
            '<div class="faq-question">\n                        What\'s the difference between GPT-3.5 and GPT-4?\n                        <span>+</span>',
            '<div class="faq-question">\n                        <span data-i18n="review.chatgpt.faq2.question">What\'s the difference between GPT-3.5 and GPT-4?</span>\n                        <span>+</span>'
        ),
        (
            '<div class="faq-answer">\n                        GPT-4 is significantly more capable than GPT-3.5. It offers better reasoning, more accurate responses, longer context window (128K vs 4K tokens), vision capabilities, and handles complex tasks much better. GPT-4 is available to Plus subscribers, while free users get limited access.\n                    </div>',
            '<div class="faq-answer">\n                        <span data-i18n="review.chatgpt.faq2.answer">GPT-4 is significantly more capable than GPT-3.5. It offers better reasoning, more accurate responses, longer context window (128K vs 4K tokens), vision capabilities, and handles complex tasks much better. GPT-4 is available to Plus subscribers, while free users get limited access.</span>\n                    </div>'
        ),

        # FAQ 3
        (
            '<div class="faq-question">\n                        Can ChatGPT access the internet?\n                        <span>+</span>',
            '<div class="faq-question">\n                        <span data-i18n="review.chatgpt.faq3.question">Can ChatGPT access the internet?</span>\n                        <span>+</span>'
        ),
        (
            '<div class="faq-answer">\n                        Yes, ChatGPT Plus users have access to web browsing capabilities, allowing it to search the internet for current information. Free users have limited browsing access. You can also enable or disable this feature in settings.\n                    </div>',
            '<div class="faq-answer">\n                        <span data-i18n="review.chatgpt.faq3.answer">Yes, ChatGPT Plus users have access to web browsing capabilities, allowing it to search the internet for current information. Free users have limited browsing access. You can also enable or disable this feature in settings.</span>\n                    </div>'
        ),

        # FAQ 4
        (
            '<div class="faq-question">\n                        Is ChatGPT good for coding?\n                        <span>+</span>',
            '<div class="faq-question">\n                        <span data-i18n="review.chatgpt.faq4.question">Is ChatGPT good for coding?</span>\n                        <span>+</span>'
        ),
        (
            '<div class="faq-answer">\n                        ChatGPT is excellent for coding assistance. It can write, debug, explain, and optimize code in most programming languages. The Code Interpreter feature allows it to actually execute Python code. However, for complex coding projects, tools like GitHub Copilot or Claude might be more specialized.\n                    </div>',
            '<div class="faq-answer">\n                        <span data-i18n="review.chatgpt.faq4.answer">ChatGPT is excellent for coding assistance. It can write, debug, explain, and optimize code in most programming languages. The Code Interpreter feature allows it to actually execute Python code. However, for complex coding projects, tools like GitHub Copilot or Claude might be more specialized.</span>\n                    </div>'
        ),

        # FAQ 5
        (
            '<div class="faq-question">\n                        How does ChatGPT compare to Claude?\n                        <span>+</span>',
            '<div class="faq-question">\n                        <span data-i18n="review.chatgpt.faq5.question">How does ChatGPT compare to Claude?</span>\n                        <span>+</span>'
        ),
        (
            '<div class="faq-answer">\n                        Both are excellent AI assistants. ChatGPT excels in versatility, ecosystem (Custom GPTs, plugins), and image generation. Claude offers a larger context window (200K vs 128K), often produces better code, and tends to be more nuanced in responses. Claude lacks image generation but excels at long document analysis.\n                    </div>',
            '<div class="faq-answer">\n                        <span data-i18n="review.chatgpt.faq5.answer">Both are excellent AI assistants. ChatGPT excels in versatility, ecosystem (Custom GPTs, plugins), and image generation. Claude offers a larger context window (200K vs 128K), often produces better code, and tends to be more nuanced in responses. Claude lacks image generation but excels at long document analysis.</span>\n                    </div>'
        ),
    ]

    count = 0
    for old, new in faq_replacements:
        if old in content:
            content = content.replace(old, new)
            count += 1
            print(f"✅ FAQ {(count+1)//2}")

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n🎉 {count} éléments FAQ corrigés!")
    else:
        print("\n⚠️  Aucune modification (peut-être déjà fait)")

if __name__ == "__main__":
    fix_faq_i18n()
