/*
  Primo e ultimo
  Scrivi due funzioni una che prenda in input tre numeri e restituisca il maggiore,
  l'altra che restituisca il minore.

  Esempio:
    Input: a = 1, b = -10, c = 4
    Output: minore = -10, maggiore = 4

  Variante:
  Scrivi due funzioni che prendano in input un array di numeri, una funzione deve restituire il valore maggiore contenuto nell'array,
  l'altra il valore minore.

  http://www.imparareaprogrammare.it
*/

var Num = [1, -10, 4]
var LM = 0
function Minus_Num() {
  for (var i of Num) {
	if (i >= LM) {
      LM = i 

    }
  } 
}
Minus_Num()

var Lm = 0
function Max_Num() {
  for (var i of Num) {
	if (i <= Lm) {
      Lm = i 
      
    }
  } 
}
Max_Num()

console.log("Minore: "+Lm)
console.log("Maggiore: "+LM)

