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

        std::unordered_map<Node*, Node*> oldToClone;
        std::queue<Node*> q;
        oldToClone[node] = new Node(node->val);
        q.push(node);

        while (!q.empty()) {
            Node* currNode = q.front();
            q.pop();

            for (Node* nei : currNode->neighbors) {
                if (!oldToClone.contains(nei)) {
                    oldToClone[nei] = new Node(nei->val);
                    q.push(nei);
                }
                oldToClone[currNode]->neighbors.push_back(oldToClone[nei]);
            }
        }
        return oldToClone[node];
    }
};
