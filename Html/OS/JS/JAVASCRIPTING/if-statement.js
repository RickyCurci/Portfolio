//ESEMPIO 1 
var sold = true; 
if (sold) {
  console.log('ok'); 
}
//ESEMPIO 2 
var results = false
if (results) {
  console.log('122')
} else {
  console.log('errato')
}
//ESEMPIO 3 
var speed = true
var aerodynamics = true
if (speed && aerodynamics) {
  console.log('ok, now you will win the championshp')
} else {
  console.log("I'm sorry you will lose the championship")
}
//ESEMPIO 4 
var time = false 
var target = true
if (time || target) {
  console.log("for lucky you have reached the target")
} else {
  console.log("oh no you don't reached the target in time")
}  
//ESEMPIO 5 
var car = false 
var pilot = false 
if (car == pilot) {
  console.log("ok you can do retur at the box")
} else {
  console.log("Seb continue the race")
}
//ESEMPIO 6 
var temp = -2
if (temp > 40) {
  console.log("hot")
} else if (temp > 25) {
  console.log("normal")
} else if (temp > 0){
  console.log("freezing")
} else {
  console.log("subzero")
}