/*
  Tanti numeri
  Scrivi un programma che dato array di numeri, calcoli la media dei valori e
  restituisca in output la media e tutti i valori minori della media.

  Esempio:
    Input: a = [3, 5, 10, 2, 8]
    Output: media = 5.6, valori minori = [3, 5, 2]

  Variante:
  Stampa anche quanti sono i valori minori della media e quanti quelli maggiori.

  http://www.imparareaprogrammare.it
*/
//RISOLVO (Riccardo Curci)
var numIN = [
  3,5,10,2,8
]
var NumIN = [
  3 + 5 + 10 + 2 + 8 
] 
var AVERAGE = (NumIN/numIN.length)
console.log(AVERAGE)
for (var numIN = 3,5,10,8; numIN < AVERAGE; numIN++) {
  console.log(numIN)
}