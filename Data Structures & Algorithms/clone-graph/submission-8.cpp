/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        
        std::unordered_map<Node*, Node*> oldToNew;
        oldToNew[node] = new Node(node->val);
        std::queue<Node*> q;

        q.push(node);

        while (!q.empty()) {
            Node* currNode = q.front();
            q.pop();

            for (Node* neighbor : currNode->neighbors) {
                if (!oldToNew.contains(neighbor)) {
                    oldToNew[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }
                oldToNew[currNode]->neighbors.push_back(oldToNew[neighbor]);
            }
        }
        return oldToNew[node];
        }
};
