def wordBreak(s, wordDict):
    dp = [True] + [False] * len(s)
    for i in range(len(s)):
        if dp[i] == True:
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    dp[j + 1] = True
    return dp[-1]

s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s,wordDict))