#include <vector>
#include <string>
using namespace std;

class WordDictionary {
public:
    struct WordNode {
        std::vector<WordNode*> children;
        bool isWord;
        WordNode() : children(26, nullptr), isWord(false) {}
    };

    WordNode* root;

    WordDictionary() {
        root = new WordNode();
    }

    void addWord(const string& word) {
        WordNode* curr = root;           // <-- local walker, don't clobber root
        for (char c : word) {
            int i = c - 'a';
            if (!curr->children[i]) {
                curr->children[i] = new WordNode();
            }
            curr = curr->children[i];
        }
        curr->isWord = true;
    }

    bool search(string word) {
        return dfs(word, 0, root);       // <-- return the result
    }

    bool dfs(const std::string& word, int index, WordNode* node) {
        if (!node) return false;         // <-- guard against null children
        if (index == (int)word.size()) return node->isWord;

        char c = word[index];
        if (c == '.') {
            for (int j = 0; j < 26; ++j) {
                if (dfs(word, index + 1, node->children[j])) return true;  // short-circuit on match
            }
            return false;
        } else {
            return dfs(word, index + 1, node->children[c - 'a']);
        }
    }
};;
