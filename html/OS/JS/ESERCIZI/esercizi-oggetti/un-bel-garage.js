/*
  Un bel garage
  Scrivi un programma per la gestione di un garage.
  Definisci un oggetto che rappresenti un automobile, dovrà contenere almeno marca del veicolo e nome del modello.
  Scrivi una funzione che prenda in input una marca e stampi i modelli presenti nel garage di quella stessa marca.

  Consigli:
  Puoi usare un array come base per salvare le automobili.

  http://www.imparareaprogrammare.it
*/
//RISOLVO (Riccardo Curci)

//DATABASE 
    var CarsINgarage = {
    FERRARI: [
      "488 Pista","F8 Tributo","Dino","Testarossa"
      ],
    LAMBORGHINI: [
      "Aventador","Huracàn","Miura","Sesto Elemento","Egoista"
      ],
    BUGATTI:[
      "Chiron","Divo"
      ]
    }
  //TECHNICAL SHEET CAR IN A GARAGE
  var Car_0F = {
    mark: "Ferrari",
    model: "488 Pista",
    engine: "v8",
    cv: "720"
  }
  var Car_1F = {
   mark: "Farrari",
   model: "F8 Tributo",
   engine: "v8",
   cv: "720"
  }
  var Car_2F = {
    mark: "Ferrari",
    model: "Dino",
    engine: "v6",
    cv: "160"
  }
  var Car_3F = {
    mark: "Ferrari",
    model: "Testarossa",
    engine: "v12",
    cv: "390"
  }
  var Car_4L = {
    mark: "Lamborghini",
    model: "Aventador",
    engine: "v12",
    cv: "770"
  }
  var Car_5L = {	
    mark: "Lamborghini",
    model: "Huràcan",
    engine: "v10",
    cv: "640"
  }
  var Car_6L = {
    mark: "Lamborghini",
    model: "Miura",
    engine: "v10",
    cv: "440"
  }
  var Car_7L = {
    mark: "Lamborghini",
    model: "Sesto Elemento",
    engine: "v10",
    cv: "570"
  }	
  var Car_8L = {
    mark: "Lamborghini",
    model: "Egoista",
    engine: "v10",  
    cv: "600"
  }
  var Car_9B = {
    mark: "Bugatti",
    model: "Chiron",
    engine: "w16",
    cv: "1500"
  }
  var Car_10B = {
   mark: "Bugatti",
   model: "Divo",
  engine: "w16",
  cv: "1500"
}	

//ALGORITMI
var Ferrari = true 
var Lamborghini = true
var Bugatti = true

function CarFinder0() {
  if (Ferrari)
    return CarsINgarage.FERRARI
  else "Non ci sono risultati"
}
function CarFinder1() {
  if (Lamborghini)
    return CarsINgarage.LAMBORGHINI
  else 
    return "Non ci sono risultati"
}
function CarFinder2() {
  if (Bugatti)
    return CarsINgarage.BUGATTI
  else 
    return "Non ci sono risultati"
}
CarFinder2(); 