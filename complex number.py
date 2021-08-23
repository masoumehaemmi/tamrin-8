
def sum_complex(a , b ):
    result_calculation={}
    result_calculation['asli'] = a["asli"] + b["asli"]
    result_calculation['mohomi'] = a["mohomi"] + b["mohomi"]
    return result_calculation
def sub_complex(a , b):
    result_calculation={}
    result_calculation["asli"] = a["asli"] - b["asli"]
    result_calculation["mohomi"] = a["mohomi"] - b ["mohomi"]
    return result_calculation
def mult_complex(a , b):
    result_calculation={}
    result_calculation["asli"] = a["asli"] * b["asli"]
    result_calculation["mohomi"] = a["mohomi"] *b ["mohomi"]
    return result_calculation
def show_menu():
    print("1- sum number complex: ")
    print("2- sub number complex: ")
    print("3- mult number complex: ")
    print("4- exit: ")


a1= int(input(" enter your number one for real1 :"))
m1= int(input(" enter your number one for mohemi1 :"))
a2= int(input(" enter your number one for real2 :"))
m2= int(input(" enter your number one for mohemi2 :"))
a={"asli":a1 , "mohomi" : m1}
m ={"asli": a2 , "mohomi" : m2
}
show_menu()

choice= int(input("enter one choice for calculation : "))
if choice == 1:
    sum=sum_complex(a,m)
    print (sum)
elif choice == 2 :
    sub=sub_complex(a,m)
    print (sub) 
elif choice == 3:
    mul=mult_complex(a,m)
    print (mul )
elif choice == 4:
    exit()