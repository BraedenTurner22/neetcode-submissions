class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> parenMap = {{'}', '{'}, {']', '['}, {')', '('}};

        std::stack<char> stk;
        
        for (char paren : s) {
            if (!parenMap.contains(paren)) stk.push(paren);
            else {
                if (stk.empty() || parenMap[paren] != stk.top()) {
                    return false;
                }
                stk.pop();
            }
        }
        return stk.empty();
    }
};
