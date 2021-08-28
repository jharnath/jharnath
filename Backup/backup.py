#!/usr/bin/python3 

import sys 
import os
import pathlib
import shutil

from backupcfg import usage_msg, job_msg, jobs, log
errors = 0
messages = []
date_string = datetime.now().strfttime("%Y%m%d%-%H%M%S")

def do_backup(job):
    
    #adding global verables
    global errors       
    global messages
    global date_string
    
    #Setting the src and dst for the backup
    src = jobs[job][0]  
    dst = jobs[job][1]
   
    #Path for both src and dst validation
    if not os.path.exists(src):                                             
        messages.append("Source " + src + "' does not exist -. FAIL")
        errors += 1
        
    if not os.path.exists(dst):
        messages.append("Destination " + src + "' does not exist -. FAIL")
        errors += 1
    #Check if backup is copying is a file or directory
    if not errors:
            
            src_path = path.PurePath(src)
            dst_path = dst + "/" src_path.name + "-" + date_string
    
        is_a_dir = pathlib.Path(scr).is_dir()
        is_a_file = pathlib.Path(scr).is_file()
   
    #Copys file to dst path and gives either succed or fail message to user
        if is_a_file:
            
            try:
                shutil.copy(src, dst_path)
                messages.append("Backup file job" + job + "SUCCED")
            except Exception, e:
                messages.append("Backup file job" + job + "FAIL")
                errors += 1
    
    #Copys dir to dst path and gives either succed or fail message to user            
    elif is_a_dir:
            
            try:
                shutil.copy(src, dst_path)
                messages.append("Backup file job" + job + "SUCCED")
            except Exception, e:
                messages.append("Backup file job" + job + "FAIL")
                errors += 1
            
#Write and or create a logfile
def do_logfile(job):
    
    global messages
    global date_string
    
    file = open(logfile, "a") #"a" to create logfile if not already created
    
    for msg in messages:
        
        log_message = date_string + " " + job " " + msg "\n"
        file.write(log_message)
        
    file.close()

#main program
usage_msg = "Usage: backup.py"

if len(sys.argv) != 2: 
    
    print(usage_msg)

else:
    
    job = sys.argv[1]
    
    if job not in jobs:
        
        print(job_msg % (job))
        
    else: 
        
        do_backup(job)
    
        if errors: 
            
            pass #do_email(job)
        
        do_logfile(job)
    
sys.exit(0)