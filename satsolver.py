import string
import itertools
print("""
And  ^ , ∧
Or  v, ∨
Not ~ , ¬
Then  >
IFF <>
All Variables have to be 1 Char long
""")

expression = input("please Enter A Currect Expression : ")
expression=expression.replace(' ','')
expression=expression.replace('v','∨')
expression=expression.replace('^','∧')
expression=expression.replace('~','¬')
correctvariablelist=list(string.ascii_lowercase)
correctvariablelist.remove('v')
variablelist=[]
Interpretations=[]
for i in range(len(expression)):
    if(expression[i] in correctvariablelist and expression[i] not in variablelist):
        variablelist.append(expression[i])
Interpretations=[]
for roll in itertools.product([0,1], repeat = len(variablelist)):
    Interpretations.append(roll)


flag=False
for i in range(len(Interpretations)):
    exp = expression
    for j in range(len(variablelist)):
        var=variablelist[j]
        exp=exp.replace(var,str(Interpretations[i][j]))

    while exp != '0' and exp != '1':
        # for T=True or F=False  ... so Your Variable cannot be T or F
        exp = exp.replace('F', '0')
        exp = exp.replace('T', '1')
        # for ¬
        exp = exp.replace('¬(1)', '(0)')
        exp = exp.replace('¬(0)', '(1)')

        while '¬1' in exp or '¬0' in exp:
            exp = exp.replace('¬1', '0')
            exp = exp.replace('¬0', '1')
        # for ∨
        exp = exp.replace('(1∨0)', '(1)')
        exp = exp.replace('(0∨1)', '(1)')
        exp = exp.replace('(1∨1)', '(1)')
        exp = exp.replace('(0∨0)', '(0)')

        # for ∧
        exp = exp.replace('(1∧1)', '(1)')
        exp = exp.replace('(1∧0)', '(0)')
        exp = exp.replace('(0∧1)', '(0)')
        exp = exp.replace('(0∧0)', '(0)')

        # for >
        exp = exp.replace('(1>1)', '(1)')
        exp = exp.replace('(0>1)', '(1)')
        exp = exp.replace('(0>0)', '(1)')
        exp = exp.replace('(1>0)', '(0)')

        # for <>
        exp = exp.replace('(1<>1)', '(1)')
        exp = exp.replace('(0<>0)', '(1)')
        exp = exp.replace('(1<>0)', '(0)')
        exp = exp.replace('(0<>1)', '(0)')

        # Others
        exp = exp.replace('1∨0', '1')
        exp = exp.replace('0∨1', '1')
        exp = exp.replace('1∨1', '1')
        exp = exp.replace('0∨0', '0')
        exp = exp.replace('1∧1', '1')
        exp = exp.replace('1∧0', '0')
        exp = exp.replace('0∧1', '0')
        exp = exp.replace('0∧0', '0')
        exp = exp.replace('1>1', '1')
        exp = exp.replace('0>1', '1')
        exp = exp.replace('0>0', '1')
        exp = exp.replace('1>0', '0')
        exp = exp.replace('1<>1', '1')
        exp = exp.replace('0<>0', '1')
        exp = exp.replace('1<>0', '0')
        exp = exp.replace('0<>1', '0')

        exp = exp.replace('(1)', '1')
        exp = exp.replace('(0)', '0')

    if exp=='1':
        print('This Expression is Satisfiable for : ')
        for k in range(len(variablelist)):
            print(variablelist[k]," : ",Interpretations[i][k])
        flag=True

if flag==False:
    print('This Expression is Not Satisfiable')
