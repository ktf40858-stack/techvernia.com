/* ============================================
   TechVernia - Main JavaScript
   Core functionality and interactions
   ============================================ */

console.log('⚙️ main.js loaded');

// ============================================
// DOM Elements
// ============================================
const navbar = document.getElementById('navbar');
const navMenu = document.getElementById('nav-menu');
const menuToggle = document.getElementById('menu-toggle');
// Theme toggle removed - site is 100% dark mode
// const themeToggle = document.getElementById('theme-toggle');
const searchBtn = document.getElementById('search-btn');
const searchModal = document.getElementById('search-modal');
const searchInput = document.getElementById('search-input');
const newsletterForm = document.getElementById('newsletter-form');

// ============================================
// Navigation
// ============================================
class Navigation {
    constructor() {
        this.navbar = navbar;
        this.navMenu = navMenu;
        this.menuToggle = menuToggle;
        this.isMenuOpen = false;
        this.lastScrollY = 0;

        this.init();
    }

    init() {
        this.setupScrollListener();
        this.setupMobileMenu();
        this.setupDropdowns();
        this.setupSmoothScroll();
    }

    setupScrollListener() {
        window.addEventListener('scroll', () => {
            const currentScrollY = window.scrollY;

            // Add scrolled class when scrolled
            if (currentScrollY > 50) {
                this.navbar.classList.add('scrolled');
            } else {
                this.navbar.classList.remove('scrolled');
            }

            // Hide/show navbar on scroll (optional)
            // if (currentScrollY > this.lastScrollY && currentScrollY > 200) {
            //     this.navbar.style.transform = 'translateY(-100%)';
            // } else {
            //     this.navbar.style.transform = 'translateY(0)';
            // }

            this.lastScrollY = currentScrollY;
        });
    }

    setupMobileMenu() {
        if (!this.menuToggle || !this.navMenu) return;

        this.menuToggle.addEventListener('click', () => {
            this.toggleMenu();
        });

        // Close menu when clicking a link
        this.navMenu.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                if (this.isMenuOpen) {
                    this.toggleMenu();
                }
            });
        });

        // Close menu on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.isMenuOpen) {
                this.toggleMenu();
            }
        });
    }

    toggleMenu() {
        this.isMenuOpen = !this.isMenuOpen;
        this.navMenu.classList.toggle('active', this.isMenuOpen);
        this.menuToggle.classList.toggle('active', this.isMenuOpen);
        document.body.style.overflow = this.isMenuOpen ? 'hidden' : '';
    }

    setupDropdowns() {
        const dropdowns = document.querySelectorAll('.dropdown');

        dropdowns.forEach(dropdown => {
            const toggle = dropdown.querySelector('.dropdown-toggle');
            const menu = dropdown.querySelector('.dropdown-menu');

            if (!toggle || !menu) return;

            // On mobile: toggle dropdown on click (but still allow navigation)
            toggle.addEventListener('click', (e) => {
                if (window.innerWidth <= 1024) {
                    // Only prevent default if dropdown is not already active
                    // This allows: first click opens dropdown, second click navigates
                    if (!dropdown.classList.contains('active')) {
                        e.preventDefault();
                        dropdown.classList.add('active');
                    }
                    // If already active, let the link navigate normally
                }
            });
        });

        // Close dropdowns when clicking outside
        document.addEventListener('click', (e) => {
            dropdowns.forEach(dropdown => {
                if (!dropdown.contains(e.target)) {
                    dropdown.classList.remove('active');
                }
            });
        });
    }

    setupSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', (e) => {
                const href = anchor.getAttribute('href');
                if (href === '#') return;

                e.preventDefault();
                const target = document.querySelector(href);

                if (target) {
                    const navHeight = this.navbar.offsetHeight;
                    const targetPosition = target.getBoundingClientRect().top + window.scrollY - navHeight;

                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }
}

// ============================================
// Theme Manager - DISABLED (100% Dark Mode)
// ============================================
// Site is now permanently in dark mode
// Theme manager code removed

// ============================================
// Search Modal
// ============================================
class SearchModal {
    constructor() {
        this.btn = searchBtn;
        this.modal = searchModal;
        this.input = searchInput;
        this.isOpen = false;

        this.init();
    }

    init() {
        if (!this.btn || !this.modal) return;

        this.setupEventListeners();
    }

    setupEventListeners() {
        // Open modal
        this.btn.addEventListener('click', () => this.open());

        // Close modal on background click
        this.modal.addEventListener('click', (e) => {
            if (e.target === this.modal) {
                this.close();
            }
        });

        // Close on escape
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.isOpen) {
                this.close();
            }

