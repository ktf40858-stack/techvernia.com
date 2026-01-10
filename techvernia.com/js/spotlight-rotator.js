/**
 * AI of the Moment - Rotating Spotlight
 * Automatically cycles through 6 featured AI tools in random order
 */

class SpotlightRotator {
    constructor() {
        this.items = document.querySelectorAll('.spotlight-item');
        this.dots = document.querySelectorAll('.progress-dot');
        this.interval = null;
        this.rotationDelay = 15000; // 15 seconds per tool
        this.previousIndex = -1;

        

        // Start with a random AI tool
        this.currentIndex = Math.floor(Math.random() * this.items.length);
        

        if (this.items.length === 0) {
            
            return;
        }

        // Show the random initial item
        this.showInitialSlide();
        this.init();
    }

    showInitialSlide() {
        
        // Remove all active classes first
        this.items.forEach(item => item.classList.remove('active'));
        this.dots.forEach(dot => dot.classList.remove('active'));

        // Show the random initial slide
        this.items[this.currentIndex].classList.add('active');
        this.dots[this.currentIndex].classList.add('active');
        this.previousIndex = this.currentIndex;
        
    }

    init() {
        // Setup dot click handlers
        this.dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                this.goToSlide(index);
                this.resetInterval(); // Reset timer when user manually clicks
            });
        });

        // Start auto-rotation
        this.startRotation();

        // Pause on hover
        const container = document.querySelector('.spotlight-container');
        if (container) {
            container.addEventListener('mouseenter', () => this.pauseRotation());
            container.addEventListener('mouseleave', () => this.startRotation());
        }
    }

    goToSlide(index) {
        // Remove active class from current item and dot
        this.items[this.currentIndex].classList.remove('active');
        this.dots[this.currentIndex].classList.remove('active');

        // Update index
        this.previousIndex = this.currentIndex;
        this.currentIndex = index;

        // Add active class to new item and dot
        this.items[this.currentIndex].classList.add('active');
        this.dots[this.currentIndex].classList.add('active');
    }

    next() {
        // Pick a random index that's different from current
        let nextIndex;
        do {
            nextIndex = Math.floor(Math.random() * this.items.length);
        } while (nextIndex === this.currentIndex && this.items.length > 1);

        
        this.goToSlide(nextIndex);
    }

    startRotation() {
        if (this.interval) {
            
            return; // Already running
        }
        
        this.interval = setInterval(() => this.next(), this.rotationDelay);
        
    }

    pauseRotation() {
        if (this.interval) {
            clearInterval(this.interval);
            this.interval = null;
        }
    }

    resetInterval() {
        this.pauseRotation();
        this.startRotation();
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new SpotlightRotator();
});
