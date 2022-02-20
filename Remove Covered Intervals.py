# 1288. Remove Covered Intervals
# https://leetcode.com/problems/remove-covered-intervals/

class Solution:
    def removeCoveredIntervals(self, intervals):
        # Brute-Force
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if (intervals[i][0]>=intervals[j][0] and intervals[i][1]<=intervals[j][1]):
                    intervals[i][0]=intervals[j][0]
                    intervals[i][1]=intervals[j][1]
                elif (intervals[j][0]>=intervals[i][0] and intervals[j][1]<=intervals[i][1]):
                    intervals[j][0]=intervals[i][0]
                    intervals[j][1]=intervals[i][1]
        l=[]
        for i in intervals:
            if i not in l:
                l.append(i)
        return len(l)
        
        '''
        # Sorting
        intervals.sort()
        x,y=-1,-1
        count=0
        for i in intervals:
            if i[0]>x and i[1]>y:
                x=i[0]
                count+=1
            y=max(y,i[1])
        return count
        '''
        
        '''
        # sort left ascending and right decending
        intervals.sort(key=lambda x: (x[0],-x[1]))
        y=-1
        count=0
        for i,j in intervals:
            count+=(j>y)
            y=max(y,j)
        return count
        '''

# obj=Solution()
# x=int(input())
# l=[]
# for i in range(x):
#     l.append(list(map(int,input().split())))
# print(obj.removeCoveredIntervals(l))