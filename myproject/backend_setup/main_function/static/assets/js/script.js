// ========================================
// SIDEBAR TOGGLE FUNCTIONALITY (FIXED)
// ========================================
(function () {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('mainContent');
    const toggleBtn = document.getElementById('toggleSidebarBtn');
    const mobileToggleBtn = document.getElementById('mobileToggleBtn');
    const closeSidebarBtn = document.getElementById('closeSidebarBtn');
    const sidebarOverlay = document.getElementById('sidebarOverlay');

    // Load saved sidebar state
    let isCollapsed = localStorage.getItem('sidebarCollapsed') === 'true';

    function setSidebarCollapsed(collapsed) {
        if (window.innerWidth > 768) {
            if (collapsed) {
                sidebar.classList.add('collapsed');
                mainContent.classList.add('expanded');
            } else {
                sidebar.classList.remove('collapsed');
                mainContent.classList.remove('expanded');
            }
            localStorage.setItem('sidebarCollapsed', collapsed);
        }
    }

    // Apply saved state on desktop
    if (isCollapsed && window.innerWidth > 768) {
        setSidebarCollapsed(true);
    }

    // Desktop toggle
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            if (window.innerWidth > 768) {
                setSidebarCollapsed(!sidebar.classList.contains('collapsed'));
            }
        });
    }

    // Mobile toggle - FIXED: Use 'active' class
    if (mobileToggleBtn) {
        mobileToggleBtn.addEventListener('click', () => {
            if (window.innerWidth <= 768) {
                sidebar.classList.toggle('active');
                if (sidebarOverlay) sidebarOverlay.classList.toggle('active');
                document.body.classList.toggle('sidebar-open');
            }
        });
    }

    // Close sidebar on mobile - FIXED
    if (closeSidebarBtn) {
        closeSidebarBtn.addEventListener('click', () => {
            if (window.innerWidth <= 768) {
                sidebar.classList.remove('active');
                if (sidebarOverlay) sidebarOverlay.classList.remove('active');
                document.body.classList.remove('sidebar-open');
            }
        });
    }

    // Close sidebar when clicking outside (mobile) - FIXED
    document.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
            if (sidebar.classList.contains('active')) {
                if (!sidebar.contains(e.target) && !mobileToggleBtn.contains(e.target)) {
                    sidebar.classList.remove('active');
                    if (sidebarOverlay) sidebarOverlay.classList.remove('active');
                    document.body.classList.remove('sidebar-open');
                }
            }
        }
    });

    // Close sidebar on nav link click (mobile)
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth <= 768) {
                sidebar.classList.remove('active');
                if (sidebarOverlay) sidebarOverlay.classList.remove('active');
                document.body.classList.remove('sidebar-open');
            }
        });
    });

    // ========================================
    // DARK/LIGHT MODE TOGGLE
    // ========================================
    const themeToggle = document.getElementById('themeToggleBtn');
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);

    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const current = document.documentElement.getAttribute('data-theme');
            const newTheme = current === 'light' ? 'dark' : 'light';
            setTheme(newTheme);
        });
    }

    // ========================================
    // PROFILE DROPDOWN TOGGLE
    // ========================================
    const dropdownBtn = document.getElementById('dropdownBtn');
    const dropdownMenu = document.getElementById('dropdownMenu');

    if (dropdownBtn && dropdownMenu) {
        dropdownBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            dropdownMenu.classList.toggle('show');
        });

        document.addEventListener('click', (e) => {
            if (!dropdownBtn.contains(e.target) && dropdownMenu.classList.contains('show')) {
                dropdownMenu.classList.remove('show');
            }
        });
    }

    // ========================================
    // HANDLE RESIZE EVENTS (FIXED)
    // ========================================
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            // Switching to desktop
            if (sidebar.classList.contains('active')) {
                sidebar.classList.remove('active');
                if (sidebarOverlay) sidebarOverlay.classList.remove('active');
                document.body.classList.remove('sidebar-open');
            }
            const saved = localStorage.getItem('sidebarCollapsed') === 'true';
            setSidebarCollapsed(saved);
        } else {
            // Switching to mobile
            sidebar.classList.remove('collapsed');
            mainContent.classList.remove('expanded');
            // Ensure mobile sidebar is closed
            sidebar.classList.remove('active');
            if (sidebarOverlay) sidebarOverlay.classList.remove('active');
            document.body.classList.remove('sidebar-open');
        }
    });
})();

