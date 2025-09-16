document.addEventListener("DOMContentLoaded", function() {
	let counterC = document.querySelector(".counterC");
	let counter = counterC.querySelector(".counter");
	let front = counterC.querySelector(".front");
	let back = counterC.querySelector(".back");
	let total = document.querySelector("#total");
	let saveBtn = counterC.querySelector(".save");
	let n = parseInt(counter.textContent);
	let total2 = document.querySelector("#total2");

	
	
	saveBtn.addEventListener("click", function(){
		total.innerHTML = n;
		for (let i = 0; i <= 0; i++){
			let t = document.createElement("span");
			t.textContent = `+${n} `;
			total2.appendChild(t);
		}
		counter.innerHTML = 0;
		n = 0;
	});
	
	front.addEventListener("click", function(){
		n++;
		counter.innerHTML = n;
	});

	back.addEventListener("click", function(event){
		if (n === 0){
			event.preventDefault();
		}
		else {
			n--;
			counter.innerHTML = n;
		}
	});

	// human-dog age ratio
	let human = document.querySelector("#human");
	let dogResult = document.querySelector("#dogResult");
	
	human.addEventListener("input", function(event){
		let humanAge = human.value;
		let dogAge = (humanAge * 7) / 1;

		dogResult.innerHTML = `${dogAge} years`;
	});

	// calculator
	let btn = document.querySelectorAll(".button");
	let input = document.querySelector("#input");
	let clear = document.querySelector(".clear");
	let equal = document.querySelector(".equal");
	let del = document.querySelector("#delete");

	del.addEventListener("click", function(){
		input.value = input.value.slice(0, -1);
	});

	clear.addEventListener("click", function(){
		input.value = "";
	});

	equal.addEventListener("click", function(){
		input.value = eval(input.value);
	});
	
	for (let i = 0; i <= btn.length; i++){
		btn[i].addEventListener("click", function(){
			input.value += btn[i].textContent;
		})
	}
	
	// blackjack game
	

	// slide in animation config
	let slideIn_1 = document.querySelector(".slideIn1");
	let slideIn_2 = document.querySelector(".slideIn2");
	slideIn_1.style.color = "red";

	let observer_1 = new IntersectionObserver((entries) => {
		entries.forEach((entry) => {
			if (entry.isIntersecting) {
				entry.target.classList.add("moveRight");
			}
			else {
				entry.target.classList.remove("moveRight");
			}
		});
	});
	observer_1.observe(slideIn_1);
})
