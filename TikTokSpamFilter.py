#! /usr/bin/env python3

# problem description
# https://www.fastprep.io/problems/tiktok-get-spam-comments
# test case 1 input
# comments = ["viral tricks to boost", "Great viral tips", "boost views and go viral"], spam_keywords = ["viral", "boost"]
# test case 1 output
# ["spam", "not_spam", "spam"]
# test case 2 input
# comments = ["The sun is bright", "Blockbuster bonanza"], spam_keywords = ["bright", "bonanza", "paid"]
# test case 2 output
# ["not_spam", "not_spam"]

class Solution:
    def getSpamComments(self, comments: list[str], spam_keywords: list[str]) -> list[str]:
        keyWordSet = set([word.lower() for word in spam_keywords])
        result = []
        for comment in comments:
            count = 0
            for word in comment.split(" "):
                if word.lower() in keyWordSet:
                    count += 1
                    if count >= 2:
                        result.append("spam")
                        break
            else:
                result.append("not_spam")
        return result


if __name__ == "__main__":
    testSolution = Solution()
    print(testSolution.getSpamComments(["viral tricks to boost", "Great viral tips", "boost views and go viral"], ["viral", "boost"]))
    print(testSolution.getSpamComments(["The sun is bright", "Blockbuster bonanza"], ["bright", "bonanza", "paid"]))