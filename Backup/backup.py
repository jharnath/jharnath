#!/usr/bin/python3 

import sys 
import os
import pathlib
import shutil

from backupcfg import usage_msg, job_msg, jobs
errors = 0
messages = []
data_string = datetime.now().strfttime("%Y%m%d%-%H%M%S")

def do_backup(job)
    global errors
    global messages
    global date_string
    
    src = jobs[job][0]
    dst = jobs[job][1]
    
    if not os.path.exists(src):
        messages.append("Source " + src + "' does not exist -. FAIL")
        errors += 1
        
    if not os.path.exists(dst):
        messages.append("Destination " + src + "' does not exist -. FAIL")
        errors += 1

    if not errors:
            
            src_path = path.PurePath(src)
            dst_path = dst + "/" src_path.name + "-" + data_string
    
        is_a_dir = pathlib.Path(scr).is_dir()
        is_a_file = pathlib.Path(scr).is_file()
        
        if is_a_file:
            
            try:
                shutil.copy(src, dst_path)
                messages.append("Backup file job" + job + "SUCCED")
            except Exception, e:
                messages.append("Backup file job" + job + "FAIL")
                errors += 1
                
    elif is_a_dir:
            
            try:
                shutil.copy(src, dst_path)
                messages.append("Backup file job" + job + "SUCCED")
            except Exception, e:
                messages.append("Backup file job" + job + "FAIL")
                errors += 1

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
        
        pass #do_logfile(job)
    
sys.exit(0)