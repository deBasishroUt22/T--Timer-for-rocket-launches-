import time

def countdown(t):
    while(t):
        timefile=open("counter.txt","w")
        mins,secs = divmod(t,60)
        if mins>60:
            hours,mins=divmod(mins,60)
        else:
            hours=0
        timeformat="-"+f"{hours:02d}:{mins:02d}:{secs:02d}"
        timefile.write(timeformat)
        timefile.close()
        time.sleep(1)
        t-=1
    if t==0:
        timefile=open("counter.txt","w")
        mins,secs = divmod(t,60)
        if mins>60:
            hours,mins=divmod(mins,60)
        else:
            hours=0
        timeformat="+"+f"{hours:02d}:{mins:02d}:{secs:02d}"
        timefile.write(timeformat)
        timefile.close()
        time.sleep(1)
        t+=1
    while(t):
        timefile=open("counter.txt","w")
        mins,secs = divmod(t,60)
        if mins>60:
            hours,mins=divmod(mins,60)
        else:
            hours=0
        timeformat="+"+f"{hours:02d}:{mins:02d}:{secs:02d}"
        timefile.write(timeformat)
        timefile.close()
        time.sleep(1)
        t+=1

countdown(1000)