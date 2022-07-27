//For Navbar Scroller

let nav = document.querySelector(".navbar");
window.onscroll = function () {
    if (document.documentElement.scrollTop > 20) {
        nav.classList.add("header-scrolled");
        scrollbtn.style.display = "block";
    } else {
        nav.classList.remove("header-scrolled");
        scrollbtn.style.display = "none";
    }
};