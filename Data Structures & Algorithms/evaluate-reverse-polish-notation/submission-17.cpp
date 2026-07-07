class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> s;
        for (auto& token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int digitTwo = s.top(); s.pop();
                int digitOne = s.top(); s.pop();
                if (token == "+") s.push(digitOne + digitTwo);
                else if (token == "-") s.push(digitOne - digitTwo);
                else if (token == "*") s.push(digitOne * digitTwo);
                else if (token == "/") s.push(digitOne / digitTwo); // truncates toward 0, matches C++ int division
            } else {
                s.push(std::stoi(token));
            }
        }
        return s.top();
    }
};
