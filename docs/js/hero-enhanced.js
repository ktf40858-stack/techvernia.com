/* ==============================================
   ENHANCED HERO ANIMATIONS
   ============================================== */

// Holographic Grid Animation
function initHolographicGrid() {
    const canvas = document.getElementById('holographic-grid');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const gridSize = 50;
    const points = [];

    // Create grid points
    for (let x = 0; x < canvas.width; x += gridSize) {
        for (let y = 0; y < canvas.height; y += gridSize) {
            points.push({ x, y, baseY: y, offset: Math.random() * Math.PI * 2 });
        }
    }

    let time = 0;

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        time += 0.01;

        // Draw grid lines
        ctx.strokeStyle = 'rgba(0, 217, 255, 0.2)';
        ctx.lineWidth = 1;

        points.forEach((point, i) => {
            // Wave effect
            point.y = point.baseY + Math.sin(time + point.offset) * 10;

            // Draw connections
            points.forEach((otherPoint, j) => {
                if (i < j) {
                    const distance = Math.hypot(point.x - otherPoint.x, point.y - otherPoint.y);
                    if (distance < gridSize * 1.5) {
                        const opacity = 1 - distance / (gridSize * 1.5);
                        ctx.strokeStyle = `rgba(0, 217, 255, ${opacity * 0.2})`;
                        ctx.beginPath();
                        ctx.moveTo(point.x, point.y);
                        ctx.lineTo(otherPoint.x, otherPoint.y);
                        ctx.stroke();
                    }
                }
            });

            // Draw point
            ctx.fillStyle = 'rgba(0, 217, 255, 0.5)';
            ctx.beginPath();
            ctx.arc(point.x, point.y, 2, 0, Math.PI * 2);
            ctx.fill();
        });

        requestAnimationFrame(animate);
    }

    animate();

    // Resize handler
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
}

// 3D AI Brain Visualization
function initAIBrain3D() {
    const canvas = document.getElementById('ai-brain-3d');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    canvas.width = 600;
    canvas.height = 600;

    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const radius = 150;

    // Create neurons
    const neurons = [];
    for (let i = 0; i < 100; i++) {
        const theta = Math.random() * Math.PI * 2;
        const phi = Math.random() * Math.PI;
        const r = radius + (Math.random() - 0.5) * 50;

        neurons.push({
            theta,
            phi,
            r,
            pulse: Math.random() * Math.PI * 2,
        });
    }

    let rotation = 0;

    function animate() {
        ctx.fillStyle = 'rgba(10, 10, 15, 0.1)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        rotation += 0.005;

        // Sort neurons by z-depth
        const projected = neurons.map((n, idx) => {
            const x = n.r * Math.sin(n.phi) * Math.cos(n.theta + rotation);
            const y = n.r * Math.sin(n.phi) * Math.sin(n.theta + rotation);
            const z = n.r * Math.cos(n.phi);

            const scale = 1 + z / 300;
            const screenX = centerX + x * scale;
            const screenY = centerY + y * scale;

            return { ...n, x: screenX, y: screenY, z, scale, idx };
        }).sort((a, b) => a.z - b.z);

        // Draw connections
        ctx.strokeStyle = 'rgba(0, 217, 255, 0.1)';
        ctx.lineWidth = 0.5;
        projected.forEach((n1, i) => {
            projected.slice(i + 1, i + 5).forEach(n2 => {
                const dist = Math.hypot(n1.x - n2.x, n1.y - n2.y);
                if (dist < 100) {
                    const opacity = 1 - dist / 100;
                    ctx.strokeStyle = `rgba(0, 217, 255, ${opacity * 0.2})`;
                    ctx.beginPath();
                    ctx.moveTo(n1.x, n1.y);
                    ctx.lineTo(n2.x, n2.y);
                    ctx.stroke();
                }
            });
        });

        // Draw neurons
        projected.forEach(n => {
            n.pulse += 0.1;
            const pulseSize = Math.sin(n.pulse) * 0.5 + 0.5;
            const size = 2 * n.scale * (1 + pulseSize * 0.5);

            const gradient = ctx.createRadialGradient(n.x, n.y, 0, n.x, n.y, size * 2);
            gradient.addColorStop(0, `rgba(0, 217, 255, ${0.8 * n.scale})`);
            gradient.addColorStop(0.5, `rgba(168, 85, 247, ${0.4 * n.scale})`);
            gradient.addColorStop(1, 'rgba(0, 217, 255, 0)');

            ctx.fillStyle = gradient;
            ctx.beginPath();
            ctx.arc(n.x, n.y, size * 2, 0, Math.PI * 2);
            ctx.fill();

            ctx.fillStyle = `rgba(255, 255, 255, ${0.9 * n.scale})`;
            ctx.beginPath();
            ctx.arc(n.x, n.y, size, 0, Math.PI * 2);
            ctx.fill();
        });

        requestAnimationFrame(animate);
    }

    animate();
}

