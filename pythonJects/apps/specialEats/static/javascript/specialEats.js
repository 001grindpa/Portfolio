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
	}
	else if (document.body.id === 'signup') {
		// sign up page configuration

		let view = document.querySelector('#view');
		let password = document.querySelector('#password_1');
        let generate_p = document.querySelector('#generate_p');
        let passwordFeed = document.querySelector('.passwordFeed');
		let signupForm = document.querySelector('.signupForm');
		let password_2 = document.querySelector('#password_2');
		let confirmP = document.querySelector('#confirmP');
		let checkbox = document.querySelector('#signupCheck');
		let confirm_container = document.querySelector('.submitContainer');
		let blur = document.querySelector('.submitBlur');
		let body = document.querySelector('body');
		let dob = document.querySelector('#dob');
		let nameError = document.querySelector("#nameError");
		let username = document.querySelector("#username");
		let signup = document.querySelector(".signupButton");


		//username error config
		username.addEventListener("input", async function(){
			let response = await fetch("/usernamecheck?namecheck=" + username.value)
			let data = await response.text();
			nameError.innerHTML = data;
			if (data === "username already exists") {
				signup.disabled = true;
				confirmP.innerHTML = "Please go back and use a different username";
			}
			else {
				signup.disabled = false;
				confirmP.innerHTML = "";
			}
		});

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
        // password_feed
        password.addEventListener('input', async function(){
            let response = await fetch('/signup/returned?q=' + password.value);
            let returned = await response.text();
            passwordFeed.innerHTML = returned;
        });
        // generated password
        generate_p.addEventListener('click', async function(){
            let response_2 = await fetch('/signup/generated?gen=10');
            let gen = await response_2.text();
            password.value = gen;
        });
        // password confirmation
        signupForm.addEventListener('submit', function(event){
        	if (password.value != password_2.value) {
        		event.preventDefault();
        		confirmP.innerHTML = 'Password mismatch';
        	}
        	else {
        		confirmP.innerHTML = 'Valid match';
        	}
        });
        // pop up configuration for sign up page
        checkbox.addEventListener('change', function(event){
        	if (checkbox.checked) {
        		body.style.overflow = 'hidden';
				dob.disabled = false;
        	}
        	else {
        		body.style.overflow = 'auto';
        	}
        });
        blur.addEventListener('click', function(event){
        	checkbox.checked = false;
        	checkbox.dispatchEvent(new Event('change'));
        });
        confirm_container.addEventListener('click', function(event){
        	event.stopPropagation();
        })
	}
	// login page configuration

	else if (document.body.id === 'login') {
		let view = document.querySelector("#view");
		let password = document.querySelector("#password");

		view.addEventListener("click", function(){
			if (password.type === "password"){
				password.type = "text";
				view.src = "static/images/hide.png";
			}
			else {
				password.type = "password";
				view.src = "static/images/view.png";
			}
		});
	}

	//home page configuration
	
	else if (document.body.id === 'home'){
		let hambugger = document.querySelector('#menuCheck');
		let body = document.querySelector('body');
		let main = document.querySelector('main');
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

		// hero slider configuration

		let navImg = document.querySelectorAll(".slide1");
		let heroSlider = document.querySelector(".heroSlider");
		let sliderImgWidth = heroSlider.querySelector(".sliderImg").offsetWidth;
		// offsetWidth is used to get the width of a child object relative to it's parent object in pixels
		let currentNav = null;
		let currentNavIndex = 0;
		let autoSlide;

		function autoClickForward() {
			autoSlide = setInterval(autoClickSlide, 10000);
		}

		for (let i = 0; i < navImg.length; i++){

			navImg[i].addEventListener("click", function(event){
				event.stopPropagation();
				for (let c of navImg){
					c.classList.remove("choosen");
				}
				currentNav = event.target;
				currentNav.classList.add("choosen");
				currentNavIndex = i;
				clearInterval(autoSlide); //this block terminates auto scrolling when manually clicked
				autoClickForward();// this block restarts auto scrolling
				
				let targetScrollPosition = currentNavIndex * sliderImgWidth;
				// when the offsetWidth is multiplied by the currentImgNav (also currentNavIndex)
				// it gives the offset width of the currentSliderImg
				//when scrollTo method is used on the slider itself, "left" allows it to scroll exactly
				// to the offset width (in pixel) from x(0) to x(targetScrollPosition)
				// we know that "targetScrollPosition" increases or reduces based on the current img index
				heroSlider.scrollTo({
					left: targetScrollPosition,
					// behavior: "smooth"
					// the above property comented out was already added with css scroll-snap behaviour
				});
			});
		}

		function autoClickSlide() {
			currentNavIndex = (currentNavIndex + 1) % navImg.length;
			// since currentNavIndex was declared globally, we can call it here and
			// use a modulus loop to increment it's value by 1 for the next sliderImg
			navImg[currentNavIndex].click();
			// auto-click on the corresponding img with the new index from the array of images (navImg)
		}

		autoClickSlide();

		// move to top button config
		let toTopBtn = document.querySelector(".toTop");
		let motionAd = document.querySelector(".motionAd");

		// the algorithm below detects and adds a class to a DOM (html element) object when it comes into view
		// --> else it remove the class
		let observer = new IntersectionObserver((entries) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					entry.target.classList.add("move");
				}
				else {
					entry.target.classList.remove("move");
				}
			});
		});

		observer.observe(toTopBtn);
		
		// for motion ad class
		let observer2 = new IntersectionObserver((entries) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					entry.target.classList.add("move2");
				}
				else {
					entry.target.classList.remove("move2");
				}
			});
		});

		observer2.observe(motionAd);
	}
})
