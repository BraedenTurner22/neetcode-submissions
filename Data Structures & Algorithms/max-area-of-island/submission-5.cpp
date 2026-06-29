class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        int rows = grid.size();
        int cols = grid[0].size();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) {
                    maxArea = std::max(maxArea, islandArea(grid, r, c));
                }
            } 
        }
        return maxArea;
    }

    int islandArea(vector<vector<int>>& grid, int row, int col) {
        int rows = grid.size();
        int cols = grid[0].size();

        std::queue<std::pair<int, int>> q;
        grid[row][col] = 0;
        q.push({row, col});

        int area = 1;

        std::vector<std::pair<int, int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();

            for (auto dir : dirs) {
                int nr = r + dir.first;
                int nc = c + dir.second;
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                    area++;
                    grid[nr][nc] = 0;
                    q.push({nr, nc});
                }
            }
       }
       return area;
    }
};
