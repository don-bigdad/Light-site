
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
    let item = document.querySelectorAll(".card.item");

    for (let i=0;i<list.length;i++){
      list[i].addEventListener("click",function(){
        for(let j=0;j<list.length;j++){
          list[j].classList.remove("active");
        }
        this.classList.add("active");

        for (let k=0;k<item.length;k++){
          item[k].classList.remove("active");
          item[k].classList.add("hide");


        }
      })

    }
