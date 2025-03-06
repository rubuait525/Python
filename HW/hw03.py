#HW_Python_User_Defined_Function

stName = "ruby"
stId = 141414
stGrade = 3.45
fullTimeStudent = True

def st_info():
    st_details =(f'Student_name: "{stName.upper()}"\nStudentId: {stId}\nStunent Grade: {stGrade:,.3f}\nIs Student Full Time: {fullTimeStudent}')
    print(st_details)
    
    
st_info()   