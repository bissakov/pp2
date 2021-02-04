#1732. Find the Highest Altitude
#https://leetcode.com/problems/find-the-highest-altitude/

class Solution(object):
    def largestAltitude(self, gain):
        road = []
        road.append(0)
        
        for i in range(0,len(gain)):
            road.append(road[i] + gain[i])
            
        mx = -999
        for i in range(0,len(road)):
            if road[i] > mx:
                mx = road[i]
            else:
                continue
        return mx