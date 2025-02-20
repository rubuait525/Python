#homeWork 2
"""
so far i know about four  types of variables
they are;
string ,int ,boolean,float

"""

myName = "abcd"
myAge = 200
fullTimeStudent = True
myGrade = 2.33

#now will print all varibles

print("-------------Print of all varibales outcome------------")
# Now, Print all the variables and their types as a outcome
print("myName:" + myName)
print(type(myName))
print("---------------------------------------------------------")
print("myAge:", myAge)
print(type(myAge))
print("---------------------------------------------------------")
print("fullTimeStudent:" , fullTimeStudent)
print(type(fullTimeStudent))
print("---------------------------------------------------------")
print("myGrade:" , myGrade)
print(type(myGrade))
print("---------------------------------------------------------")

text = ("""Most already know about the $9 toll to enter Manhattan at or below 60th Street,
in what's called the Congestion Relief Zone, 
but here's a look at exactly where drivers are and aren't being charged. 
Manhattan's Congestion Relief Zone starts at 60th Street and heads south to include the Lincoln, Holland and Hugh L. 
Carey tunnels on the Hudson River side, and the Queensboro Bridge, Queens Midtown Tunnel, Williamsburg Bridge, Manhattan Bridge and Brooklyn Bridge on the East Side.
 """)
print(text)
print("--------------------------------------------------------------------------")

text1 = ("Drivers coming from the Bronx or Upper Manhattan will be charged once they reach 60th Street.")
print(text1)
print("--------------------------------------------------------------------------")
print("here is new text ====== " + text, end=" ")
print("--------------------------------------------------------------------------------")

print('''\tMost already know about the $9 toll to enter \n"Manhattan's" at or below 60th Street,
in what's called the Congestion Relief Zone, 
but here's a look at exactly where drivers are and aren't being charged. 
Manhattan's Congestion Relief Zone starts at 60th Street and heads south to include the Lincoln, Holland and Hugh L. 
Carey tunnels on the Hudson River side, and the "Queensboro" Bridge, Queens Midtown Tunnel, Williamsburg Bridge, Manhattan Bridge and Brooklyn Bridge on the East Side.
 ''')
print("--------------------------------------------------------------------------")
