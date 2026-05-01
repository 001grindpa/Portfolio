document.addEventListener("DOMContentLoaded", () => {
    const body = document.querySelector("body");
    const viewResumeBtn = body.querySelector(".section-1 .subSection label");
    const resumeCont = body.querySelector(".section-1 .subSection .resumeCont");
    const resume = body.querySelector(".section-1 .subSection .resume");
    const resumeCheck = body.querySelector(".section-1 .subSection #res");
    let exp = body.querySelector("#exp");
    let currentYear = body.querySelector("#currentYear");

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
            resumeCheck.checked = false;
        }

        resume.addEventListener("click", (e) => {
            e.stopImmediatePropagation();
        })
    })
})