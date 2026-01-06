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

        console.log('SpotlightRotator initialized with', this.items.length, 'items');

        // Start with a random AI tool
        this.currentIndex = Math.floor(Math.random() * this.items.length);
        console.log('Starting with item index:', this.currentIndex);

        if (this.items.length === 0) {
            console.warn('No spotlight items found!');
            return;
        }

        // Show the random initial item
        this.showInitialSlide();
        this.init();
    }

    showInitialSlide() {
        console.log('Showing initial slide at index:', this.currentIndex);
        // Remove all active classes first
        this.items.forEach(item => item.classList.remove('active'));
        this.dots.forEach(dot => dot.classList.remove('active'));

        // Show the random initial slide
        this.items[this.currentIndex].classList.add('active');
        this.dots[this.currentIndex].classList.add('active');
        this.previousIndex = this.currentIndex;
        console.log('Initial slide shown');
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

        console.log('Transitioning from', this.currentIndex, 'to', nextIndex);
        this.goToSlide(nextIndex);
    }

    startRotation() {
        if (this.interval) {
            console.log('Rotation already running');
            return; // Already running
        }
        console.log('Starting rotation with delay:', this.rotationDelay, 'ms');
        this.interval = setInterval(() => this.next(), this.rotationDelay);
        console.log('Interval ID:', this.interval);
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
