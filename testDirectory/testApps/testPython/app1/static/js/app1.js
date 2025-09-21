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
			async function get_r() {
				try {
					let response = await fetch('/api/spin_result');
					let data = await response.json();
					for (let d in data) {
						rCon.textContent = data[d];
					}
					success();
				}
				catch (error) {
					console.log(error);
				}
			}
			setTimeout(get_r, 3000)
		});
	}
});
