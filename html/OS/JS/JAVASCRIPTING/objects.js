//ESEMPIO 1
var James = {
  name: 'James',
  age: 20,
  adress: "Boston",
}
console.log(James)
//ESEMPIO 2 
var James = {
  name: 'James',
  age: 20,
  adress: "Boston",
}
console.log(James.age)
//ESEMPIO 3 
var garage = {
  make: "Ferrari",
  model: "458",
  year: 2019
}
garage ['fuel'] = 3.7 
console.log(garage)
//ESEMPIO 4 
var garage = {
  make: "Ferrari",
  model: "458",
  year: 2019
}
garage.wheel = 3.7 
console.log(garage)
//ESEMPIO 5 
var garage = {
  make: "Ferrari",
  model: "458",
  year: 2019,
  fuel: 3.7
} 
delete garage ['fuel']
console.log(garage)
//ESEMPIO 6 
var garage = {
  make: "Ferrari",
  model: "458",
  year: 2019,
  fuel: 3.7
}
garage.make = "Lamborghini" 
console.log(garage)