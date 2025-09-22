document.addEventListener("DOMContentLoaded", function(){
	if (document.body.id === "home"){
		let tBody = document.querySelector("#tBody");
		let input = document.querySelector("#input");

		input.addEventListener("input", async function(event){
			let response = await fetch("/api/shows?title=" + input.value);
			let data = await response.json();
			//let data = JSON.parse(rawData);
			if(input.value === "") {
				tBody.innerHTML = "";
			}
			
			for(let i of data) {
				let tr = document.createElement("tr");
				tBody.appendChild(tr);
				for(let val in i) {
					let td = i[val];
					tr.innerHTML += "<td>" + td + "</td>";
				}
			}
		});

		// js for the spin game
		let poolContainer = document.querySelector(".poolContainer")
		let btn = document.querySelector(".spinBtn");
		let rCon = poolContainer.querySelector(".r");
		let spinText = poolContainer.querySelector("#spin");
		let loadText = poolContainer.querySelector("#load");
		let bal = poolContainer.querySelector(".bal");

		function loading() {
			spinText.style.display = "none";
			loadText.style.display = "block";
		}
		function success() {
			loadText.style.display = "none";
			spinText.style.display = "block";
			spinText.textContent = "Spin again";
		}

		btn.addEventListener("click", () => {
			loading();
			btn.disabled = true;
			async function get_r() {
				try {
					let response = await fetch('/api/spin_result');
					let data = await response.json();
					for (let d in data) {
						rCon.textContent = data[d];
						let r = data[d];
						if (r === "better luck next time") {
							success();
							btn.disabled = false;
							return console.log(r);
						}
						bal.textContent = Number(bal.textContent) + r;
						btn.disabled = false;
						success();
					}
				}
				catch (error) {
					console.log(error);
				}
			}
			setTimeout(get_r, 7000);
		});


		// function info() {
		// 	return `${this.name} is ${this.age} years old`;
		// }

		// let person_1 = {
		// 	name: "Jane", age: 25, info
		// };

		// console.log(person_1.info());

		// let person_2 = {
		// 	name: "Chuks", age: 28, bio: function () {
		// 		return this.name + " is " + this.age + " years old";
		// 	}
		// };
		// console.log(person_2.bio())

		// function balance() {
		// 	return `This ${this.bank} account has a balance of $${this.bal}`
		// }
		// function deposit(amt) {
		// 	this.bal = this.bal + amt
		// 	return `Credit Alert:\nThe sum of $${amt} has been deposited into your account\nNew Bal: $${this.bal}`
		// }

		// let acc_1 = {
		// 	bank: "UBA",
		// 	bal: 0,
		// 	balance,
		// 	deposit
		// }

		// console.log(acc_1.balance())
		// console.log(acc_1.deposit(20))
	}
});
