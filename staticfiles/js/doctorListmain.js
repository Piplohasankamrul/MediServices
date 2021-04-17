console.log("Sd Connected!");
/*
const accordionItemHeaders = document.querySelectorAll(".accordian--item--header");
accordionItemHeaders.forEach(accordionItemHeader => {
    accordionItemHeader.addEventListener("click", event => {
        $('.accordian--item--header').toggleClass('collapsed');
        $('.accordian--item--header').toggleClass('accordian--item--header--active');
        
        const currentlyActiveAccordionItemHeader = document.querySelector(".accordian--item--content");
        if(currentlyActiveAccordionItemHeader && currentlyActiveAccordionItemHeader!==accordionItemHeader) {
        currentlyActiveAccordionItemHeader.classList.toggle("show");
        
        //currentlyActiveAccordionItemHeader.nextElementSibling.style.maxHeight = 0;
     }
    
        
    
  });
});
*/
$(document).ready(function(){
	  $(".accordian--item--header").click(function(){
       // self clicking close
       if($(this).next(".accordian--item--content").hasClass("show")){
         $(this).next(".accordian--item--content").removeClass("show").slideUp();
         $('.accordian--item--header').toggleClass('collapsed');
         $('.accordian--item--header').toggleClass('accordian--item--header--active');	
       }
     else{
	    $(".accordian--item--content").removeClass("show").slideUp();
        $(this).next(".accordian--item--content").addClass("show").slideDown();
        $('.accordian--item--header').toggleClass('collapsed');
        $('.accordian--item--header').toggleClass('accordian--item--header--active');
      }
	  })
	})

















/*
('.accordian--item').on('click',function(){
    $('.accordian--item a').removeClass('collapsed');
    $('.accordian--item a').attr("aria-selected","true");
    $('#accordian-213074').addClass('show');
})

$('.accordian--item').toggle(function(){
    $('.accordian--item a').removeClass('collapsed');
    $('.accordian--item a').attr("aria-selected","true");
    $('#accordian-213074').addClass('show');
});/*,
    function(){
    $('#accordian-213074').removeClass('show');
    $('.accordian--item a').attr("aria-selected","false");
    $('.accordian--item a').addClass('collapsed');
    
    }*/


/*
function myFunction() {
  var x = document.getElementsByClassName("accordian--item--header").getAttribute("aria-expanded"); 
  if (x === "false") 
  {
  x = "true"
  } else {
  x = "false"
  }
  document.getElementsByClassName("accordian--item--header").setAttribute("aria-expanded", x);
  }
  */










