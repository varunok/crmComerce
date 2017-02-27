/**
 * Created by varunok on 03.08.16.
 */
$(document).ready(function() {
    $('#add_makler').on('click', function (event) {
        event.preventDefault();
        $.get('maklers/form_makler').success( function (data) {
            $('#add_form').html(data);
            $('.makler-form').animate({top: '10%'}, 1000)
        });
    });
    
    $('#add_form').on('click', '#cancel_add_makler', function (event) {
        event.preventDefault();
        $('.makler-form').animate({top: '-860px'}, 1000)
    });   
    
    $('#add_form').on('click', '#send_form_makler', function (event) {
        event.preventDefault();
        var msg   = $('#send_form').serialize();
        // console.log(msg)
        $.post('maklers/add_makler', msg)
            .success( function (data) {
                $('.makler-form').animate({top: '-860px'}, 1000);
                $('.add_apend_makler').append(data);
                // $('.add_apend_makler').children('tr').fadeIn('slow')
        })
            .error(function(data) {
                $('#add_form').html(data.responseText);
                $('.makler-form').css('top', '10%');
                wrongForm();
            });
    });
    $('table').on('click', '.fa-pencil', function (event) {
        event.preventDefault();
        var id = $(this).parents('a').attr('id-makler');
        $.post('maklers/edit_makler', {'id':id})
        .success( function (data) {
            $('#add_form').html(data);
            $('.makler-form').animate({top: '10%'}, 1000)
        });
    });

    $('table').on('click', '.fa-times', function (event) {
        event.preventDefault();
        var id = $(this).parents('a').prev().attr('id-makler');
        var _this = $(this).parents('tr');
        $.post('maklers/del_makler', {'id':id})
        .success( function (data) {
            $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
            $('.messageServer').text(data).fadeIn(1000).delay(2000).fadeOut(500);
            _this.fadeOut('slow', function() {
                
            });
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    });

    $('#add_form').on('click', '#edit_form_makler', function (event) {
        event.preventDefault();
        var msg   = $('#send_form').serialize();
        var id = $(this).attr('id-makler-btn');
        $.post('maklers/save_edit_makler/'+id, msg)
        .success( function (data) {
            $('.makler-form').animate({top: '-860px'}, 1000);
            $('[id-makler="'+id+'"]').parents('tr').replaceWith(data);
        })
        .error(function(data) {
                $('#add_form').html(data.responseText);
                $('.makler-form').css('top', '10%');
                wrongForm();
            });
    });

    function wrongForm() {
        $('.makler-form').animate({top: '15%'},50);
        $('.makler-form').animate({top: '10%'},50);
        $('.makler-form').animate({top: '14%'},80);
        $('.makler-form').animate({top: '10%'},80);
        $('.makler-form').animate({top: '13%'},100);
        $('.makler-form').animate({top: '10%'},100);
        $('.makler-form').animate({top: '12%'},120);
        $('.makler-form').animate({top: '10%'},120);
        $('.makler-form').animate({top: '11%'},150);
        $('.makler-form').animate({top: '10%'},150);
    }

    $('#send_email_makler').on('click', function (event) {
        event.preventDefault();
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').text('Идет рассылка').fadeIn(1000);
        data = {
            "subject": $('#email_subject').val(),
            "body": $('#email_body').val()
        }
        $.post('send_email_makler', data)
        .success( function (data) {
            $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
            $('.messageServer').text('Отправлено '+data+' сообщений').fadeIn(1000).delay(2000).fadeOut(500);
            ('#write_email').val('');
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
    $('#search_makler').on('click', function (event) {
        event.preventDefault();
        var data = $('#search_form').serialize();
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').text('Идет поиск').fadeIn(1000);
        $.post('search_makler', data)
        .success( function (data) {
            //('#list_makler').text('');
            $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
            $('.messageServer').text('Поиск завершен').fadeIn(1000).delay(2000).fadeOut(500);
            $('#list_makler').html(data);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    })
    
});