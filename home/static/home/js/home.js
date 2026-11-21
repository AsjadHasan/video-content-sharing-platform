'use strict';

const topicsTrack = document.getElementById('topicsTrack');
const topicChips = document.querySelectorAll('.topic-chip');
const videoCards = document.querySelectorAll('.video-card');
const emptyState = document.getElementById('emptyState');

// Demo-only filtering. Replace with backend query parameters when videos are dynamic.
function filterVideos(category) {
    let visibleCount = 0;
    videoCards.forEach((card) => {
        const categories = (card.dataset.category || '').split(' ');
        const show = category === 'All' || categories.includes(category);
        card.hidden = !show;
        if (show) visibleCount += 1;
    });
    document.querySelector('.shorts-shelf').hidden = category !== 'All';
    emptyState.hidden = visibleCount > 0;
}

topicChips.forEach((chip) => {
    chip.addEventListener('click', () => {
        topicChips.forEach((other) => {
            other.classList.remove('is-active');
            other.setAttribute('aria-pressed', 'false');
        });
        chip.classList.add('is-active');
        chip.setAttribute('aria-pressed', 'true');
        filterVideos(chip.dataset.category);
    });
});

document.querySelector('.topic-arrow-left').addEventListener('click', () => {
    topicsTrack.scrollBy({ left: -360, behavior: 'smooth' });
});
document.querySelector('.topic-arrow-right').addEventListener('click', () => {
    topicsTrack.scrollBy({ left: 360, behavior: 'smooth' });
});

// Placeholder links remain non-navigating until video detail routes exist.
document.querySelectorAll('[data-demo-link]').forEach((link) => {
    link.addEventListener('click', (event) => event.preventDefault());
});

// Options buttons have a simple demo menu, not backend actions.
document.querySelectorAll('.video-menu, .shelf-menu').forEach((button) => {
    button.addEventListener('click', () => {
        button.title = 'More options — coming soon';
    });
});
