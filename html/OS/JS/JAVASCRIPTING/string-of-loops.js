var contains = false 
var word = 'tacos'
for (var letter of word) {
  if (letter === "a") {
    contains = true
  }
}
console.log(contains)
//ESEMPIO 2 
var contains = false 
var word = "burrito"
for (var letter of word) {
  contains = contains || (letter === "a")
}
console.log(contains)
//ESEMPIO 3
function checkLetter(check, word) {
  var contains = false 
  for (var letter of word) {
    contains = contains || (letter === check)
  }
  return contains
}
console.log(checkLetter)
//ESEMPIO 4 
function checkLetter(check, word) {
  for (var letter of word) {
    if (letter === check) {
      return true 
    }
  }
  return false 
}
console.log(checkLetter)