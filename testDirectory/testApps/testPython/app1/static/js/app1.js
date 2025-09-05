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
	}
});
