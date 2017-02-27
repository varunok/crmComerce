/*$(function(){
    $(window).scroll(function() {
        var top = $(document).scrollTop();
        if (top < 180) $("nav").css({top: '0', position: 'relative'});
        else $("nav").css({top: '0px', position: 'fixed'});
    });
});
*/


$(document).ready(function(){
  $('#call_back, .close_order, .overlay').click(function (){
    $('#call_back, .overlay, .call_popup, .add_popup, .ordered_inspection, .osmotr_inner, .diplom_popup').css('opacity','0');
    $('#call_back, .overlay, .call_popup, .add_popup, .ordered_inspection, .osmotr_inner, .diplom_popup').css('visibility','hidden');
  });
  $('a.call_me').click(function (e){
    $('#call_back, .overlay, .call_popup').css('opacity','1');
    $('#call_back, .overlay, .call_popup').css('visibility','visible');
    e.preventDefault();
  });
  $('a.open_dip').click(function (e){
    $('#call_back, .overlay, .diplom_popup').css('opacity','1');
    $('#call_back, .overlay, .diplom_popup').css('visibility','visible');
    e.preventDefault();
  });
  $('a.add_advert').click(function (e){
    $('#call_back, .overlay, .add_popup').css('opacity','1');
    $('#call_back, .overlay, .add_popup').css('visibility','visible');
    e.preventDefault();
  });
  $('a.osmotr').click(function (e){
    $('#call_back, .overlay, .ordered_inspection').css('opacity','1');
    $('#call_back, .overlay, .ordered_inspection').css('visibility','visible');
    e.preventDefault();
  });
  $('a.request_view').click(function (e){
    $('#call_back, .overlay, .ordered_inspection').css('opacity','1');
    $('#call_back, .overlay, .ordered_inspection').css('visibility','visible');
    e.preventDefault();
  });
  $('a.osmotr-btn').click(function (e){
    $('#call_back, .overlay, .osmotr_inner').css('opacity','1');
    $('#call_back, .overlay, .osmotr_inner').css('visibility','visible');
    e.preventDefault();
  });

  $('#my_setting .close_order, .overlay').click(function (){
    $('#my_setting, .overlay').css('opacity','0');
    $('#my_setting, .overlay').css('visibility','hidden');
  });
  $('a.my_setting').click(function (e){
    $('#my_setting, .overlay').css('opacity','1');
    $('#my_setting, .overlay').css('visibility','visible');
    e.preventDefault();
  });


  $('#video_instructions .close_order, .overlay').click(function (){
    $('#video_instructions, .overlay').css('opacity','0');
    $('#video_instructions, .overlay').css('visibility','hidden');
  });
  $('a.video_instructions').click(function (e){
    $('#video_instructions, .overlay').css('opacity','1');
    $('#video_instructions, .overlay').css('visibility','visible');
    e.preventDefault();
  });


  $('#payment_account .close_order, .overlay').click(function (){
    $('#payment_account, .overlay').css('opacity','0');
    $('#payment_account, .overlay').css('visibility','hidden');
  });
  $('a.payment_account').click(function (e){
    $('#payment_account, .overlay').css('opacity','1');
    $('#payment_account, .overlay').css('visibility','visible');
    e.preventDefault();
  });


  $('#edit_addvert .close_order, .overlay').click(function (){
    $('#edit_addvert, .overlay').css('opacity','0');
    $('#edit_addvert, .overlay').css('visibility','hidden');
  });
  $('a.edit_addvert').click(function (e){
    $('#edit_addvert, .overlay').css('opacity','1');
    $('#edit_addvert, .overlay').css('visibility','visible');
    e.preventDefault();
  });
});

/*function changeImg(img_id){
  var iid;
  var imgSrc = ["img/tmp_appartments1.jpg", "img/tmp_appartments2.jpg", "img/tmp_appartments3.jpg"];
  var curImg = 0;

  iid = setInterval(function(){
    curImg < imgSrc.length-1 ? ++curImg : curImg = 0;
    $("#"+img_id+" img").attr("src", imgSrc[curImg]);
  }, 500);

  $("#"+img_id+" img").bind('mouseout', function() { clearInterval(iid); curImg = 0; this.src=imgSrc[0]});
}*/


$(function() {
    $('.image-editing img').hover(function() {
        var _this = this,
            images = _this.getAttribute('data').split(',');
            counter = 0;
        this.setAttribute('data-src', this.src);    
        //
        _this.timer = setInterval(function() {
            if(counter > images.length-1) {
                counter = 0;
            }
            _this.src=images[counter];

            counter++;
        }, 500);

    }, function() {
        this.src = this.getAttribute('data-src');
        clearInterval(this.timer);
    });
});


function showhide_elements(el){
  $('#'+el).fadeToggle('slow', 'linear');
}


jQuery( document ).ready(function() {
  jQuery('#scrollup img').mouseover( function(){
    jQuery( this ).animate({opacity: 0.65},100);
  }).mouseout( function(){
    jQuery( this ).animate({opacity: 1},100);
  }).click( function(){
    window.scroll(0 ,0); 
    return false;
  });

  jQuery(window).scroll(function(){
    if ( jQuery(document).scrollTop() > 0 ) {
      jQuery('#scrollup').fadeIn('fast');
    } else {
      jQuery('#scrollup').fadeOut('fast');
    }
  });
});