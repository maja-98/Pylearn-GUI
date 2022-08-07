#score viewer,statistics
import time
import shutil
import subprocess
import sys
#from Data.Backup.Path2.Task01 import replace_new
from basic_modules.validater import tc_runner,score_generater
from basic_modules.backup import backupfunc
from basic_modules.database_handler import *
from basic_modules.navigation import *
from basic_modules.login import login
from Data.sample_tc import data as sample_tc
from Data.sample_op import data as sample_op
from Data.submit_tc import data as submit_tc
from Data.submit_op import data as submit_op

#config
notepad_path = r"C:\Program Files (x86)\Notepad++\notepad++.exe"
idle_path = r"C:\Program Files\Python38\Lib\idlelib\idle.bat"

try:
    conn = connect()
    username = login(conn)
    print('Logged in successfully')
    print('---User details---')
    user_details = view_user(conn,username)
    print('Name:',user_details[0][1])
    print('Username:',user_details[0][2])
    print('Rating:',round(user_details[0][4],2))
    path = select_path()
    task = select_task(path)

except KeyboardInterrupt:    
    print('Closing Session...')
    sys.exit()

#username = 'MAJA'
#path = 'Path2'
#task = 'Task02'
def main(username,path,task):
    
    difficulty_dict = {
        'Path1':{
            'Task01':0.2,
            'Task02':0.2,
            'Task03':0.2,
            'Task04':0.2,
            'Task05':0.2,
            'Task06':0.2,
            'Task07':0.4,
            'Task08':0.4,
            'Task09':0.4,
            'Task10':0.4
            },
        'Path2':{
            'Task01':0.4,
            'Task02':0.4,
            'Task03':0.6,
            'Task04':0.6,
            'Task05':0.6,
            'Task06':0.6,
            'Task07':0.6,
            'Task08':0.6,
            'Task09':0.8,
            'Task10':0.8
            },
        'Path3':{
            'Task01':0.8,
            'Task02':0.8,
            'Task03':0.8,
            'Task04':0.8,
            'Task05':1.0,
            'Task06':1.0,
            'Task07':1.0,
            'Task08':1.0,
            'Task09':1.0,
            'Task10':1.0
            }
        }
            
    try:
        while True:
            
            sample_tc_task = sample_tc[path][task]['tc']
            sample_expected_op = sample_op[path][task]
            inbuilt_check = sample_tc[path][task]['inbuilt']
            submit_tc_task = submit_tc[path][task]['tc']
            submit_expected_op = submit_op[path][task]
            func_name = sample_tc[path][task]['func_name']
            difficulty = difficulty_dict[path][task]

                    import sys;sys.exit()
            print('Edit the answer and save and close after completed')
            time.sleep(2)
            subprocess.call([notepad_path, "Data\current_edit.py"])
            tc_runner(conn,username,path,task,sample_tc_task,sample_expected_op,func_name,difficulty,inbuilt_check=inbuilt_check)
            print('WARNING: If you submit with failed cases , It will impact your rating')
            key = input("Press 1 to submit or enter any other key: ")
            if key == '1':
                tc_runner(conn,username,path,task,submit_tc_task,submit_expected_op,func_name,difficulty,submit_fl=1,inbuilt_check=inbuilt_check)
                time.sleep(10)


    except KeyboardInterrupt:
        try:
            quit_fl = input('Press y to quit, for change task press any other key: ').lower()
        
            if quit_fl != 'y':
                path = select_path()
                task = select_task(path)
                main(username,path,task)
            else:
                conn.close()
                print('Session Ended')
        except KeyboardInterrupt:
            print('Session Ended')
main(username,path,task)
    
'''
y
MAJA
1234
2
1
'''
