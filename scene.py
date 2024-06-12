from meshs.quad_mesh import QuadMesh
from meshs.triangle_mesh import TriangleMesh
from world_objects.chunk import Chunk


class Scene:
    def __init__(self, app):
        self.app = app
        # self.quad = QuadMesh(self.app)
        # self.triangle = TriangleMesh(self.app)
        self.chunk = Chunk(self.app)

    def update(self):
        pass

    def render(self):
        # self.quad.render()
        # self.triangle.render()
        self.chunk.render()
