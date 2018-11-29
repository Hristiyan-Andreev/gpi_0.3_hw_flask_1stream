src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"

$(document).ready(function() {
	$('form').submit(function (event) {
		var form_id = $(this).attr('id')
		var url = $(this).attr('action')
		event.preventDefault(); 		// block the traditional submission of the form.
		console.log($('form').serialize())
		$.ajax({
			type: "POST",
			url: url,
			data: $('form').serialize(), // serializes the form's elements.
			success: function (data) {
				console.log(data)  // display the returned data in the console.
			}
		});
	});
	// Inject CSRF_TOKEN as a header in the AJAX request
	var csrf_token = "{{ csrf_token() }}";
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrf_token);
			}
		}
	});	
});