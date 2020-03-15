#tIP POINTS OPTIMIZED CODE

arr=[]

for (i,j) in valleys:
    arr.append(j)

average=sum(arr)/len(arr)
corners=[]
tips=[]

for i in hull:
        corners.append((cnt[i[0]][0][0],cnt[i[0]][0][1]))

for (i,j) in corners:
        if j < average:
            tips.append((i,j))



tips=sorted(tips)
tips=unique(tips)

for (i,j) in tips:
        cv2.circle(drawing,(i,j),7,[0,255,255],-1)
