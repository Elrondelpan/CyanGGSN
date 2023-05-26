import csv

def genEntry():
    archivof= open("FinalGGSN.txt","w")
    entrada=100
    with open ('WhatsApp_IPLOV_202305.csv') as archivo:
        reader =csv.reader(archivo, delimiter='|')        
        for fila in archivo:
            entrada=str(entrada)
            archivof.write("entry ")
            archivof.write(entrada+"\n")
            archivof.write("shutdown\n") 
            archivof.write("no entry ")
            archivof.write(entrada+"\n")
            archivof.write("exit\n")
            entrada=int(entrada)
            entrada=entrada+1
        """entrada=str(entrada)
        archivof.write("entry ")
        archivof.write(entrada+"\n")
        archivof.write("shutdown\n") 
        archivof.write("no entry ")
        archivof.write(entrada+"\n")
        archivof.write("exit\n")
        entrada=int(entrada)"""
    pass

def genNewIp():
    entrada=100
    lineas=0
    lineas=lineas+100
    archivof= open("FinalGGSN.txt","a")
    with open ('WhatsApp_IPLOV_202305.csv') as archivo:
        for row in archivo:
            lineas+=1
            ip=row
            entrada=str(entrada)
            ip=str(ip)
            i=ip.replace('|','')
            archivof.write("entry "+entrada+" create\n")
            archivof.write('description "lovwhatsapp ip 202305"\n')
            archivof.write("server-address eq "+i)
            archivof.write("application ""lovwhatsapp""\n")
            archivof.write("no shutdown\n")
            archivof.write("exit\n")
            entrada=int(entrada)
            entrada+=1

        """archivof.write("entry "+entrada+" create\n")
        archivof.write('description "lovwhatsapp ip 202305"\n')
        archivof.write("server-address eq "+ip)
        archivof.write("application ""lovwhatsapp""\n")
        archivof.write("no shutdown\n")
        archivof.write("exit\n")
        archivof.write("exit\n")
        archivof.write("commit\n")
        archivof.write("exit all\n")
        archivof.write("admin save\n")"""
    pass    
genEntry()
genNewIp()