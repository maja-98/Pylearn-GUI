import os
def select_path(dim=80):
    paths = ['Path1','Path2','Path3']
    print('-'*dim)
    print(' SELCET PATH '.center(dim))
    print('-'*dim)
    for i in range(len(paths)):
        print (str(i+1).rjust(2,'0'),':',paths[i])
    print('-'*dim)
    path = paths[int(input('Enter the number: '))-1]
    print('-'*dim)
    return path
def select_task(path,dim=80):
    tasks = sorted(filter(lambda x: x[7:9]=='py',os.listdir('Data/Backup/'+path)))
    #tasks = ['TASK01','TASK02','TASK03','TASK04','TASK05','TASK06','TASK07','TASK08','TASK09','TASK10']
    print('-'*dim)
    print(' SELCET TASK '.center(dim))
    print('-'*dim)
    for i in range(len(tasks)):
        print (str(i+1).rjust(2,'0'),':',tasks[i])
    print('-'*dim)
    task = tasks[int(input('Enter the number: '))-1]
    print('-'*dim)
    return task.title()[:6]
