/*
  Maggiore e minore
  Scrivi un programma che dati quattro numeri in input,
  restituisca in output il maggiore e il minore.

  Esempio:
    Input: a = 3, b = -1, c = 4, d = -2
    Output: maggiore = 4, minore = -2
    

  http://www.imparareaprogrammare.it
*/
var Number = [3, -1, 4, -2]

var LM = -10000000000000000000000000000000000000
var Lm = 10000000000000000000000000000000000000
for (var i of Number) {
  if (i >= LM) {
    LM = i
  } 
  
  if (i <= Lm) {
    Lm = i 
  }
}

var Num_M = LM
var Num_m = Lm 

console.log("maggiore: "+Num_M+" minore: "+Num_m)
