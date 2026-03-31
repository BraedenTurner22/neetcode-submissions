class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupedAnagrams = defaultdict(list)
        
        for str1 in strs:
            charList = [0] * 26
            for char in str1:
                charList[ord(char)-ord('a')] +=1 
            groupedAnagrams[tuple(charList)].append(str1)
        
        return groupedAnagrams.values()