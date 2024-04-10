
const prompt = require('prompt-sync')();
// let age = prompt("Enter your age.\n");
// console.log("Output: " +age)
// let friend;
// do{
//     friend = prompt("Who is your friend?")
// }while (!friend)
//     console.log("Your friend is: "+ friend)

// age > 45 ? console.log("Robert"): console.log("Oyadier")
// console.assert(age, 4)
// while (age > 0)
// {
//     hello("Robert")
//     console.log(age)
//     age -=2
// }
// function hello(name = "name"){
//     console.log("Hello "+ name)
// }

// for (let days = 0; days < 10; days++)
// {
//     console.log(days)
// }

let array =  [4, 4, 5]
array[0] = 3
array.forEach(element => {
    console.log(element)
});
console.log(array[0])

let student = {
    names:"",
    age:0,
}
student.names = prompt("Enter your name.\n")
console.log(student.names)
let stu = "cat"
stu = "rat"
console.log(stu)