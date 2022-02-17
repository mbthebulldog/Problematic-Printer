#def arithmetic_arranger(problems, answered=False):
problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "24 - 34", "223 + 3"]
answered = True
#Remove line above this when pasting into replit
import re

#Make a regex to parse the operands and operators from the input
pattern = re.compile(r"(\d+)\s+([-\+])\s(\d+)")
mo = []
for problem in problems:
    mo.append(pattern.search(problem).groups())
print(len(mo))

#Convert mo to a nested list (insetad of tuples)
def listit(t):
    return list(map(listit, t)) if isinstance(t, (list, tuple)) else t
mo = listit(mo)
print('problems: ', mo) #debug

#Calculate and append each problem's answer
for item in mo:
    if (item[1] == '-'):
        item.append(str(int(item[0]) - int(item[2])))
    if (item[1] == '+'):
        item.append(str(int(item[0]) + int(item[2])))
print("answers: ", mo) #debug

#Initialize width variable and strings for each line
width = 0
line1, line2, line3, line4 = '', '','',''

#Loop through the problems one at a time
for item in mo: #set width to the longer operand's length
    if (len(item[0]) > len(item[2])):
        width = len(item[0])
    else:
        width = len(item[2])
    width = width + 2 #make room for the operator
    
    #build the strings for each line
    line1 = line1 + (str(item[0].rjust(width))) + '    '
    line2 = line2 + (str(item[1],) + ' ' + str(item[2].rjust(width-2))) + '    '
    line3 = line3 + '-'*width + '    '
    line4 = line4 + (str(item[3].rjust(width))) + '    '

print(line1, line2, line3, sep='\n') #debug
if (answered): #Print answers only if answered==True
    print(line4)
    
#TODO: Return errors
if (len(mo) > 5):
      print("Error: Too many problems.")

#TODO: Return formatted problems to be printed by main.py