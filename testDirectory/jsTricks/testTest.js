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
})
