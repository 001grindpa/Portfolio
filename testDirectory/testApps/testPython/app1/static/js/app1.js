document.addEventListener("DOMContentLoaded", function(){
	if (document.body.id === "home"){
		let tr = document.querySelector("#tBody");
		let input = document.querySelector("#input");
		input.style.background = "black";

		input.addEventListener("input", function(event){
			let response = await fetch("/api/shows?title=" + input.value);
			let data = response.json();
			alert(data);
		});
	}
})
