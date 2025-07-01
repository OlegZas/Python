'''
Pseudo code: 
1.	User accesses the web app through the external IP address of the GCP’s cloud server. 
2.	User input’s his or her name and the initial of the last name. 
a.	A set of validations runs on the background. 
b.	If the name and the initial are in the list, then it returns the values. 
c.	If the name and initial are not in the list, it will show the error to the user and ask to try again.  
d.	If the user input’s incorrect name more than 3 times, then a default message will be sent. I will think about this one. 
3.	User input’s rank (jr., mid, sr.) and sales
a.	Validation: 
b.	If the rank is correct: 
i.	A loop runs through the ranks dictionary to get the commission of the corresponding rank 
ii.	Operations are performed to multiply user’s salary input by commission rate 
iii.	Return the result 
c.	Prompt the user if he/she wants to test another case: 
i.	Yes: restart the loop (step 2) 
ii.	no: ciao bambina seniorita 
d.	If the rank is wrong: 
i.	Error message. 
'''

#List for testing, later will connect database 
employee1 = {"NAME": "OLEG", "SALARY": 120000, "RANK": "JR", "COMMISSION": 0.1}

#user input 
print("Please enter your REAL name and the first name ")
userinput = input()
print(userinput)
if userinput.upper() ==  employee1["NAME"]: 
        print(f"Here is the {userinput} record", employee1)
else : 
        print("kaka")
#validate the input 