const close = document.querySelector(".close");
const navmenu = document.querySelector(".navmenu")
const hamburger = document.querySelector(".hamburger")

close.addEventListener("click", function () {
    navmenu.classList.remove("displayflex")
});
hamburger.addEventListener("click", function () {
  navmenu.classList.add("displayflex");
});
