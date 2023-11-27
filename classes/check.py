class Check:
    def __init__(self, old_vertices, segment_i) -> None:
        self.old_vertices = old_vertices
        self.segment_i = segment_i

    def check_points_lst(self) -> None:
        if self.old_vertices[0] != self.old_vertices[-1]:
            raise "Polygon isn`t finished!"

        if self.segment_i > len(self.old_vertices) - 2:
            raise "Segment is too big"
