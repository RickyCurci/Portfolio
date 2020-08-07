SpecialChar = "±"
def Addition(): 
	Value = input("1: Value: ")
	Uncertainty = input("Uncertainty: ")
	
	CValue = float(Value)
	CUncertainty = float(Uncertainty)
	
	Value_1 = input("2: Value: ")
	Uncertainty_1 = input("2: Uncertainty: ")
	
	CValue_1 = float(Value_1)
	CUncertainty_1 = float(Uncertainty_1)

	ValueLogic = CValue + CValue_1
	UncertaintyLogic = CUncertainty + CUncertainty_1
	
	print("Results: ")
	print(ValueLogic, SpecialChar, UncertaintyLogic)

def Subtraction(): 
	Value = input("1: Value: ")
	Uncertainty = input("1: Uncertainty: ")
	
	CValue = float(Value)
	CUncertainty = float(Uncertainty)
	
	Value_1 = input("2: Value: ")
	Uncertainty_1 = input("2: Uncertainty: ")
	
	CValue_1 = float(Value_1)
	CUncertainty_1 = float(Uncertainty_1)
	
	ValueLogic = CValue - CValue_1 
	UncertaintyLogic = CUncertainty + CUncertainty_1
	
	print("Results: ")
	print(ValueLogic, SpecialChar, UncertaintyLogic)
	
def Multiplication():
	Value = input("1: Value: ")
	Uncertainty = input("1: Uncertainty: ")
	
	CValue = float(Value)
	CUncertainty = float(Uncertainty)
	
	Value_1 = input("2: Value: ")
	Uncertainty_1 = input("2: Uncertainty: ")
	
	CValue_1 = float(Value_1)
	CUncertainty_1 = float(Uncertainty_1)
	
	UncertaintyRelative = CUncertainty / CValue
	UncertaintyRelative_1 = CUncertainty_1 / CValue_1
	
	ValueLogic = CValue * CValue_1 
	UncertaintyLogic = (UncertaintyRelative + UncertaintyRelative_1) * ValueLogic
	
	print(ValueLogic, SpecialChar, UncertaintyLogic) 
	
def Division(): 
	Value = input("1: Value: ")
	Uncertainty = input("1: Uncertainty")
	
	CValue = float(Value)
	CUncertainty = float(Uncertainty)
	
	Value_1 = input("2: Value: ")
	Uncertainty_1 = input("2: Uncertainty: ")
	
	CValue_1 = float(Value_1)
	CUncertainty_1 = float(Uncertainty_1)
	
	UncertaintyRelative = CUncertainty / CValue
	UncertaintyRelative_1 = CUncertainty_1 / CValue_1
	
	ValueLogic = CValue / CValue_1 
	UncertaintyLogic = (UncertaintyRelative + UncertaintyRelative_1) * ValueLogic
	
	print(ValueLogic, SpecialChar, UncertaintyLogic) 
		
HomePage = """	
Fisic

 	[ 0 ]Addition
 	[ 1 ]Subtraction 
 	[ 2 ]Multiplication 
 	[ 3 ]Division 		

"""
print(HomePage)
Value = [ "0","1","2","3"]
Label = input("Enter: ")

if Label == Value[0]: 
	print(Addition())
if Label == Value[1]: 
	print(Subtraction())
if Label == Value[2]: 
	print(Multiplication())
if Label == Value[3]: 
	print(Division())
	
	
