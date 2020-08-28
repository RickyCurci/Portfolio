var Letter = "ABCDEFGHIKLMNOPQRSTVXYZabcdefghiklmnopqrstuvxyz123456789#@"
var Char = Letter.split("")
var Limit = 3
function Generator() {
  var Password = []

  for (var i in Char){
    
    var Range =  parseInt(Math.floor(Math.random() * 55) + 1)
    var Element = Char[Range]
     
    Password.push(Element)
  }
  console.log(Password)
  Password.reverse()
  Password = Password.join("")
  Password = Password.slice(0,Limit)

  
  console.log("YOUR PASSWORD IS: ",Password)
  
}

Generator()