const filterButtons = [...document.querySelectorAll('[data-filter]')];
const projectCards = [...document.querySelectorAll('.project-card')];
const filterStatus = document.querySelector('#filter-status');

function setProjectFilter(category) {
  let visibleCount = 0;

  projectCards.forEach((card) => {
    const matches = category === 'all' || card.dataset.category === category;
    card.hidden = !matches;
    if (matches) visibleCount += 1;
  });

  filterButtons.forEach((button) => {
    const isActive = button.dataset.filter === category;
    button.classList.toggle('is-active', isActive);
    button.setAttribute('aria-pressed', String(isActive));
  });

  const label = category === 'all' ? 'dự án' : `dự án ${category === 'web' ? 'Web' : 'Mobile'}`;
  filterStatus.textContent = `Đang hiển thị ${visibleCount} ${label}.`;
  if (window.AOS) AOS.refreshHard();
}

filterButtons.forEach((button) => {
  button.addEventListener('click', () => setProjectFilter(button.dataset.filter));
});

if (window.AOS) {
  AOS.init({
    duration: 700,
    easing: 'ease-out-quart',
    once: true,
    offset: 75,
    disable: window.matchMedia('(prefers-reduced-motion: reduce)').matches
  });
} else {
  document.querySelectorAll('[data-aos]').forEach((element) => {
    element.removeAttribute('data-aos');
  });
}
