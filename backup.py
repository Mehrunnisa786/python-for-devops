#Taking backup

import shutil
import datetime
import os

def backup_files(source,destination):
   today = datetime.date.today()
   backup_file_name = os.path.join(destination, f"bckup_{today}.tar.gz")
   shutil.make_archive(backup_file_name.replace("tar.gz", " "),'gztar', source)

source = "/Users/mehrunnisa/Documents/Linux/Pyhton"
destination = "/Users/mehrunnisa/Documents/Linux/Pyhton/backups"

backup_files(source , destination)

   #f -formateed string agar kisis bhi string ke beech vairiable dalan hoto curly braces ke anar daaldo
   #os- os is a library jisme os ke kaam krskte usme ek path daalna h aur usme ek file bun jaaye
