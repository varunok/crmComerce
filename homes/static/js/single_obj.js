/**
 * Created by varunok on 28.07.16.
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
    // "use strict";

    // START BLOCK ARENDATOR
    $(document).on('click', '#add_arendator_id', function (event) {
        event.preventDefault();
        var id_a = $('#id_arendator').val();
        $.get('add_arendator_to_tie/'+id_a, {'id': $('#sisingle_obj_id').attr('sisingle_obj_id')}).success( function (data) {
            $('#add_tr').prepend(data);
            $('.show_tr').fadeIn('slow');
            var plus_count = parseInt($('#get_arendator').children('span').text())+1;
            $('#get_arendator').children('span').text(plus_count);
        });
    });
    $(document).on('change', '.id_shows', function (event) {
        var _this = $(this).parents('.color');
        var id_a = $(this).attr('id-arendator-sin');
        var id_o = $('#sisingle_obj_id').attr('sisingle_obj_id');
        var id_show = $(this).val();
        $.get('change_shows/a-'+id_a+'='+'o-'+id_o+'='+'s-'+id_show)
        .success( function (data) {
            _this.removeClass().addClass(table_color(id_show)+' color');
            $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text(data).fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text(data.responseText).fadeIn(1000).delay(2000).fadeOut(500);
        });
    });
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
        // var price_automat = $("#price_automat").prop("checked");
        // var area_automat = $("#area_automat").prop("checked");
        // var rooms_automat = $("#rooms_automat").prop("checked");
        // var repairs_automat = $("#repairs_automat").prop("checked");
        // var type_obj_automat = $("#type_obj_automat").prop("checked");
        // var district_automat = $("#district_automat").prop("checked");
        // var data = {
        //     "price_automat": price_automat,
        //     "area_automat": area_automat,
        //     "rooms_automat": rooms_automat,
        //     "repairs_automat": repairs_automat,
        //     "type_obj_automat": type_obj_automat,
        //     "district_automat": district_automat,
        //     "id_so": $('#sisingle_obj_id').attr('sisingle_obj_id'),
        //     "type_operations": "arendator"
        // };
        var data = $('#avtomat_form').serialize();
        $.get('automat_tie', data).success( function (data) {
            $('#add_tr').html(' ');
            $('#add_tr').fadeIn('slow');
            $('#add_tr').prepend(data);
            $('.show_tr').fadeIn('slow');
            var count_ar = parseInt($('#add_tr').children('.show_tr').length);
            $('#get_arendator').children('span').text(count_ar);
        });
    });
    $(document).on('click', '.delete_arendator_tr', function (event) {
        event.preventDefault();
        var del_obj = $(this).parents('.show_tr');
        var dai = $(this).attr('del-arendator-id');
        $.post('delete_tie_arendator/'+dai, {'id': $('#sisingle_obj_id').attr('sisingle_obj_id')})
            .success( function (data) {
                del_obj.fadeOut('slow', function () {
                    $('#add_tr').children('#show_tr-'+dai).remove();
                    var plus_count = parseInt($('#get_arendator').children('span').text())-1;
                    $('#get_arendator').children('span').text(plus_count);
                });

            });
    });
    
    $(document).on('click', '#clear_all_arendator', function (event) {
        event.preventDefault();
        $.post('clear_all_arendator', {'id': $('#sisingle_obj_id').attr('sisingle_obj_id')})
            .success( function (data) {
                $('#add_tr').fadeOut('slow', function () {
                    $('#add_tr').html(' ');
                    $('#add_tr').fadeIn('slow');
                    $('#get_arendator').children('span').text('0');
                })
            });
    });
    $(document).on('click', '#delivery_email_arendator', function(event) {
        event.preventDefault();
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').text('Идет рассылка').fadeIn(1000);
        data = {
            'plus_email': $('#plus_email').val(),
            'id_a': $("input:checkbox:checked").map(function() {return this.value;}).get().join(),
            'id_so': $('#sisingle_obj_id').attr('sisingle_obj_id'),
        }
        $.post('delivery_email_arendator', data)
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

    $(document).on('click', '#delivery_sms_arendator', function(event) {
        event.preventDefault();
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').text('Идет рассылка').fadeIn(1000);
        data = {
            'plus_phone': $('#plus_phone').val(),
            'id_a': $("input:checkbox:checked").map(function() {return this.value;}).get().join(),
            'id_so': $('#sisingle_obj_id').attr('sisingle_obj_id'),
        }
        $.post('delivery_sms_arendator', data)
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

    // END BLOCK ARENDATOR

//    BLOCK BUYER
    $(document).on('click', '#add_buyer_id', function (event) {
        event.preventDefault();
        var id_a = $('#id_buyer').val();
        $.get('add_buyer_to_tie/'+id_a, {'id': $('#sisingle_obj_id').attr('sisingle_obj_id')}).success( function (data) {
            $('#add_tr').prepend(data);
            $('.show_tr').fadeIn('slow');
            var plus_count = parseInt($('#get_buyer').children('span').text())+1;
            $('#get_buyer').children('span').text(plus_count);
        });
    });
    $(document).on('change', '.id_shows_buyer', function (event) {
        var _this = $(this).parents('.color');
        var id_a = $(this).attr('id-buyer-sin');
        var id_o = $('#sisingle_obj_id').attr('sisingle_obj_id');
        var id_show = $(this).val();
        $.get('change_shows_buyer/a-'+id_a+'='+'o-'+id_o+'='+'s-'+id_show)
        .success( function (data) {
            _this.removeClass().addClass(table_color(id_show)+' color');
            $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text(data).fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text(data.responseText).fadeIn(1000).delay(2000).fadeOut(500);
        });
    });
    $(document).on('click', '#avtomat_add_buyer', function (event) {
        event.preventDefault();
        $('#modal_avto').fadeIn('slow');
    });
    $(document).on('click', '#cencel_automat_btn', function (event) {
        event.preventDefault();
        $('#modal_avto').fadeOut('slow');
    });
    $(document).on('click', '#ok_automat_btn_buyer', function (event) {
        event.preventDefault();
        $('#modal_avto').fadeOut('slow');
        var price_automat = $("#price_automat").prop("checked");
        var area_automat = $("#area_automat").prop("checked");
        var rooms_automat = $("#rooms_automat").prop("checked");
        var repairs_automat = $("#repairs_automat").prop("checked");
        var type_obj_automat = $("#type_obj_automat").prop("checked");
        var district_automat = $("#district_automat").prop("checked");
        var data = {
            "price_automat": price_automat,
            "area_automat": area_automat,
            "rooms_automat": rooms_automat,
            "repairs_automat": repairs_automat,
            "type_obj_automat": type_obj_automat,
            "district_automat": district_automat,
            "id_so": $('#sisingle_obj_id').attr('sisingle_obj_id')
        };
        $.get('automat_tie_buyer', data).success( function (data) {
            $('#add_tr').html(' ');
            $('#add_tr').fadeIn('slow');
            $('#add_tr').prepend(data);
            $('.show_tr').fadeIn('slow');
            var count_ar = parseInt($('#add_tr').children('.show_tr').length);
            $('#get_buyer').children('span').text(count_ar);
            console.log(count_ar)
        });
    });
    $(document).on('click', '.delete_buyer_tr', function (event) {
        event.preventDefault();
        var del_obj = $(this).parents('.show_tr');
        var dai = $(this).attr('del-buyer-id');
        $.post('delete_tie_buyer/'+dai, {'id': $('#sisingle_obj_id').attr('sisingle_obj_id')})
            .success( function (data) {
                del_obj.fadeOut('slow', function () {
                    $('#add_tr').children('#show_tr-'+dai).remove();
                    var plus_count = parseInt($('#get_buyer').children('span').text())-1;
                    $('#get_buyer').children('span').text(plus_count);
                });

            });
    });

    $(document).on('click', '#clear_all_buyer', function (event) {
        event.preventDefault();
        $.post('clear_all_buyer', {'id': $('#sisingle_obj_id').attr('sisingle_obj_id')})
            .success( function (data) {
                $('#add_tr').fadeOut('slow', function () {
                    $('#add_tr').html(' ');
                    $('#add_tr').fadeIn('slow');
                    $('#get_buyer').children('span').text('0');
                })
            });
    });
    $(document).on('click', '#delivery_email_buyer', function(event) {
        event.preventDefault();
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').text('Идет рассылка').fadeIn(1000);
        data = {
            'plus_email': $('#plus_email').val(),
            'id_b': $("input:checkbox:checked").map(function() {return this.value;}).get().join(),
            'id_so': $('#sisingle_obj_id').attr('sisingle_obj_id'),
        }
        $.post('delivery_email_buyer', data)
        .success( function (data) {
            $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
            // $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text('Отправлено '+data+' Email').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    });

    $(document).on('click', '#delivery_sms_buyer', function(event) {
        event.preventDefault();
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').text('Идет рассылка').fadeIn(1000);
        data = {
            'plus_phone': $('#plus_phone').val(),
            'id_b': $("input:checkbox:checked").map(function() {return this.value;}).get().join(),
            'id_so': $('#sisingle_obj_id').attr('sisingle_obj_id'),
        }
        $.post('delivery_sms_buyer', data)
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

    // END BLOCK BUYER
    
    //  START  Block TASK
    $('.tabs-rule').on('click', '#add_task_form', function (event) {
        event.preventDefault();
        data = {
            'id_so': $('#sisingle_obj_id').attr('sisingle_obj_id')
        };
        $.get('get_form_task', data).success( function (data) {
            $('#add_form_t').html(data);
            $('.task-form').animate({top: '10%'}, 1000);
            $('#add_form_t').children('.task-form').fadeIn('slow');
            $('#add_form_t').trigger('click');
            $('select').select2();
            var $so = $("#id_task_facility").select2();
            var id_facility = $('#sisingle_obj_id').attr('sisingle_obj_id');    
            $so.val(id_facility).trigger("change");
            // $("#id_task_facility").prop("disabled", true);
        });
    });

    $('.tabs-rule').on('click','#cancel_add_form', function (event) {
        event.preventDefault();
        $('.task-form').hide('scale');
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
                    $('#get_tasks').children('.label').text(parseInt($('#get_tasks').children('.label').text())+1)
                }
                var id_so = $('#sisingle_obj_id').attr('sisingle_obj_id');
                $.get('get_tasks_active', {"id_so": id_so}, function(data) {
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
                    $('#get_tasks').children('.label').text(parseInt($('#get_tasks').children('.label').text())-1)
                    var id_so = $('#sisingle_obj_id').attr('sisingle_obj_id');
                    $.get('get_tasks', {"id_so":id_so}, function(data) {
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
                    var is_so = $('#sisingle_obj_id').attr('sisingle_obj_id');
                    $.get('get_tasks_archive', {"id_so": is_so}, function(data) {
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




    // START BLOCK MEET
    $('.tabs-rule').on('click', '#add_task_form_meet', function (event) {
        event.preventDefault();
        data = {
            'id_so': $('#sisingle_obj_id').attr('sisingle_obj_id')
        };
        $.get('get_form_meet', data).success( function (data) {
            $('#add_form_m').html(data);
            $('.task-form').animate({top: '10%'}, 1000);
            $('#add_form_m').children('.task-form').fadeIn('slow');
            $('#add_form_m').trigger('click');
            $('select').select2();
            var $so = $("#id_meet_facility").select2();
            var id_facility = $('#sisingle_obj_id').attr('sisingle_obj_id');    
            $so.val(id_facility).trigger("change");
            // $("#id_meet_facility").prop("disabled", true);
            
        });
    });
    $('.tabs-rule').on('click','#cancel_add_form', function (event) {
        event.preventDefault();
        $('.task-form').hide('scale');
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
                    $('#get_meetings').children('.label').text(parseInt($('#get_meetings').children('.label').text())+1)
                }
                var id_so = $('#sisingle_obj_id').attr('sisingle_obj_id');
                $.get('get_meetings_active', {"id_so": id_so}, function(data) {
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
                    $('#get_meetings').children('.label').text(parseInt($('#get_meetings').children('.label').text())-1)
                    var id_so = $('#sisingle_obj_id').attr('sisingle_obj_id');
                    $.get('get_meetings', {"id_so":id_so}, function(data) {
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
                    var is_so = $('#sisingle_obj_id').attr('sisingle_obj_id');
                    $.get('get_meetings_archive', {"id_so": is_so}, function(data) {
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




    // START BLOCK POSTING
    $('.tabs-rule').on('click', '#post_obj', function (event) {
        event.preventDefault();
        var obj_status = $(this);
        var status = $(this).attr('status');
        var sisingle_obj_id = $('#sisingle_obj_id').attr('sisingle_obj_id');
        $.post('post/'+status, {'id_so': sisingle_obj_id})
            .success( function (data) {
                var data = jQuery.parseJSON(data)
                if (data.data === 'true') {
                    obj_status.attr('status', 'true');
                    obj_status.text('Снять с публикации');
                    obj_status.removeClass('sl-green');
                    obj_status.addClass('sl-grey');
                    $('.info_status').text('Публикуется')
                }
                else{
                    obj_status.attr('status', 'false');
                    obj_status.text('Опубликовать');
                    obj_status.removeClass('sl-grey');
                    obj_status.addClass('sl-green');
                    $('.info_status').text('Не публикуется')
                }
            })
            .error(function (data) {
                $('.info_status').text('Ошибка.')
                $('.info_status').css('background-color', 'red');
            })
    });
    // END BLOCK POSTING
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

    function table_color(arg){
        if(arg === '1'){return 'info'}
        else if(arg === '2'){return 'warning'}
        else if(arg === '3'){return 'danger'}
        else if(arg === '4'){return 'success'}
        else {return ' '}
    }

});
