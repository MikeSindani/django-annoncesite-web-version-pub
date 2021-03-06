$(document).ready(function(){
    $('.owl-carousel').owlCarousel({
        loop:true,
        margin:100,
        nav:true,
        dots:true,
        autoplay:true,
        autoplayTimeout:4000,
        autoplaySpeed:1000,
        responsiveClass:true,
    responsive:{
        0:{
            items:1,
            nav:true
        },
       300:{
            items:2,
            nav:false
        },
        600:{
            items:3.7,
            nav:false
        },
        900:{
            items:3.5,
            nav:false
        },
        1100:{
            items:4.5,
            nav:true,
            loop:false
        }
    }
    });

});

