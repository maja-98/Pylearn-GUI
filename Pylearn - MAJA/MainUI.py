import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget,QDialog,QMessageBox,QComboBox
from PyQt5 import QtCore,QtWidgets
from UI.loginUI import Ui_MainWindow as loginUI
from UI.signupUI import Ui_MainWindow as signupUI
from UI.navigationUI import Ui_MainWindow as navigationUI
from UI.codeEditorUI import Ui_MainWindow as codeEditorUI
from UI.resultUI import Ui_MainWindow as resultUI
import time
import shutil
import subprocess
import sys
#from Data.Backup.Path2.Task01 import replace_new
from basic_modules.validater import tc_runner,score_generater
from basic_modules.backup import backupfunc
from basic_modules.database_handler import *
from Data.sample_tc import data as sample_tc
from Data.sample_op import data as sample_op
from Data.submit_tc import data as submit_tc
from Data.submit_op import data as submit_op
#config
notepad_path = r"C:\Program Files (x86)\Notepad++\notepad++.exe"
idle_path = r"C:\Program Files\Python38\Lib\idlelib\idle.bat"

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("PYLEARN")
        self.setStyleSheet("background-color: #cce7e8;")
        self.setGeometry(0, 0, 800, 600)
        self.loginUI = loginUI()
        self.signupUI = signupUI()
        self.navigationUI = navigationUI()
        self.resultUI =resultUI()
        self.codeEditorUI = codeEditorUI()
        self.conn = connect()
        self.startloginUI()
        self.difficulty_dict = {
            'Path1':{            'Task01':0.2,            'Task02':0.2,            'Task03':0.2,            'Task04':0.2,            'Task05':0.2,
                                 'Task06':0.2,            'Task07':0.4,            'Task08':0.4,            'Task09':0.4,            'Task10':0.4            },
            'Path2':{            'Task01':0.4,            'Task02':0.4,            'Task03':0.6,            'Task04':0.6,            'Task05':0.6,
                                 'Task06':0.6,            'Task07':0.6,            'Task08':0.6,            'Task09':0.8,            'Task10':0.8            },
            'Path3':{            'Task01':0.8,            'Task02':0.8,            'Task03':0.8,            'Task04':0.8,            'Task05':1.0,
                                 'Task06':1.0,            'Task07':1.0,            'Task08':1.0,            'Task09':1.0,            'Task10':1.0            }
            }
    def startloginUI(self):
        self.username = ''
        self.user_rating = 0.0
        self.loginUI.setupUi(self)            
        self.loginUI.login_btn.clicked.connect(lambda :self.login(self.loginUI.username.text(),self.loginUI.password.text()))
        self.loginUI.signup_btn.clicked.connect(self.startsignupUI)
        self.quit_function(self.loginUI)
        self.show()

    def startsignupUI(self):
        self.signupUI.setupUi(self)
        self.quit_function(self.signupUI)
        self.signupUI.create_btn.clicked.connect(lambda : self.create_user(self.signupUI.name.text(),self.signupUI.username.text(),
                                                                                      self.signupUI.password.text()))
        self.signupUI.login_btn.clicked.connect(self.startloginUI)
        self.show()

    def startnavigationUI(self):
        self.user_rating = str(round(view_user(self.conn,self.username)[0][4],2))
        self.navigationUI.setupUi(self)
        self.style_rating(self.navigationUI)
        self.navigationUI.profile.setText(self.username)
        self.navigationUI.rating.setText(self.user_rating+" ★")
        self.select_task(self.navigationUI.path.currentText())
        self.navigationUI.path.currentTextChanged.connect(lambda:self.select_task(self.navigationUI.path.currentText()))
        self.navigationUI.start_btn.clicked.connect(lambda: self.startcodeEditorUI(self.navigationUI.path.currentText(),self.navigationUI.task.currentText()))
        self.signout_function(self.navigationUI)
        self.quit_function(self.navigationUI)
        self.show()
    def startcodeEditorUI(self,path,task):
        self.path = path
        self.task = task
        self.codeEditorUI.setupUi(self)
        self.style_rating(self.codeEditorUI)
        self.codeEditorUI.profile.setText(self.username)
        self.codeEditorUI.rating.setText(str(self.user_rating)+" ★")
        self.codeEditorUI.path_lbl.setText(path)
        self.codeEditorUI.task_lbl.setText(task)
        try:
            shutil.copyfile('UserData/'+self.username+'/'+path+'/'+task+'.py',r'Data/current_edit.py')
        except:
            if os.path.exists('Data/Backup/'+path+'/'+task+'.py'):
                shutil.copyfile('Data/Backup/'+path+'/'+task+'.py',r'Data/current_edit.py')
            else:
                QMessageBox.about(self, "Invalid Task", "Task not Created yet")
        
        with open('Data/current_edit.py') as file:
            lines = file.readlines()
            questions = list((map(lambda x:x.strip('#'),filter(lambda x:x[0]=='#',lines))))
            answer_template = list(map(lambda x:x.replace('    ','\t'),filter(lambda x:x[0]!='#',lines)))
        question=''.join(questions)
        self.codeEditorUI.question.setText(question)
        self.codeEditorUI.code.setTabStopDistance(12)
        
        self.codeEditorUI.code.setPlainText(''.join(answer_template))
        self.codeEditorUI.back_btn.clicked.connect(self.startnavigationUI)
        
        self.codeEditorUI.run_btn.clicked.connect(lambda: self.test_runner(question,self.codeEditorUI.code.toPlainText(),0))
        self.codeEditorUI.submit_btn.clicked.connect(lambda: self.test_runner(question,self.codeEditorUI.code.toPlainText(),1))
        self.signout_function(self.codeEditorUI)
        self.quit_function(self.codeEditorUI)
        self.show()
    def startresultUI(self,submit_fl,output):
        self.user_rating = str(round(view_user(self.conn,self.username)[0][4],2))
        self.resultUI.setupUi(self)
        self.style_rating(self.resultUI)
        self.resultUI.profile.setText(self.username)
        self.resultUI.rating.setText(self.user_rating+" ★")
        self.resultUI.path_lbl.setText(self.path)
        self.resultUI.task_lbl.setText(self.task)
        self.resultUI.results.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #if submit flag is there hide submit button
        if submit_fl:
            self.resultUI.submit_btn.hide()
        else:
            self.resultUI.submit_btn.clicked.connect(lambda: self.test_runner(self.question,self.answer,1))
        i=0
        for i in range(len(output)):
            self.resultUI.result = QtWidgets.QTextBrowser(self.resultUI.scrollAreaWidgetContents)
            self.resultUI.result.setGeometry(QtCore.QRect(21, 10*(10*(i+1))-70, 461, 90))
            self.resultUI.result.setText('\n'.join(output[i]))
            self.resultUI.result.setStyleSheet("background-color:white")
            self.resultUI.result.setObjectName("ans"+str(i))
            
        self.resultUI.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 519, 10*(10*(i+1))+40))
        self.resultUI.back_btn.clicked.connect(lambda: self.startcodeEditorUI(self.path,self.task))
        self.signout_function(self.resultUI)
        self.quit_function(self.resultUI)
        self.show()
    def select_task(self,path):
        tasks = sorted(filter(lambda x: x[7:9]=='py',os.listdir('Data/Backup/'+path)))
        self.navigationUI.task.clear()
        for task in tasks:
            self.navigationUI.task.addItem(task.replace('.py',''))
    def login(self,username,password):
        error_code,self.username = login_user(self.conn,username,password)
        if error_code==4:
            QMessageBox.about(self, "Invalid Credentials", "Password is Wrong")
        elif error_code==5:
            QMessageBox.about(self, "Invalid Login", "You are not a Pylearner, Signup")
        else:
            self.startnavigationUI()

    def create_user(self,name,username,password):
        if view_user(self.conn,username):
            QMessageBox.about(self, "Username already exists", "There is already a pylearner exists with same name")
        else:
            error_code = create_user(self.conn,name,username,password)
            if error_code ==2:
                self.startloginUI()
            else:
                QMessageBox.about(self, "Invalid", "Make sure every required column is filled")        
    def test_runner(self,question,answer,submit_fl):
        self.question = question
        self.answer = answer
        question = ''.join(list(map(lambda x:'#'+x+'\n',question.splitlines())))
        
        with open('Data/current_edit.py','w') as file:
            file.write(question+answer)
        if submit_fl:
            tc_task = submit_tc[self.path][self.task]['tc']
            expected_op = submit_op[self.path][self.task]
        else:
            tc_task = sample_tc[self.path][self.task]['tc']
            expected_op = sample_op[self.path][self.task]
        inbuilt_check = sample_tc[self.path][self.task]['inbuilt']

        func_name = sample_tc[self.path][self.task]['func_name']
        difficulty = self.difficulty_dict[self.path][self.task]

        status_code,message,output =tc_runner(self.conn,self.username,self.path,self.task,tc_task,expected_op,func_name,
                                              difficulty,submit_fl=submit_fl,inbuilt_check=inbuilt_check)
        if status_code in [3,4]:
            QMessageBox.about(self, "Error", message)
        else:
            self.startresultUI(submit_fl,output)

    def quit_function(self,UI):
        UI.menubar.setStyleSheet("background-color:#EAF6F6;font-family:'Berlin Sans FB'")
        UI.actionQuit.triggered.connect(lambda :sys.exit())
    def signout_function(self,UI):

        UI.actionSignOut.triggered.connect(self.startloginUI)
    def style_rating(self,UI):
        UI.profile.setGeometry(QtCore.QRect(424, 30, 100, 25))
        UI.rating.setGeometry(QtCore.QRect(534, 30, 65, 25))
        UI.profile.setStyleSheet("font-family:'Felix Titling';font-size:9pt;font-weight: bold; border-style:solid;border-width:1px;background-color:white;")
        UI.rating.setStyleSheet("font-family:'Felix Titling';font-size:9pt;font-weight: bold; border-style:solid;border-width:1px;background-color:white;")
        UI.profile.setAlignment(QtCore.Qt.AlignCenter)
        UI.rating.setAlignment(QtCore.Qt.AlignCenter)        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
