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
        $.post('parsehidnua', msg)
        .success( function (data) {
            var data = jQuery.parseJSON(data);
            $('#include_parse_text').html('');
            $('#wait_icon').html('');
            for(var i in data){
                // $('#include_parse_text').append("<div></div><a href='"+data[i].sity+"'>"+data[i].sity+"</a></div>");
                if (i != 'id_page'){
                    $('#include_parse_text').append("<tr><td>"+data[i].article+"</td><td>"+data[i].phone+"</td><td><a class='btn btn-green done' href='#'>Отработано</a></td></tr>");
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
        $.post('parsehidnua', msg)
        .success( function (data) {
            var data = jQuery.parseJSON(data);
            $('#wait_icon').html('');
            for(var i in data){
                // $('#include_parse_text').append("<div></div><a href='"+data[i].sity+"'>"+data[i].sity+"</a></div>");
                if (i != 'id_page'){
                    $('#include_parse_text').append("<tr><td>"+data[i].article+"</td><td>"+data[i].phone+"</td><td><a class='btn btn-green done' href='#'>Отработано</a></td></tr>");
                }
            }
            $('#more_icon').html('<a href="#" class="btn btn-green"><i class="fa fa-plus fa-4x fa-fw"></i></a>');
            $('#numb_page').val(data.id_page);
        })
        .error(function(data) {
            $('#wait_icon').html('ERROR');
        });
    });
    $(document).on('click', '.done', function(event) {
        event.preventDefault();
        $(this).parents('tr').addClass('success')
    });
})