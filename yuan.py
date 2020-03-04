import random

class Shishen:
    ID = 0
    speed = 0
    yuan = 0
    def __init__(self,_ID,_speed):
        self.ID = _ID
        self.speed = _speed

speed=[Shishen(1,270),Shishen(2,240),Shishen(3,140),Shishen(4,139),Shishen(5,138),Shishen(6,128)]
l=[]
for i in range(1,11):
    l=l+[Shishen(x.ID, x.speed*i) for x in speed]
l.sort(key=lambda x: x.speed)

last = l[0]
l.remove(last)
success = 0
failure = 0
epoch = 0

for now in l:
    roll = random.random()
    if roll>0 and roll<0.25:
        now.yuan = 1
    elif roll>0.25 and roll<0.5:
        now.yuan = 2
    elif roll>0.5 and roll<0.75:
        now.yuan = 3
    else:
        now.yuan = 4
    if now.yuan == last.yuan:
        success = success + 1
    else:
        failure = failure + 1
    last = now
    if success == 7:
        print epoch
        break
    epoch = epoch+1     
