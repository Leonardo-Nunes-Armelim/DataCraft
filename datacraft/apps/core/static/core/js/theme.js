// Sidebar Toggle
const sidebar = document.getElementById('sidebar');
const toggleBtn = document.getElementById('toggle-btn');
const themeToggleBtn = document.getElementById('theme-toggle');

const THEME_STORAGE_KEY = 'theme';

function getSavedTheme() {
  return localStorage.getItem(THEME_STORAGE_KEY) === 'dark' ? 'dark' : 'light';
}

function applyTheme(theme) {
  const nextTheme = theme === 'dark' ? 'dark' : 'light';

  document.documentElement.setAttribute('data-theme', nextTheme);
  document.body?.setAttribute('data-theme', nextTheme);

  if (sidebar) {
    sidebar.setAttribute('data-theme', nextTheme);
  }

  localStorage.setItem(THEME_STORAGE_KEY, nextTheme);

  if (themeToggleBtn) {
    themeToggleBtn.textContent =
      nextTheme === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode';
  }
}

if (toggleBtn && sidebar) {
  toggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('collapsed');
  });
}

applyTheme(getSavedTheme());

if (themeToggleBtn) {
  themeToggleBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
    applyTheme(nextTheme);
  });
}
