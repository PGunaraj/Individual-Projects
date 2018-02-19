currValue="0"

#RECEIVER CLASS
class Calculator(object):
    def Add(self,num):
        global currValue
        currValue=str(eval(currValue+"+"+num))
    def Subtract(self,num):
        global currValue
        currValue=str(eval(currValue+"-"+num))
    def Multiply(self,num):
        global currValue
        currValue=str(eval(currValue+"*"+num))
    def Divide(self,num):
        global currValue
        currValue=str(eval(currValue+"/"+num))

#INVOKER CLASS
class CalculatorInvoker(object):
    '''def __init__(self):
        self.history=[]
    @property
    def history(self):
        return self.history'''
    def execute(self,command,num):
        #self.history.append(command,num)
        command.execute(num)

#COMMAND CLASS
class command(object):
    def __init__(self,obj):
        self.receiver=obj
    def execute(self,num):
        raise NotImplementedError

#CONCRETE COMMAND CLASS
class AddNumbers(command):
    def execute(self,num):
        self.receiver.Add(num)
class SubtractNumbers(command):
    def execute(self,num):
        self.receiver.Subtract(num)
class MultiplyNumbers(command):
    def execute(self,num):
        self.receiver.Multiply(num)
class DivideNumbers(command):
    def execute(self,num):
        self.receiver.Divide(num)

#CLIENT CLASS
class CalculatorClient(object):
    def __init__(self):
        #CREATING RECEIVER CLASS OBJECT
        self.rec=Calculator()
        #CREATING INVOKER CLASS OBJECT
        self.inv=CalculatorInvoker()
    '''@property
    def historyInvoke(self):
        return self.inv'''
    def invoke(self,op,b):
        if op=="+":
            self.inv.execute(AddNumbers(self.rec),b)
        elif op=="-":
            self.inv.execute(SubtractNumbers(self.rec),b)
        elif op=="*":
            self.inv.execute(MultiplyNumbers(self.rec),b)
        elif op=="/":
            self.inv.execute(DivideNumbers(self.rec),b)
    
def computeValue(exp):
    if exp[0].isdigit() or exp.startswith('-') or exp.startswith('+'):
        i=1
        while i<len(exp) and exp[i]!=" ":
            i=i+1
        temp=exp[0:i]
        if temp.find("/")!=-1:
            pos=temp.find("/")
            a=temp[0:pos]
            b=temp[pos+1:]
            return(i,str(int(a)/int(b)))
        elif temp.find("!")!=-1:
            pos=temp.find("!")
            a=temp[0:pos]
            ans=1
            k=1
            while k <= int(a):
                ans=ans*k
                k=k+1
            return(i,str(ans))
        return(i,temp)

if __name__=="__main__":
    #GET INPUT FROM USER
    exp=input("enter the expression: ")
    
    #IF INPUT IS Q, THEN QUIT THE PROGRAM
    if len(exp)==1 and exp[0]=='Q':
        print("Program Ended")
    else:
        #SET THE CURRENT VALUE TO BE THE FIRST NUMBER OF THE EXPRESSION
        i,currValue = computeValue(exp)

        #CALL CLIENT
        client=CalculatorClient()

        #PARSE THE EXPRESSION
        operators={"+","-","*","/"}
        while i<len(exp):
            while i<len(exp) and exp[i]==" ":
                i=i+1
            if i<len(exp) and exp[i]=="A":
                currValue="0"
                i=i+1
            while i<len(exp) and exp[i]==" ":
                i=i+1
            if i<len(exp) and exp[i] in operators:
                op=exp[i]
            i=i+1
            while i<len(exp) and exp[i]==" ":
                i=i+1
            if i<len(exp):
                j,b=computeValue(exp[i:])
                i=i+j
                client.invoke(op,b)
            i=i+1
        #print(client.historyInvoke.history)
    print("the answer is: ",currValue)
