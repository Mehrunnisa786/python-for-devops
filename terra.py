import subprocess
#subprocess- apke system me python ke through command subprocesses run krne deti h aur wait bhi krne deti h

def terraform_run(command):
    subprocess.run(command, shell=True)
    #print(process.stdout.decode())
    #print(process.stderr.decode())

directory = "/Users/mehrunnisa/Documents/Linux/Python/Wanderlust-Mega-Project/terraform"

#command = f"terraform -chdir={directory} init"
#command = f"terraform -chdir={directory} plan"
#command = f"terraform -chdir={directory} apply"
command = f"terraform -chdir={directory} destroy"

terraform_run(command)

# created the id_rsa.pub using this command (chatgpt).   cp ~/.ssh/id_rsa.pub /Users/mehrunnisa/Documents/Linux/Python/Wanderlust-Mega-Project/terraform/



#after running above code we get this command
# terraform -chdir=/Users/mehrunnisa/Documents/Linux/Pyhton/terra-automate/Wanderlust-Mega-Project/terraform init
#terraform_run(command)


    #subprocess python document se likh skte
  #https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://docs.python.org/3/library/subprocess.html&ved=2ahUKEwiK3N7Mh8-TAxUUoa8BHTBfGCYQFnoECBgQAQ&usg=AOvVaw13tAcPYwTJqhVk1hrcVHTt
#"/Users/mehrunnisa/Documents/Linux/Python/Wanderlust-Mega-Project/terraform"

