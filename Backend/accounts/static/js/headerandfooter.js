const close = document.querySelector(".close");
const navmenu = document.querySelector(".navmenu")
const hamburger = document.querySelector(".hamburger")
const icondown = document.querySelector(".icondown")
const headerdropdown = document.querySelector(".headerdropdown")

close.addEventListener("click", function () {
    navmenu.classList.remove("displayflex")
});
hamburger.addEventListener("click", function () {
  navmenu.classList.add("displayflex");
});

icondown.addEventListener("click", function(){
  headerdropdown.classList.toggle("displayflex")
})
