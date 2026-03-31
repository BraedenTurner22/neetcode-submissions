class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        letterFreqToWord = defaultdict(list)

        for word in strs:
            letterFreq = [0] * 26
            for letter in word:
                letterFreq[ord(letter)-ord('a')] += 1
            
            letterFreqToWord[tuple(letterFreq)].append(word)
        
        return list(letterFreqToWord.values())