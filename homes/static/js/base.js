 $(document).ready(function() {

 	setInterval(function () {
		get_online(get_date());
		get_messege();
    },60000);

    var get_date = function(){
 		var date = new Date();
		var day = date.getDate();
		var month = date.getMonth();
		var year = date.getFullYear();
		var hours = date.getHours();
		var minutes = date.getMinutes();
		var seconds = date.getSeconds();
		var dates = year + '-' + (month+1) + '-' + day + ' ' + hours + ':' + minutes + ':' + seconds;
		return dates;
    };

 	var get_online = function(dates) {$.get('who_online',{"date": dates}, function(data) {
 	 			var data = jQuery.parseJSON(data);
 	 			var online = []
 	 			for (i in data) {
 	 				if (data[i].login==='online') {
 	 					online.push(data[i].login)
 	 				}

 	 			}
 	 			$('.len_online').text(online.length)
 	 		});
 	};

 	var get_messege = function (){
            $.get('get_messege', function(data) {
                var data = jQuery.parseJSON(data);
                $('.count_message').text(data.new_message)
            });
        };

    get_online(get_date());
    get_messege();

    $('#get_who_online').on('click', function(event) {
    	event.preventDefault();
    	$.get('who_online_html', function(data) {
    		$('#who_online').html('');
    		$('#who_online').append(data);
    	});
    });
    $('#show_message').on('click', function(event) {
			event.preventDefault();
			$.get('get_new_message_html', function(data) {
				$('#new_message').html('');
				$('#new_message').html(data);
			});
		});

    $('#show_activity').on('click', function(event) {
        event.preventDefault();
        var user_id = $("#user_id_activity option:selected").val();
        var dateto = $('#dateto').val();
        var datefrom = $('#datefrom').val();
        $.get('show_activity_index', {'user_id': user_id, 'dateto': dateto, 'datefrom': datefrom}, function(data) {
            var data = jQuery.parseJSON( data);
            $('#arendators').text(data.arendators);
            $('#facilitys').text(data.facilitys);
            $('#taskings').text(data.taskings);
            $('#buyers').text(data.buyers);
            $('#maklers').text(data.maklers);
            $('#meetings').text(data.meetings);
        });
    });
});
