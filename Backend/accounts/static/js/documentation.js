
const mobilemenu = document.querySelector(".aside")
const asidehamburger = document.querySelector('.asidehamburger')
const closeasidemenu = document.querySelector(".closeasidemenu")


asidehamburger.addEventListener("click", function(){
    mobilemenu.classList.add("display")
    closeasidemenu.classList.add("display");
})

closeasidemenu.addEventListener("click", function () {
  mobilemenu.classList.remove("display");
  closeasidemenu.classList.remove("display");
});
