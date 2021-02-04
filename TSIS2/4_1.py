gain = [-5,1,5,0,-7]
road = []
road.append(0)

for i in range(0,len(gain)):
	road.append(road[i] + gain[i])

mx = -999
for i in range(0,len(road)):
	#print(road[i],end=" ")
	if road[i] > mx:
		mx = road[i]
	else:
		continue

print(mx)