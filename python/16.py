class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        def dfs(grid, i, j):
            # If the current cell is out of bounds or water, stop the DFS
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            # Mark the cell as visited
            grid[i][j] = '0'
            # Visit all 4 directions: up, down, left, right
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # Found an island
                    island_count += 1
                    dfs(grid, i, j)  # Mark all cells in this island as visited

        return island_count
