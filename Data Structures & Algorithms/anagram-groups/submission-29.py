class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        subLists = []

        for string in strs:
            letterFreq = [0] * 26
            for char in string:
                letterFreq[ord(char)-ord('a')] += 1
            if tuple(letterFreq) not in anagrams:
                anagrams[tuple(letterFreq)] = []
            anagrams[tuple(letterFreq)].append(string)
        
        for value in anagrams.values():
            subLists.append(value)
        
        return subLists