class Solution {
private:
    int islands = 0;

public:
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        for (int x = 0; x < rows; x++) {
            for (int y = 0; y < cols; y++) {
                if (grid[x][y] == '1') {
                    bfs(grid, x, y);
                    islands++;
                }
            }
        }
        return islands;
    }

    void bfs(std::vector<std::vector<char>>& grid, int x, int y) {
        int rows = grid.size();
        int cols = grid[0].size();

        std::vector<std::pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        std::queue<std::pair<int, int>> q;
        grid[x][y] = '0';
        q.push({x, y});

        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();
            for (const auto& dir : dirs) {
                int nr = r + dir.first;
                int nc = c + dir.second;

                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == '1') {
                    grid[nr][nc] = '0';
                    q.push({nr, nc});
                }
            }
        }
    }
};
