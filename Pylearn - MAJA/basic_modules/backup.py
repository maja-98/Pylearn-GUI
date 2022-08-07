import os
import shutil
def backupfunc(username):
    print('Enter the path and file to reset')
    paths = ['Path1','Path2','Path3']
    task_range = list(range(1,11))
    print('Select Path')
    
    for num,val in enumerate(paths):
        print(num+1,':',val)
    print('Enter all to reset all')
    print('Enter 0 to quit')
    path_ind = input('Enter the value: ').lower()
    print('Select Tasks')
    for num in task_range:
        print(num,':','Task'+str(num).rjust(2,'0'))
    print('Enter all to reset all')
    print('Enter 0 to quit')
    taskfile = input('Enter Value: ').lower()
    confirm = input('You are about to reset files, press y to confirm: ')

    initial_load(username,path_ind=path,taskfile=taskfile,confirm=confirm,initial=0)

def initial_load(username,path_ind='all',taskfile='all',confirm='y',initial=1):
    paths = ['Path1','Path2','Path3']
    task_range = list(range(1,11))
    try:      
        if path_ind == 'all':
            pass
        elif path_ind == '0':
            return
        else:
            paths= paths[int(path_ind)-1]            
            if taskfile == 'all':
                pass
            elif taskfile == '0':
                return
            else:
                try:
                    taskfile = int(taskfile)
                    task_range= [taskfile]
                except:
                    print('Invalid Key,Please try again')
                    return backupfunc()                
    except Exception as e:
        print(e)
        print('Invalid Key,Please try again')
        return backupfunc()        
    
    if confirm == 'y':
        for path in paths:
            if not os.path.exists('UserData/'+username+'/'+path+'/'):
                os.makedirs('UserData/'+username+'/'+path+'/')
            path_val = 'Data/Backup/'+path
            files = os.listdir(path_val)
            for file in files:
                if 'Task' in file :
                    #print(file[-5:-3])
                    if int(file[-5:-3]) in  task_range:
                        shutil.copyfile(path_val+'/'+file,'UserData/'+username+'/'+path+'/'+file)
                        if not initial:
                            print(file+' in '+path+' Successfully reset')
    else:
        return 
def load_file(username):
    paths = ['Path1','Path2','Path3']
    for path in paths:
        path_val = 'UserData/'+username+'/'+path+'/'
        if os.path.exists(path_val):
            files = os.listdir(path_val)
            for file in files:
                shutil.copyfile(path_val+file,'Data/'+path+'/'+file)
    
def save_file(file):
    if not os.path.exists("Saved_Files"):
        os.mkdir("Saved_Files")
    path,task = file.split('/')
    file_name = "Saved_Files/"+path[0]+path[-1]+task[0]+task.replace('.py','')[-1]
    files = os.listdir("Saved_Files")
    if file_name.split('/')[-1]+'00.py' in files:
        print(list(filter(lambda x: file_name.split('/')[-1] in x,files)))
        files_max_num = max(list(map(lambda x: int(x.replace('.py','')[-2::]),filter(lambda x: file_name.split('/')[-1] in x,files))))+1
    else:
        files_max_num = 0
    file_name= file_name + str(files_max_num).rjust(2,'0')+'.py'
    #print(files_max_num)
    shutil.copyfile(file,file_name)
    return file_name

