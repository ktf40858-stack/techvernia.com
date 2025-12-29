/* ============================================
   GenuisNet.ai - Animation Engine
   Neural network backgrounds, particles, and effects
   ============================================ */

console.log('🎨 animations.js loaded');

// ============================================
// Neural Network Background
// ============================================
class NeuralNetwork {
    constructor(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.nodes = [];
        this.connections = [];
        this.mouse = { x: null, y: null, radius: 150 };
        this.nodeCount = 80;
        this.connectionDistance = 150;
        this.animationId = null;

        this.init();
        this.setupEventListeners();
        this.animate();
    }

    init() {
        this.resize();
        this.createNodes();
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    createNodes() {
        this.nodes = [];
        for (let i = 0; i < this.nodeCount; i++) {
            this.nodes.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5,
                radius: Math.random() * 2 + 1,
                color: this.getRandomColor()
            });
        }
    }

    getRandomColor() {
        const colors = [
            'rgba(0, 217, 255, 0.8)',   // Cyan
            'rgba(124, 58, 237, 0.8)',  // Purple
            'rgba(16, 185, 129, 0.6)',  // Green
            'rgba(236, 72, 153, 0.5)'   // Pink
        ];
        return colors[Math.floor(Math.random() * colors.length)];
    }

    setupEventListeners() {
        window.addEventListener('resize', () => {
            this.resize();
            this.createNodes();
        });

        window.addEventListener('mousemove', (e) => {
            this.mouse.x = e.clientX;
            this.mouse.y = e.clientY;
        });

        window.addEventListener('mouseout', () => {
            this.mouse.x = null;
            this.mouse.y = null;
        });
    }

    drawNode(node) {
        this.ctx.beginPath();
        this.ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
        this.ctx.fillStyle = node.color;
        this.ctx.fill();
    }

    drawConnection(node1, node2, distance) {
        const opacity = 1 - (distance / this.connectionDistance);
        this.ctx.beginPath();
        this.ctx.moveTo(node1.x, node1.y);
        this.ctx.lineTo(node2.x, node2.y);

        const gradient = this.ctx.createLinearGradient(node1.x, node1.y, node2.x, node2.y);
        gradient.addColorStop(0, `rgba(0, 217, 255, ${opacity * 0.3})`);
        gradient.addColorStop(1, `rgba(124, 58, 237, ${opacity * 0.3})`);

        this.ctx.strokeStyle = gradient;
        this.ctx.lineWidth = 1;
        this.ctx.stroke();
    }

    updateNode(node) {
        // Mouse interaction
        if (this.mouse.x !== null && this.mouse.y !== null) {
            const dx = this.mouse.x - node.x;
            const dy = this.mouse.y - node.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance < this.mouse.radius) {
                const force = (this.mouse.radius - distance) / this.mouse.radius;
                node.vx -= (dx / distance) * force * 0.02;
                node.vy -= (dy / distance) * force * 0.02;
            }
        }

        // Update position
        node.x += node.vx;
        node.y += node.vy;

        // Boundary check with bounce
        if (node.x < 0 || node.x > this.canvas.width) node.vx *= -1;
        if (node.y < 0 || node.y > this.canvas.height) node.vy *= -1;

        // Keep within bounds
        node.x = Math.max(0, Math.min(this.canvas.width, node.x));
        node.y = Math.max(0, Math.min(this.canvas.height, node.y));

        // Friction
        node.vx *= 0.99;
        node.vy *= 0.99;

        // Minimum velocity
        if (Math.abs(node.vx) < 0.1) node.vx = (Math.random() - 0.5) * 0.5;
        if (Math.abs(node.vy) < 0.1) node.vy = (Math.random() - 0.5) * 0.5;
    }

    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // Update and draw nodes
        this.nodes.forEach(node => {
            this.updateNode(node);
            this.drawNode(node);
        });

        // Draw connections
        for (let i = 0; i < this.nodes.length; i++) {
            for (let j = i + 1; j < this.nodes.length; j++) {
                const dx = this.nodes[i].x - this.nodes[j].x;
                const dy = this.nodes[i].y - this.nodes[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < this.connectionDistance) {
                    this.drawConnection(this.nodes[i], this.nodes[j], distance);
                }
            }
        }

        this.animationId = requestAnimationFrame(() => this.animate());
    }

    destroy() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
        }
    }
}

