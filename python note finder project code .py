##import os
##import re
##myfile1= open('1introduction.txt',mode ='r')
##myfile2= open('2types of education.txt',mode='r')
##myfile3= open('3history of education.txt',mode='r')
##myfile4= open('4school education.txt',mode='r')
##userinput=input('enter your word:')
##print(myfile1.name)
##print(myfile1.read())
##f1=myfile.readlines()
##for i in myfile1:
##    if userinput in i:
##        print(i)
##for  j in myfile2:
##    if userinput in j:
##        print(j)
##for k in myfile3:
##    if userinput in k:
##        print(k)
##for l in myfile4:
##    if userinput in l:
##        print(l)
##import os
##import re
##os.chdir('C:\Users\lenovo\Desktop\python'):
##  file=os.listdir()
##for in file:
##    if i in file:
##        print(readlines(),readfile=name)

##import re    
##import os 
##
##inst_num = []
##
##f1=os.chdir (r"C:\Users\lenovo\Desktop\python")
##for file in f1("*.txt"):
##    with open (file, 'r') as f: 
##        for line in f:
##            inst = re.compile ('instruction:(\d+)',line)
##            if inst.search(line) is not None:
##                inst_num = inst.search(line).group(1)
##
##import os
##import re
##word=input('enter any word would u like to fine:')
##f1=os.chdir(r'C:\Users\lenovo\Desktop\python')
##for file in f1('*.txt'):
##    with open(file,'r')as f:
##        for i in f:
##            if i in word:
##                print(word,'string exists in file')
####                print('line number',line.index(line))
##                print('line:',line)
##import os
##import re
##path=os.listdir(r'C:\Users\lenovo\Desktop\python')
##words=input('enter the words would you like to fined')
##list=[]
##for  i in path:
##    if words=='*.txt':
##        print(i)
##myfile=open(i,mode='r')
##filename=myfile.name
##line=myfile.readline()
import os
import re
##word_search=input('enter your word would u like to find:')
##
##filelist=os.listdir(r"C:\Users\lenovo\Desktop\python")
##flienamelist=[]
##def funct(a):
##    match=list(re.finditer(r'.txt$',a))
##    if(match!=[]):
##        return True
##    else:
##        return False
##    filenamelist=list(filter(funct,filelist))
##    print('list of files-',filenamelist)
##    for i in filenamelist:
##        myfile=open(i,mode='r')
##        file_name=(myfile.name)
##        list_of_line=[]
##        linenumber=1
##        while True:
##            line=myfile.readline()
##            if not line:
##                break
##            line=line.lower()
##            found=list(re.finditer(text_to_search,line))
##            if(found!=[]):
##                list_of_line.append(linenumber)
##                linenumber +=1
##            if(list_of_line!=[]):
##                print(text_to_search,"is found in",file_name,"at line",list_of_line)
##            else:
##                print("not found in",file_name)
##
##    myfile.close() 
##







import os
import re
word=input("enter a word would you like to find :")
pattern_for_match=word
pattern1=re.compile('(line\d+):')
pattern=re.compile(word)
for i in os.listdir(r'C:\Users\mdmaa\OneDrive\Desktop\saba\python'):
    if i.endswith('.txt'):
        with open(i,mode = 'r')as string:
            match=string.readlines()
##            print(match)
            for file in match:
                    if re.search(pattern_for_match,file):
                        y = re.finditer(pattern_for_match ,file)
                        print(y)
                        for j in y:
                            print(j)
##                    if re.search(pattern1, file):
##                        print(f'find in {i},{y}')










                        #myfile = open('text.txt',mode='r')

##n = re.finditer(word,myfile.read())
##print("The start indices of 'again' in the file are :")
##
##for i in n:
##    print(i.start())
##print('\n')




##|\w\W\D








