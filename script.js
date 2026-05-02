document.addEventListener("DOMContentLoaded", () => {
    const body = document.querySelector("body");
    const viewResumeBtn = body.querySelector(".section-1 .subSection label");
    const resumeCont = body.querySelector(".section-1 .subSection .resumeCont");
    const resume = body.querySelector(".section-1 .subSection .resume");
    const resumeCheck = body.querySelector(".section-1 .subSection #res");
    let exp = body.querySelector("#exp");
    let currentYear = body.querySelector("#currentYear");
    const aboutMe = body.querySelector(".section-2");
    const expSection = body.querySelector(".section-3");

    // dynamic years config
    // for years of experience
    let year = new Date().getFullYear();
    let expYear = year - 2023;
    exp.textContent = expYear;
    // for footer
    currentYear.textContent = year;

    // view resume logic
    resumeCont.addEventListener("click", () => {
        if (resumeCheck.checked == true) {
            resumeCheck.click();
        }
    })
    resume.addEventListener("click", (e) => {
        e.stopPropagation();
    })
    // event handler for frezzing and unfreezing page
    resumeCheck.addEventListener("change", () => {
        if (resumeCheck.checked == true) {
            body.style.overflowY = "hidden";
        } else if (resumeCheck.checked == false) {
            body.style.overflowY = "auto";
        }
    })

    // use intersection observer to add class
    let observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            let target = entry.target;

            if (entry.isIntersecting) {
                target.classList.add("slide-up");
            }
        })
    })
    observer.observe(aboutMe);
    observer.observe(expSection);
})