function Add(Line,Column) {

	Scene = [

		[[],[],[]],
		[[],[],[]],
		[[],[],[]]

	]

	Scene[Line][Column] = 0
	function Printer() {

		console.log(Scene[0])
		console.log(Scene[1])
		console.log(Scene[2])
	}

	Printer()
}

Add(0,2)
