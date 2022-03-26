class Sqrt:

    def findSqrt(self, target):
        return self.findSqrtInner(target, 0, (target//2)+1)

    def findSqrtInner(self, target, low, high):
        if (low <= high):
            mid = low+(high-low)//2
            if((mid**2 <= target) and (mid+1)**2 > target):
                if(mid**2 == target):
                    return mid
                else:
                    return self.findAccurate(mid, mid+1, target)
            elif mid**2 > target:
                return self.findSqrtInner(target, low, mid-1)
            else:
                return self.findSqrtInner(target, mid+1, high)
        return low

    def findAccurate(self, left, right, target):
        if(left <= right):
            middle = (left+right)/2
            middle_sq = middle*middle
            if(middle_sq == target or abs(middle_sq-target) < 0.001):
                return middle
            elif middle_sq < target:
                return self.findAccurate(middle, right, target)
            else:
                return self.findAccurate(left, middle, target)
        return left


if __name__ == "__main__":
    obj = Sqrt()
    print(f"Sqrt of {27} : {obj.findSqrt(27)}")
