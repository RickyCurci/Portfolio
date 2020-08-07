/*
  La calcolatrice
  Scrivi un programma che dati:
    - Due numeri
    - Una stringha che identifichi l'operazione da eseguire, es: "somma"
  Restituisca il valore ottenuto calcolando l'operazione tra i due numeri.

  Le operazioni supportate sono le suguenti:
    somma
    sottrazione
    moltiplicazione
    divisione
    modulo (solo tra interi)
    potenza
    media


  Esempi:
    Input: a = 5, b = 6, operazione = "somma"
    Output: 11

    Input: a = 5, b = 6, operazione = "media"
    Output: 5.5


  Utilizza il costrutto Switch-Case, gestire anche il caso di operazione non valida (non presente tra le operazioni consentite).


  http://www.imparareaprogrammare.it
*/

var Supp_Operation = {
  
  Somma: 1,
  Sottrazione: 2,
  Moltiplicazione: 3,
  Divisione: 4,
  Modulo: 5,
  Potenza: 6,
  Media: 7
  
}


var Num_1 = 4
var Num_2 = 2


var Chooser = 5
if (Chooser == Supp_Operation.Somma) {
  var Result = Num_1 + Num_2
  console.log(Result)
} else if (Chooser == Supp_Operation.Sottrazione) {
  var Result = Num_1 - Num_2
  console.log(Result)
} else if (Chooser == Supp_Operation.Moltiplicazione) {
  var Result = Num_1 * Num_2
  console.log(Result)
} else if (Chooser == Supp_Operation.Divisione) {
  var Result = Num_1 / Num_2
  console.log(Result)
} else if (Chooser == Supp_Operation.Modulo) { 
  var Result = Num_1 % Num_2
  console.log(Result)
} else if (Chooser == Supp_Operation.Potenza) {
  var Result = Num_1**Num_2
  console.log(Result)
} else if (Chooser == Supp_Operation.Media) {
  var Result = (Num_1 + Num_2) / 2
  console.log(Result)
}
    

    
    
    