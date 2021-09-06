jobs = {"job1": ['/home/ec2-user/environment/LogsAndFile/file','/home/ec2-user/environment/LogsAndFile/file2'],
        "job2": ['/home/ec2-user/environment/LogsAndFile/file2','/home/ec2-user/environment/LogsAndFile/Backup'],
        "job3": ['/home/ec2-user/environment/LogsAndFile/file3','/home/ec2-user/environment/LogsAndFile/Backup'],
        "job4": ['/home/ec2-user/environment/LogsAndFile/dir1','/home/ec2-user/environment/LogsAndFile/Backup'],
        "job5": ['/home/ec2-user/environment/LogsAndFile/dir1','/home/ec2-user/environment/LogsAndFile/Backup1']}
        
usage_msg = "Usage: python backup.py <job name from backupcfg.py>"
job_msg = "Error: job '%s' not in jobs list"
logfile = "/home/ec2-user/environment/LogsAndFile/backup.log"

