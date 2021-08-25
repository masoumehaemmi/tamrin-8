def sum_time(x,y):
    result ={}
    result["s"] = x["s"] + y["s"]
    result["m"] = x["m"] + y["m"]
    result["h"] = x["h"] + y["h"]
    
    if result["s"] >=60:
        result["s"] -= 60
        result["m"] += 1

    if result["m"] >= 60:
        result["m"] -=60
        result["h"] +=1

    if result["h"] > 23 :
        result["h"] -= 24

    return result
def sub_time(x,y):
    result={}
    result["s"]=x["s"] - y["s"]
    result["m"]=x["m"] - y["m"]
    result["h"]=x["h"] - y["h"]
    if result["s"] < 0:
        result["m"] =- 1
        result["h"] =+ 60
    if result["m"] < 0:
        result["h"] -= 1
        result["m"] =+ 60
    return result

def sec_to_hours():
    sec=int(input("enter second for convert to hours:"))
    result={}
    result["h"] = sec // 3600
    result["m"] = (sec % 3600) // 60
    result["s"] = (sec % 3600) % 60
    return result

def hours_to_sec(x):
    #x["h"] = x["h"] * 3600
    #x["m"] = x["m"] * 60
    #x["s"] = x["s"]
    second =(x['h']*3600 + x['m']*60 + x['s'])
    return second

def show(x):
    print(x["h"], ":", x["m"], ":", x["s"])

t1 ={"h":3, "m":30, "s":45}
t2={"h":13, "m":46, "s":30}
t3= show(sum_time(t1, t2))
print(t3)

sub1=show(sub_time(t1,t2))
print (sub1)

s_to_h=show(sec_to_hours())
print (s_to_h)

h_to_s=hours_to_sec(t1)
print(h_to_s)
