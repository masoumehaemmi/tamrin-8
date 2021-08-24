rows=int(input("enter your number for rows a and column:"))
def rasm_diamond(rows):
    for i in range(rows):
     print(" "*(rows-i-1)+"* "*(i+1))
    for j in range(rows-1,0,-1):
      print(" "*(rows-j)+"* "*(j))
    #return rows
rasm_diamond(rows)
