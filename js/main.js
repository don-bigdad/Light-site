
(function() {
    "use strict";
  
/**
 * Easy selector helper function
 */
const select = (el, all = false) => {
    el = el.trim()
    if (all) {
    return [...document.querySelectorAll(el)]
    } else {
    return document.querySelector(el)
    }
}
/**
   * Menu isotope and filter
   */
window.addEventListener('load', () => {
    let menuContainer = select('.menu-container');
    if (menuContainer) {
      let menuIsotope = new Isotope(menuContainer, {
        itemSelector: '.menu-item',
        layoutMode: 'fitRows'
      });

      let menuFilters = select('#menu-flters li', true);

      on('click', '#menu-flters li', function(e) {
        e.preventDefault();
        menuFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');
        
        menuIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });

      }, true);
    }

  });
})()



const countDownDate = new Date("Nov 31,2022 00:00:00").getTime();  


var countDownFunction =setInterval(function() {
    var now = new Date().getTime();

    var distance = countDownDate-now;

    var days = Math.floor(distance /(1000*60*60*24));

    var hours = Math.floor((distance % (1000*60*60*24))/(1000*60*60));

    var minutes = Math.floor((distance % (1000*60*60))/(1000*60));

    var seconds = Math.floor((distance % (1000*60))/1000);

    document.getElementById("timer").innerHTML = 
    days+"D "+hours+"H "+minutes+"M "+seconds+"S ";


    if (distance <= 0){
        clearInterval(countDownFunction);
        document.getElementById("timer").innerHTML = "Sales end"
    }
},1000)


    let list = document.querySelectorAll(".list");
    let itembox = document.querySelectorAll(".item");

    for (let i=0;i<list.length;i++){
      list[i].addEventListener("click",function(){
        for(let j=0;j<list.length;j++){
          list[j].classList.remove("active");
        }
        this.classList.add("active");

        let dataFilter = this.getAttribute("data-filter");
        
        for (let k=0;k<itembox.length;k++){
          itembox[k].classList.remove("active");
          itembox[k].classList.add("hide");

          if (itembox[k].getAttribute("data-item")==dataFilter ||
          dataFilter == "all"){
            itembox[k].classList.remove("hide");
            itembox[k].classList.add("active");
          }
        }
      })

    }
