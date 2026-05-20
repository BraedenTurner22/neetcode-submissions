class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        std::map<std::vector<int>, std::vector<std::string>> freqToWord = {};

        for (std::string& str : strs) {
            std::vector<int> frequencies(26, 0);
            for (char& c : str) {
                frequencies[c - 'a']++;
            }
            freqToWord[frequencies].push_back(str);
        }
        std::vector<std::vector<std::string>> response;
        for (auto const& [freq, words] : freqToWord) {
            response.push_back(words);
        }

        return response;
    }
};
