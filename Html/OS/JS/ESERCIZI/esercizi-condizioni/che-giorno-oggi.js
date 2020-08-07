/*
  Che giorno è oggi?
  Scrivi un programma che dato un numero intero compreso tra 1 a 7
  visualizzi il corrispondente giorno della settimana. Sapendo che:
    1 = lunedì
    2 = martedì
    3 = mercoledì
    ...
    7 = domenica
  Utilizza il costrutto Switch-case e prevedi anche il caso in cui il valore immesso non sia valido
  (nel caso stampare un messaggio di errore a tua scelta).

  Esempi:
    Input: numero = 6
    Output: "Sabato"

    Input: numero = 10
    Output: "Errore! Giorno della settimana non valido!"

  Variante:
  Scrivere una versione che anziché i giorni della settimana, visualizzi i nomi dei mesi.

  http://www.imparareaprogrammare.it
*/
var Week_Day = [
  "Lunedi","Martedì","Mercoledì","Giovedì","Venerdì","Sabato","Domenica"
]

var Chooser = 7

if (Chooser <= 7) {
  console.log(Week_Day[Chooser-1]) 
} else if (Chooser > 7) {
  console.log("Errore! Giorno della settimana non valido!")
}
