jobs = {"job1": ['/home/ec2-user/enviroment/LogsAndFile/file1','/home/ec2-user/enviroment/LogsAndFile/Backup'],
        "job2": ['/home/ec2-user/enviroment/LogsAndFile/file2','/home/ec2-user/enviroment/LogsAndFile/Backup'],
        "job3": ['/home/ec2-user/enviroment/LogsAndFile/file3','/home/ec2-user/enviroment/LogsAndFile/Backup'],
        "job4": ['/home/ec2-user/enviroment/LogsAndFile/dir1','/home/ec2-user/enviroment/LogsAndFile/Backup'],
        "job5": ['/home/ec2-user/enviroment/LogsAndFile/dir1','/home/ec2-user/enviroment/LogsAndFile/Backup1']}
        
usage_msg = "Usage: python backup.py <job name from backupcfg.py>"
job_msg = "Error: job '%s' not in jobs list"
logfile = "/home/ec2-user/enviroment/LogsAndFile/backup.log"

