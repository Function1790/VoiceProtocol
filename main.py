import pyautogui as pg
import speech_recognition as sr
import threading as td
import time
from time import sleep
from os import system

enable_memo=False
memo_text=""
mecro_tread=None

PATH="D:\\Py6\\VoiceProtocol\\record"
LINK="link\\"

Program_List={
    "페인트":"Paint.NET",
    "브라우저":"Chrome",
    "디스코드":"Discord",
    "카카오톡":"KaKaoTalk",
    "오버워치":"Overwatch",
    "발로란트":"VALORANT",
    "브라우저":"Chrome",
    "음식 제조기":"CookingSim",
    "메신저":"Messenger",
    "마인크래프트":"Minecraft",
    "오토마우스":"Automouse",
    "러시아 키보드":"RussiaKeyboard",
    "가루":"PowderToy"
}

def Log(title, content):
    print(f"[{title}] >> {content}")

def RunProgram(file_name):
    Log("Execute", file_name)
    system(LINK+file_name+".lnk")

def isRun(text):
    for i in Program_List:
        if i+" 열어 줘" in text:
            RunProgram(Program_List[i])
            return True
        if i+" 실행" in text:
            RunProgram(Program_List[i])
            return True
    return False

def Process(text):
    global isMecro
    global enable_memo
    global memo_text

    if "메모 활성화" in text:
        memo_text=""
        enable_memo=True
        Log("Command", "Memo Enabled")
    elif "메모 비활성화" in text:
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
    if "관리자 권한 나가기" in text:
        break