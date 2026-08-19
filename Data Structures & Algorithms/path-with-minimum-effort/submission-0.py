import heapq

class Solution:
    def minimumEffortPath(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        # effort[r][c] = minimum effort needed to reach (r, c)
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0

        # (current_effort, row, col)
        pq = [(0, 0, 0)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            curr_effort, r, c = heapq.heappop(pq)

            # If we reached the destination
            if r == rows - 1 and c == cols - 1:
                return curr_effort

            # Ignore outdated entries
            if curr_effort > effort[r][c]:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:

                    difference = abs(
                        heights[r][c] - heights[nr][nc]
                    )

                    new_effort = max(curr_effort, difference)

                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(
                            pq,
                            (new_effort, nr, nc)
                        )

        return 0