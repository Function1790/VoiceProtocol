import pyautogui as pg
import speech_recognition as sr
import threading as td
import time
from time import sleep
from os import system

#Command Variable
enable_memo=False
memo_text=""
mecro_tread=None

#Constant(Folder)
PATH="D:\\Py6\\VoiceProtocol\\record"
LINK="link\\" #lnk files

#Link
Program_List={
    "CALL NAME":"lnk File",
}

def Log(title, content):
    print(f"[{title}] >> {content}")

def RunProgram(file_name):
    Log("Execute", file_name)
    system(LINK+file_name+".lnk")

def isRun(text):
    for i in Program_List:
        if i+" open" in text:
            RunProgram(Program_List[i])
            return True
        if i+" execute" in text:
            RunProgram(Program_List[i])
            return True
    return False

#Commands
def Process(text):
    global isMecro
    global enable_memo
    global memo_text

    if "memo enable" in text:
        memo_text=""
        enable_memo=True
        Log("Command", "Memo Enabled")
    elif "memo disable" in text:
        f=open("memo.txt","w",encoding="utf-8")
        f.writelines(memo_text)
        f.close()
        enable_memo=True
        Log("Command", "Memo Disabled")
    elif enable_memo:
        memo_text+=" "+text
        return True    
    elif isRun(text):
        return True
    
#Voice -> Text
cnt=0
def Voice_Recognition():
    global cnt
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #print("P:Say")
        audio=r.listen(source)
        said=" "
        cnt+=1
        try:
            said=r.recognize_google(audio, language='ko-KR')
            now = time.localtime()
            log_time="%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)
            Log(log_time ,said)
        except Exception as e:
            now = time.localtime()
            log_time="%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec)
            Log(log_time, "Missing..")
    return said

#Main
list01=[]

while True:
    text=Voice_Recognition()
    if enable_memo:
        memo_text+=text
    Process(text)
    if "administer exit" in text:
        break
