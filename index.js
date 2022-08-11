let target = document.querySelector(".target");
let btn = document.querySelector(".toggle");
let rotater = false;
let runner1;
let runner2;
let degrees = 0;
let negativedegrees = 0
const mobilemenu = document.querySelector(".menu");
const mobilemenulist = document.querySelector(".mobilemenulist");
const closemenu = document.querySelector(".closemenu");
const mobilemenuitem = document.getElementsByClassName("mobilemenuitem");
const logoball = document.querySelector(".logoball")
const rotateball = document.querySelectorAll(".rotateball")
const rotated = document.querySelector(".rotated")
const attention = document.querySelector(".attention")
const suspend = document.querySelector(".suspend")
const quake = document.querySelector(".quake")
const rebound = document.querySelector(".rebound")
const jiggle = document.querySelector(".jiggle")
const invert = document.querySelector(".invert")
const dropbtn = document.querySelectorAll(".dropbtn")
const w = window.innerWidth;

// FOR NAV BAR
// if (w > 500){
//   console.log(w)
//   mobilemenulist.className = "mobilemenulist"
// }

mobilemenu.addEventListener("click", function () {
  mobilemenulist.classList.add("displayflex");
});
closemenu.addEventListener("click", function () {
  mobilemenulist.classList.remove("displayflex");
});

// FOR MOBILE NAV 
// for (let x = 0; x < mobilemenuitem.length; x++) {
//   const activeitem = mobilemenuitem[x];
//   activeitem.style.backgroundColor = "white";
//   activeitem.addEventListener("click", function () {
//     activeitem.style.backgroundColor = "#5A189A";
//     activeitem.style.Color = "white";
//   });
// }

// FOR ANIMATION OF ROTATING SECTION
function start() {
  clearInterval(runner2);
  runner1 = setInterval(function () {
    degrees++;
    negativedegrees--
    target.style.webkitTransform = "rotate(" + degrees + "deg)";
    logoball.style.webkitTransform = "rotate(" + negativedegrees + "deg)";
    for (let x = 0; x < rotateball.length; x++) {
      const balls = rotateball[x];
      rotateball[x].style.webkitTransform =
        "rotate(" + negativedegrees + "deg)";
    }
  }, 50);
}

function stop() {
    clearInterval(runner1);
}

btn.addEventListener("mouseover", function () {
    rotater = true;
    start();
})
btn.addEventListener("mouseout", function () {
    rotater = false;
    stop();
});
btn.addEventListener("click", function(){
  degrees = degrees + 2
  runner2 = setInterval(function () {
      target.style.webkitTransform = "rotate(" + degrees + "deg)";
    }, 50);
})

// Animation demo for each box
for (let x = 0; x < dropbtn.length; x++) {
  const targetbtn = dropbtn[x];
  targetbtn.addEventListener("click", function () {
    if (targetbtn.nextElementSibling.classList.contains("displayblock")){
    targetbtn.nextElementSibling.classList.remove("displayblock")
  }else {
    targetbtn.nextElementSibling.classList.add("displayblock")
  }
})
}

const reboundItem = document.querySelectorAll(".reboundItem")
for (let x = 0; x < reboundItem.length; x++) {
  const targetClass = reboundItem[x];
  let targetClassName = targetClass.innerHTML
  targetClass.addEventListener("click", function(){
    rebound.className = "rebound anibry";
    rebound.classList.add(`${targetClassName}`);
  })
}

const rotatedItem = document.querySelectorAll(".rotatedItem");
for (let x = 0; x < rotatedItem.length; x++) {
  const targetClass = rotatedItem[x];
  let targetClassName = targetClass.innerHTML;
  targetClass.addEventListener("click", function () {
    rotated.className = "rebound anibry";
    rotated.classList.add(`${targetClassName}`);
  });
}

const attentionItem = document.querySelectorAll(".attentionItem");
for (let x = 0; x < attentionItem.length; x++) {
  const targetClass = attentionItem[x];
  let targetClassName = targetClass.innerHTML
  targetClass.addEventListener("click", function(){
    attention.className = "rebound anibry";
    attention.classList.add(`${targetClassName}`);
  })
}

const turnItem = document.querySelectorAll(".turnItem");
for (let x = 0; x < turnItem.length; x++) {
  const targetClass = turnItem[x];
  let targetClassName = targetClass.innerHTML
  targetClass.addEventListener("click", function(){
    turn.className = "rebound anibry";
    turn.classList.add(`${targetClassName}`);
  })
}

const quakeItem = document.querySelectorAll(".quakeItem");
for (let x = 0; x < quakeItem.length; x++) {
  const targetClass = quakeItem[x];
  let targetClassName = targetClass.innerHTML
  targetClass.addEventListener("click", function(){
    quake.className = "rebound anibry";
    quake.classList.add(`${targetClassName}`);
  })
}

const jiggleItem = document.querySelectorAll(".jiggleItem");
for (let x = 0; x < jiggleItem.length; x++) {
  const targetClass = jiggleItem[x];
  let targetClassName = targetClass.innerHTML
  targetClass.addEventListener("click", function(){
    jiggle.className = "rebound anibry";
    jiggle.classList.add(`${targetClassName}`);
  })
}

const invertItem = document.querySelectorAll(".invertItem");
for (let x = 0; x < invertItem.length; x++) {
  const targetClass = invertItem[x];
  let targetClassName = targetClass.innerHTML
  targetClass.addEventListener("click", function(){
    invert.className = "rebound anibry";
    invert.classList.add(`${targetClassName}`);
  })
}
for (let x = 0; x < reboundItem.length; x++) {
  const targetClass = reboundItem[x];
  let targetClassName = targetClass.innerHTML
  targetClass.addEventListener("click", function(){
    rebound.className = "rebound anibry";
    rebound.classList.add(`${targetClassName}`);
  })
}