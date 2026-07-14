class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        int numFF = 0;
        int numMinutes = 0;

        std::vector<std::pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        std::queue<std::pair<std::pair<int, int>, int>> q;

        for (int r{0uz}; r < rows; ++r) {
            for (int c(0uz); c < cols; ++c) {
                if (grid[r][c] == 1) numFF++;
                else if (grid[r][c] == 2) q.push({{r, c}, 0});
            }
        }

        while (!q.empty()) {
            auto rottenFruitIndex = q.front().first;
            auto minCount = q.front().second;
            q.pop();

            numMinutes = std::max(numMinutes, minCount);

            for (auto& [r, c] : dirs) {
                int nr = r + rottenFruitIndex.first;
                int nc = c + rottenFruitIndex.second;

                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                    numFF--;
                    grid[nr][nc] = 2;
                    q.push({{nr, nc}, minCount+1});
                }
            }
        }

        if (numFF != 0) return -1;
        else return numMinutes;
    }
};
