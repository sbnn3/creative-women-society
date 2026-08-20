// Creative Women Society — site interactions
// Subtle, elegant, never distracting (per Chapter 11.12).

document.addEventListener('DOMContentLoaded', function () {

  // Footer year
  var yearEl = document.getElementById('footerYear');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Header scroll state
  var header = document.getElementById('siteHeader');
  function onScroll() {
    if (!header) return;
    if (window.scrollY > 40) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile nav toggle
  var navToggle = document.getElementById('navToggle');
  var navLinks = document.getElementById('navLinks');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      navLinks.classList.toggle('is-open');
    });
    navLinks.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { navLinks.classList.remove('is-open'); });
    });
  }

  // Reveal on scroll
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  }

  // FAQ accordion
  document.querySelectorAll('.faq-item').forEach(function (item) {
    var q = item.querySelector('.faq-q');
    if (!q) return;
    q.addEventListener('click', function () {
      var wasOpen = item.classList.contains('is-open');
      item.parentElement.querySelectorAll('.faq-item').forEach(function (i) { i.classList.remove('is-open'); });
      if (!wasOpen) item.classList.add('is-open');
    });
  });

  // Journal / experience tag filter (client-side, progressive enhancement)
  var tagPills = document.querySelectorAll('.tag-pill[data-filter]');
  var filterItems = document.querySelectorAll('[data-tags]');
  if (tagPills.length && filterItems.length) {
    tagPills.forEach(function (pill) {
      pill.addEventListener('click', function () {
        tagPills.forEach(function (p) { p.classList.remove('active'); });
        pill.classList.add('active');
        var filter = pill.getAttribute('data-filter');
        filterItems.forEach(function (item) {
          var tags = (item.getAttribute('data-tags') || '').split(',');
          item.style.display = (filter === 'all' || tags.indexOf(filter) !== -1) ? '' : 'none';
        });
      });
    });
  }

  // Sub-nav active state on scroll (Society / Legacy / Membership anchor pages)
  var subnavLinks = document.querySelectorAll('.subnav a[href*="#"]');
  if (subnavLinks.length) {
    var sections = [];
    subnavLinks.forEach(function (link) {
      var id = link.getAttribute('href').split('#')[1];
      var section = document.getElementById(id);
      if (section) sections.push({ link: link, section: section });
    });
    function onSubnavScroll() {
      var scrollPos = window.scrollY + 160;
      var current = null;
      sections.forEach(function (s) {
        if (s.section.offsetTop <= scrollPos) current = s;
      });
      subnavLinks.forEach(function (l) { l.classList.remove('active'); });
      if (current) current.link.classList.add('active');
    }
    window.addEventListener('scroll', onSubnavScroll, { passive: true });
    onSubnavScroll();
  }

  // Contact / membership form: graceful placeholder submit (no backend yet)
  document.querySelectorAll('form[data-cws-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = form.querySelector('.form-note');
      if (note) {
        note.textContent = 'Thank you — your message has been received. A member of the Society will be in touch shortly.';
        note.style.display = 'block';
      }
      form.reset();
    });
  });

});
