#! /usr/bin/env python3

# problem description
# https://www.fastprep.io/problems/tiktok-count-twin-pairs
# test case 1 input
# words = ["abca", "abaa", "baab", "cba"]
# test case 1 output
# 2
# test case 2 input
# words = ["apple", "apel", "silent", "listen", "papel"]
# test case 2 output
# 4

class Solution:
    def countTwinPairs(self, words: list[str]) -> int:
        freqList = []
        for word in words:
            freq = [None] * 26
            for char in word:
                freq[ord(char) - ord('a')] = True
            freqList.append(freq[:])

        count = 0
        for i in range(len(freqList)):
            for j in range(i + 1, len(freqList)):
                if freqList[i] == freqList[j]:
                    count += 1
        return count


if __name__ == "__main__":
    testSolution = Solution()
    print(testSolution.countTwinPairs(["abca", "abaa", "baab", "cba"]))
    print(testSolution.countTwinPairs(["apple", "apel", "silent", "listen", "papel"]))