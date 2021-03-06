def Calculator(inp):
	s=[]		#number stack
	op=""		#operator
	result=""	#output
	
	#possible operators
	operators={'+','-','*','/'}
	
	for i in range(len(inp)):
		
		#if it is a number, push it to number stack
		if inp[i].isdigit():
			s.append(inp[i])
			
		#if it is a character, check what operation to do
		elif inp[i].isalpha():
			

			#12345
			#clear previous number and operator alone
			if inp[i].upper()=="C":
				#print(s)
				s.pop()
				op=""
				#print(s)
			
			#clear the result and start fresh
			elif inp[i].upper()=="A":
				while len(s) != 0:
					s.pop()
				op=""
				result=""
				
			#quit the program
			elif inp[i].upper()=="Q":
				return None
		
		#if its an operator, calculate the value
		elif inp[i] in operators:
			if op=="":
				op=inp[i]
			else:
				B=s.pop()
				A=s.pop()
				result=str(eval(A+op+B))
				#print(op,A,B,result)
				s.append(result)
				op=inp[i]
	
	#for last calculation
	if op!="" and len(s)>0:
		B=s.pop()
		A=s.pop()
		result=str(eval(A+op+B))
		#print(op,A,B,result)
		
	return result


inp1="2+6-3*7/5"
inp2="2+6-3*7/3C/5"
inp3="2+6-3*7/3A5/5"
inp4="2+3Q"
print("res  normal: ",Calculator(inp1))
print("res after C: ",Calculator(inp2))
print("res after A: ",Calculator(inp3))
print("res after Q: ",Calculator(inp4))
