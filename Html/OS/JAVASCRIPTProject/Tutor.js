/* Class: 
A = Vehicle with for wheals for example Audi, Mercedes, Maserati, Ferrari
B = MotorCycle whith a cilindrate undere 125cc 
C = The TIR 
*/

// promemoria = sensori a posto infine quandl
// DATACENTER
var DataBase = { 
 A: {
  AA_000_AA: {
    Class: "A",
    Mark: "Alfa Romeo",
    Model: "Giulia Veloce",
    ProprietaryAddress: "Via Roma 23a, MILANO(UE(ITA))"
  },
  AA_001_AA: {
    Class: "A",
    Mark: "Fiat",
    Model: "600",
    ProrpietaryAddress: "Viale della Spiga 3, MILANO(EU(ITA))"
  }
},
B: { 
  AA_002_AA: {
    Class: "B",
    Mark: "Bmw",
    Model: "HP4 Race",
    ProprietaryAddress: "Breite Stra, BERLINO(EU(GER))"
  }
 },
C: {
 AA_003_AA: {
  Class: "C",
  Mark: "VolVO",
  Model: "FH",
  ProprietaryAddress: "Abacksgatan, GOTEBORG(EU(SVE))"
  }
 }
}
var TutorPosition = 000

var AA_000_AA = DataBase.A.AA_000_AA
var AA_001_AA = DataBase.A.AA_001_AA
var AA_002_AA = DataBase.B.AA_002_AA
var AA_003_AA = DataBase.C.AA_003_AA

var Class = [ "A","B,","C"]

var Sendfine = "Your vehicle weblog AA_000_AAA has exceeded the speed limit and now you will must pay a 250$ of fine"

function Tutor() {     
//INPUT
var VehicleDistance = 000 
var VehicleSpeed = 150
var VehicleClass = DataBase.C.AA_003_AA.Class
var Vehicle = DataBase.A.AA_000_AA
//SENSOR
var ActiveSensor = false 
var TutorCamera = AA_000_AA
var ScannClass = TutorCamera  

if (VehicleDistance = TutorPosition) {
  return ActiveSensor = true 
}

if (ScannClass = AA_000_AA) {
  return VehicleClass = DataBase.A.AA_000_AA.Class
} else if (ScannClass = AA_001_AA) {
  return VehicleClass = DataBase.A.AA_001_AA.Class
} else if (ScannClass = AA_002_AA) {
  return VehicleClass = DataBase.B.AA_002_AA.Class 
} else if (ScannClass = AA_003_AA) {
  return VehicleClass = DataBase.C.AA_003_AA.Class
}
  
//LOGIC 
function Tutor_A_B() {
var A_B_SpeedLimit = 150
var VehicleClassCorrect = true 
var ScannResults = "Regular"

if (VehicleClass = Class[0]) { 
 return VehicleClassCorrect = true 
} else if (VehicleClass = Class[1]) {
 return VehicleClassCorrect = true   
} else if (VehicleClass = CLass[2]) {
  return VehicleClassCorrect = false
}
  
if (VehicleSpeed <= A_B_SpeedLimit) {
  return ScannResults = "Regular"
} else {
    return ScannResults = "Incorrect"
}  
  
 }
  
}