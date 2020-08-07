/*
  Verifica la data
  Scrivi un programma che definisca un oggetto per la rappresentazione di una data e verifichi se è valida o meno.
  L'oggetto sarà composto da giorno, mese e anno (input a piacere).

  Esempio:
    Input:
      day: 18
      month: 19
      year: 2016
    Output:
      "La data non è valida!"

  http://www.imparareaprogrammare.it
*/
//RISOLVO (Riccardo Curci)
var date = {
  day: 18,
  month: 19,
  year: 2016
}
console.log(date)
date = false 
if (date) {
  console.log('la data è corretta')
} else {
  console.log('la data non è valida')
} 