            // Open on Cmd/Ctrl + K
            if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                e.preventDefault();
                this.toggle();
            }
        });

        // Search input handling
        if (this.input) {
            this.input.addEventListener('input', (e) => {
                this.handleSearch(e.target.value);
            });
        }
    }

    open() {
        this.isOpen = true;
        this.modal.classList.add('active');
        document.body.style.overflow = 'hidden';

        if (this.input) {
            setTimeout(() => this.input.focus(), 100);
        }
    }

    close() {
        this.isOpen = false;
        this.modal.classList.remove('active');
        document.body.style.overflow = '';

        if (this.input) {
            this.input.value = '';
        }
    }

    toggle() {
        if (this.isOpen) {
            this.close();
        } else {
            this.open();
        }
    }

    handleSearch(query) {
        // Implement search logic here
        // This is a placeholder for actual search functionality
        console.log('Searching for:', query);

        // You could implement:
        // - Client-side search through tool data
        // - API call to search endpoint
        // - Fuzzy matching
        // - Category filtering
    }
}

// ============================================
// Newsletter Form
// ============================================
class NewsletterForm {
    constructor() {
        this.form = newsletterForm;

        this.init();
    }

    init() {
        if (!this.form) return;

        this.form.addEventListener('submit', (e) => this.handleSubmit(e));
    }

    async handleSubmit(e) {
        e.preventDefault();

        const formData = new FormData(this.form);
        const email = this.form.querySelector('input[type="email"]').value;
        const submitBtn = this.form.querySelector('button[type="submit"]');

        // Validate email
        if (!this.validateEmail(email)) {
            this.showMessage('Please enter a valid email address', 'error');
            return;
        }

        // Disable button during submission
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span class="spinner"></span>';

        try {
            // Simulate API call (replace with actual endpoint)
            await this.simulateSubmit(email);

            this.showMessage('Successfully subscribed! Check your inbox.', 'success');
            this.form.reset();
        } catch (error) {
            this.showMessage('Something went wrong. Please try again.', 'error');
        } finally {
            submitBtn.disabled = false;
            submitBtn.innerHTML = window.i18n?.getTranslation('newsletter.btn') || 'Subscribe';
        }
    }

    validateEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    simulateSubmit(email) {
        return new Promise((resolve) => {
            setTimeout(resolve, 1500);
        });
    }

    showMessage(message, type) {
        // Remove existing message
        const existingMsg = this.form.querySelector('.form-message');
        if (existingMsg) existingMsg.remove();

        // Create message element
        const msgEl = document.createElement('p');
        msgEl.className = `form-message form-message--${type}`;
        msgEl.textContent = message;
        msgEl.style.cssText = `
            margin-top: 1rem;
            padding: 0.75rem 1rem;
            border-radius: 0.5rem;
            font-size: 0.875rem;
            background: ${type === 'success' ? 'rgba(16, 185, 129, 0.1)' : 'rgba(239, 68, 68, 0.1)'};
            color: ${type === 'success' ? '#10B981' : '#EF4444'};
            border: 1px solid ${type === 'success' ? 'rgba(16, 185, 129, 0.2)' : 'rgba(239, 68, 68, 0.2)'};
        `;

        this.form.appendChild(msgEl);

        // Remove after 5 seconds
        setTimeout(() => msgEl.remove(), 5000);
    }
}

// ============================================
// Tool Cards Interaction
// ============================================
class ToolCards {
    constructor() {
        this.cards = document.querySelectorAll('.tool-card, .category-card');

        this.init();
    }

    init() {
        this.setupHoverEffects();
    }

    setupHoverEffects() {
        this.cards.forEach(card => {
            card.addEventListener('mouseenter', (e) => {
                this.handleMouseEnter(e, card);
            });

            card.addEventListener('mousemove', (e) => {
                this.handleMouseMove(e, card);
            });

            card.addEventListener('mouseleave', (e) => {
                this.handleMouseLeave(e, card);
            });
        });
    }

    handleMouseEnter(e, card) {
        card.style.transition = 'transform 0.1s ease';
    }

