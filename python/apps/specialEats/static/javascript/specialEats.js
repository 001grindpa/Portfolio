document.addEventListener('DOMContentLoaded', function(){
	if (document.body.id === 'landing'){
		let buggerContainer = document.querySelector('.menucheck')
		let hambugger = document.querySelector('#menuCheck');
		let body = document.querySelector('body');
		let main = document.querySelector('main');
	    let order_now = document.querySelector('#check');
	    let background = document.querySelector('.access');
	    let section = document.querySelector('#check-2');
	    let section_background = document.querySelector('#section');
	    let innerOrder = document.querySelector('.innerAccess');
	    let innerSection = document.querySelector('.sectionForm');
		let uk_flag = document.querySelector('#flag_1');
		let languages = document.querySelector('#languages');
		let uk_flag_2 = document.querySelector('#flag_2');
		let languages_2 = document.querySelector('#languages_2');
			
	    // hero section pop-up configuration
		if (main && hambugger) {
			main.addEventListener('click', function(){
				hambugger.checked = false;
			});	
		}
		
		if (background && order_now) {
			background.addEventListener('click', function(event){
		        order_now.checked = false;
		        order_now.dispatchEvent(new Event('change'));
		    });	
		}
	    
	    if (section_background && section) {
	    	section_background.addEventListener('click', function(event){
		        section.checked = false;
		        section.dispatchEvent(new Event('change'));
		    });	
	    }
	    
	    order_now.addEventListener('change', function(){
	        if (order_now.checked) {
	            body.style.overflow = 'hidden';
	        }
	        else {
	            body.style.overflow = 'auto';
	        }
	    });
	    
	    section.addEventListener('change', function(event){
	        if (section.checked) {
	            body.style.overflow = 'hidden';
	        }
	        else {
	            body.style.overflow = 'auto';
	        }
	    });
	    
	    innerOrder.addEventListener('click', function(event){
	        event.stopPropagation();
	    });
	    
	    innerSection.addEventListener('click', function(event){
	        event.stopPropagation();
	    });
	
	    // flag configuration
	
	    languages.addEventListener('change', function(event){
			if (languages.value == 'English'){
				uk_flag.src = 'static/images/uk.png';
			}
			else {
				uk_flag.src = 'static/images/ng.png';
			}
	    });
	
	    languages_2.addEventListener('change', function(event){
			if (languages_2.value == 'English'){
				uk_flag_2.src = 'static/images/uk.png';
			}
			else {
				uk_flag_2.src = 'static/images/ng.png';
			}
	    });	
	};
	else if (document.body.id === 'signup') {
		// sign up page configuration
		let view = document.querySelector('#view');
		let password = document.querySelector('#password_1');
	
	    // password config
	    view.addEventListener('click', function(event){
	        if (password.type === 'password') {
	            password.type = 'text';
	            view.src = 'static/images/hide.png';
	        }
	        else {
	            password.type = 'password';
	            view.src = 'static/images/view.png';
	        }
	    });	
	};
	
})
