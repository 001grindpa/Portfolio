document.addEventListener('DOMContentLoaded', function(){
	let buggerContainer = document.querySelector('.menucheck')
	let hambugger = document.querySelector('#menuCheck');
	let body = document.querySelector('body');

	hambugger.addEventListener('change', function(){
		if (hambugger.checked) {
			body.style.overflow = 'hidden';
		}
		else {
			body.style.overflow = 'auto';
		}
	})	
})
