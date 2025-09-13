document.addEventListener("DOMContentLoaded", function(){
	let nextBtn = document.querySelector("#next");
	let prevBtn = document.querySelector("#prev");
	let list = document.querySelector(".list");
	let thumbnail =	document.querySelector(".thumbnail");
    let autoclickNext;
    
    function startAutoSlide() {
        autoclickNext = setInterval(autoClickNext, 15000);
    }
    function removeNext() {
        list.classList.remove("next");
    }
    function removePrev() {
        list.classList.remove("prev");
    }

    nextBtn.addEventListener("click", function(){
        showSlider("next");
    });
    prevBtn.addEventListener("click", function(){
        showSlider("prev");
    })
	
    function showSlider(type) {
        let slider = document.querySelectorAll(".list .item");
        let thumbnailItem = document.querySelectorAll(".thumbnail .item2");

        if (type === "next") {
            list.appendChild(slider[0]);
            thumbnail.appendChild(thumbnailItem[0]);
            list.classList.add("next");
            setTimeout(removeNext, 2000);
            clearInterval(autoclickNext);
            startAutoSlide();
        }
        else if (type === "prev") {
            let lastListSlide = slider.length - 1;
            list.prepend(slider[lastListSlide]);
            thumbnail.prepend(thumbnailItem[lastListSlide]);
            list.classList.add("prev");
            setTimeout(removePrev, 2000);
            clearInterval(autoclickNext);
            startAutoSlide();
        }
    }
    function autoClickNext() {
        nextBtn.click();
    }

    autoClickNext();
    
});