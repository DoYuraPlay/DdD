log=input("Ведите логин:     ")
par=input("Ведите пароль:     ")
if log=="Nagibator":
    print("    ")
    if par=="q111":
        print("Добро пожаловать",log,"!")
        print("      ")
        yu=open("Yura pragrama.txt","r", encoding='UTF-8')
        inta=yu.readline()
        int2=yu.readline()
        print(inta)
        print(int2)
        yu.close()
elif log !="Nagibator":
    print("    ")
    if par =="q111":
        print("Логин не верен")
if log =="Nagibator":
    print("    ")
    if par !="q111":
        print("Пароль не верен")
elif log !="Nagibator":
    print("    ")
    if par !="q111":
        print("Логин и пароль не верен")
