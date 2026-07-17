class TrieNode {
public:
    TrieNode* children[26];
    bool isEnd;

    TrieNode() {
        for (int i{0uz}; i < 26; ++i) {
            children[i] = nullptr;
        }
        isEnd = false;
    }
};

class PrefixTree {
public:
    TrieNode* root;

    PrefixTree() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* currNode = root;
        for (const char& c : word) {
            int i = c - 'a';
            if (!currNode->children[i]) currNode->children[i] = new TrieNode();
            currNode = currNode->children[i];
        }
        currNode->isEnd = true;

    }
    
    bool search(string word) {
        TrieNode* currNode = root;
        for (const char& c : word) {
            int i = c - 'a';
            if (!currNode->children[i]) return false;
            currNode = currNode->children[i];
        }
        return currNode->isEnd;
    }
    
    bool startsWith(string prefix) {
        TrieNode* currNode = root;
        for (const char& c : prefix) {
            int i = c - 'a';
            if (!currNode->children[i]) return false;
            currNode = currNode->children[i];
        }
        return true;
    }
};
