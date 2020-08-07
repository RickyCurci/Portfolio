/*
  Somma e media
  Scrivi un programma che dati 5 numeri restituisca in output la somma e la media.

  Esempio:
    Input: a = 1, b = 2, c = 3, d = 4, e = 5
    Output: somma = 15, media = 3
  
  http://www.imparareaprogrammare.it
*/

//RISOLUZIONE (Riccardo Curci)
var A = 20; 
var B = 2;
var C = 34; 
var D = 56; 
var E = 4;
var NUMBER = 5; 
var SUM = (A+B+C+D+E);
var AVERAGE = Math.ceil((A+B+C+D+E)/NUMBER); 
console.log('la somma è di '+SUM);
console.log('la media è di '+AVERAGE);