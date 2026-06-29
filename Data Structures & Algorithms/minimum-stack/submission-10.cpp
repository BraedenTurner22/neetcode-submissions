class MinStack {
private:
std::stack<int> minStack;
std::stack<int> minAtIndexStack;

public:
    MinStack() {
        minStack = {};
        minAtIndexStack = {}; 
    }
    
    void push(int val) {
        minStack.push(val);
        if (minAtIndexStack.empty()) minAtIndexStack.push(val);
        else {
            int min = std::min(val, minAtIndexStack.top());
            minAtIndexStack.push(min);
        }
    }
    
    void pop() {
        if (!minStack.empty()) {
        minStack.pop();
        minAtIndexStack.pop();
        }
    }
    
    int top() {
        if (!minStack.empty()) {
            return minStack.top();
        }
    }
    
    int getMin() {
        return minAtIndexStack.top();
    }
};
