/**
 * Created by varunok on 06.08.16.
 */
$(document).ready(function() {
        $.datepicker.regional['ru'] = {
        closeText: 'Закрыть',
        prevText: '<Пред',
        nextText: 'След>',
        currentText: 'Сегодня',
        monthNames: ['Январь','Февраль','Март','Апрель','Май','Июнь',
        'Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'],
        monthNamesShort: ['Янв','Фев','Мар','Апр','Май','Июн',
        'Июл','Авг','Сен','Окт','Ноя','Дек'],
        dayNames: ['воскресенье','понедельник','вторник','среда','четверг','пятница','суббота'],
        dayNamesShort: ['вск','пнд','втр','срд','чтв','птн','сбт'],
        dayNamesMin: ['Вс','Пн','Вт','Ср','Чт','Пт','Сб'],
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

    $('tr').attr('style', '');

    $('#add_task_form').on('click', function (event) {
        event.preventDefault();
        $.get('tasking/get_form_task').success( function (data) {
            $('#add_form').html(data);
            $('.task-form').animate({top: '10%'}, 1000);
            $('#add_form').trigger('click');
            $('select').select2();
        });
    });

    $('#add_form').on('click','#cancel_add_form', function (event) {
        event.preventDefault();
        //$('.task-form').hide('scale');
        $('.task-form').animate({top: '-700px'}, 500);
    });

    $("#add_form").on('click', function(event) {
        event.preventDefault();
        $('#id_dead_line').datetimepicker($.timepicker.regional['ru']);
    });

    $('#add_form').on('click', '#save_form_tasking', function (event) {
        event.preventDefault();
        var msg   = $('#send_form').serialize();
        $.post('tasking/save_form_tasking', msg)
        .success( function (data) {
            $('.task-form').animate({top: '20%'}, 2000);
            $('.task-form').animate({top: '-700px'}, 500, function () {
                window.location.replace("/tasking");
                // $('#add_single_task').append(data);
                // $('tr').fadeIn('slow');
                // $('.count_active_task').text(parseInt($('.count_active_task').text())+1);
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

    $('.task').on('click', '.fa-play', function (event) {
        event.preventDefault();
        var id_task = $(this).parents('td').attr('id-task');
        var task = $(this).parents('tr');
        $.post('tasking/to_archive', {"id": id_task})
        .success( function (data) {
            task.fadeOut('slow', function () {
                task.remove();
                $('.count_active_task').text(parseInt($('.count_active_task').text())-1);
                $('.count_archive_task').text(parseInt($('.count_archive_task').text())+1);
            });
        })
        .error(function(data) {});
    });

    $(document).on('click', '.fa-times', function(event){
        event.preventDefault();
        var id_task = $(this).parents('td').attr('id-task');
        var task = $(this).parents('tr');
        var is_archive = $(this).parents('td').children('a').eq(0).children('.fa-play')
        $.post('tasking/to_trash', {"id": id_task})
        .success( function (data) {
            task.fadeOut('slow', function () {
                task.remove();
                if (is_archive.length){
                    $('.count_active_task').text(parseInt($('.count_active_task').text())-1);
                } else {
                    $('.count_archive_task').text(parseInt($('.count_archive_task').text())-1);
                }
                $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
                $('.messageServer').text('Задача удалена').fadeIn(1000).delay(2000).fadeOut(500);
            });
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        });

    });

    $('#search_task').on('click', function (event) {
        event.preventDefault();
        var msg   = $('#search_form').serialize();
        $.post('tasking/search_task', msg)
        .success( function (data) {
            $('#add_single_task').fadeOut('slow', function () {
                // $('#add_single_task').html('');
                $('#add_single_task').html(data);
                $('#add_single_task').fadeIn('slow');
            });

        })
        .error(function(data) {});
    });
    $(document).on('click', '.fa-pencil', function(event){
        event.preventDefault();
        var id_task = $(this).parents('td').attr('id-task');
        $.post('tasking/edit_form', {"id": id_task})
        .success( function (data) {
            $('#add_form').html(data);
            $('.task-form').animate({top: '10%'}, 2000);
            $('#add_form').trigger('click');
            $('select').select2();
        })
        .error(function(data) {});
    })
});