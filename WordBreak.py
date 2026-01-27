#Word reak Problem:
# Create a arrayfor booleans with length +1 where first one is considered for empty string and defaulted to True.
# Condition is #For every substring from start of the word to index, check if there is a word in the list . Also check if the substring as a whole is seen in dictionary. Once the confitions are met, the specific index falg is se as 0 to find the subsequent workds
class solution:

    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        booleanArray = [True] + [False] * len(s)
        for index in range(1, len(s) + 1):

            for word in wordDict:
                if index >= len(word) and booleanArray[index - len(word)] and s[:index].endswith(word):
                    booleanArray[index] = True
                    break

        return booleanArray[-1]





sols=solution()

wordlist=["cat","dog","and","sand"]
word="catsanddog"

print(sols.wordBreak(word,wordlist))