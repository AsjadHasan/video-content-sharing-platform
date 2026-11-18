'use strict';
const menuToggle = document.getElementById('menuToggle');
const overlay = document.getElementById('mobileOverlay');
const mobileQuery = window.matchMedia('(max-width: 700px)');
const tabletQuery = window.matchMedia('(max-width: 1100px)');
function expanded() {
    if (mobileQuery.matches) return document.body.classList.contains('mobile-sidebar-open');
    if (tabletQuery.matches) return document.body.classList.contains('sidebar-expanded') && !document.body.classList.contains('sidebar-collapsed');
    return !document.body.classList.contains('sidebar-collapsed');
}
function updateMenu() {
    const open = mobileQuery.matches && document.body.classList.contains('mobile-sidebar-open');
    overlay.hidden = !open;
    menuToggle.setAttribute('aria-expanded', String(expanded()));
}
menuToggle.addEventListener('click', () => {
    if (mobileQuery.matches) document.body.classList.toggle('mobile-sidebar-open');
    else if (tabletQuery.matches) {
        document.body.classList.toggle('sidebar-expanded');
        document.body.classList.remove('sidebar-collapsed');
    } else document.body.classList.toggle('sidebar-collapsed');
    updateMenu();
});
overlay.addEventListener('click', () => { document.body.classList.remove('mobile-sidebar-open'); updateMenu(); });
document.addEventListener('keydown', event => {
    if (event.key === 'Escape') { document.body.classList.remove('mobile-sidebar-open'); updateMenu(); }
});
window.addEventListener('resize', () => {
    document.body.classList.remove('mobile-sidebar-open');
    if (!tabletQuery.matches) document.body.classList.remove('sidebar-expanded');
    updateMenu();
});
document.querySelectorAll('.expand-button').forEach(button => {
    button.addEventListener('click', () => {
        const target = document.getElementById(button.dataset.target);
        const isOpen = button.getAttribute('aria-expanded') === 'true';
        target.hidden = isOpen;
        button.setAttribute('aria-expanded', String(!isOpen));
        button.querySelector('span').textContent = isOpen ? 'Show more' : 'Show less';
        button.querySelector('i').className = isOpen ? 'bi bi-chevron-down' : 'bi bi-chevron-up';
    });
});
document.querySelectorAll('[data-placeholder]').forEach(link => {
    link.addEventListener('click', event => event.preventDefault());
});
updateMenu();
