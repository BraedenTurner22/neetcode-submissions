class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

         std::vector<std::vector<bool>> seen(rows, std::vector(cols, false));

         std::queue<std::pair<int, int>> q;

         std::vector<std::pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

         for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 0) {
                    seen[r][c] = true;
                    q.push({r, c});
                }
            }
         }

         while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();

            int prevValue = grid[r][c];

            for (const auto& dir : dirs) {
                int nr = r + dir.first;
                int nc = c + dir.second;

                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] != -1 && seen[nr][nc] != true) {
                    grid[nr][nc] = prevValue + 1;
                    seen[nr][nc] = true;
                    q.push({nr, nc});
                }
            }


         }
    }
};
