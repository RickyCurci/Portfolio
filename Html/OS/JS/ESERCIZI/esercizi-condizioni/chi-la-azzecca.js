/*
  Chi l'azzecca?
  Scrivi un programma che dati due numeri di due ipotetici giocatori,
  generi un numero casuale compreso tra 1 e 100 (zero escluso),
  verifichi se uno dei due giocatori ha azzeccato il numero casuale,
  e in caso contrario quale dei due si è avvicinato di più al numero.

  Esempio:
    Input: giocatore 1 = 5, giocatore 2 = 10
    Output: Numero casuale generato = 7
            "Nessuno dei due ha azzeccato il numero casuale, ma il giocatore 1 si è avvicinato di più!"

  Consigli:
  Per generare un numero casuale utlizza la funzione javascript Math.random() che restituisce un intervallo compreso tra 0 e 1.
  Il valore ottenuto dovrà essere convertito per ottenere un valore valido per il tuo intervallo, in questo modo:
    (Math.random() * (max-min) + min) ovvero, nel tuo caso:
    (Math.random() * (100-1) + 1)
  Ricordati che il valore dovrà essere intero quindi dovrai arrontondarlo usando Math.floor()

  http://www.imparareaprogrammare.it
*/
var Player_1 = 12 
var Player_2 = 10 

var Random_Num = 8

if ((Player_1 == Random_Num) && (Player_2 != Random_Num)) {
  
  console.log("Numero casuale generato = "+Random_Num)
  console.log("Il giocatore 1 ha indovinato il numero casuale!!!")
  console.log("GIOCATORE 1 = "+Player_1+" / "+"NUMERO CASUALE = "+Random_Num)
  
} else if ((Player_2 == Random_Num) && (Player_1 != Random_Num)) {
  
  console.log("Numero casuale generato = "+Random_Num)
  console.log("Il giocatore 2 ha indovinato il numero casuale!!!")
  console.log("GIOCATORE 2 = "+Player_2+" / "+"NUMERO CASUALE = "+Random_Num)
  
} else if (Player_2 && Player_1 == Random_Num) {
  
  console.log("Numero casuale generato = "+Random_Num)
  console.log("Il giocatore 1 e Giocatore 2 hanno indovinato il numero casuale!!!")
  console.log("GIOCATORE 1 = "+Player_1+" GIOCATORE 2 = "+Player_2+" / "+"NUMERO CASUALE = "+Random_Num)
  
}

if ((Player_1 && Player_2 != Random_Num) && ((Player_1 - Random_Num) <= (Player_2 - Random_Num))) {

  console.log("Numero casuale generato = "+Random_Num)
  console.log("Nessuno dei due giocatori ha indovinato il numero casuale, ma il giocatore 1 si è avvicinato di più")

} else if ((Player_1 && Player_2 != Random_Num) && ((Player_1 - Random_Num) >= (Player_2 - Random_Num))) {
  
  console.log("Numero casuale generato = "+Random_Num)
  console.log("Nessuno dei due giocatori ha indovinato il numero casuale, ma il giocatore 2 si è avvicinato di più")

} 

