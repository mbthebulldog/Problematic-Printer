def arithmetic_arranger(problems, answered=False):
    #initialize a return variable
    result = ''
    import re

    #Make a regex to parse the operands and operators from the input
    pattern = re.compile(r"(\S+)\s+(\S)\s(\S+)")
    mo = []
    for problem in problems:
        mo.append(pattern.search(problem).groups())

    #Convert mo to a nested list (insetad of tuples)
    def listit(t):
        return list(map(listit, t)) if isinstance(t, (list, tuple)) else t

    mo = listit(mo)
    #print('problems: ', mo)  #debug
    
    #Error check: too many problems
    if (len(problems) > 5):
      result = "Error: Too many problems."
      return result

    #Error check: too many digits
    for item in mo:
      if (len(item[0]) > 4 or len(item[2]) > 4):
        result = "Error: Numbers cannot be more than four digits."
        return result

   #Error check: only digits
    for item in mo:
      if (re.search(r"\D", item[0]) or re.search(r"\D", item[2])):
        result = "Error: Numbers must only contain digits."
        return result

    #Error check: wrong operator
    for item in mo:
      if (item[1] == '/' or item[1] == '*'):
        result = "Error: Operator must be '+' or '-'."
        return result

    #Calculate and append each problem's answer
    for item in mo:
        if (item[1] == '-'):
            item.append(str(int(item[0]) - int(item[2])))
        if (item[1] == '+'):
            item.append(str(int(item[0]) + int(item[2])))
    #print("answers: ", mo)  #debug

    #Initialize width variable and strings for each line
    width = 0
    line1, line2, line3, line4 = '', '', '', ''

    #Loop through the problems one at a time
    for item in mo:  #set width to the longer operand's length
        if (len(item[0]) > len(item[2])):
            width = len(item[0])
        else:
            width = len(item[2])
        width = width + 2  #make room for the operator

        #build the strings for each line
        line1 = line1 + (str(item[0].rjust(width))) + '    '
        line2 = line2 + (str(item[1], ) + ' ' +
                         str(item[2].rjust(width - 2))) + '    '
        line3 = line3 + '-' * width + '    '
        line4 = line4 + (str(item[3].rjust(width))) + '    '
    #print(line1, line2, line3, sep='\n')  #debug

    #Strip whitespace and add newlines
    line1 = line1.rstrip() + '\n'
    line2 = line2.rstrip() + '\n'
    line3 = line3.rstrip()
    line4 = line4.rstrip()

    #Return formatted problems to be printed by main.py
    result = line1 + line2 + line3

    if (answered == True):  #Print answers only if answered==True
        result = result + '\n' + line4
    
    return result