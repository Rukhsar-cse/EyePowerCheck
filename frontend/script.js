function showScreen(screenId) {
    document.querySelectorAll(".screen").forEach(screen => {
        screen.classList.remove("active");
    });

    document.getElementById(screenId).classList.add("active");

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

function selectAnswer(button) {
    document.querySelectorAll(".options button").forEach(btn => {
        btn.classList.remove("selected");
    });

    button.classList.add("selected");
}