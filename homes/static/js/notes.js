$(document).ready(function() {
    var $grid = $('.grid').masonry({
                  initLayout: true,
                });
    $('#test-popup').on('click', '.btn-green', function(event) {
        event.preventDefault();
        var note_value = $('#test-popup').children().eq(1).children('textarea').val();
        $.get('note_add',{'notes':note_value}, function(data) {
            var data = jQuery.parseJSON(data);
            if (data.response) {
                var elements = '<div id="note-'+data.id+'" class="col-md-6 grid-item"><div class="panel panel-default"><div class="panel-heading"><h3 class="panel-title">'+data.name+'</h3><div class="panel-edit"><a class="note_edit" href="#"><i class="fa fa-pencil"></i></a><a class="note_del note-'+data.id+'" href="#"><i class="fa fa-times"></i></a></div></div><div class="panel-body">'+ note_value +'</div><div class="date"><i class="fa fa-clock-o"></i>'+data.date+'</div></div></div>';
                var $elements = $(elements)
                $grid.prepend( $elements ).masonry( 'prepended', $elements );
            }
            $.magnificPopup.close();
        });
    });
    $('.grid').on('click', '.note_del', function(event) {
        event.preventDefault();
        var id_note = $(this).attr('class');
        $.get('note_del', {'del': id_note}, function(data) {
            var data = jQuery.parseJSON(data);
            if (data.status) {
                var id_note = 'note-'+ data.id;
                var id_note = $('#'+id_note);
                $grid.masonry('remove',id_note).masonry('layout');
            }
        });
    });
    $('.grid').on('click', '.note_edit', function(event) {
        event.preventDefault();
        var text = $(this).parents('.panel').children('.panel-body').text();
        $(this).parents('.panel').children('.panel-body').html('<textarea class="text_edit"></textarea><a href="#" class="btn btn-green gedit">OK</a>')
        $(this).parents('.panel').children('.panel-body').children('textarea').val($.trim(text));
        $grid.masonry('reloadItems').masonry('layout');



    });
    $('.grid').on('click', '.gedit', function(event) {
            event.preventDefault();
            var note_edit = $(this).parents('.grid-item').attr('id');
            var text_edit = $(this).prev('textarea').val();
            // $(this).parents('.panel-body').html('');
            var th = $(this).parents('.panel-body');
            // $(this).parents('.panel-body').text(text_edit);
            $grid.masonry('reloadItems').masonry('layout');
            $.get('note_edit', {'edit': note_edit, 'text': text_edit}, function(data) {
                var data = jQuery.parseJSON(data);
                th.text(text_edit);
                th.prev('.panel-heading').children('.panel-title').text(data.name)
                // console.log(th.next('.date'))
                th.next('.date').html('<i class="fa fa-clock-o"></i>'+data.date)
            });
        });
})