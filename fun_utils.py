import os
import datetime

command = "df -h"
command = "uptime"
command = "date"
#command = "sysctl hw.memsize" #ram check

print(os.system(command)) #yaha command wo ram ka lega ram, rampar ram check hoga q ki varible ki w\valu change hoti h

#Function
def check_cpu(command): #defining. a function
    print(os.system(command))
check_cpu("df -h") #calling a function

def chek_ram(command):
    print(os.system(command))
chek_ram("sysctl hw.memsize")

def check_date(commad):
    return os.system(command) #return bhi krskate h
check_date("date")

#itne baar fuction define and call krne ki zaroorat nhi h bus ek. baar define kro fucntion
#ko aur call kro

def run_command(command):
    return os.system(command)
run_command("date")
run_command("df -h")
run_command("uptime")



#IMPORTING DATETIME LIBRARY
def show_date():
 return datetime.datetime.today()
show_date() # e kch print nhi kar raha that iss liye usko ek varibale me daalkar define krdiya
today= show_date()
print(today)
