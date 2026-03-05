def findMinArrowShots(self, points) -> int:
        def get_end(interval):
            return interval[1]

        points.sort(key=get_end)
#Where can I place one point to cover the most intervals?
#The best greedy choice is: place arrow at the smallest end
        arrows = 1
        arrow_pos = points[0][1]

        for start, end in points:
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end

        return arrows