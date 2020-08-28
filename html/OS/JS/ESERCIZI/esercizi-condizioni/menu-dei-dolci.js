/*
  Menu dei dolci
  Scrivi un programma che dato il seguente menu (da stampare):
    MENU:
    1. Tiramisù
    2. Torta della nonna
    3. Cheesecake alla nutella
    4. Macedonia

  Prenda in input un valore numerico che rappresenti la scelta e restituisca:
    - se la scelta non è tra quelle elencate la scritta 'Dolce non disponibile',
    - altrimenti la scelta effettuata 'Hai scelto il dolce X'.


  Esempi:
    Input: scelta = 4
    Output: Hai scelto il dolce Macedonia

    Input: scelta = 7
    Output: Dolce non disponibile

  http://www.imparareaprogrammare.it
*/

var Item = [
  "1. Tiramisù",
  "2. Torta della nonna",
  "3. Cheesecake alla nutella",
  "4. Macedonia"
]
var Chooser = 7 

//MENU PRINT 
var Menu = {
  1.: "Tiramisù",
  2.: "Torta della nonna",
  3.: "Cheesecake alla nutella",
  4.: "Macedonia"
}
// CHOOSER CONDITION 
if (Chooser >= Item.lenght) {
  Menu ["--------------"] = "----------------"
  console.log(Menu)
  console.log("Dolce non disponibili")
} else {
  Menu ["--------------"] = "----------------"
  Menu ["Choose"] = "SCELTA: "
  Menu ["Item"] = Item[Chooser - 1]
  console.log(Menu)
}
