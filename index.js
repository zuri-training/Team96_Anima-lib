let target = document.querySelector(".target");
let btn = document.querySelector(".toggle");
let rotate = false;
let runner1;
let runner2;
let degrees = 0;
const mobilemenu = document.querySelector(".menu");
const mobilemenulist = document.querySelector(".mobilemenulist");
const closemenu = document.querySelector(".closemenu");
const mobilemenuitem = document.getElementsByClassName("mobilemenuitem");

mobilemenu.addEventListener("click", function () {
  mobilemenulist.classList.add("displayflex");
});
closemenu.addEventListener("click", function () {
  mobilemenulist.classList.remove("displayflex");
});

for (let x = 0; x < mobilemenuitem.length; x++) {
  const activeitem = mobilemenuitem[x];
  activeitem.style.backgroundColor = "white";
  activeitem.addEventListener("click", function () {
    activeitem.style.backgroundColor = "#5A189A";
    activeitem.style.Color = "white";
  });
}

function start() {
  clearInterval(runner2);
  runner1 = setInterval(function () {
    degrees++;
    target.style.webkitTransform = "rotate(" + degrees + "deg)";
  }, 50);
}

function stop() {
    clearInterval(runner1);
    runner2 = setInterval(function () {
        degrees--;
      target.style.webkitTransform = "rotate(" + degrees + "deg)";
    }, 50);
}

btn.addEventListener("click", function () {
  if (!rotate) {
    rotate = true;
    start();
  } else {
    rotate = false;
    stop();
  }
});
