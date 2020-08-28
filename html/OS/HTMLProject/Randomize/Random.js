function Random() {
  var Response = "Number printed in a page"
  var Input = parseInt(document.querySelector("#Max").value)
  var Output = Math.floor(Math.random() * Input + 1)
  document.querySelector("#RandomNumber").innerHTML = Output
  console.log(Response)
}



