import re
sheik = list()
with open('/home/ubuntu/kaushik.txt', 'r') as ismail:
    for sh in ismail:
        shake = (re.sub('[0-9]+.', "", sh))
        sheik.append(shake.strip())
with open('/home/ubuntu/Downloads/commands.txt','r') as kaushik,  open('/home/ubuntu/Downloads/linux_commands.txt','r') as yesh:
    k = set(i.strip() for i in kaushik)
    y = set(k.strip() for k in yesh)
    # print(k)
    # print(y)
    z = y-k
    final = z-set(sheik)
    print(final)
    with open('/home/ubuntu/missing_commands.txt','w') as yesh:
        for all in final:
            yup = '\n' + all
            yesh.write(yup)




#print(set(sheik))

