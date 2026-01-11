document.addEventListener("DOMContentLoaded", () => {
    const input = document.querySelector("input[name='username']");
    const button = document.querySelector("button");

    button.addEventListener("click", () => {
        if (!input.value) {
            alert("Please enter a GitHub username!");
        }
    });

    console.log("GitHub Profile Analyzer Loaded ✅");
});
