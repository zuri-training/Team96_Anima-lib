const close = document.querySelector(".close");
const innernav = document.querySelector(".innernav")
const hamburger = document.querySelector(".hamburger")
const icondown = document.querySelector(".icondown")
const headerdropdown = document.querySelector(".headerdropdown")

close.addEventListener("click", function () {
    innernav.classList.remove("displayflex")
});
hamburger.addEventListener("click", function () {
  innernav.classList.add("displayflex");
});

icondown.addEventListener("click", function(){
  headerdropdown.classList.toggle("displayflex")
})
