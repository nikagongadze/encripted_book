import string
import random
import pyfiglet
import os
import time

letters=string.ascii_lowercase+" "+","+"."+"?"+"!"+"1"+'2'+'3'+'4'+'5'+'6'+\
        '7'+'8'+'9'+'0'+'/'+'('+')'+'['+']'+'@'+'#'\
        +'$'+'^'+'&'+'*'+'-'+'_'+'+'+'='+':'+";"+"|"+'<'+'>'

start=pyfiglet.figlet_format('encripted    notes')
for g in start:
    print(g,end='',flush=True)
    time.sleep(0.002)
User_input=str(input('which do you want , decrypt or encrypt file ?! | type d/e :   '))
os.system('clear')
if User_input=='e' or User_input == 'encrypt':
    Sec_inp=str(input("make new note or continue with exiting note | type n/e"))

    if Sec_inp=="n" or Sec_inp=="new":
        def Encrypt(string):
            num_lst = []
            sec_lst = []
            real = []
            count = 0
            in_txt = ""
            for i in range(len(string)):
                randoms = random.randint(1, 31)
                num_lst.append(randoms)

            for j in string:
                res = letters.index(j)
                real.append(res)
                finres = num_lst[count] + res
                count += 1
                sec_lst.append(finres)

            for k in sec_lst:
                try:
                    in_txt = in_txt + letters[k]
                except:
                    continue

            with open('encript.txt', 'w') as f:
                f.write(str(sec_lst))

            with open('index.txt', 'w') as d:
                d.write(str(num_lst))
            return 'done , you should not delete any folder in this directory , otherwise your decripted or encripded files will be lost'


        sttr = str(input("enter text which you want to will be encripted:  "))
        os.system('clear')
        print(Encrypt(sttr.lower()))
    elif Sec_inp=="e" or Sec_inp=="exiting":
        def Continue(string):
            num_lst = []
            sec_lst = []
            real = []
            count = 0
            in_txt = ""
            lst1=[]
            lst11=[]
            for i in range(len(string)):
                randoms = random.randint(1, 31)
                num_lst.append(randoms)

            for j in string:
                res = letters.index(j)
                real.append(res)
                finres = num_lst[count] + res
                count += 1
                sec_lst.append(finres)

            for k in sec_lst:
                try:
                    in_txt = in_txt + letters[k]
                except:
                    continue

            with open('encript.txt', 'r') as f:
                res = f.readline()

            join1 = res.replace("[", '').replace("]", "")
            result = join1.split(',')

            for i in result:
                lst1.append(int(i))

            for_apppend = lst1 + sec_lst

            with open('encript.txt', 'w') as d:
                d.write(str(for_apppend))

            with open('index.txt', 'r') as d:
                res2 = d.readline()

            join11 = res2.replace("[", '').replace("]", "")
            result11 = join11.split(',')

            for i in result11:
                lst11.append(int(i))


            for_apppend1 = lst11 + num_lst

            with open('index.txt', 'w') as d:
                d.write(str(for_apppend1))

            return 'done , you should not delete any folder in this directory , otherwise your decripted or encripded files will be lost'

        sttr = str(input("enter text which you want to will be encripted:  "))
        os.system('clear')
        print(Continue(" "+sttr.lower()))



elif User_input=='d' or User_input=='decript':

    def Decript(x, y):
        usr_in = input(
            "the file which you 'ENCRYPT' many times ago will be decripted  --| click enter for continue")
        os.system('clear')
        count1 = 0
        lst1 = []
        lst12 = []
        fin_str = ""

        correct = x.replace(']', '').replace('[', '')
        result1 = correct.split(',')

        correct1 = y.replace(']', '').replace('[', '')
        result2 = correct1.split(',')

        for i in list(result1):
            lst1.append(int(i))

        for j in list(result2):
            lst12.append(int(j))

        for i in lst1:
            rng = i - lst12[count1]
            count1 += 1
            fin_str = fin_str + letters[rng]
        Input_user=str(input('do you want to save decripted file in txt file or see it in cmd? cmd or txt : '))
        if Input_user=='txt' or Input_user=='t' or Input_user=='T':
            Input_user1=str(input("enter name for txt file : "))
            with open(Input_user1+".txt",'w') as p:
                p.write(fin_str)
                p.close()
                return 'done'
        elif Input_user=='cmd' or Input_user=='c' or Input_user=='C':
            return "\n" + 'decripted file :  ' + "\n" +"\n"+ fin_str
        else:
            return 'invalid input'

    try:
        with open('encript.txt') as f:
            res = f.readline()

    except:
        print("error : encript.txt is missing or you havn't made it ")
    try:
        with open('index.txt', 'r') as d:
            res1 = d.readline()

    except:
        print("error : index.txt is missing or you havn't made it ")
    try:
        print(Decript(res, res1))
    except:
        pass




