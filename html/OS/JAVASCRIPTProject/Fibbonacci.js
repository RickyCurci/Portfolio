var n = 2
var Fb = [0,1]

while (n > 1) {
  
  var L = (n - 1) + (n -2)
  Fb.push(L)

  n++
  
  if (n == 233) {
     break
  }

}

console.log(Fb)