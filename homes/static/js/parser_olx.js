/**
 * Created by varunok on 14.08.16.
 */
$(document).ready(function() {
    $('#parse').on('click', function (event) {
        event.preventDefault();
        var msg   = $('#parse_form').serializeArray();
        // var msg   = $('#parse_form').serialize();
        for (var item in msg)
        {
          if (msg[item].name == 'id_page') {
            msg[item].value = '1';
          }
        }
        $('#include_parse_text').html('');
        $('#more_icon').html('');
        $('#wait_icon').html('<i class="fa fa-spinner fa-pulse fa-4x fa-fw"></i>');
        $.post('parse', msg)
        .success( function (data) {
            var data = jQuery.parseJSON(data);
            $('#include_parse_text').html('');
            $('#wait_icon').html('');
            for(var i in data){
                // $('#include_parse_text').append("<div></div><a href='"+data[i].sity+"'>"+data[i].sity+"</a></div>");
                if (i != 'id_page'){
                    $('#include_parse_text').append("<tr><td>"+data[i].sity+"</td><td>"+data[i].title+"</td><td>"+data[i].phone+"</td><td><a class='btn btn-darkblue' target='_blank' href='"+data[i].link+"'>Перейти</a></td><td><a class='btn btn-green done' href='#'>Отработано</a></td></tr>");
                }
            }
            $('#more_icon').html('<a href="#" class="btn btn-green"><i class="fa fa-plus fa-4x fa-fw"></i></a>');
            $('#numb_page').val(data.id_page);
        })
        .error(function(data) {
            $('#wait_icon').html('ERROR');
        });
    });
    $('.row').on('click', '#more_icon', function (event) {
        event.preventDefault();
        var msg   = $('#parse_form').serialize();
        $('#more_icon').html('');
        $('#wait_icon').html('<i class="fa fa-spinner fa-pulse fa-4x fa-fw"></i>');
        $.post('parse', msg)
        .success( function (data) {
            var data = jQuery.parseJSON(data);
            $('#wait_icon').html('');
            for(var i in data){
                // $('#include_parse_text').append("<div></div><a href='"+data[i].sity+"'>"+data[i].sity+"</a></div>");
                if (i != 'id_page'){
                    $('#include_parse_text').append("<tr><td>"+data[i].sity+"</td><td>"+data[i].title+"</td><td>"+data[i].phone+"</td><td><a class='btn btn-darkblue' target='_blank' href='"+data[i].link+"'>Перейти</a></td><td><a class='btn btn-green done' href='#'>Отработано</a></td></tr>");
                }
            }
            $('#more_icon').html('<a href="#" class="btn btn-green"><i class="fa fa-plus fa-4x fa-fw"></i></a>');
            $('#numb_page').val(data.id_page);
        })
        .error(function(data) {
            $('#wait_icon').html('ERROR');
        });
    });
//    START CONFIG
    $('#sity_conf_btn').on('click', function () {
       var sity_conf = $('#sity_conf').val();
        $.post('sity_conf', {'sity_conf': sity_conf})
        .success( function (data) {
            $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text('Сохранено').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
    
    $('#SITE_URL_btn').on('click', function () {
       var SITE_URL = $('#SITE_URL').val();
        $.post('site_url', {'SITE_URL': SITE_URL})
        .success( function (data) {
            $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text('Сохранено').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
    
    $('#AJAX_PHONE_btn').on('click', function () {
       var AJAX_PHONE = $('#AJAX_PHONE').val();
        $.post('ajax_phone', {'AJAX_PHONE': AJAX_PHONE})
        .success( function (data) {
            $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text('Сохранено').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
    
    $('#SELECTOR_GETLINK_CATEGORIES_btn').on('click', function () {
       var SELECTOR_GETLINK_CATEGORIES = $('#SELECTOR_GETLINK_CATEGORIES').val();
        $.post('selector_getlink_categories', {'SELECTOR_GETLINK_CATEGORIES': SELECTOR_GETLINK_CATEGORIES})
        .success( function (data) {
            $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text('Сохранено').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
    
    $('#SELECTOR_GETTEXT_CATEGORIES_btn').on('click', function () {
       var SELECTOR_GETTEXT_CATEGORIES = $('#SELECTOR_GETTEXT_CATEGORIES').val();
        $.post('selector_gettext_categories', {'SELECTOR_GETTEXT_CATEGORIES': SELECTOR_GETTEXT_CATEGORIES})
        .success( function (data) {
            $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text('Сохранено').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
    
    $('#SELECTOR_GETLINK_ARTICLES_btn').on('click', function () {
       var SELECTOR_GETLINK_ARTICLES = $('#SELECTOR_GETLINK_ARTICLES').val();
        $.post('selector_getlink_articles', {'SELECTOR_GETLINK_ARTICLES': SELECTOR_GETLINK_ARTICLES})
        .success( function (data) {
            $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text('Сохранено').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
    
    $('#SELECTOR_SITY_btn').on('click', function () {
       var SELECTOR_SITY = $('#SELECTOR_SITY').val();
        $.post('selector_sity', {'SELECTOR_SITY': SELECTOR_SITY})
        .success( function (data) {
            $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text('Сохранено').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
    
    $('#SELECTOR_TITLE_btn').on('click', function () {
       var SELECTOR_TITLE = $('#SELECTOR_TITLE').val();
        $.post('selector_title', {'SELECTOR_TITLE': SELECTOR_TITLE})
        .success( function (data) {
            $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text('Сохранено').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
    
    $('#SELECTOR_DATE_btn').on('click', function () {
       var SELECTOR_DATE = $('#SELECTOR_DATE').val();
        $.post('selector_date', {'SELECTOR_DATE': SELECTOR_DATE})
        .success( function (data) {
            $('.messageServer').css('backgroundColor', '#5bc0de');
            $('.messageServer').text('Сохранено').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    });
//    END CONFIG
    $(document).on('click', '.done', function(event) {
        event.preventDefault();
        $(this).parents('tr').addClass('success')
    });
});