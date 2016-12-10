#!/usr/bin/python
import sys
import datetime
import webbrowser
import random
import time

def debugLog(string):
    if len(sys.argv) > 3:
        if sys.argv[3] is "T":
            print string

hour = int(sys.argv[1])
minute = int(sys.argv[2])
debug = False
time0 = datetime.datetime.now()
musicList = []
done = False

debugLog("Current Hour is %s while entered hour is %s" %(time0.hour, hour))
debugLog("Current Minute is %s while entered minute is %s" %(time0.minute, minute))

while not done:
    #Get current time
    time0 = datetime.datetime.now()
    #Check if current hour matches
    if hour == time0.hour:
        debugLog("Same hour")
        #Check if the current minute matches
        if minute is time0.minute:
            debugLog("Same Minute, ALARM STARTING!!")
            musicFile = open("music.txt", "r")
            musicList = musicFile.readlines()
            webbrowser.get('firefox').open_new(musicList[random.randint(0,8)])
            musicFile.close()
            done = True
            break
    #If current hour or minute dont match, go to sleep for a minute then try again.
    print "Sleeping... Zzz..."
    time.sleep(60)
print "Done"
