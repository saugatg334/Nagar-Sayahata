// ========================================
// ADMIN UI MODULE
// ========================================
(function () {
    const selectors = {
        sidebar: '#sidebar',
        mainContent: '#mainContent',
        toggleBtn: '#toggleSidebarBtn',
        themeToggle: '#themeToggleBtn',
        dropdownBtn: '#dropdownBtn',
        dropdownMenu: '#dropdownMenu',
    };

    const state = {
        sidebarCollapsed: localStorage.getItem('sidebarCollapsed') === 'true',
        hoverTimeout: null,
        isHovering: false,
        theme: localStorage.getItem('theme') || 'light',
    };

    const elements = {
        sidebar: document.querySelector(selectors.sidebar),
        mainContent: document.querySelector(selectors.mainContent),
        toggleBtn: document.querySelector(selectors.toggleBtn),
        themeToggle: document.querySelector(selectors.themeToggle),
        dropdownBtn: document.querySelector(selectors.dropdownBtn),
        dropdownMenu: document.querySelector(selectors.dropdownMenu),
    };

    function isDesktop() {
        return window.innerWidth > 768;
    }

    function isMobile() {
        return !isDesktop();
    }

    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
        state.theme = theme;
    }

    function applySidebarState(collapsed) {
        if (!elements.sidebar || !elements.mainContent) {
            return;
        }

        if (isDesktop()) {
            if (collapsed) {
                elements.sidebar.classList.add('collapsed');
                elements.mainContent.classList.add('expanded');
            } else {
                elements.sidebar.classList.remove('collapsed', 'hover-preview');
                elements.mainContent.classList.remove('expanded', 'hover-preview');
            }
            state.sidebarCollapsed = collapsed;
            localStorage.setItem('sidebarCollapsed', String(collapsed));
        }
    }

    function enableHoverPreview() {
        if (!elements.sidebar || !elements.mainContent || !isDesktop()) {
            return;
        }

        if (elements.sidebar.classList.contains('collapsed')) {
            elements.sidebar.classList.add('hover-preview');
            elements.mainContent.classList.add('hover-preview');
        }
    }

    function disableHoverPreview() {
        if (!elements.sidebar || !elements.mainContent) {
            return;
        }

        elements.sidebar.classList.remove('hover-preview');
        elements.mainContent.classList.remove('hover-preview');
    }

    function clearHoverTimeout() {
        if (state.hoverTimeout) {
            clearTimeout(state.hoverTimeout);
            state.hoverTimeout = null;
        }
    }

    function handleDesktopResize() {
        applySidebarState(state.sidebarCollapsed);
    }

    function handleMobileResize() {
        if (!elements.sidebar || !elements.mainContent) {
            return;
        }

        elements.sidebar.classList.remove('collapsed', 'hover-preview', 'active');
        elements.mainContent.classList.remove('expanded', 'hover-preview');
        clearHoverTimeout();
    }

    function setupSidebarInteractions() {
        if (!elements.sidebar) {
            return;
        }

        if (elements.toggleBtn) {
            elements.toggleBtn.addEventListener('click', () => {
                if (isDesktop()) {
                    clearHoverTimeout();
                    disableHoverPreview();
                    applySidebarState(!elements.sidebar.classList.contains('collapsed'));
                }
            });
        }

        elements.sidebar.addEventListener('mouseenter', () => {
            if (isDesktop() && elements.sidebar.classList.contains('collapsed')) {
                state.isHovering = true;
                state.hoverTimeout = setTimeout(() => {
                    if (state.isHovering) {
                        enableHoverPreview();
                    }
                }, 150);
            }
        });

        elements.sidebar.addEventListener('mouseleave', () => {
            if (isDesktop()) {
                state.isHovering = false;
                clearHoverTimeout();
                disableHoverPreview();
            }
        });
    }

    function setupThemeToggle() {
        if (!elements.themeToggle) {
            return;
        }

        setTheme(state.theme);

        elements.themeToggle.addEventListener('click', () => {
            const nextTheme = document.documentElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
            setTheme(nextTheme);
        });
    }

    function setupDropdown() {
        if (!elements.dropdownBtn || !elements.dropdownMenu) {
            return;
        }

        elements.dropdownBtn.addEventListener('click', (event) => {
            event.stopPropagation();
            elements.dropdownMenu.classList.toggle('show');
        });

        document.addEventListener('click', (event) => {
            if (!elements.dropdownBtn.contains(event.target) && elements.dropdownMenu.classList.contains('show')) {
                elements.dropdownMenu.classList.remove('show');
            }
        });
    }

    function handleResize() {
        clearHoverTimeout();
        disableHoverPreview();

        if (isDesktop()) {
            handleDesktopResize();
        } else {
            handleMobileResize();
        }
    }

    function init() {
        setupSidebarInteractions();
        setupThemeToggle();
        setupDropdown();
        handleResize();
        window.addEventListener('resize', handleResize);
    }

    init();
})();

