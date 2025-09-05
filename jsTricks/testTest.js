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
})
