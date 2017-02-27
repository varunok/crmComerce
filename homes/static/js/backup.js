$(document).ready(function() {

    $('#object_xls').on('click', function(event) {
        event.preventDefault();
        
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').html('<div><i class="fa fa-spinner fa-pulse fa-1x fa-fw"></i>Создание</div').fadeIn(500).delay(2000);
        $.post('create_object_xls')
        .success( function (data) {
            window.location.href = data;
            $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
            $('.messageServer').text('Создано').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        });
    });

    $(document).on('click', '#backup_global', function(event) {
        event.preventDefault();
        var _this = $(this)
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').html('<div><i class="fa fa-spinner fa-pulse fa-1x fa-fw"></i>Создание</div').fadeIn(500).delay(2000);
        $.post('get_backup_global')
        .success( function (data) {
            $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
            $('.messageServer').text('Создано').fadeIn(1000).delay(2000).fadeOut(500);
            _this.parent().removeClass('col-md-6');
            _this.parent().addClass('col-md-5');
            $('#backup_global_link').parent().fadeIn('slow');
            $('#backup_global_link').attr('download', data);
            // window.location.href = data;
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        });
    });

    $(document).on('click', '#backup_dropbox', function(event) {
        event.preventDefault();
        var _this = $(this)
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').html('<div><i class="fa fa-spinner fa-pulse fa-1x fa-fw"></i>Создание</div').fadeIn(500).delay(2000);
        $.post('backup_dropbox')
        .success( function (data) {
            $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
            $('.messageServer').text('Создано').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        });
    });

    // $('#not_click').on('click', function(event) {
    //     event.preventDefault();
    //     /* Act on the event */
    // });

    var files;
        $('input[type=file]').change(function(){
            files = this.files;
            var data = new FormData();
            $.each( files, function( key, value ){
                data.append( key, value );
            });
            $.ajax({
                url: 'restore_file_save',
                type: 'POST',
                data: data,
                cache: false,
                // dataType: 'json',
                processData: false,
                contentType: false,
            })
            .done( function (data) {
                $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
                $('.messageServer').text('Файл загружен').fadeIn(1000).delay(2000).fadeOut(500);
            })
            .fail(function(data) {
                $('.messageServer').css('backgroundColor', '#c9302c');
                $('.messageServer').text('Ошибка. Неверний формат файла.').fadeIn(1000).delay(2000).fadeOut(500);
            });
        });
        
    $(document).on('click', '#restore_databases', function(event) {
        event.preventDefault();
        var _this = $(this)
        $('.messageServer').css('backgroundColor', '#FCCD1B');
        $('.messageServer').html('<div><i class="fa fa-spinner fa-pulse fa-1x fa-fw"></i>Востановление</div').fadeIn(500).delay(2000);
        $.post('restore_databases')
        .success( function (data) {
            $('.messageServer').animate({backgroundColor: '#5bc0de'}, 1000);
            $('.messageServer').text('Востановлено').fadeIn(1000).delay(2000).fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').css('backgroundColor', '#c9302c');
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        });
    });
})
