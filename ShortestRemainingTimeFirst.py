n=int(input("Enter Number of Processes: "))
bt=[]
at=[]
wt=[]
tt=[]
ft=[]
avgwt=0
avgtt=0
totaltime=0;
timeelapsed=0
print("Enter Burst Times of Processes : ")
for x in range(0,n):
    bt.insert(x,int(input()))
print("Enter Arrival Times of Processes : ")
for x in range(0,n):
    at.insert(x,int(input()))
tbt=0
for x in range(0,n):
    tbt+=bt[i]
totaltime=bt[0]
var=0
ch=False
for j in range(0,tbt):
    for i in range(0,n-1):
        if(var<totaltime):
            timeelapsed+=1
            totaltime-=1
            var+=1
            if(totaltime!=0):
                for j in range(0,n-i-1):
                    if(timeelapsed>=at[j+1] or timeelapsed>=at[j-1] and ch==False):
                        if(totaltime<bt[j+1] or totaltime<bt[j-1]):
                            totaltime=bt[j+1]
                            var=0
            elif(totaltime==0):
                timeelapsed=ft[i]
                ch=True
wt.insert(0,0-at[0])
tt.insert(0,ft[0]-at[0])
for i in range(1,len(bt)):
    wt.insert(i,bt[i-1]-at[i])
    tt.insert(i,ft[i]-at[i])
    avgwt+=wt[i]
    avgtt+=tt[i]
avgwt=float(avgwt)/n
avgtt=float(avgtt)/n
print("Wainting Times of processes: ")
for i in range(0,n):
    print(wt[i])
print("Turnaround Times of Processes: ")
for i in range(0,n):
    print(tt[i])
print("Average Waiting Time: ",avgwt)
print("Average Turnaround Time: ",avgtt)
