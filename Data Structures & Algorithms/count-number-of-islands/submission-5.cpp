class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int islandCount = 0;
        int rows = grid.size(), cols = grid[0].size();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    bfs(grid, r, c);
                    islandCount++;
                }
            }
        }
        return islandCount;
    }

    void bfs(vector<vector<char>>& grid, int r, int c) {
        std::vector<std::pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int rows = grid.size(), cols = grid[0].size();

        std::queue<std::pair<int, int>> q;
        grid[r][c] = '0';
        q.push({r, c});

        while (!q.empty()) {
            auto currNode = q.front();
            q.pop();

            for (auto& dir : dirs) {
                int nr = currNode.first + dir.first;
                int nc = currNode.second + dir.second;

                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == '1') {
                    q.push({nr, nc});
                    grid[nr][nc] = '0';
                }
            }
        }
    }
};
