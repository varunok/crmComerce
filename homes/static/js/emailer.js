$(document).ready(function() {
	$('#send_email').on('click', function(event) {
		event.preventDefault();
        var message_text = $('#write_email').val();
        $('#write_email').val('');
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').html('<div><i class="fa fa-spinner fa-pulse fa-1x fa-fw"></i>Отправка</div').fadeIn(500).delay(2000);
		$.post('send_email_rieltor', {'text': message_text})
		.success( function (data) {
            $('.messageServer').animate({'backgroundColor': '#5bc0de'}, 300);
            $('.messageServer').text('Отправлено').fadeIn(1000).delay(2000).fadeOut(500);
            ('#write_email').val('');
        })
        .error(function(data) {
            $('.messageServer').animate({'backgroundColor': '#c9302c'}, 300);
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
	});	
	$('#send_email_so').on('click', function(event) {
		event.preventDefault();
        var id_so = $('#sisingle_obj_id').attr('sisingle_obj_id');
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').html('<div><i class="fa fa-spinner fa-pulse fa-1x fa-fw"></i>Отправка</div').fadeIn(500).delay(2000);
        data = {
            'email': $('#text_email_so').val(),
            'id_so': id_so
        }
		$.post('send_email_so', data)
    		.success( function (data) {
            $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text('Отправлено').fadeIn(1000).delay(2000).fadeOut(500);
            ('#write_email').val('');
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
	});


});