// ============================================
// Floating Particles
// ============================================
class ParticleSystem {
    constructor(container) {
        this.container = container;
        this.particles = [];
        this.particleCount = 30;

        this.init();
    }

    init() {
        for (let i = 0; i < this.particleCount; i++) {
            this.createParticle();
        }
    }

    createParticle() {
        const particle = document.createElement('div');
        particle.className = 'particle';

        const size = Math.random() * 4 + 2;
        const duration = Math.random() * 20 + 15;
        const delay = Math.random() * 10;

        particle.style.cssText = `
            width: ${size}px;
            height: ${size}px;
            left: ${Math.random() * 100}%;
            animation-duration: ${duration}s;
            animation-delay: -${delay}s;
            opacity: ${Math.random() * 0.5 + 0.2};
        `;

        this.container.appendChild(particle);
        this.particles.push(particle);
    }

    destroy() {
        this.particles.forEach(p => p.remove());
        this.particles = [];
    }
}

// ============================================
// Typing Effect
// ============================================
class TypingEffect {
    constructor(element, words, options = {}) {
        this.element = element;
        this.words = words;
        this.typeSpeed = options.typeSpeed || 100;
        this.deleteSpeed = options.deleteSpeed || 50;
        this.pauseTime = options.pauseTime || 2000;
        this.currentWordIndex = 0;
        this.currentText = '';
        this.isDeleting = false;
        this.timeout = null;

        this.type();
    }

    type() {
        const currentWord = this.words[this.currentWordIndex];

        if (this.isDeleting) {
            this.currentText = currentWord.substring(0, this.currentText.length - 1);
        } else {
            this.currentText = currentWord.substring(0, this.currentText.length + 1);
        }

        this.element.textContent = this.currentText;

        let speed = this.isDeleting ? this.deleteSpeed : this.typeSpeed;

        if (!this.isDeleting && this.currentText === currentWord) {
            speed = this.pauseTime;
            this.isDeleting = true;
        } else if (this.isDeleting && this.currentText === '') {
            this.isDeleting = false;
            this.currentWordIndex = (this.currentWordIndex + 1) % this.words.length;
            speed = 500;
        }

        this.timeout = setTimeout(() => this.type(), speed);
    }

    destroy() {
        if (this.timeout) {
            clearTimeout(this.timeout);
        }
    }

    updateWords(newWords) {
        this.words = newWords;
    }
}

// ============================================
// Counter Animation
// ============================================
class CounterAnimation {
    constructor(elements) {
        this.elements = elements;
        this.animated = new Set();

        this.setupObserver();
    }

    setupObserver() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !this.animated.has(entry.target)) {
                    this.animateCounter(entry.target);
                    this.animated.add(entry.target);
                }
            });
        }, { threshold: 0.5 });

        this.elements.forEach(el => observer.observe(el));
    }

    animateCounter(element) {
        const target = parseInt(element.getAttribute('data-count'));
        const duration = 2000;
        const start = 0;
        const startTime = performance.now();

        const updateCounter = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);

            // Easing function (ease-out-expo)
            const easeProgress = 1 - Math.pow(2, -10 * progress);
            const current = Math.floor(start + (target - start) * easeProgress);

            element.textContent = current;

            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target;
            }
        };

        requestAnimationFrame(updateCounter);
    }
}

// ============================================
// Scroll Animations
// ============================================
class ScrollAnimations {
    constructor() {
        this.elements = document.querySelectorAll('[data-animate]');
        this.staggerElements = document.querySelectorAll('[data-stagger]');

        this.setupObserver();
    }

