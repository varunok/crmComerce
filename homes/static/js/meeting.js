/**
 * Created by varunok on 18.09.16.
 */
$(document).ready(function() {
    $.datepicker.regional['ru'] = {
        closeText: 'Закрыть',
        prevText: '<Пред',
        nextText: 'След>',
        currentText: 'Сегодня',
        monthNames: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        monthNamesShort: ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн',
            'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'],
        dayNames: ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота'],
        dayNamesShort: ['вск', 'пнд', 'втр', 'срд', 'чтв', 'птн', 'сбт'],
        dayNamesMin: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
        weekHeader: 'Не',
        dateFormat: 'yy-mm-dd',
        firstDay: 1,
        isRTL: false,
        showMonthAfterYear: false,
        yearSuffix: ''
    };
    $.datepicker.setDefaults($.datepicker.regional['ru']);

    $.timepicker.regional['ru'] = {
        timeOnlyTitle: 'Выберите время',
        timeText: 'Время',
        hourText: 'Часы',
        minuteText: 'Минуты',
        secondText: 'Секунды',
        millisecText: 'Миллисекунды',
        timezoneText: 'Часовой пояс',
        currentText: 'Сейчас',
        closeText: 'Закрыть',
        timeFormat: 'HH:mm',
        amNames: ['AM', 'A'],
        pmNames: ['PM', 'P'],
        isRTL: false
    };
    $.timepicker.setDefaults($.timepicker.regional['ru']);


    $('#add_meet_form').on('click', function (event) {
        event.preventDefault();
        $.get('meeting/get_form_task').success( function (data) {
            $('#add_form').html(data);
            $('.task-form').animate({top: '10%'}, 1000);
            $('#add_form').trigger('click');
            $('select').select2();
        });
    });

    $(document).on('click','#cancel_add_form', function (event) {
        event.preventDefault();
        //$('.task-form').hide('scale');
        $('.task-form').animate({top: '-700px'}, 500);
    });

    $("#add_form").on('click', function(event) {
        event.preventDefault();
        $('#id_meet_date').datetimepicker($.timepicker.regional['ru']);
    });

    $(document).on('click', '#save_form_meeting', function (event) {
        event.preventDefault();
        var msg   = $('#send_form').serialize();
        $.post('meeting/save_form_meeting', msg)
        .success( function (data) {
            $('.task-form').animate({top: '20%'}, 2000);
            $('.task-form').animate({top: '-700px'}, 500, function () {
                window.location.replace("/meeting");
                // $('#add_single_meet').append(data);
                // $('tr').fadeIn('slow');
                // $('.count_active_meet').text(parseInt($('.count_active_meet').text())+1);
            });

        })
        .error(function(data) {
            $('#add_form').html(data.responseText);
            $('.task-form').css('top', '10%');
            $('#add_form').trigger('click');
            $('select').select2();
            wrongForm();
        })
    });
    function wrongForm() {
        $('.task-form').animate({top: '15%'},50);
        $('.task-form').animate({top: '10%'},50);
        $('.task-form').animate({top: '14%'},80);
        $('.task-form').animate({top: '10%'},80);
        $('.task-form').animate({top: '13%'},100);
        $('.task-form').animate({top: '10%'},100);
        $('.task-form').animate({top: '12%'},120);
        $('.task-form').animate({top: '10%'},120);
        $('.task-form').animate({top: '11%'},150);
        $('.task-form').animate({top: '10%'},150);
    }

    $(document).on('click', '.fa-play', function (event) {
        event.preventDefault();
        var id_meet = $(this).parents('td').attr('id-meet');
        var meet = $(this).parents('tr');
        $.post('meeting/to_archive', {"id": id_meet})
        .success( function (data) {
            meet.fadeOut('slow', function () {
                meet.remove();
                $('.count_active_meet').text(parseInt($('.count_active_meet').text())-1);
                $('.count_archive_meet').text(parseInt($('.count_archive_meet').text())+1);
            });
        })
        .error(function(data) {});
    });

    $(document).on('click', '.fa-times', function(event){
        event.preventDefault();
        var id_meet = $(this).parents('td').attr('id-meet');
        var meet = $(this).parents('tr');
        var is_archive = $(this).parents('td').children('a').eq(0).children('.fa-play')
        $.post('meeting/to_trash', {"id": id_meet})
        .success( function (data) {
            meet.fadeOut('slow', function () {
                meet.remove();
                if (is_archive.length){
                    $('.count_active_meet').text(parseInt($('.count_active_meet').text())-1);
                } else {
                    $('.count_archive_meet').text(parseInt($('.count_archive_meet').text())-1);
                }
                $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
                $('.messageServer').text('Встреча удалена').fadeIn(1000).delay(2000).fadeOut(500);
            });
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        });

    });

    $(document).on('click', '.fa-pencil', function(event){
        event.preventDefault();
        var id_meet = $(this).parents('td').attr('id-meet');
        $.post('meeting/edit_form', {"id": id_meet})
        .success( function (data) {
            $('#add_form').html(data);
            $('.task-form').animate({top: '10%'}, 2000);
            $('#add_form').trigger('click');
            $('select').select2();
        })
        .error(function(data) {});
    })

    $('#search_meet').on('click', function (event) {
        event.preventDefault();
        var msg   = $('#search_form').serialize();
        $.post('meeting/search_meet', msg)
        .success( function (data) {
            $('#add_single_meet').fadeOut('slow', function () {
                // $('#add_single_task').html('');
                $('#add_single_meet').html(data);
                $('#add_single_meet').fadeIn('slow');
            });

        })
        .error(function(data) {});
    });
});