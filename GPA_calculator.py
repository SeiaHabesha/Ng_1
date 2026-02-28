#GPA calculator
print("_-"*20)
print("GPA CALCULATOR!!")
print("_-"*20)
grades={"A+":4, 
			     "A": 4,
				"A-":3.75, 
				 "B+":3.5,
				 "B":3,
				 "B-":2.75,
				 "C+":2.5,
				 "C":2,
				 "C-":1.75,
				 "D":1,
				 "F":0

}


total_point=0
total_credit=0
while True:
	try:
		number_of_course=int(input("ENTER NUMBER OF COURSE : "))
		status=input("enter your H_P_E RESULT:  ")
		break
	
	except ValueError:
		print('please enter only number! ')

for i in range(number_of_course):
	grade=input("ENTER YOUR GPA:  ")
	credit_hour=int(input("enter the credit hour:  "))

	if grade in grades:
		value=grades[grade]
		total_point+=(value *credit_hour )
		total_credit +=credit_hour
	else:
		print("incorect gpa value! please enter  corect gpa  in upper case : ")
		
result=0	

try:		
	if status != " " :
		result=int(status)
	
	if result >=50:
		print("H_P_E > status/pass")
	else:
		print("H_P_E > status/fail")

except ValueError:
	print("incorrct h_p_e value: PLEAS ENTERYOUR CORECT RESULT ")



if total_credit >0:
	GPA=float(total_point /total_credit)
	print(f"your this year GPA is: {GPA:.2f} ")



	if GPA >=3.0:
			print("\033[92m  keep it up \033[0m ")
	elif GPA>1.7:
		print("\033[93mplease study Hard \033[0m")
	elif GPA >=1.5 :
		print("\033[91m on warning \033[0m")
	else:
			print("\033[91m Dissmied \033[0m")
else:
	print("novalid data entered: ")
		
print("_-"*20)
	





