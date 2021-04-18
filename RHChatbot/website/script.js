
function criaBot (){

$(document).ready(function () {

	//Widget Code
	var bot = '<div class="chatCont" id="chatCont">' +
		'<div class="bot_profile">' +
		'<img src="chat.gif" class="img-circle img-profile">' +
		'<div class="profile_div2">' +
		'<div class="row">' +
		'<div class="col-hgt col-sm-offset-2">' +
		'</div><!--col-hgt end-->' +
		'<div class="col-hgt">' +
		'<div class="chat-txt">' +
		'' +
		'</div>' +
		'</div><!--col-hgt end-->' +
		'</div><!--row end-->' +
		'</div>' +
		'</div><!--bot_profile end-->' +
		'<div id="result_div" class="resultDiv" style="background-image: url(logo.png); background-position: center;  background-size:cover";></div>' +
		'<div class="chatForm" id="chat-div">' +
		'<div class="spinner">' +
		'<div class="bounce1"></div>' +
		'<div class="bounce2"></div>' +
		'<div class="bounce3"></div>' +
		'</div>' +
		'<input type="text" id="chat-input" autocomplete="off" placeholder="Digite aqui"' + 'class="form-control bot-txt"/>' +
		'</div>' +
		'</div><!--chatCont end-->' +

		'<div class="profile_div">' +
		'<div class="row">' +
		'<div class="col-hgt col-sm-offset-2">' +
		'<img src="chat.gif" class="img-circle img-profile">' +
		'</div><!--col-hgt end-->' +
		'<div class="col-hgt">' +
		'<div class="chat-txt">' +
		'' +
		'</div>' +
		'</div><!--col-hgt end-->' +
		'</div><!--row end-->' +
		'</div><!--profile_div end-->';

	$("mybot").html(bot);

	var fistClick = false;
	// ------------------------------------------ Toggle chatbot -----------------------------------------------
	$('.profile_div').click(function () {
		
		$('.profile_div').toggle();
		//$('.profile_div').attr('class', 'profile_div2')
		$('.chatCont').toggle();
		$('.bot_profile').toggle();
		$('.chatForm').toggle();
		document.getElementById('chat-input').focus();
		if (!fistClick){
			setBotResponse([{recipient_id: $( "#usuarios option:selected" /*"default"*/ ).val(), text: "Olá " + $("#usuarios option:selected" ).text().split(" ")[0] + "! Em que posso lhe ajudar?"}]);
			fistClick = true;
		}

	});

	$('.profile_div2').click(function () {
		$('.profile_div').toggle();
		$('.chatCont').toggle();
		$('.bot_profile').toggle();
		$('.chatForm').toggle();
	});

	// on input/text enter--------------------------------------------------------------------------------------
	$('#chat-input').on('keyup keypress', function (e) {
		var keyCode = e.keyCode || e.which;
		var text = $("#chat-input").val();
		if (keyCode === 13) {
			if (text == "" || $.trim(text) == '') {
				e.preventDefault();
				return false;
			} else {
				$("#chat-input").blur();
				setUserResponse(text);
				send(text);
				e.preventDefault();
				return false;
			}
		}
	});

	//------------------------------------- Set user response in result_div ------------------------------------
	function setUserResponse(val) {
		var UserResponse = '<p class="userEnteredText">' + val + '</p><div class="clearfix"></div>';
		$(UserResponse).appendTo('#result_div');
		$("#chat-input").val('');
		scrollToBottomOfResults();
		showSpinner();
		$('.suggestion').remove();
	}
});
};

function setSlot(text, slotName) {
	$.ajax({
		url: 'http://localhost:5005/conversations/' + /*$( "#usuarios option:selected" ).val()*/ 'default' + '/tracker/events?include_events=NONE', //  RASA API
		type: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		data: JSON.stringify({
			"event": "slot",
			"name": slotName,
			"value": text,
			"timestamp": 0
		}),
		success: function (data, textStatus, xhr) {
			console.log(data);

		},
		error: function (xhr, textStatus, errorThrown) {
			console.log('Error in Operation');
		}
	});
}

function selecionaUsuario(){
	$(document.body).append('<mybot></mybot>');
	$('#usuarios').attr("disabled", true); 
	criaBot();
	setSlot($("#usuarios option:selected" ).text(), "colaborador");
	setSlot($( "#usuarios option:selected" ).val(), "id_colaborador");
  }

  function carregarUsuarios() {
	$.ajax({
	  url: 'http://localhost:5000/colaboradores',
	  type: 'OPTIONS',
	  headers: {
		'Content-Type': 'application/json',
	  },
	  success: function (data, textStatus, xhr) {
		console.log(data);
		for (a in data){
		  $('#usuarios').append($('<option>', {
			value: data[a].ID,
			text: data[a].Nome + ' - ' + data[a].Cargo
		  }));
		  console.log(data[a].Nome);
		}

	  },
	  error: function (xhr, textStatus, errorThrown) {
		console.log('Error in Operation');
	  }
	});
  }

	//------------------------------------------- Call the RASA API--------------------------------------
	function send(text) {
		$.ajax({
			url: 'http://localhost:5005/webhooks/rest/webhook', //  RASA API
			type: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			data: JSON.stringify({
				"message": text,
				"sender": $( "#usuarios option:selected" ).val()
				//"sender": "default"
			}),
			success: function (data, textStatus, xhr) {
				console.log(data);
				setBotResponse(data);

			},
			error: function (xhr, textStatus, errorThrown) {
				console.log('Error in Operation');
				setBotResponse('error');
			}
		});
	}

	//---------------------------------- Scroll to the bottom of the results div -------------------------------
	function scrollToBottomOfResults() {
		var terminalResultsDiv = document.getElementById('result_div');
		terminalResultsDiv.scrollTop = terminalResultsDiv.scrollHeight;
	}


	//---------------------------------------- Spinner ---------------------------------------------------
	function showSpinner() {
		$('.spinner').show();
	}

	function hideSpinner() {
		$('.spinner').hide();
	}

	//------------------------------------ Set bot response in result_div -------------------------------------
	function setBotResponse(val) {
		setTimeout(function () {

			if ($.trim(val) == '' || val == 'error') { //if there is no response from bot or there is some error
				val = 'Desculpe, não consegui entender sua consulta. Vamos tentar outra coisa!'
				var BotResponse = '<p class="botResult">' + val + '</p><div class="clearfix"></div>';
				$(BotResponse).appendTo('#result_div');
			} else {

				//if we get message from the bot succesfully
				var msg = "";
				for (var i = 0; i < val.length; i++) {
					msg += '<p class="botResult">' + val[i].text + '</p><div class="clearfix"></div>';
				}
				BotResponse = msg;
				$(BotResponse).appendTo('#result_div');
				
				msg = "";
				if (val[0].buttons){
					for (var i = 0; i < val[0].buttons.length; i++) {
						msg += '<button type="button" class="botResult" onclick="send(' + "'" +val[0].buttons[i].payload + "'" + ')">' + val[0].buttons[i].title + '</button>'
					}

					BotResponse = msg;
					$(BotResponse).appendTo('#result_div');
				}
			}
			scrollToBottomOfResults();
			hideSpinner();
		}, 500);
	}