/*
  Conta il tempo
  Scrivi un programma che dato un numero di secondi, calcoli la quantità di ore, minuti e secondi corrispondenti e
  poi stampi il risultato. L'output avrà solo numeri interi.

  Esempio:
    Input: 12560
    Output: 3 ore, 29 minuti e 20 secondi.

  Consigli:
  In un'ora ci sono 60 minuti, in un minuto 60 secondi. Quindi quanti secondi ci sono in un'ora? ;)

  http://www.imparareaprogrammare.it
*/
//RISOLUZIONE (Riccardo Curci)
var secondsINPUT = 12560 
var secondsINhour = 3600
const secondsINminute = 60
const X = 1760
var hours = Math.round(secondsINPUT / secondsINhour); 
var minutes = Math.round((secondsINPUT - hours * secondsINhour) / secondsINminute)
var seconds = (X % secondsINminute)
console.log( 'in '+secondsINPUT+' ci sono: '+hours+' ore, '+minutes+' minuti e '+seconds+' secondi'); 