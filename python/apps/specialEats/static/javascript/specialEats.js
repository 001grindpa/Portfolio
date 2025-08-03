document.addEventListener('DOMContentLoaded', function(){
	let buggerContainer = document.querySelector('.menucheck')
	let hambugger = document.querySelector('#menuCheck');
	let body = document.querySelector('body');
	let main = document.querySelector('main');

	main.addEventListener('click', function(){
		hambugger.checked = false;
	})	
})
