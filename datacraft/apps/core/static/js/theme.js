// Sidebar Toggle
const sidebar = document.getElementById('sidebar');
const toggleBtn = document.getElementById('toggle-btn');

toggleBtn.addEventListener('click', () => {
  sidebar.classList.toggle('collapsed');
});

// Dark Theme Toggle
const themeToggleBtn = document.getElementById('theme-toggle');
const contentDiv = document.getElementById('content');
let isDarkMode = false;

themeToggleBtn.addEventListener('click', () => {
  isDarkMode = !isDarkMode;
  if (isDarkMode) {
    contentDiv.style.backgroundColor = '#0F101A';
    contentDiv.style.color = '#FFFFFF';
    themeToggleBtn.textContent = '☀️ Light Mode';
  } else {
    contentDiv.style.backgroundColor = '#f5f5f5';
    contentDiv.style.color = '#000000';
    themeToggleBtn.textContent = '🌙 Dark Mode';
  }
});
