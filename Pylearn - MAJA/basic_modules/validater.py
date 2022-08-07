import time
import shutil
import os
import importlib
from .database_handler import view_score,add_score,view_user,update_rating
class MalpracticeError(Exception):
    '''If user try to malpractice'''
    pass


def inbuilt_checker(file,task_fl,inbuilt_checks):
    if inbuilt_checks:
        for line in file.splitlines():
            for inbuilt_check in inbuilt_checks:
                if (inbuilt_check in line.strip().split('#')[0]):
                    try:
                        raise MalpracticeError("Tried to use inbuilt function")
                    except Exception as e:
                        task_fl = 0
                        return 4
                        
        
    return task_fl
def score_generater(conn,username,difficulty,correct,incorrect,path,task):
    #difficulty in 0.2,0.4,0.6,0.8,1.0
    
    num_ind = int(task[5:7])-1
    try:
        score_old_list = list(view_score(conn,username,path)[0])
    except:
        score_old_list = [0]*10
    
    score_old = score_old_list[num_ind]
    rating = view_user(conn,username)[0][4]
    #print(score_old)
    score_new = correct *2 +incorrect*(-0.5)
    if score_new>score_old:
        score_old_list[num_ind] = score_new
        #print(score_old_list)
        rating += (difficulty/10)*(score_new-score_old)
        add_score(conn,path,username,score_old_list)
    elif score_new<score_old:
        rating += ((1-difficulty)/10)*(score_new-score_old)
    
    update_rating(conn,path,username,rating)
    #print(view_user(conn,username))
    #print(view_score(conn,username))
    

def tc_runner(conn,username,path,task,input_list,output_list,function,difficulty,submit_fl=0,task_fl = 0,inbuilt_check=''):
    #print(sample_input)
    correct = 0
    incorrect = 0 
    with open('Data/current_edit.py') as edit_file:
        file_lines = edit_file.read()
        function_name_replace = file_lines.replace(function,'func')
        backup_file = open('Data/Backup/'+path+'/'+task+'.py')
        backup_file_lines = (backup_file.read().replace('    ','\t'))
        backup_file.close()
    if backup_file_lines != file_lines:
        task_fl = 1
    else:
        return 3,'Please Edit the file and try again',[]
    
    task_fl = inbuilt_checker(file_lines,task_fl,inbuilt_check)
    if task_fl==4:
        return 4,'Trying to use inbuilt function',[]
    with open('Data/current_edit.py','w') as edit_file:
        edit_file.write(function_name_replace)
    
    import Data.current_edit  
    importlib.reload(Data.current_edit)
    func = Data.current_edit.func
    result_texts =[]
    if task_fl:
        for i in range(len(input_list)):
            texts =[]
            tc_name = ('TC'+str(i+1).rjust(2,'0'))
            texts.append((tc_name + ' Executing').center(80,'-'))
            success = 0
            start_time = time.time()
            try:
                answer = func(*input_list[i])
                show_answer = str(answer)
                show_output = str(output_list[i])
                if len(show_answer)> 100:
                    show_answer = show_answer[:100]+'...'
                if len(show_output)>100:
                    show_output = show_output[:100]+'...'
            except Exception as e:
                texts.append('Test Case Failed')
                texts.append(str(type(e).__name__)+":"+str(e))
                incorrect += 1
                task_fl = 0
            end_time = time.time()
            if task_fl:
                try:
                    assert  answer == output_list[i]
                    success = 1
                    correct +=1
                    texts.append('Test Case Passed')
                    texts.append('Actual Result for '+tc_name+ ': '+ show_output)
                    texts.append('Your Result for '+tc_name+ ': '+ show_answer)
                except AssertionError:
                    incorrect +=1
                    texts.append('Test Case Failed')
                    texts.append('Actual Result for '+tc_name+ ': '+ show_output)
                    texts.append('Your Result for '+tc_name+ ': '+ show_answer)
                    success = 1

            
                if success == 1:
                    texts.append('Total time taken '+str(round(end_time-start_time,2))+' seconds')
            texts.append((tc_name + ' Completed').center(80,'-'))
            result_texts.append(texts)

        if not os.path.exists('UserData/'+username+'/'+path+'/'):
            os.makedirs('UserData/'+username+'/'+path+'/')
        with open('Data/current_edit.py','w') as edit_file:
            edit_file.write(function_name_replace.replace('func',function))
        shutil.copyfile('Data/current_edit.py','UserData/'+username+'/'+path+'/'+task+'.py')
        if submit_fl:
            
            score_generater(conn,username,difficulty,correct,incorrect,path,task)
            #enter code to save the scores in the database
        return 2,'Success',result_texts
            
            
        
