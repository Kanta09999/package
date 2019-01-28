from tool.imports import *
import tool.calculatorOfMslib as coml

class Calculator:
    def getResult(self,targetPoints, comprePoints):
        ans = 0
        """
        positions = [[12, 27],
                    [12, 39],
                    [14, 59],
                    [15, 59],
                    [16, 59],
                    [16, 67]]"""
        ans = 0
        for i in range(6):
            tlist = targetPoints[i].split(",")
            clist = comprePoints[i].split(",")
            temp = coml.getDistance(float(tlist[0]), float(tlist[1]), float(tlist[2]), float(tlist[3]), float(clist[0]), float(clist[1]), float(clist[2]), float(clist[3]))
            print(temp)
            ans += temp
        print(ans)
        return max(100 - ans * 45  , 0)