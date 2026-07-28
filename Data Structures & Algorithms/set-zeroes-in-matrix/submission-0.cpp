class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<int> candidateRows;
        vector<int> candidateCols;

        for (int i{0}; i < matrix.size(); ++i) {
            for (int j{0}; j < matrix[0].size(); ++j) {
                if (matrix[i][j] == 0) {
                    candidateRows.push_back(i);
                    candidateCols.push_back(j);
                }
            }
        }

        for (int i{0}; i < matrix.size(); ++i) {
            for (int col : candidateCols) {
                matrix[i][col] = 0;
            }
        }

        for (int j{0}; j < matrix[0].size(); ++j) {
            for (int row : candidateRows) {
                matrix[row][j] = 0;
            }
        }
    }
};
