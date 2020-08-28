/*
  Indovina il giorno
  Scrivi un programma con due funzioni, la prima prende in ingresso un intero e verifica se sia compreso nel range da 1 a 7.
  Se è compreso, la funzione restituirà TRUE, se non è compreso restituirà FALSE.

  La seconda funzione:
  - nel caso la prima restituisca TRUE visualizza il giorno della settimana corrispondente,
    considerando la seguente corrispondenza:
        1 = Lunedì
        ...
        7 = Domenica
  - nel caso il giorno non sia compreso nel range, la funzione dovrà restituire un messaggio d'errore simile a questo: 'Peccato, non posso indovinare il giorno.'


  http://www.imparareaprogrammare.it
*/
var Number = 3

var Days = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
var STATUS = false 

function Range_Verify() {
  if (Number <= 7) {
    STATUS = true 
  } else if (Number > 7) {
    STATUS = false 
  }
}
Range_Verify()

function Day_Verify() {
  if (STATUS == true) {
    console.log(Number+" = "+Days[Number-1])
  } else if (STATUS == false) {
  	console.log("Peccato, non possiamo indovinare il giorno, CONTROLLA IL NUMERO INSERITO ")    
  }
}

Day_Verify()