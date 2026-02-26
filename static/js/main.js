/**
 * Portfolio Hub - Safe Minimal JavaScript
 */

document.addEventListener('DOMContentLoaded', function () {

    console.log("Portfolio Hub JS Loaded");

    // Smooth scroll (SAFE version)
    const anchors = document.querySelectorAll('a[href^="#"]');
    anchors.forEach(anchor => {
        anchor.addEventListener('click', function (e) {

            const targetId = this.getAttribute('href');

            if (targetId.length > 1) {
                const target = document.querySelector(targetId);

                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

});