// Counter Animation
function animateCounters() {
    const counters = document.querySelectorAll('.counter');

    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-count'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };

        // Start animation when element is visible
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    updateCounter();
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        observer.observe(counter);
    });
}

// Typewriter Effect
function initTypewriter() {
    const textElement = document.querySelector('.typewriter-text');
    if (!textElement) return;

    const texts = [
        'Explore 256+ cutting-edge AI tools across 22 categories',
        'Expert reviews, guides, and comparisons for every need',
        'From ChatGPT to specialized enterprise solutions',
        'Your ultimate AI tools directory starts here'
    ];

    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 100;

    function type() {
        const currentText = texts[textIndex];

        if (isDeleting) {
            textElement.textContent = currentText.substring(0, charIndex - 1);
            charIndex--;
            typingSpeed = 50;
        } else {
            textElement.textContent = currentText.substring(0, charIndex + 1);
            charIndex++;
            typingSpeed = 100;
        }

        if (!isDeleting && charIndex === currentText.length) {
            isDeleting = true;
            typingSpeed = 2000; // Pause at end
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            textIndex = (textIndex + 1) % texts.length;
        }

        setTimeout(type, typingSpeed);
    }

    type();
}

// Particle System for Background
function createParticleSystem() {
    const container = document.getElementById('particles-container');
    if (!container) return;

    for (let i = 0; i < 50; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.cssText = `
            position: absolute;
            width: ${Math.random() * 3 + 1}px;
            height: ${Math.random() * 3 + 1}px;
            background: rgba(0, 217, 255, ${Math.random() * 0.5 + 0.2});
            border-radius: 50%;
            left: ${Math.random() * 100}%;
            top: ${Math.random() * 100}%;
            animation: particleFloat ${Math.random() * 10 + 5}s linear infinite;
            animation-delay: ${Math.random() * 5}s;
            box-shadow: 0 0 ${Math.random() * 10 + 5}px rgba(0, 217, 255, 0.5);
        `;
        container.appendChild(particle);
    }
}

// Smooth Scroll
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;

            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Parallax Effect
function initParallax() {
    let ticking = false;

    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                const scrolled = window.pageYOffset;

                // Move orbs
                document.querySelectorAll('.orb').forEach((orb, index) => {
                    const speed = 0.5 + index * 0.1;
                    orb.style.transform = `translateY(${scrolled * speed}px)`;
                });

                // Move floating cards
                document.querySelectorAll('.preview-card').forEach((card, index) => {
                    const speed = 0.3 + index * 0.1;
                    card.style.transform = `translateY(${scrolled * speed}px)`;
                });

                ticking = false;
            });

            ticking = true;
        }
    });
}

// Mouse Trail Effect
function initMouseTrail() {
    const trail = [];
    const trailLength = 20;

    document.addEventListener('mousemove', (e) => {
        trail.push({ x: e.clientX, y: e.clientY, time: Date.now() });

        if (trail.length > trailLength) {
            trail.shift();
        }

        // Create temporary particle
        const particle = document.createElement('div');
        particle.style.cssText = `
            position: fixed;
            width: 4px;
            height: 4px;
            background: rgba(0, 217, 255, 0.6);
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            left: ${e.clientX}px;
            top: ${e.clientY}px;
            animation: fadeOut 0.5s ease-out forwards;
        `;
        document.body.appendChild(particle);

        setTimeout(() => particle.remove(), 500);
    });
}

// Add CSS for particle fade out
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeOut {
        to {
            opacity: 0;
            transform: scale(0);
        }
    }

    @keyframes particleFloat {
        0% {
            transform: translateY(0) translateX(0);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateY(-100vh) translateX(${Math.random() * 100 - 50}px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Initialize everything when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    initHolographicGrid();
    initAIBrain3D();
    animateCounters();
    initTypewriter();
    createParticleSystem();
    initSmoothScroll();
    initParallax();
    initMouseTrail();

    
});

// Handle window resize
window.addEventListener('resize', () => {
    // Re-initialize grid on resize
    initHolographicGrid();
});
