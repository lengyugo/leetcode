class Solution:
    def checkSubTree(self, t1, t2) -> bool:
        def track(p,q):
            if q == None:
                return True
            elif p == None and q != None:
                return False
            elif p.val != q.val:
                return False
            else:
                return track(p.left,q.left) and track(p.right,q.right)

        if not t1: return False
        if not t2: return True
        return track(t1,t2) or track(t1.left,t2) or track(t1.right,t2)