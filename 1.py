file = "./input.txt"
stack = []
num = []
operation = ''
with open(file) as fileHandler:
    fileRead = fileHandler.read()
    summer = 0
    for r in fileRead:
         c = r.strip()
         if(c == ''):
              suming = 0
              for i in range(0,len(num)):
                  suming += int(num[i]) * 10 ** (len(num) - i - 1)
              if(operation == '+'): summer += suming
              if(operation == '-'): summer -= suming
              num = []
         elif(c == '+'): operation = '+'
         elif(c == '-'): operation = '-'
         elif( int(c) >= 0 and int(c) <= 9 ):
             num.append(c)
print(summer)


