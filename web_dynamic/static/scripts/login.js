console.log

const btnGree = document.getElementById('send');

btnGree.addEventListener("click", function () {

    const first_name = document.getElementById('first');
    const last_name = document.getElementById('last');
    const first = first_name.value;
    const last = last_name.value;

    const welcome = document.getElementById('oya');
    welcome.textContent = welcome.textContent.concat(first);
    printInput(first, last)
});

// Add new Button
let count = 10
const list = document.getElementById('buttons')
let result = 0;
const btn = document.getElementById('compute').addEventListener('click', function () {
    let elem = [];
    list.querySelectorAll('ol').forEach(element => {
        element.querySelectorAll('input').forEach(e => {
            elem.push(e.value)

        })

        sumOfInputs(elem)
        //sumOfInputs(list.children)
    });

});

const news = document.getElementById('new_button');
const ul = document.getElementById('buttons')

news.addEventListener('click', inputElements)
// Create new input element
function inputElements() {
    if (count > 0) {
        const list_button = document.createElement('ol')
        const but = document.createElement('input')
        but.setAttribute('type', 'text')
        but.setAttribute('value', 'Default Value')
        ul.appendChild(list_button).appendChild(but)
    } count -= 1;
}

function sumOfInputs(numbers) {
    let result = 0;

    console.log("Final result: " + " : " + numbers)
}
