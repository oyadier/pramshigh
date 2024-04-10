console.log

const btnGree = document.getElementById('send');

btnGree.addEventListener("click", function(){

const first_name = document.getElementById('first');
const last_name = document.getElementById('last');
const first = first_name.value;
const last = last_name.value;

const welcome = document.getElementById('oya');
    welcome.textContent = welcome.textContent.concat(first);
console.log(first, last);
});

// Add new Button
let count = 10
const ul = document.getElementById('buttons')
const news = document.getElementById('new_button');

news.addEventListener('click', function (){
    if(count > 0){
        const list_button = document.createElement('ol')
const but = document.createElement('input')
   ul.appendChild(list_button).appendChild(but)
   console.log(ul.lastChild);
    }count -= 1;
})

