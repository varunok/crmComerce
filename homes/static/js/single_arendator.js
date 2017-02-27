
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
    $(document).on('click', '#avtomat_add_arendator', function (event) {
        event.preventDefault();
        $('#modal_avto').fadeIn('slow');
    });
    $(document).on('click', '#cencel_automat_btn', function (event) {
        event.preventDefault();
        $('#modal_avto').fadeOut('slow');
    });
    $(document).on('click', '#ok_automat_btn', function (event) {
        event.preventDefault();
        $('#modal_avto').fadeOut('slow');
        var data = $('#avtomat_form').serialize();
        $.get('automat_tie_arendator', data)
            .success( function (data) {
            // $('#add_tr').html(' ');
            // $('#add_tr').fadeIn('slow');
            // $('#add_tr').prepend(data);
            // $('.show_tr').fadeIn('slow');
            // var count_ar = parseInt($('#add_tr').children('.show_tr').length);
            // $('#get_arendator').children('span').text(count_ar);
            $('.tabs-rule').fadeOut('200', function() {
                    $(this).html('');
                    $(this).html(data);
                    $(this).fadeIn('200');
                });
        });
    });
    $(document).on('click', '#add_id_cont_owner', function(event) {
        event.preventDefault();
        var data = $('#cont_form').serialize();
        $.get('add_id_cont_owner', data)
        .success( function (data) {
            $('.tabs-rule').fadeOut('200', function() {
                    $(this).html('');
                    $(this).html(data);
                    $(this).fadeIn('200');
                });
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text(data.responseText).fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
    $(document).on('click', '#clear_cont_owner', function(event) {
        event.preventDefault();
        var data = $('#clear_form').serialize();
        $.post('clear_cont_owner', data)
        .success( function (data) {
            $('.tabs-rule').fadeOut('200', function() {
                    $(this).html('');
                    $(this).html(data);
                    $(this).fadeIn('200');
                });
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text(data.responseText).fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
    $(document).on('click', '#del_cont_owner', function(event) {
        event.preventDefault();
        var id_arendator = $(this).prev('.id_arendator').val();
        var id_cont_owner = $(this).next('.id_cont_owner').val();
        var data = {
            'id_arendator': id_arendator,
            'id_cont_owner': id_cont_owner
        }
        $.post('del_cont_owner', data)
        .success( function (data) {
            $('.tabs-rule').fadeOut('200', function() {
                    $(this).html('');
                    $(this).html(data);
                    $(this).fadeIn('200');
                });
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text(data.responseText).fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
    $(document).on('change', '.show_cont_owner', function(event) {
        event.preventDefault();
        var _this = $(this).parents('.color');
        var show = $(this).val();
        var id_arendator = $(this).prev('.id_arendator').val();
        var id_cont_owner = $(this).next('.id_cont_owner').val();
        var data = {
            'show': show,
            'id_arendator': id_arendator,
            'id_cont_owner': id_cont_owner
        }
        $.post('change_show_owner', data)
        .success( function (data) {
            _this.removeClass().addClass(table_color(show)+' color');
            $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text(data).fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text(data.responseText).fadeIn(1000).delay(2000).fadeOut(500);
        });
    });

    function table_color(arg){
        if(arg === '1'){return 'info'}
        else if(arg === '2'){return 'warning'}
        else if(arg === '3'){return 'danger'}
        else if(arg === '4'){return 'success'}
        else {return ' '}
    }


    // START BLOCK MEET
    $('.tabs-rule').on('click', '#add_task_form_meet', function (event) {
        event.preventDefault();
        data = {
            'id_so': $('#single_arendator_id').attr('single_arendator_id')
        };
        $.get('get_form_meet', data).success( function (data) {
            $('#add_form_m').html(data);
            $('.task-form').animate({top: '10%'}, 1000);
            $('#add_form_m').children('.task-form').fadeIn('slow');
            $('#add_form_m').trigger('click');
            $('select').select2();
            $("#id_meet_buyer").prop("disabled", true);
            var $arendator_id = $("#id_meet_arendator").select2();
            var id_arendator = $('#single_arendator_id').attr('single_arendator_id');    
            $arendator_id.val(id_arendator).trigger("change");
            // $("#id_meet_arendator").prop("disabled", true);
        });
    });

    $('.tabs-rule').on('click','#cancel_add_form', function (event) {
        event.preventDefault();
        $('.task-form').animate({top: '-700px'}, 1000);
    });

    $('.tabs-rule').on('click', '#add_form_m', function(event) {
        event.preventDefault();
        $('#id_meet_date').datetimepicker($.timepicker.regional['ru']);
    });

    $('.tabs-rule').on('click', '#save_form_meeting', function (event) {
        event.preventDefault();
        var msg   = $('#send_form').serialize();
        $.post('save_form_meeting', msg)
        .success( function (data) {
            $('.task-form').animate({top: '20%'}, 2000);
            $('.task-form').animate({top: '-700px'}, 500, function () {
                if ($('#id_meet').length === 0 ) {
                    $('#get_meeting_arendator').children('.label').text(parseInt($('#get_meeting_arendator').children('.label').text())+1)
                }
                var id_arendator = $('#single_arendator_id').attr('single_arendator_id');
                $.get('get_meeting_arendator', {"id_arendator": id_arendator}, function(data) {
                    $('.tabs-rule').fadeOut('200', function() {
                        $(this).html('');
                        $(this).html(data);
                        $(this).fadeIn('200');
                    });
                });
            });
        })
        .error(function(data) {
            $('#add_form_m').html(data.responseText);
            $('.task-form').css('top', '10%');
            $('#add_form_m').trigger('click');
            $('select').select2();
            wrongForm();
        })
    });
    $('.tabs-rule').on('click', '#meets_active', function(event) {
        event.preventDefault();
        var id_arendator = $('#single_arendator_id').attr('single_arendator_id');
        $.get('get_meetings_active', {"id_arendator":id_arendator}, function(data) {
            $('.tabs-rule').fadeOut('200', function() {
                $(this).html('');
                $(this).html(data);
                $(this).fadeIn('200');
            });
        });
    });
    $('.tabs-rule').on('click', '#meets_archive', function(event) {
        event.preventDefault();
        var id_arendator = $('#single_arendator_id').attr('single_arendator_id');
        $.get('get_meetings_archive', {"id_arendator":id_arendator}, function(data) {
            $('.tabs-rule').fadeOut('200', function() {
                $(this).html('');
                $(this).html(data);
                $(this).fadeIn('200');
            });
        });
    });

    $('.tabs-rule').on('click', '#meets_all', function(event) {
        event.preventDefault();
        var id_arendator = $('#single_arendator_id').attr('single_arendator_id');
        $.get('get_meeting_arendator', {"id_arendator":id_arendator}, function(data) {
            $('.tabs-rule').fadeOut('200', function() {
                $(this).html('');
                $(this).html(data);
                $(this).fadeIn('200');
            });
        });
    });

    $('.tabs-rule').on('click', '.fa-times', function(event){
        event.preventDefault();
        var id_meet = $(this).parents('td').attr('id-meet');
        if (id_meet) {
            var meet = $(this).parents('tr');
            var is_archive = $(this).parents('td').children('a').eq(0).children('.fa-play')
            $.post('to_trash_meet', {"id": id_meet})
            .success( function (data) {
                meet.fadeOut('slow', function () {
                    meet.remove();
                    $('#get_meeting_arendator').children('.label').text(parseInt($('#get_meeting_arendator').children('.label').text())-1)
                    var id_arendator = $('#single_arendator_id').attr('single_arendator_id');
                    $.get('get_meeting_arendator', {"id_arendator": id_arendator}, function(data) {
                        $('.tabs-rule').fadeOut('200', function() {
                            $(this).html('');
                            $(this).html(data);
                            $(this).fadeIn('200');
                        });
                    });
                    $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
                    $('.messageServer').text('Встреча удалена').fadeIn(1000).delay(2000).fadeOut(500);
                });
            })
            .error(function(data) {
                $('.messageServer').css('backgroundColor', '#c9302c');
                $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
            });
        }

    });
    $('.tabs-rule').on('click', '.fa-play', function (event) {
        event.preventDefault();
        var id_meet = $(this).parents('td').attr('id-meet');
        if (id_meet) {
            var meet = $(this).parents('tr');
            $.post('to_archive_meet', {"id": id_meet})
            .success( function (data) {
                meet.fadeOut('slow', function () {
                    meet.remove();
                    var id_arendator = $('#single_arendator_id').attr('single_arendator_id');
                    $.get('get_meetings_archive', {"id_arendator": id_arendator}, function(data) {
                        $('.tabs-rule').fadeOut('200', function() {
                            $(this).html('');
                            $(this).html(data);
                            $(this).fadeIn('200');
                        });
                    });
                });
            })
            .error(function(data) {});
        }
    });
    $('.tabs-rule').on('click', '.met', function(event){
        event.preventDefault();
        var id_meet = $(this).parents('td').attr('id-meet');
        if (id_meet) {
            $.post('edit_form_meet', {"id": id_meet})
            .success( function (data) {
                $('#add_form_m').html(data);
                $('.task-form').animate({top: '10%'}, 1000);
                // $('#add_form_t').children('.task-form').fadeIn('slow');
                $('#add_form_m').trigger('click');
                $('select').select2();
            })
            .error(function(data) {});
        }
    })
    // END BLOCK MEET

    //  START  Block TASK
    $('.tabs-rule').on('click', '#add_task_form', function (event) {
        event.preventDefault();
        data = {
            'id_so': $('#single_arendator_id').attr('single_arendator_id')
        };
        $.get('get_form_single_task', data).success( function (data) {
            $('#add_form_t').html(data);
            $('.task-form').animate({top: '10%'}, 1000);
            $('#add_form_t').children('.task-form').fadeIn('slow');
            $('#add_form_t').trigger('click');
            $('select').select2();
            $("#id_task_buyer").prop("disabled", true);
            var $arendator_id = $("#id_task_arendator").select2();
            var id_arendator = $('#single_arendator_id').attr('single_arendator_id');    
            $arendator_id.val(id_arendator).trigger("change");
            // $("#id_task_arendator").prop("disabled", true);
        });
    });
    $('.tabs-rule').on('click', '#add_form_t', function(event) {
        event.preventDefault();
        $('#id_dead_line').datetimepicker($.timepicker.regional['ru']);
    });

    $('.tabs-rule').on('click', '#save_form_tasking', function (event) {
        event.preventDefault();
        var msg   = $('#send_form').serialize();
        $.post('save_form_tasking_task', msg)
        .success( function (data) {
            $('.task-form').animate({top: '20%'}, 2000);
            $('.task-form').animate({top: '-700px'}, 500, function () {
                if ($('#id_task').length === 0 ) {
                    $('#get_tasking_arendator').children('.label').text(parseInt($('#get_tasking_arendator').children('.label').text())+1)
                }
                var id_arendator = $('#single_arendator_id').attr('single_arendator_id');
                $.get('get_tasking_arendator', {"id_arendator": id_arendator}, function(data) {
                    $('.tabs-rule').fadeOut('200', function() {
                        $(this).html('');
                        $(this).html(data);
                        $(this).fadeIn('200');
                    });
                });
            });
        })
        .error(function(data) {
            $('#add_form_t').html(data.responseText);
            $('.task-form').css('top', '10%');
            $('#add_form_t').trigger('click');
            $('select').select2();
            wrongForm();
        })
    });

    $('.tabs-rule').on('click', '.fa-times', function(event){
        event.preventDefault();
        var id_task = $(this).parents('td').attr('id-task');
        if (id_task) {
            var task = $(this).parents('tr');
            var is_archive = $(this).parents('td').children('a').eq(0).children('.fa-play')
            $.post('to_trash_task', {"id": id_task})
            .success( function (data) {
                task.fadeOut('slow', function () {
                    task.remove();
                    $('#get_tasking_arendator').children('.label').text(parseInt($('#get_tasking_arendator').children('.label').text())-1)
                    var id_arendator = $('#single_arendator_id').attr('single_arendator_id');
                    $.get('get_tasking_arendator', {"id_arendator":id_arendator}, function(data) {
                        $('.tabs-rule').fadeOut('200', function() {
                            $(this).html('');
                            $(this).html(data);
                            $(this).fadeIn('200');
                        });
                    });
                    $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
                    $('.messageServer').text('Задача удалена').fadeIn(1000).delay(2000).fadeOut(500);
                });
            })
            .error(function(data) {
                $('.messageServer').css('backgroundColor', '#c9302c');
                $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
            });
        }

    });
    $('.tabs-rule').on('click', '.fa-play', function (event) {
        event.preventDefault();
        var id_task = $(this).parents('td').attr('id-task');
        if (id_task) {
            var task = $(this).parents('tr');
            $.post('to_archive_task', {"id": id_task})
            .success( function (data) {
                task.fadeOut('slow', function () {
                    task.remove();
                    var id_arendator = $('#single_arendator_id').attr('single_arendator_id');
                    $.get('get_tasks_archive', {"id_arendator": id_arendator}, function(data) {
                    $('.tabs-rule').fadeOut('200', function() {
                        $(this).html('');
                        $(this).html(data);
                        $(this).fadeIn('200');
                    });
                });
                });
            })
            .error(function(data) {});
        }
    });
    $('.tabs-rule').on('click', '.tsk', function(event){
        event.preventDefault();
        var id_task = $(this).parents('td').attr('id-task');
        $.post('edit_form_task', {"id": id_task})
        .success( function (data) {
            $('#add_form_t').html(data);
            $('.task-form').animate({top: '10%'}, 1000);
            // $('#add_form_t').children('.task-form').fadeIn('slow');
            $('#add_form_t').trigger('click');
            $('select').select2();
        })
        .error(function(data) {});
    })

    //  END  Block TASK
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

    // START BLOCK DELIVERY
    $(document).on('click', '#delivery_email_arendator_single', function(event) {
        event.preventDefault();
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').text('Идет рассылка').fadeIn(1000);
        data = {
            'plus_email': $('#plus_email').val(),
            'id_obj': $("input:checkbox:checked").map(function() {return this.value;}).get().join(),
            'id_a': $('#single_arendator_id').attr('single_arendator_id'),
        }
        $.post('delivery_email_arendator_single', data)
        .success( function (data) {
            $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
            // $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text('Отправлено'+data+'Email').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    }); 
    
    $(document).on('click', '#delivery_sms_arendator_single', function(event) {
        event.preventDefault();
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').text('Идет рассылка').fadeIn(1000);
        data = {
            'plus_phone': $('#plus_phone').val(),
            'id_obj': $("input:checkbox:checked").map(function() {return this.value;}).get().join(),
            'id_a': $('#single_arendator_id').attr('single_arendator_id'),
        }
        $.post('delivery_sms_arendator_single', data)
        .success( function (data) {
            $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
            // $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text('Отправлено '+data+' SMS').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text(data.responseText).fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
    // END BLOCK DELIVERY 
});