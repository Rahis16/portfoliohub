document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("sidebar");
    const sidebarToggle = document.getElementById("sidebarToggle");
    const sidebarbtn = document.querySelector(".sidebar-btn");
    const closeSidebar = document.getElementById("closeSidebar");
    const header = document.getElementById("header");

    let isSidebarOpen = false;
    let lastScrollTop = 0; // Track the last scroll position

    function openSidebar() {
        sidebar.classList.add("active");
        sidebar.style.animation = "slideIn 0.4s forwards";
        header.classList.add("shift");
        sidebarbtn.classList.add("hide");
        isSidebarOpen = true;
    }

    function closeSidebarFunc() {
        sidebar.style.animation = "slideOut 0.4s forwards";
        setTimeout(() => {
            sidebar.classList.remove("active");
            header.classList.remove("shift");
            sidebarbtn.classList.remove("hide");
        }, 50);
        isSidebarOpen = false;
    }

    sidebarToggle.addEventListener("click", function () {
        isSidebarOpen ? closeSidebarFunc() : openSidebar();
    });

    closeSidebar.addEventListener("click", closeSidebarFunc);

    // Hide the header when scrolling exceeds 100px and show the header when scrolling up
    window.addEventListener("scroll", function () {
        const currentScroll = window.scrollY;

        // Hide the header when scrolling down and exceeding 100px
        if (currentScroll > 100) {
            header.style.animation = "slideUp 0.5s forwards";
        } else {
            header.style.animation = "none"; // Reset the animation
            header.style.display = "flex";  // Ensure header is visible
        }

        // Show the header when scrolling up after exceeding 50px
        if (currentScroll < lastScrollTop && currentScroll > 50) {
            header.style.animation = "slideDown 0.5s forwards";
        }

        // Update the last scroll position
        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
    });
});
