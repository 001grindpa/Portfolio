document.addEventListener("DOMContentLoaded", function(){
	let testBlock = document.querySelector("#testBlock");
	testBlock.style.display = "flex";
	
	function intChecker(f, s){
		if (f > s){
			return testBlock.innerHTML = `${f} is greater than ${s}`;
		}
		else if (f < s){
			return testBlock.innerHTML = `${f} is less than ${s}`;
		}
	}

	//intChecker(2, 8);

	let i = 1;
	while(i <= 5) {
		let testChild = document.createElement("div");
		testChild.textContent = i;
		testBlock.appendChild(testChild);
		i ++;
	}

	//function red(){
	//	testBlock.style.background = (testBlock.style.background === "black") ? "red" : "black";	
	//}

	testBlock.addEventListener("click", function(){
		testBlock.style.background = testBlock.style.background = (testBlock.style.background === "black") ? "red" : "black";
	})

	let input = document.querySelector("#testInput");
	
	input.addEventListener("input", function(event){
		let chars = input.value;
		if (chars.length >= 6){
			alert("6 or more characters entered");
		}
	})

	// slide in animation config
	let slideIn_1 = document.querySelector(".slideIn1");
	let slideIn_2 = document.querySelector(".slideIn2");

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

	let observer_2 = new IntersectionObserver((entries) => {
		entries.forEach((entry) => {
			if (entry.isIntersecting) {
				entry.target.classList.add("moveLeft");
			}
			else {
				entry.target.classList.remove("moveLeft");
			}
		});
	});
	
	observer_2.observe(slideIn_2);


	// testing functions

	// let doneWorking = () => {
	// 	console.log("done with this work");
	// }

	// function doWork(work, callback) {
	// 	console.log("working on " + work);
	// 	callback();
	// }

	// doWork("assignment", () => console.log("done working"));

	// creating an object method
	let car = {
		brand: "Lexus",
		start: function(status, need) {
			console.log(`${this.brand} is starting... ${this.brand} is ${status}, it needs ${need}`);
		}
	}
	car.start("working", "washing");

	// function sportCar(name, price, year_released) {
	// 	let car = {
	// 		name: name,
	// 		price: price,
	// 		year: year_released,
	// 		info: function() {
	// 			console.log(`This ${this.name} was released in ${this.year} and cost around $${this.price}`);
	// 		}
	// 	}
	// 	car.info();
	// }
	// sportCar("Lamburgini", 300000, 2024);
})
