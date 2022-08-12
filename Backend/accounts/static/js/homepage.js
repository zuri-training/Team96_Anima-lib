let acc = document.getElementsByClassName("faqq");

let i;
for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
    this.classList.toggle("active");
    let tick = this.nextElementSibling;
    if (tick.style.maxHeight) {
      tick.style.maxHeight = null;
    } else {
      tick.style.maxHeight = 20 + tick.scrollHeight + "px";
    }
  });
}
