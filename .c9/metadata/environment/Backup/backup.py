{"changed":true,"filter":false,"title":"backup.py","tooltip":"/Backup/backup.py","value":"#!/usr/bin/python3 \n\nimport sys \nimport os\nimport pathlib\nimport shutil\nfrom datetime import datetime\n\nfrom backupcfg import usage_msg, job_msg, jobs, logfile\nerrors = 0\nmessages = []\ndate_string = datetime.now().strftime(\"%Y%m%d-%H%M%S\")\n\ndef do_backup(job):\n    \n    #adding global verables\n    global errors       \n    global messages\n    global date_string\n    \n    #Setting the src and dst for the backup\n    src = jobs[job][0]  \n    dst = jobs[job][1]\n   \n    #Path for both src and dst validation\n    if not os.path.exists(src):                                             \n        messages.append(\"Source \" + src + \"' does not exist -. FAIL\")\n        errors += 1\n        \n    if not os.path.exists(dst):\n        messages.append(\"Destination \" + src + \"' does not exist -. FAIL\")\n        errors += 1\n    #Check if backup is copying is a file or directory\n    if not errors:\n            \n        src_path = pathlib.PurePath(src)\n        dst_path = dst + \"/\" + src_path.name + \"-\" + date_string\n    \n        is_a_dir = pathlib.Path(src).is_dir()\n        is_a_file = pathlib.Path(src).is_file()\n   \n    #Copys file to dst path and gives either succed or fail message to user\n        if is_a_file:\n            \n            try:\n                shutil.copy(src, dst_path)\n                messages.append(\"Backup file job: \" + job + \" SUCCED\")\n            except Exception as e:\n                messages.append(\"Backup file job: \" + job + \" FAIL\")\n                errors += 1\n    \n    #Copys dir to dst path and gives either succed or fail message to user            \n        elif is_a_dir:\n            \n            try:\n                shutil.copy(src, dst_path)\n                messages.append(\"Backup file job: \" + job + \" SUCCED\")\n            except Exception as e:\n                messages.append(\"Backup file job: \" + job + \" FAIL\")\n                errors += 1\n            \n#Write and or create a logfile\ndef do_logfile(job):\n    \n    global messages\n    global date_string\n    global logfile\n    \n    file = open(logfile, \"a\") #\"a\" to create logfile if not already created\n    \n    for msg in messages:\n        \n        log_message = date_string + \" \" + job + \" \" + msg + \"\\n\"\n        file.write(log_message)\n        \n    file.close()\n\n#main program\nusage_msg = \"Usage: backup.py\"\n\nif len(sys.argv) != 2: \n    \n    print(usage_msg)\n\nelse:\n    \n    job = sys.argv[1]\n    \n    if job not in jobs:\n        \n        print(job_msg % (job))\n        \n    else: \n        \n        do_backup(job)\n    \n        if errors: \n            \n            pass #do_email(job)\n        \n        do_logfile(job)\n    \nsys.exit(0)","undoManager":{"mark":96,"position":100,"stack":[[{"start":{"row":35,"column":33},"end":{"row":35,"column":36},"action":"remove","lines":["src"],"id":8},{"start":{"row":35,"column":33},"end":{"row":35,"column":41},"action":"insert","lines":["src_path"]}],[{"start":{"row":35,"column":41},"end":{"row":35,"column":42},"action":"insert","lines":["."],"id":9},{"start":{"row":35,"column":42},"end":{"row":35,"column":43},"action":"insert","lines":["n"]},{"start":{"row":35,"column":43},"end":{"row":35,"column":44},"action":"insert","lines":["a"]},{"start":{"row":35,"column":44},"end":{"row":35,"column":45},"action":"insert","lines":["m"]},{"start":{"row":35,"column":45},"end":{"row":35,"column":46},"action":"insert","lines":["e"]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["e"],"id":11}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"remove","lines":["e"],"id":12},{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"remove","lines":["a"]}],[{"start":{"row":10,"column":3},"end":{"row":10,"column":4},"action":"insert","lines":["e"],"id":13}],[{"start":{"row":35,"column":58},"end":{"row":35,"column":59},"action":"remove","lines":["a"],"id":14}],[{"start":{"row":35,"column":58},"end":{"row":35,"column":59},"action":"insert","lines":["e"],"id":15}],[{"start":{"row":35,"column":55},"end":{"row":35,"column":66},"action":"remove","lines":["date_string"],"id":16},{"start":{"row":35,"column":55},"end":{"row":35,"column":66},"action":"insert","lines":["date_string"]}],[{"start":{"row":35,"column":33},"end":{"row":35,"column":34},"action":"insert","lines":["="],"id":17}],[{"start":{"row":35,"column":34},"end":{"row":35,"column":35},"action":"insert","lines":[" "],"id":18}],[{"start":{"row":35,"column":34},"end":{"row":35,"column":35},"action":"remove","lines":[" "],"id":19},{"start":{"row":35,"column":33},"end":{"row":35,"column":34},"action":"remove","lines":["="]}],[{"start":{"row":35,"column":33},"end":{"row":35,"column":34},"action":"insert","lines":["+"],"id":20}],[{"start":{"row":35,"column":34},"end":{"row":35,"column":35},"action":"insert","lines":[" "],"id":21}],[{"start":{"row":37,"column":8},"end":{"row":37,"column":12},"action":"insert","lines":["    "],"id":22}],[{"start":{"row":38,"column":8},"end":{"row":38,"column":12},"action":"insert","lines":["    "],"id":23}],[{"start":{"row":34,"column":8},"end":{"row":34,"column":12},"action":"remove","lines":["    "],"id":24}],[{"start":{"row":35,"column":8},"end":{"row":35,"column":12},"action":"remove","lines":["    "],"id":25}],[{"start":{"row":37,"column":8},"end":{"row":37,"column":12},"action":"remove","lines":["    "],"id":26}],[{"start":{"row":38,"column":8},"end":{"row":38,"column":12},"action":"remove","lines":["    "],"id":27}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":8},"action":"insert","lines":["    "],"id":28}],[{"start":{"row":46,"column":28},"end":{"row":46,"column":29},"action":"remove","lines":[","],"id":29}],[{"start":{"row":46,"column":18},"end":{"row":46,"column":19},"action":"insert","lines":[":"],"id":30}],[{"start":{"row":46,"column":31},"end":{"row":46,"column":32},"action":"remove","lines":[":"],"id":31}],[{"start":{"row":46,"column":31},"end":{"row":46,"column":32},"action":"insert","lines":[":"],"id":32}],[{"start":{"row":46,"column":18},"end":{"row":46,"column":19},"action":"remove","lines":[":"],"id":33}],[{"start":{"row":46,"column":29},"end":{"row":46,"column":30},"action":"insert","lines":["a"],"id":34},{"start":{"row":46,"column":30},"end":{"row":46,"column":31},"action":"insert","lines":["s"]}],[{"start":{"row":46,"column":31},"end":{"row":46,"column":32},"action":"insert","lines":[" "],"id":35}],[{"start":{"row":56,"column":29},"end":{"row":56,"column":30},"action":"remove","lines":[" "],"id":36},{"start":{"row":56,"column":28},"end":{"row":56,"column":29},"action":"remove","lines":[","]}],[{"start":{"row":56,"column":28},"end":{"row":56,"column":29},"action":"insert","lines":[" "],"id":37},{"start":{"row":56,"column":29},"end":{"row":56,"column":30},"action":"insert","lines":["a"]},{"start":{"row":56,"column":30},"end":{"row":56,"column":31},"action":"insert","lines":["s"]}],[{"start":{"row":56,"column":31},"end":{"row":56,"column":32},"action":"insert","lines":[" "],"id":38}],[{"start":{"row":70,"column":46},"end":{"row":70,"column":47},"action":"insert","lines":["="],"id":39}],[{"start":{"row":70,"column":47},"end":{"row":70,"column":48},"action":"insert","lines":[" "],"id":40}],[{"start":{"row":70,"column":47},"end":{"row":70,"column":48},"action":"remove","lines":[" "],"id":41},{"start":{"row":70,"column":46},"end":{"row":70,"column":47},"action":"remove","lines":["="]}],[{"start":{"row":70,"column":46},"end":{"row":70,"column":47},"action":"insert","lines":["+"],"id":42}],[{"start":{"row":70,"column":47},"end":{"row":70,"column":48},"action":"insert","lines":[" "],"id":43}],[{"start":{"row":70,"column":58},"end":{"row":70,"column":59},"action":"insert","lines":["+"],"id":44}],[{"start":{"row":70,"column":59},"end":{"row":70,"column":60},"action":"insert","lines":[" "],"id":45}],[{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"insert","lines":[","],"id":46}],[{"start":{"row":7,"column":52},"end":{"row":7,"column":53},"action":"insert","lines":[" "],"id":47}],[{"start":{"row":7,"column":53},"end":{"row":7,"column":54},"action":"insert","lines":["l"],"id":48},{"start":{"row":7,"column":54},"end":{"row":7,"column":55},"action":"insert","lines":["o"]},{"start":{"row":7,"column":55},"end":{"row":7,"column":56},"action":"insert","lines":["g"]},{"start":{"row":7,"column":56},"end":{"row":7,"column":57},"action":"insert","lines":["f"]},{"start":{"row":7,"column":57},"end":{"row":7,"column":58},"action":"insert","lines":["i"]},{"start":{"row":7,"column":58},"end":{"row":7,"column":59},"action":"insert","lines":["l"]},{"start":{"row":7,"column":59},"end":{"row":7,"column":60},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":59},"end":{"row":7,"column":60},"action":"remove","lines":["e"],"id":49},{"start":{"row":7,"column":58},"end":{"row":7,"column":59},"action":"remove","lines":["l"]}],[{"start":{"row":7,"column":58},"end":{"row":7,"column":59},"action":"insert","lines":["l"],"id":50},{"start":{"row":7,"column":59},"end":{"row":7,"column":60},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":48},"end":{"row":7,"column":51},"action":"remove","lines":["log"],"id":51}],[{"start":{"row":7,"column":48},"end":{"row":7,"column":50},"action":"remove","lines":[", "],"id":52}],[{"start":{"row":64,"column":22},"end":{"row":65,"column":0},"action":"insert","lines":["",""],"id":53},{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"insert","lines":["    "]},{"start":{"row":65,"column":4},"end":{"row":65,"column":5},"action":"insert","lines":["g"]},{"start":{"row":65,"column":5},"end":{"row":65,"column":6},"action":"insert","lines":["l"]},{"start":{"row":65,"column":6},"end":{"row":65,"column":7},"action":"insert","lines":["o"]}],[{"start":{"row":65,"column":7},"end":{"row":65,"column":8},"action":"insert","lines":["b"],"id":54},{"start":{"row":65,"column":8},"end":{"row":65,"column":9},"action":"insert","lines":["a"]},{"start":{"row":65,"column":9},"end":{"row":65,"column":10},"action":"insert","lines":["l"]}],[{"start":{"row":65,"column":10},"end":{"row":65,"column":11},"action":"insert","lines":[" "],"id":55},{"start":{"row":65,"column":11},"end":{"row":65,"column":12},"action":"insert","lines":["l"]},{"start":{"row":65,"column":12},"end":{"row":65,"column":13},"action":"insert","lines":["o"]},{"start":{"row":65,"column":13},"end":{"row":65,"column":14},"action":"insert","lines":["g"]},{"start":{"row":65,"column":14},"end":{"row":65,"column":15},"action":"insert","lines":["f"]}],[{"start":{"row":65,"column":15},"end":{"row":65,"column":16},"action":"insert","lines":["i"],"id":56},{"start":{"row":65,"column":16},"end":{"row":65,"column":17},"action":"insert","lines":["l"]},{"start":{"row":65,"column":17},"end":{"row":65,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":13},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":58},{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["i"]},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["m"]},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["p"]},{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":["o"]},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["r"]},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":[" "],"id":59},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["p"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["a"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["t"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["h"]}],[{"start":{"row":6,"column":7},"end":{"row":6,"column":11},"action":"remove","lines":["path"],"id":60},{"start":{"row":6,"column":7},"end":{"row":6,"column":14},"action":"insert","lines":["pathlib"]}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":14},"action":"remove","lines":["lib"],"id":61},{"start":{"row":6,"column":0},"end":{"row":6,"column":3},"action":"insert","lines":["lib"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":14},"action":"remove","lines":["libimport path"],"id":62},{"start":{"row":5,"column":13},"end":{"row":6,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":37,"column":34},"end":{"row":37,"column":35},"action":"remove","lines":["r"],"id":63}],[{"start":{"row":37,"column":34},"end":{"row":37,"column":35},"action":"insert","lines":["r"],"id":64}],[{"start":{"row":37,"column":34},"end":{"row":37,"column":35},"action":"remove","lines":["r"],"id":65},{"start":{"row":37,"column":33},"end":{"row":37,"column":34},"action":"remove","lines":["c"]}],[{"start":{"row":37,"column":33},"end":{"row":37,"column":34},"action":"insert","lines":["r"],"id":66},{"start":{"row":37,"column":34},"end":{"row":37,"column":35},"action":"insert","lines":["c"]}],[{"start":{"row":37,"column":32},"end":{"row":37,"column":35},"action":"remove","lines":["src"],"id":67},{"start":{"row":37,"column":32},"end":{"row":37,"column":35},"action":"insert","lines":["src"]}],[{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"remove","lines":["r"],"id":68},{"start":{"row":38,"column":34},"end":{"row":38,"column":35},"action":"remove","lines":["c"]}],[{"start":{"row":38,"column":34},"end":{"row":38,"column":35},"action":"insert","lines":["r"],"id":69},{"start":{"row":38,"column":35},"end":{"row":38,"column":36},"action":"insert","lines":["c"]}],[{"start":{"row":38,"column":33},"end":{"row":38,"column":36},"action":"remove","lines":["src"],"id":70},{"start":{"row":38,"column":33},"end":{"row":38,"column":36},"action":"insert","lines":["src"]}],[{"start":{"row":34,"column":23},"end":{"row":34,"column":24},"action":"insert","lines":["l"],"id":71},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"insert","lines":["i"]},{"start":{"row":34,"column":25},"end":{"row":34,"column":26},"action":"insert","lines":["b"]}],[{"start":{"row":34,"column":19},"end":{"row":34,"column":26},"action":"remove","lines":["pathlib"],"id":72},{"start":{"row":34,"column":19},"end":{"row":34,"column":26},"action":"insert","lines":["pathlib"]}],[{"start":{"row":5,"column":13},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":73},{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["i"]},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["m"]}],[{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"remove","lines":["m"],"id":74},{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"remove","lines":["i"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["i"],"id":75},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["m"]},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["p"]},{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":["o"]},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["r"]},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":[" "],"id":76},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["d"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["a"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["t"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":7},"end":{"row":6,"column":11},"action":"remove","lines":["date"],"id":77},{"start":{"row":6,"column":7},"end":{"row":6,"column":15},"action":"insert","lines":["datetime"]}],[{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["f"],"id":78},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["r"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["o"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["m"]}],[{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"remove","lines":["m"],"id":79},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"remove","lines":["o"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"remove","lines":["r"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"remove","lines":["f"]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["f"],"id":80},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["r"]},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["o"]},{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":[" "],"id":81}],[{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["d"],"id":82},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["a"]},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["t"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["e"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["t"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["i"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["m"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":[" "],"id":83}],[{"start":{"row":11,"column":37},"end":{"row":11,"column":38},"action":"remove","lines":["e"],"id":84},{"start":{"row":11,"column":36},"end":{"row":11,"column":37},"action":"remove","lines":["m"]},{"start":{"row":11,"column":35},"end":{"row":11,"column":36},"action":"remove","lines":["i"]},{"start":{"row":11,"column":34},"end":{"row":11,"column":35},"action":"remove","lines":["t"]},{"start":{"row":11,"column":33},"end":{"row":11,"column":34},"action":"remove","lines":["t"]},{"start":{"row":11,"column":32},"end":{"row":11,"column":33},"action":"remove","lines":["f"]},{"start":{"row":11,"column":31},"end":{"row":11,"column":32},"action":"remove","lines":["r"]}],[{"start":{"row":11,"column":31},"end":{"row":11,"column":32},"action":"insert","lines":["r"],"id":85}],[{"start":{"row":11,"column":29},"end":{"row":11,"column":32},"action":"remove","lines":["str"],"id":86},{"start":{"row":11,"column":29},"end":{"row":11,"column":37},"action":"insert","lines":["strftime"]}],[{"start":{"row":11,"column":33},"end":{"row":11,"column":34},"action":"insert","lines":["r"],"id":87},{"start":{"row":11,"column":34},"end":{"row":11,"column":35},"action":"insert","lines":["o"]},{"start":{"row":11,"column":35},"end":{"row":11,"column":36},"action":"insert","lines":["m"]}],[{"start":{"row":11,"column":35},"end":{"row":11,"column":36},"action":"remove","lines":["m"],"id":88},{"start":{"row":11,"column":34},"end":{"row":11,"column":35},"action":"remove","lines":["o"]},{"start":{"row":11,"column":33},"end":{"row":11,"column":34},"action":"remove","lines":["r"]}],[{"start":{"row":11,"column":53},"end":{"row":11,"column":54},"action":"insert","lines":["%"],"id":89}],[{"start":{"row":11,"column":45},"end":{"row":11,"column":46},"action":"remove","lines":["%"],"id":90}],[{"start":{"row":11,"column":52},"end":{"row":11,"column":53},"action":"remove","lines":["%"],"id":91}],[{"start":{"row":56,"column":59},"end":{"row":56,"column":60},"action":"insert","lines":[" "],"id":92}],[{"start":{"row":58,"column":59},"end":{"row":58,"column":60},"action":"insert","lines":[" "],"id":93}],[{"start":{"row":48,"column":59},"end":{"row":48,"column":60},"action":"insert","lines":[" "],"id":94}],[{"start":{"row":46,"column":59},"end":{"row":46,"column":60},"action":"insert","lines":[" "],"id":95}],[{"start":{"row":46,"column":52},"end":{"row":46,"column":53},"action":"insert","lines":["\""],"id":96},{"start":{"row":46,"column":53},"end":{"row":46,"column":54},"action":"insert","lines":["\""]}],[{"start":{"row":46,"column":53},"end":{"row":46,"column":54},"action":"remove","lines":["\""],"id":97},{"start":{"row":46,"column":52},"end":{"row":46,"column":53},"action":"remove","lines":["\""]}],[{"start":{"row":46,"column":48},"end":{"row":46,"column":49},"action":"insert","lines":[" "],"id":98}],[{"start":{"row":48,"column":48},"end":{"row":48,"column":49},"action":"insert","lines":[" "],"id":99}],[{"start":{"row":56,"column":48},"end":{"row":56,"column":49},"action":"insert","lines":[" "],"id":100}],[{"start":{"row":58,"column":48},"end":{"row":58,"column":49},"action":"insert","lines":["s"],"id":101}],[{"start":{"row":58,"column":49},"end":{"row":58,"column":50},"action":"insert","lines":[" "],"id":102}],[{"start":{"row":58,"column":49},"end":{"row":58,"column":50},"action":"remove","lines":[" "],"id":103},{"start":{"row":58,"column":48},"end":{"row":58,"column":49},"action":"remove","lines":["s"]}],[{"start":{"row":58,"column":48},"end":{"row":58,"column":49},"action":"insert","lines":["s"],"id":104}],[{"start":{"row":58,"column":48},"end":{"row":58,"column":49},"action":"remove","lines":["s"],"id":105}],[{"start":{"row":58,"column":48},"end":{"row":58,"column":49},"action":"insert","lines":[" "],"id":106}],[{"start":{"row":46,"column":48},"end":{"row":46,"column":49},"action":"insert","lines":[":"],"id":107}],[{"start":{"row":48,"column":48},"end":{"row":48,"column":49},"action":"insert","lines":[":"],"id":108}],[{"start":{"row":56,"column":48},"end":{"row":56,"column":49},"action":"insert","lines":[":"],"id":109}],[{"start":{"row":58,"column":48},"end":{"row":58,"column":49},"action":"insert","lines":[":"],"id":110}]]},"ace":{"folds":[],"scrolltop":2160,"scrollleft":0,"selection":{"start":{"row":98,"column":17},"end":{"row":98,"column":31},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":76,"state":"start","mode":"ace/mode/python"}},"timestamp":1630920905620}