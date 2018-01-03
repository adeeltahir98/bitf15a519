n=int(input("Enter Total Number of Processes : "))
bt=[]
at=[]
wt=[]
tt=[]
avgwt=0
avgtt=0
print("Enter Burst Times of Processes : ")
for x in range(0,n):
    bt.insert(x,int(input()))
print("Enter Arrival Times of Processes : ")
for x in range(0,n):
    at.insert(x,int(input()))
wt.insert(0,0-at[0])
tt.insert(0,bt[0]-at[0])
for i in range(1,n):
    wt.insert(i,bt[i-1]-at[i])
    tt.insert(i,bt[i]-at[i])
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