    handleMouseMove(e, card) {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = (y - centerY) / 20;
        const rotateY = (centerX - x) / 20;

        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-5px)`;
    }

    handleMouseLeave(e, card) {
        card.style.transition = 'transform 0.5s ease';
        card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
    }
}

// ============================================
// Affiliate Link Tracking
// ============================================
class AffiliateTracker {
    constructor() {
        this.affiliateLinks = document.querySelectorAll('a[href*="?ref="], a[data-affiliate]');

        this.init();
    }

    init() {
        this.affiliateLinks.forEach(link => {
            link.addEventListener('click', (e) => this.trackClick(e, link));
        });
    }

    trackClick(e, link) {
        const toolName = link.getAttribute('data-tool') || link.textContent.trim();
        const destination = link.href;

        // Log affiliate click (replace with actual analytics)
        console.log('Affiliate click:', {
            tool: toolName,
            destination: destination,
            timestamp: new Date().toISOString()
        });

        // You could send this to:
        // - Google Analytics
        // - Custom analytics endpoint
        // - Facebook Pixel
        // etc.
    }
}

// ============================================
// Lazy Loading Images
// ============================================
class LazyLoader {
    constructor() {
        this.images = document.querySelectorAll('img[data-src]');

        this.init();
    }

    init() {
        if ('IntersectionObserver' in window) {
            this.setupObserver();
        } else {
            this.loadAllImages();
        }
    }

    setupObserver() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.loadImage(entry.target);
                    observer.unobserve(entry.target);
                }
            });
        }, {
            rootMargin: '50px 0px'
        });

        this.images.forEach(img => observer.observe(img));
    }

    loadImage(img) {
        const src = img.getAttribute('data-src');
        if (!src) return;

        img.src = src;
        img.removeAttribute('data-src');
        img.classList.add('loaded');
    }

    loadAllImages() {
        this.images.forEach(img => this.loadImage(img));
    }
}

// ============================================
// Language Selector
// ============================================
class LanguageSelector {
    constructor() {
        console.log('🌐 LanguageSelector constructor called');
        this.selector = document.querySelector('.language-selector');
        this.langBtn = document.getElementById('lang-btn');
        this.langDropdown = document.getElementById('lang-dropdown');
        this.langOptions = document.querySelectorAll('.lang-option');
        this.langCurrent = document.querySelector('.lang-current');
        this.isOpen = false;
        this.currentLang = localStorage.getItem('selectedLanguage') || 'en';

        console.log('🔍 Elements found:', {
            selector: !!this.selector,
            langBtn: !!this.langBtn,
            langDropdown: !!this.langDropdown,
            langOptions: this.langOptions.length,
            langCurrent: !!this.langCurrent
        });

        this.init();
    }

    init() {
        if (!this.selector || !this.langBtn || !this.langDropdown) {
            console.warn('⚠️ LanguageSelector elements not found - skipping initialization');
            return;
        }

        console.log('⚙️ Setting up LanguageSelector event listeners');
        this.setupEventListeners();
        this.updateCurrentLanguage();
        console.log('✅ LanguageSelector initialized successfully');
    }

    setupEventListeners() {
        // Toggle dropdown
        this.langBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            this.toggle();
        });

        // Select language
        this.langOptions.forEach(option => {
            option.addEventListener('click', (e) => {
                e.stopPropagation();
                const lang = option.getAttribute('data-lang');
                this.selectLanguage(lang);
            });
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if (!this.selector.contains(e.target)) {
                this.close();
            }
        });

        // Close on escape
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && this.isOpen) {
                this.close();
            }
        });
    }

    toggle() {
        if (this.isOpen) {
            this.close();
        } else {
            this.open();
        }
    }

    open() {
        this.isOpen = true;
        this.selector.classList.add('active');
        console.log('🔓 Dropdown opened');
    }

    close() {
        this.isOpen = false;
        this.selector.classList.remove('active');
        console.log('🔒 Dropdown closed');
    }

    selectLanguage(lang) {
        console.log('🎯 Language selected:', lang);
        this.currentLang = lang;
        localStorage.setItem('selectedLanguage', lang);

        // Update active state
        this.langOptions.forEach(option => {
            option.classList.toggle('active', option.getAttribute('data-lang') === lang);
        });

        // Update current language display
        this.updateCurrentLanguage();

        // Call i18n.setLanguage to actually translate the page
        if (window.i18n && window.i18n.setLanguage) {
            console.log('🌍 Calling window.i18n.setLanguage(' + lang + ')');
            window.i18n.setLanguage(lang);
        } else {
            console.warn('⚠️ window.i18n.setLanguage not available');
            // Fallback: Dispatch event for i18n files to listen to
            const event = new CustomEvent('languageChanged', {
                detail: { language: lang }
            });
            console.log('📢 Dispatching languageChanged event:', lang);
            document.dispatchEvent(event);
        }

        // Close dropdown
        this.close();
    }

    updateCurrentLanguage() {
        const langMap = {
            'en': 'EN',
            'es': 'ES',
            'fr': 'FR',
            'de': 'DE',
            'pt': 'PT',
            'zh': 'ZH',
            'ja': 'JA',
            'ko': 'KO',
            'ar': 'AR',
            'hi': 'HI'
        };

        if (this.langCurrent) {
            this.langCurrent.textContent = langMap[this.currentLang] || 'EN';
        }

        // Update active option
        this.langOptions.forEach(option => {
            option.classList.toggle('active', option.getAttribute('data-lang') === this.currentLang);
        });
    }
}

// ============================================
// Cookie Consent (GDPR)
// ============================================
class CookieConsent {
    constructor() {
        this.consentKey = 'cookie_consent';

        this.init();
    }

    init() {
        if (!this.hasConsent()) {
            this.showBanner();
        }
    }

    hasConsent() {
        return localStorage.getItem(this.consentKey) === 'accepted';
    }

    showBanner() {
        const banner = document.createElement('div');
        banner.className = 'cookie-banner';
        banner.innerHTML = `
            <div class="cookie-content">
                <p>We use cookies to enhance your experience. By continuing to visit this site you agree to our use of cookies.</p>
                <div class="cookie-actions">
                    <button class="btn btn-primary cookie-accept">Accept</button>
                    <button class="btn btn-outline cookie-settings">Settings</button>
                </div>
            </div>
        `;

        banner.style.cssText = `
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: var(--bg-card);
            border-top: 1px solid var(--border-color);
            padding: 1.5rem;
            z-index: 1000;
            transform: translateY(100%);
            transition: transform 0.3s ease;
        `;

        document.body.appendChild(banner);

        // Animate in
        setTimeout(() => {
            banner.style.transform = 'translateY(0)';
        }, 100);

        // Accept button
        banner.querySelector('.cookie-accept').addEventListener('click', () => {
            this.acceptCookies();
            this.hideBanner(banner);
        });

        // Settings button
        banner.querySelector('.cookie-settings').addEventListener('click', () => {
            // Open settings modal or redirect to privacy page
            window.location.href = 'pages/privacy.html';
        });
    }

    acceptCookies() {
        localStorage.setItem(this.consentKey, 'accepted');
    }

    hideBanner(banner) {
        banner.style.transform = 'translateY(100%)';
        setTimeout(() => banner.remove(), 300);
    }
}

// ============================================
// Performance Monitoring
// ============================================
class PerformanceMonitor {
    constructor() {
        this.init();
    }

    init() {
        // Log Core Web Vitals
        if ('PerformanceObserver' in window) {
            this.observeLCP();
            this.observeFID();
            this.observeCLS();
        }
    }

    observeLCP() {
        try {
            const observer = new PerformanceObserver((list) => {
                const entries = list.getEntries();
                const lastEntry = entries[entries.length - 1];
                console.log('LCP:', lastEntry.startTime);
            });
            observer.observe({ type: 'largest-contentful-paint', buffered: true });
        } catch (e) {
            // LCP not supported
        }
    }

    observeFID() {
        try {
            const observer = new PerformanceObserver((list) => {
                const entries = list.getEntries();
                entries.forEach(entry => {
                    console.log('FID:', entry.processingStart - entry.startTime);
                });
            });
            observer.observe({ type: 'first-input', buffered: true });
        } catch (e) {
            // FID not supported
        }
    }

    observeCLS() {
        try {
            let clsValue = 0;
            const observer = new PerformanceObserver((list) => {
                const entries = list.getEntries();
                entries.forEach(entry => {
                    if (!entry.hadRecentInput) {
                        clsValue += entry.value;
                    }
                });
                console.log('CLS:', clsValue);
            });
            observer.observe({ type: 'layout-shift', buffered: true });
        } catch (e) {
            // CLS not supported
        }
    }
}

// ============================================
// Initialize Everything
// ============================================
function initApp() {
    // Core functionality
    new Navigation();
    new LanguageSelector();
    // new ThemeManager(); // Disabled - 100% dark mode
    new SearchModal();
    new NewsletterForm();

    // UI enhancements
    new ToolCards();
    new LazyLoader();

    // Tracking & compliance
    new AffiliateTracker();
    new CookieConsent();

    // Performance (dev only)
    if (window.location.hostname === 'localhost') {
        new PerformanceMonitor();
    }

    console.log('✅ TechVernia initialized');
    console.log('📊 All modules loaded successfully');
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
} else {
    initApp();
}

// Export for external use
window.app = {
    Navigation,
    SearchModal,
    NewsletterForm,
    ToolCards,
    AffiliateTracker,
    init: initApp
};
