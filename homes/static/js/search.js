$(document).ready(function() {
    $('.fa-search').on('click keypress', function(event) {
        event.preventDefault();
        SendSearch();
    });
    $('#searching').on('keypress', function(e) {
        if(e.keyCode==13){SendSearch()}
    });

    function SendSearch(){
        var search_text = $('#searching').val();
        $('.messageServer').animate({backgroundColor: '#FCCD1B'}, 1000);
        $('.messageServer').html('<div><i class="fa fa-spinner fa-pulse fa-1x fa-fw"></i>Поиск</div').fadeIn(1000).delay(2000);
        // $('.messageServer').text('Поиск').fadeIn(1000).delay(2000).fadeOut(500);
        $.get('searching', {"search_text": search_text})
        .success( function (data) {
            $('#search_results').html(data);
            $('.messageServer').fadeOut(500);
        })
        .error(function(data) {
            $('.messageServer').animate({'backgroundColor': '#c9302c'}, 300);
            $('.messageServer').text('Ошибка').fadeIn(1000).delay(2000).fadeOut(500);
        })
    }
})