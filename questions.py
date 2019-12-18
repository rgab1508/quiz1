import os
def cls():
    os.system("cls")
Qs = []

questions = [
   
    {
        "question":"An entire path name, consisting of several sub-directory names can contain upto",
        "options":["13 character","36 character","63 character","53 character","63 character"],
        "answer":2
    },
    {

        "question":"In which year the first operating system was developed",
        "options":["1910","1940","1950","1980","1950"],
        "answer":2
    },
    {
        "question":"MS-DOS developed in",
        "options":["1991","1984","1971","1961","1984"],
        "answer":1
    },
    {
        "question":"Maximum length of DOS command using any optional parameter is",
        "options":["87 characters","127 characters","None of the above","127 characters"],
        "answer":2
    },
	{
        "question":"In which version of DOS. CHKDSK command has been changed to SCANDISK?",
        "options":["6.2","6.0","6.2","6.2"],
        "answer":3

    },
    {
        "question":"CHKDSK command is used to",
        "options":["Diagnose the hard disk error","Report the status of files on disk","All of the above","All of the above"],
        "answer":3
    },
    {
        "question":"Which file is the batch file that is read while booting a computer?",
        "options":["Auto-batch","Autoexecutive.bat","Auto.bat","Autoexec.bat"],
        "answer":0
    }
]
"""
     mainWorking(i,ans,time_taken,time_limit,'b','B',"Which command is used to backup in DOS 6+ Version","BACKUP","MSBACKUP","MSBACKEDUP","All of the above","MSBACKUP");
	
     "Copy and Xcopy are same in the sense","Both are internal command of DOS","Both are external commands of DOS","Both can be used to copy file or group of files","All of the above","Both can be used to copy file or group of files");
	
     mainWorking(i,ans,time_taken,time_limit,'a','A',"Which command is used to clear the screen","Cls","Clear","Clscreen","All of the above","Cls");
	
     "internal command in Dos are","Cls, rd label","Dir, ren, sys","Time, type, dir","Del, disk copy, label","Time, type, dir");
	
     mainWorking(i,ans,time_taken,time_limit,'a','A',"Which command is used to copy files?","Copy","Diskcopy","type","All of the above","copy");
	
     "To copy the hidden system files of DOS to another disk you can use the command","Copy","Ren","Sys","Diskcopy","sys");
	
     mainWorking(i,ans,time_taken,time_limit,'b','B',"Disk copy command in DOS is used to","Copy a file","Copy contents of one floppy disk to another","Copy contents of CD-ROM to another","All of the above","Copy contents of one floppy disk to another");
	
     mainWorking(i,ans,time_taken,time_limit,'a','A',"SYS command is used to","Copy DOS system files to new disk","Copy DOS configuration files to a new disk","Update the DOS system files","None of the above","Copy DOS system files to new disk");
	
     mainWorking(i,ans,time_taken,time_limit,'d','D',"Which command be used to clear display the operating system prompt on the first line of the display?","Cd","Md","Rename","cls","cls");
	
     mainWorking(i,ans,time_taken,time_limit,'b','B',"The command used to copy a file named temp.doc from drive C: to drive A: is","Copy temp.doc to a:","Copy c:temp.doc a:","Copy c: a:","Copy temp a: c:","Copy c:temp.doc a:");
	
     mainWorking(i,ans,time_taken,time_limit,'B','b',"External command in DOS are","Copy, edit, sys, format","Edit, sys, chkdsk","Chkdsk, prompt, date","Sys, ver, vol","Edit, sys, chkdsk");
	
     "Which keys can be pressed quit without saving in DOS","Ctrl + A","Ctrl + B","Ctrl + C","Ctrl + D","Ctrl + C");
	
     mainWorking(i,ans,time_taken,time_limit,'a','A',"Which command is used to get the current date only?","Date","Time","Second","All of the above","Date");
	
     mainWorking(i,ans,time_taken,time_limit,'d','D',"Generally, the DATE is entered in the form","DD-YY-MM","YY-DD-MM","MM-YY-DD","MM-DD-YY","MM-DD-YY");
	
     mainWorking(i,ans,time_taken,time_limit,'a','A',"DEL command is used to","Delete files","Delete directory","Delete labels","Delete contents of file","Delete files");
	
     "Which command be used to ask you to confirm that you want to delete the directory?","Deltree","Deltree/f","Del *.*/p","Erase *.*","Del *.*/p");
	
     "Which statement is correct?","Directories can be kept inside a file","Files can not be kept inside a directory","1 millisec = 10 ^ 3 sec","None of above","1 millisec = 10 ^ 3 sec");
	
     mainWorking(i,ans,time_taken,time_limit,'d','D',"CHKDSK can be used to find","Disks bad portion","Occupied space","Free space","All of above","All of above");
	
     mainWorking(i,ans,time_taken,time_limit,'a','A',"DIR command is used to display","a list of files","contents of files","ype of files","All of above","Display a list of files in a directory");
	
     "The deleted file in MS-DOS can be recovered if you use the command mention below immediately, the command is:","DO NOT DELETE","NO DELETE","UNDELETE","ONDELETE","UNDELETE");
	
     "To copy the file command.com from drive c: to drive a:","Drive c: copy drive a:\command.com","C:A: copy command.com","Copy c:\command.com a:","Both b and c","Copy c:\command.com a:");
	
     mainWorking(i,ans,time_taken,time_limit,'a','A',"While working with MS-DOS which key is used to get the p[revious command used:","F3","F1","F6","F9","F3");
	
     "FAT stands for","File Accomodation Table","File Access Tape","File Allocation Table","File Activity Table","File Allocation Table");
	
     mainWorking(i,ans,time_taken,time_limit,'d','D',"xcopy command can copy","individual files or group of files","directories including subdirectories","to diskette of a different capacity","all of above","all of above");
	
     mainWorking(i,ans,time_taken,time_limit,'a','A',"Which command is used to make a new directory?","Md","Cd","Rd","None of above","Md");
	
     "Full form of MS-DOS is","Micro System Disk Operating System","Micro Simple Disk Operating System","Micro Soft Disk Operating System","Micro Sort Disk Operating System","Micro Soft Disk Operating System");
	
     "Operating System is like a","Parliament","Secretary","Government","None of the above","Government");
	
     "Format command is used to","Prepare a blank disk","Create a new blank disk from a used one","Both of above","None of above","Both of above");
	
     mainWorking(i,ans,time_taken,time_limit,'b','B',"The following command set is correct according to their function","RD can MD","DEL and ERASE","CD and RD","COPY and RENAME","DEL and ERASE");
	
     "Which command is used to change the file name?","Ren","Rename","Both of above","None of above","Both of above");
	
     mainWorking(i,ans,time_taken,time_limit,'d','D',"While working with MS-DOS, which command is used to copying the files to transfer from one PC to another one?","Rename","Path","Dir","Copy","Copy");
	
     mainWorking(i,ans,time_taken,time_limit,'a','A',"RESTORE command is used to","Restore files from disks made using the BACKUP command","Restore files which are deleted","Restore files from recycle bin","Restore files which are deleted recently","Restore files from disks made using the BACKUP command");
	
     "The vol command is used to","see the value of list","see the veriety of language","see the disk volume label","see the volume of largest","see the disk volume label");
	
     mainWorking(i,ans,time_taken,time_limit,'b','B',"In MS-DOS you can use small or capital letter of combination of both to enter a command\n\t but internally MS-DOS work with.","Small letter","Capital letter","Both a and b","None of above","Capital letter");
	
     mainWorking(i,ans,time_taken,time_limit,'b','B',"The maximum length in DOS commands is","80 chars","127 chars","100 chars","8 chars","127 chars");
	
     mainWorking(i,ans,time_taken,time_limit,'d','D',"The time command is used to display _____ time.","US time","Greenwich Mean Time","Julian Time","System Time","System Time");
	
     mainWorking(i,ans,time_taken,time_limit,'d','D',"WWW stands for ?","World Whole Web","Wide World Web","Web World Wide","World Wide Web","World Wide Web");
	
     mainWorking(i,ans,time_taken,time_limit,'b','B',"Which of the following are components of Central Processing Unit(CPU)?","Arithmetic logic unit,Mouse","Arithmetic logic unit,Control unit","Arithmetic logic unit, Integrated Circuits","Control Unit,Monitor","Arithmetic logic unit,Control unit");
	
     mainWorking(i,ans,time_taken,time_limit,'a','A',"Which among following first generation of computers had?","Vaccum Tubes and Magnetic Drum","Integrated Circuits","Magnetic Tape and Transistors","All of above","Vaccum Tubes and Magnetic Drum");
	
     "Where is RAM located?","Expansion Board","External Drive","Mother Board","All of above","Mother Board");
	
     mainWorking(i,ans,time_taken,time_limit,'b','B',"If a computer has more than one processor then it is known as?","Uniprocess","Multiprocessor","Multithreaded","Multiprogramming","Multiprocessor");
	
     "If a computer provides database services to other, then it will be known as?","Web server","Application server","Database server","FTP server","Database server");
	
     mainWorking(i,ans,time_taken,time_limit,'a','A',"Full form of URL is?","Uniform Resource Locator","Uniform Resource Link","Uniform Registered Link","Unified Resource Link","Uniform Resource Locator");
"""


class Question:
    def __init__(self, ques, options, answer):
        self.ques = ques
        self.options = options
        self.answer = answer
        self.timeTaken = 0

    def checkAnswer(self,ans, timeTaken):
        self.timeTaken = timeTaken
        if self.answer == ans:
            return True
        else:
            False
        
    def printQ(self,id,q_no):
        cls()
        print("\n\n")
        print("\t\t\t",end="")
        print(f"{q_no}.) {self.ques}")
        print("\n")
        print("\t\t\t",end="")
        print(f"A) {self.options[0]}",end="")
        print("\t\t\t",end="")
        print(f"B) {self.options[1]}")
        
        print("\n")
        print("\t\t\t",end="")
        print(f"C) {self.options[2]}",end="")
        print("\t\t\t",end="")
        print(f"D) {self.options[3]}")




for i in range(len(questions)):
    _q = questions[i]
    q = Question(_q["question"],_q["options"],_q["answer"])
    Qs.append(q)

