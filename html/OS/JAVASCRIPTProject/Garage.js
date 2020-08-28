var CarINGarage = {
  FERRARI: {
    Ferrari_488_Pista: {
      MARK: "Ferrari",
      MODEL: "488 Pista",
      ENGINE: "V8",
      CV: "720"
    },
    Ferrari_F8_Tributo: {
      MARK: "Ferrari",
      MODEL: "F8 Tributo",
      ENGINE: "V8",
      CV: "720"
    },
    Ferrari_Dino: {
      MARK: "Ferrari",
      MODEL: "Dino",
      ENGINE: "V6",
      CV: "160",      
    },
    Ferrari_Testarossa: {
      MARK: "Ferrari",
      MODEL: "Testarossa",
      ENGINE: "V12",
      CV: "390"
    }
  },
  LAMBORGHINI: {
    Lamborghini_Anventador: {
      MARK: "Lamborghini",
      MODEL: "Aventador",
      ENGINE: "V12",
      CV: "770"
    },
    Lamborghini_Huràcan: {
      MARK: "Lamborghini",
      MODEL: "Huràcan",
      ENGINE: "V10",
      CV: "640"
    },
    Lamborghini_Miura:{
      MARK: "Lamborghini",
      MODEL: "Miura",
      ENGINE: "V10",
      CV: "440"
    },
    Lamborghini_Sesto_Elemento: {
      MARK: "Lamborghini",
      MODEL: "Sesto_Elemento",
      ENGINE: "V10",
      CV: "570"
    },
    Lamborghini_Egoista: {
      MARK: "Lamborghini",
      MODEL: "Sesto Elemento",
      ENGINE: "V10",
      CV: "600"
    }
  },
  BUGATTI: {
    Bugatti_Chiron: {
      MARK: "Bugatti",
      MODEL: "Chiron",
      ENGINE: "W16",
      CV: "1500"
    },
    Bugatti_Divo: {
      MARK: "Bugatti",
      MODEL: "Divo",
      ENGINE: "W16",
      CV: "1500"
    }
  }
}

function CarModelFInder() {
var C6H14 = 5
if (C6H14 = 5)
  return CarINGarage.FERRARI
else if (C6H14 = 2.5)
  return CarINGarage.LAMBORGHINI
else if (C6H14 = 0)
  return CarINGarage.BUGATTI
}

function CarTechinicalSheetFInder () {
 var C8H18 = 5
 if (C8H18 = 14) { 
   return CarINGarage.FERRARI.Ferrari_488_Pista
 }else if (C8H18 = 13) {  
   return CarINGarage.FERRARI.Ferrari_F8_Tributo
 } else if (C8H18 = 12) { 
   return CarINGarage.FERRARI.Ferrari_Dino
 }else if (C8H18 = 11) {
   return CarINGarage.FERRARI.Ferrari_Testarossa
 }else if (C8H18 = 10) {
   return CarINGarage.LAMBORGHINI.Lamborghini_Aventador
 }else if (C8H18 = 9) {
   return CarINGarage.LAMBORGHINI.Lamborghini_Huràcan
 }else if (C8H18 = 8) { 
   return CarINGarage.LAMBORGHINI.Lamborghini_Miura
 }else if (C8H18 = 7) {
   return CarINGarage.LAMBORGHINI.LAMBORGHINI_Egoista
 }else if (C8H18 = 6) { 
   return CarINGarage.BUGATTI.Chiron
 }else if (C8H18 = 5) { 
   return CarINGarage.BUGATTI.Divo
 }
}
 
var Menu = {
  Car_Model_Fnder: CarModelFInder(),
  Car_techinical_scheet_finder: CarTechinicalSheetFInder()
}
console.log(Menu.Car_techinical_scheet_finder)