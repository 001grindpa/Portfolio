document.addEventListener("DOMContentLoaded", function(){
    if (document.body.id === "signup"){
        let datePicker = document.querySelector(".datePicker");
        let dateImg = document.querySelector(".pickerImgC");
        let body = document.querySelector("body");
        let dates = document.querySelector(".dates");
        let cancel = document.querySelector(".cancel");
        let apply = document.querySelector(".apply");
        let selectedDate = new Date();
        let month = new Date().getMonth();
        let year = new Date().getFullYear();
        let prev = document.querySelector(".prev");
        let next = document.querySelector(".next");
        let yearInput = document.querySelector(".year");
        let monthSelector = document.querySelector("#month");
        let dob = document.querySelector("#dob");

        dob.addEventListener("click", function(event){
            dob.disabled = true;
        });
        datePicker.style.display = "none";
        dateImg.addEventListener("click", function(event){
            datePicker.style.display = "block";
            event.stopPropagation();
        });
        body.addEventListener("click", function(){
            datePicker.style.display = "none";
        });
        datePicker.addEventListener("click", function(event){
            event.stopPropagation();
        });
        cancel.addEventListener("click", function(){
            let selected = dates.querySelector(".sDate");
            if (selected) selected.classList.remove("sDate");
            selectedDate = new Date();
            datePicker.style.display = "none";
        });

        next.addEventListener("click", function(){
            if (year == 11) year++
            month = (month + 1) % 12;
            displayDates();
        });
        prev.addEventListener("click", function(){
            if (year == 0) year--
            month = (month -1 + 12) % 12;
            displayDates();
        });

        function configMonthYear(){
            monthSelector.selectedIndex = month;
            yearInput.value = year;
        };

        monthSelector.addEventListener("change", function(){
            month = monthSelector.selectedIndex;
            displayDates();
        });
        yearInput.addEventListener("input", function(){
            year = yearInput.value;
            displayDates();
        });

        apply.addEventListener("click", function(){
            dob.value = selectedDate.toLocaleDateString("en-US", {
                year: "numeric",
                month: "2-digit",
                day: "2-digit"
            });
            datePicker.style.display = "none";
        });

        function displayDates(){
            let lastOfMonth = new Date(year, month + 1, 0);
            let lastOfPrevMonth = new Date(year, month, 0);
            let firstOfNextMonth = new Date(year, month + 1, 1);

            dates.innerHTML = "";
            
            configMonthYear();

            for (let j = 0; j <= lastOfPrevMonth.getDay(); j++){
                let text = lastOfPrevMonth.getDate() - lastOfPrevMonth.getDay() + j;
                let button = createDateButton(text, true, false);
                dates.appendChild(button);
            }

            for (let i = 1; i <= lastOfMonth.getDate(); i++){
                let isToday = selectedDate.getDate() === i &&
                selectedDate.getMonth() === month &&
                selectedDate.getFullYear() === year;
                let button = createDateButton(i, false, isToday);
                button.addEventListener("click", function (event){
                    let selected = dates.querySelector(".sDate");

                    if (selected) selected.classList.remove("sDate");

                    button.classList.add("sDate");
                    selectedDate = new Date(year, month, parseInt(button.textContent));
                });
                dates.appendChild(button);
            }

            for (let h = firstOfNextMonth.getDay(); h <= 6; h++){
                let text = firstOfNextMonth.getDate() - firstOfNextMonth.getDay() + h;
                let button = createDateButton(text, true, false);
                dates.appendChild(button);
            }
        };
        displayDates();

        function createDateButton(text, isDisabled=false, isToday=false){
            let button = document.createElement("button");
            button.disabled = isDisabled;
            button.textContent = text;
            button.classList.toggle("today", isToday);
            return button;
        };

        // function selectDate(event){
        //     let btn = event.target();
        //     let selected = dates.querySelector(".sDate");

        //     if (selected) selected.classList.remove("sDate");

        //     btn.classList.add("sDate");
        //     selectedDate = new Date(year, month, parseInt(btn.textContent));
        // }
    };
})