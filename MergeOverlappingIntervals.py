# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        tupleList = []

        for intv in intervals:
            tupleList.append((intv.start, 's'))
            tupleList.append((intv.end, 'z')) # using 'z' instead of 'e' helps in sorting

        tupleList.sort()

        output = []
        start = tupleList[0][0]
        end = 0
        bConsume = True
        count = 0

        for tup in tupleList:
            current = tup[1]
            if (current == 'z'):
                count -= 1
                end = tup[0]
                bConsume = False
            else:
                if count==0:
                    start = start = tup[0]
                count += 1

            if (count == 0):
                intv = Interval(start, end)
                output.append(intv)
                bConsume = True

        if (bConsume == False):
            intv = Interval(start, end)
            output.append(intv)

        return output
