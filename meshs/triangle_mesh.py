import numpy as np

from meshs.base_mesh import BaseMesh


class TriangleMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.ctx = app.ctx

        self.program = app.shader_program.triangle
        self.vbo_format = '3f 3f'
        self.attrs = ('in_position', 'in_color')
        self.vao = self.get_vao()

    def get_vertex_data(self) -> np.array:
        vertices = [
            (0.0, 0.0, 0.0), (0.5, 0.0, 0.0), (0.0, 0.5, 0.0)
        ]

        color = [
            (1, 1, 1), (1, 1, 1), (1, 1, 1)
        ]

        vertex_data = np.hstack([vertices, color], dtype='float32')
        return vertex_data
