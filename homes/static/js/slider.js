jQuery(document).ready(function(){
	function htmSlider(wrap,prev,next,item){

		var slideWrap = jQuery('.'+wrap);

		var nextLink = jQuery(next);
		var prevLink = jQuery(prev);

		var playLink = jQuery('.auto');

		var is_animate = false;

		var slideWidth = jQuery('.slide-item').outerWidth();

		var newLeftPos = slideWrap.position().left - slideWidth;

		nextLink.click(function(){
			if(!slideWrap.is(':animated')) {
				slideWrap.animate({left: newLeftPos}, 500, function(){
					slideWrap
						.find('.slide-item:first')
						.appendTo(slideWrap)
						.parent()
						.css({'left': 0});
				});
			}
		});

		prevLink.click(function(){
			if(!slideWrap.is(':animated')) {
				slideWrap
					.css({'left': newLeftPos})
					.find('.slide-item:last')
					.prependTo(slideWrap)
					.parent()
					.animate({left: 0}, 500);
			}
		});

		function autoplay(){
			if(!is_animate){
				is_animate = true;
				slideWrap.animate({left: newLeftPos}, 500, function(){
					slideWrap
						.find('.slide-item:first')
						.appendTo(slideWrap)
						.parent()
						.css({'left': 0});
					is_animate = false;
				});
			}
		}

		playLink.click(function(){
			if(playLink.hasClass('play')){
				playLink.removeClass('play').addClass('pause');
				jQuery('.navy').addClass('disable');
				timer = setInterval(autoplay, 1500);
			} else {
				playLink.removeClass('pause').addClass('play');
				jQuery('.navy').removeClass('disable');
				clearInterval(timer);
			}
		});

	}

	htmSlider('slide-wrap1','.prev1','.next1','');
	htmSlider('slide-wrap2','.prev2','.next2','');
});