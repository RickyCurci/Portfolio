/*
  Quanti anni ha?
  Scrivi un programma che dato l'anno corrente e un anno di nascita determini:
    - l'età della persona,
    - quanti anni sono necessari per raggiungere i 100
  Restituisca in output entrambi i risultati.

  Esempio:
    Input: anno corrente = 2018, anno di nascita = 1991
    Ouput: età = 27, anni mancanti = 73

  http://www.imparareaprogrammare.it
*/
//RISOLUZIONE (Riccardo Curci)
var bornYears = 1991;  
var currenYears = 2018; 
var objectYears = 100;
var ages = (currenYears - bornYears);
var missingYears = (objectYears - ages); 
console.log('luca ha '+ages+' anni e per raggiungere i 100 anni li mancano '+missingYears+' anni'); 