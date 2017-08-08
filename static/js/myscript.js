$(function(){
    
    // Всплывающее подменю
    
    $('#categoryClick').bind('click', function(e) {
        e.preventDefault();
        if ($('.sub-menu').hasClass('open')) {
            $('.sub-menu').hide('fast');
            $('.sub-menu').removeClass('open');
        } else {
            $('.sub-menu').addClass('open');
            $('.sub-menu').show('slow');
        }
    });
    
    
    //Слайдер    
    
    
    $('.flexslider').flexslider({
        animation: "fade",
        slideshow: true,
        slideshowSpeed: 8000,
        animationSpeed: 1000,
        directionNav: true,
        controlNav: true,
        prevText: "",
        nextText: ""
    });
    
    //
    //$(".event-pic").each(function(){
 	  //$(this).css("height",($(this).width()));
    //});
        
    //alert($(window).width());
    
    $(".menu-mobil").click(function(){
        $(".menu").slideToggle(500);
    });
    
    // закладки
      $('.bookmark').on('click', 'li:not(.active)', function() {  
        $(this).addClass('active').siblings().removeClass('active').parents('.tabs').find('.bookmarker-box').eq($(this).index()).fadeIn(150).siblings('.bookmarker-box').hide();  
      })  
      $(".bookmark li").eq(0).click();
      
    //
    
    $(".more-foto").click(function(){
        $(".foto-article-block").slideToggle();
        $(this).toggleClass("active");
    });
    
    //
    
    $(".characteristic").click(function(){
        $(this).toggleClass("active");
        $(this).parent().find(".characteristic-table").slideToggle();
    });
    
    //
    
    $(".open-fights").click(function(){
        $(this).toggleClass("active");
        $(this).parent().find(".fights").slideToggle();
    });
        
	 $(".title-gallery").click(function(){
        $(this).toggleClass("active");
        $(this).parent().find(".gallery-block").slideToggle();
    });
    
//
$(".progress-bar").each(function(){
    if($(this).width() < 20){
        $(this).css("color","#000000");
        
    }
});

	
});//конец ready