  const selectedAll = document.querySelectorAll(".selected");

  selectedAll.forEach ((selected) => {
   const optionsContainer = selected.previousElementSibling;
   const searchBox = selected.nextElementSibling;
 

   const optionsList = optionsContainer.querySelectorAll(".option");

   selected.addEventListener("click", () => {

      if  (optionsContainer.classList.contains("active")) {
      optionsContainer.classList.remove("active");
      } 
      else {
         let currentActive = document.querySelector("options-container.active");

         if(currentActive) {
            currentActive.classList.remove("active");
         }

          optionsContainer.classList.add("active");
      }

      // optionsContainer.classList.toggle("active");

      searchBox.value = "";
      filterList("");

      if (optionsContainer.classList.contains("active")){
         searchBox.focus();
      };
   });

   optionsList.forEach( o => {
      o.addEventListener( "click", () => {
         selected.innerHTML = o.querySelector("label").innerHTML;
         optionsContainer.classList.remove("active");   
      });
   });
})