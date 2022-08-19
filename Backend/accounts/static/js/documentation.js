
const mobilemenu = document.querySelector(".aside")
const asidehamburger = document.querySelector('.asidehamburger')
const closeasidemenu = document.querySelector(".closeasidemenu")
const acc = document.querySelector("#contentcontainer")
const listcontent = document.querySelector("#listcontent")

asidehamburger.addEventListener("click", function(){
    mobilemenu.classList.add("display")
    closeasidemenu.classList.add("display");
})

closeasidemenu.addEventListener("click", function () {
  mobilemenu.classList.remove("display");
  closeasidemenu.classList.remove("display");
});

acc.addEventListener("click", function () {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the aniList */
    this.classList.toggle("active");

    /* Toggle between hiding and showing the active aniList */
    let aniList = this.nextElementSibling;
    if (aniList.style.display === "block") {
      aniList.style.display = "none";
    } else {
      aniList.style.display = "block";
    }
})
acc.addEventListener("click", function () {
    this.classList.toggle("active");
    let aniList = this.nextElementSibling;
    if (aniList.style.maxHeight) {
      aniList.style.maxHeight = null;
    } else {
      aniList.style.maxHeight = aniList.scrollHeight + "px";
    }
});