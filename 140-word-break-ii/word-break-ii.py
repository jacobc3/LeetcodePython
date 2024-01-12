class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.topDown(s, wordDict)

    def backtrack_naive(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        path = []
        res = []
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(path))
            for w in words:
                if i + len(w) <= len(s) and s[i: i+ len(w)] == w:
                    path.append(w)
                    backtrack(i+len(w))
                    path.pop()
        backtrack(0)
        return res

    def topDown(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        path = []
        memo = {}
        def dp(i):
            res = []
            if i == len(s):
                return [""]
            if i in memo:
                return memo[i]
            for w in words:
                if i + len(w) <= len(s) and s[i: i+len(w)] == w:
                    suffixs = dp(i+len(w))
                    for suffix in suffixs:
                        if suffix == "":
                            res.append(w)
                        else:
                            res.append(w + " " + suffix)
            memo[i] = res
            return res
        return dp(0)



    def downTop(self, s: str, wordDict: List[str]) -> List[str]:
        path = []
        return path