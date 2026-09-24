class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        dic_s_t={}
        dic_t_s={}

        for i in range(len(s)):
            if s[i] in dic_s_t:
                if dic_s_t[s[i]]!=t[i]:
                    return False
            else:
                dic_s_t[s[i]]=t[i]
            
            if t[i] in dic_t_s:
                if dic_t_s[t[i]]!=s[i]:
                    return False
            else:
                dic_t_s[t[i]]=s[i]
        return True
