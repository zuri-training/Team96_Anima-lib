let acc = document.getElementsByClassName("aniFamilyName");
const dropicon = document.getElementsByClassName("dropicon")
const view = document.querySelector(".view");
const codeblock = document.querySelector(".row3");
const p = document.querySelectorAll("p")
const ellipse = document.querySelector("#ellipse")
const animationsmenu = document.querySelector(".animationsmenu")
const leftbox = document.querySelector(".left-box")

let i;
for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
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
  });
}
for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    let aniList = this.nextElementSibling;
    if (aniList.style.maxHeight) {
      aniList.style.maxHeight = null;
    } else {
      aniList.style.maxHeight = aniList.scrollHeight + "px";
    }
  });
}

view.addEventListener("click", function () {
  codeblock.classList.toggle("display");
  const togglecode = document.querySelector(".togglecode")
  if (togglecode.innerHTML == "view code"){
    togglecode.innerHTML = "hide code"
  }else{
    togglecode.innerHTML = "view code";
  }
});

for (let x = 0; x < p.length; x++) {
  const targetClass = p[x];
  let targetClassName = targetClass.innerHTML
  targetClass.addEventListener("click", function(){
    ellipse.className = "anibry"
    ellipse.classList.add(`${targetClassName}`);
    let windowWidth = window.innerWidth;
    if (windowWidth == 650 || windowWidth < 650){
      leftbox.classList.remove("display")
    }
  })
  
}

// FOR MOBILE VIEW OF ANIMATIONS
const closeicon = document.querySelector(".closeicon")
animationsmenu.addEventListener("click", function(){
  leftbox.classList.toggle("display")
})
closeicon.addEventListener("click", function(){
  leftbox.classList.remove("display")
})



