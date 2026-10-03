class Solution:
    def longestValidParentheses(self, s: str) -> int:
        best=0
        open_,close=0,0
        for c in s:
            if c=='(':
                open_+=1
            else:
                close+=1
            if open_==close:
                best=max(best,2*close)
            elif close>open_:
                open_,close=0,0
        open_,close=0,0
        for c in reversed(s):
            if c=="(":
                open_+=1
            else:
                close+=1
            if open_==close:
                best=max(best,2*close)
            elif open_>close:
                open_,close=0,0
                


        return best