    setupObserver() {
        const options = {
            root: null,
            rootMargin: '0px 0px -100px 0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                }
            });
        }, options);

        this.elements.forEach(el => observer.observe(el));
        this.staggerElements.forEach(el => observer.observe(el));
    }
}

// ============================================
// Parallax Effect
// ============================================
class ParallaxEffect {
    constructor() {
        this.elements = document.querySelectorAll('[data-parallax]');
        this.ticking = false;

        if (this.elements.length > 0) {
            this.setupScrollListener();
        }
    }

    setupScrollListener() {
        window.addEventListener('scroll', () => {
            if (!this.ticking) {
                requestAnimationFrame(() => {
                    this.updateParallax();
                    this.ticking = false;
                });
                this.ticking = true;
            }
        });
    }

    updateParallax() {
        const scrollY = window.scrollY;
        document.documentElement.style.setProperty('--scroll', scrollY + 'px');
    }
}

// ============================================
// Magnetic Button Effect
// ============================================
class MagneticButton {
    constructor(elements) {
        this.elements = elements;
        this.bindEvents();
    }

    bindEvents() {
        this.elements.forEach(el => {
            el.addEventListener('mousemove', (e) => this.handleMove(e, el));
            el.addEventListener('mouseleave', (e) => this.handleLeave(e, el));
        });
    }

    handleMove(e, el) {
        const rect = el.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;

        el.style.transform = `translate(${x * 0.2}px, ${y * 0.2}px)`;
    }

    handleLeave(e, el) {
        el.style.transform = 'translate(0, 0)';
    }
}

// ============================================
// Smooth Reveal on Scroll
// ============================================
class SmoothReveal {
    constructor() {
        this.sections = document.querySelectorAll('.section');
        this.setupObserver();
    }

    setupObserver() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        this.sections.forEach(section => {
            section.classList.add('reveal-section');
            observer.observe(section);
        });
    }
}

// ============================================
// Initialize All Animations
// ============================================
function initAnimations() {
    console.log('🎬 Initializing animations...');

    // Neural Network Background
    const neuralCanvas = document.getElementById('neural-bg');
    if (neuralCanvas) {
        console.log('✅ Neural canvas found, creating NeuralNetwork');
        window.neuralNetwork = new NeuralNetwork(neuralCanvas);
    } else {
        console.log('⚠️ Neural canvas not found');
    }

    // Particles
    const particlesContainer = document.getElementById('particles-container');
    if (particlesContainer) {
        window.particleSystem = new ParticleSystem(particlesContainer);
    }

    // Typing Effect
    const typingElement = document.getElementById('typing-text');
    if (typingElement) {
        const currentLang = window.i18n?.getCurrentLanguage() || 'en';
        const words = window.i18n?.typingWords[currentLang] || [
            "Best AI Tools",
            "Perfect Solution",
            "Smart Automation",
            "AI Innovation"
        ];
        window.typingEffect = new TypingEffect(typingElement, words);
    }

    // Counter Animation
    const counters = document.querySelectorAll('[data-count]');
    if (counters.length > 0) {
        new CounterAnimation(counters);
    }

    // Scroll Animations
    new ScrollAnimations();

    // Parallax
    new ParallaxEffect();

    // Smooth Reveal
    new SmoothReveal();

    // Magnetic Buttons
    const magneticBtns = document.querySelectorAll('.btn-primary');
    if (magneticBtns.length > 0) {
        new MagneticButton(magneticBtns);
    }

    // Listen for language changes
    window.addEventListener('languageChanged', (e) => {
        if (window.typingEffect) {
            const words = window.i18n?.typingWords[e.detail.language] || window.i18n?.typingWords.en;
            window.typingEffect.words = words;
        }
    });
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAnimations);
} else {
    initAnimations();
}

// Export for external use
window.animations = {
    NeuralNetwork,
    ParticleSystem,
    TypingEffect,
    CounterAnimation,
    ScrollAnimations,
    ParallaxEffect,
    MagneticButton,
    init: initAnimations
};
