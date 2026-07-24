class Solution {
public:
    bool checkValidString(string s) { 
        std::stack<int> left, star;

        for (int i{0}; i < s.size(); ++i) {
            if (s[i] == '(') left.push(i);
            else if (s[i] == '*') star.push(i);
            else if (left.empty() && s[i] == ')') {
                if (star.empty()) return false;
                else star.pop();

            }
            else left.pop();
        }

        while (!left.empty() && !star.empty()) {
            if (left.top() > star.top()) return false;
            left.pop();
            star.pop();
        }

        return left.empty();
    }
};
