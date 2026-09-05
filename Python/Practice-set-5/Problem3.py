#Can we have set with 18(int) and '18'(str) as value in it
s = set()
s.add(18)
s.add("18")
print(s)

#Yes we can have set with int 18 and str 18, because in python 
#18 !== '18', Python treats them as two distinct items