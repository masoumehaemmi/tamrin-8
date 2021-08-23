def sum_fraction(x,y):
    result={}
    result["s"]=x["s"] * y["m"] + x["m"] * y["s"]
    result["m"]=x["m"] * y["m"]
    return result
def mul_fraction(x,y):
    result={}
    result["s"] = x ["s"] * y ["s"]
    result["m"] = x["m"] * y["m"]
    return result
def sub_fraction(x,y):
    result={}
    result["s"]= x ["s"] * y ["m"] - x["m"] * y["s"]
    result["m"]= x["m"] * y["m"]
    return result
def div_fraction(x,y):
    result={}
    result["s"]= x["s"] * y["m"]
    result["m"]= x["m"] * y["s"]
    return result

a={"s": 4, "m": 6}
b={"s":5 , "m": 8}
print("sum :" , sum_fraction(a,b)  ,"mul:" ,mul_fraction(a,b),"sub:" , sub_fraction(a,b), "div:" ,div_fraction(a,b)  )
