function Active_System() {
  var Support = true 
  var Support1 = true 
}
Active_System()

var CTK = "Celsius to Kelvin"
var KTC = "Kelvin to Celsius"


//Celsius to Kelvin 
function Celsius_To_Kelvin() {
 var Input = 800


var LogicC = Input + 273.15
var Output = LogicC 


  return Output
 
}

//Kelvin to Celsius
function Kelvin_To_Celsius() {
 var Input = 5784

var LogicK = Input - 273.15 
var Output = LogicK

 return Output
}


//User Interface

var UserLabel = CTK

if (UserLabel = "Celsius to Kelvin") {
  console.log(Celsius_To_Kelvin())
}

if (UserLabel = "Kelvin to Celsius") {
  console.log(Kelvin_To_Celsius()) 
}

