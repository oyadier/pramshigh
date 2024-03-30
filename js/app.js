const btnGreeting = document.getElementById("hello");

btnGreeting.addEventListener("click", function(){
    const greet = document.getElementById("output");

    greet.textContent = "Hello! Word"
});