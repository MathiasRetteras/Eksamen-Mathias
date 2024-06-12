/*kode for confetti effekten på "success" siden. denne ble limt inn så vet ikke helt hva alt betyr men skal prøve å forklare*/
/*jeg bruker jQuery funksjon her for første gang og måtte skrive det inn i html dokumentet også for at det skulle funke*/
jQuery("document").ready(function($){
	var flakes = '',
	randomColor;
	for(var i = 0, len = 400; i < len; i++) {
	randomColor = Math.floor(Math.random()*16777215).toString(16);
	/*her "spawner" jeg inn et tilfeldig antall confetti*/
	flakes += '<div class="ball" style="background: #'+randomColor;
	flakes += '; animation-duration: '+(Math.random() * 9 + 2)+'s; animation-delay: ';
	flakes += (Math.random() * 2 + 0)+'s;"></div>';
	}
	document.getElementById('confetti').innerHTML = flakes;
   });