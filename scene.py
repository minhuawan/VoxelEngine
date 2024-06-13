from world import World


class Scene:
    def __init__(self, app):
        self.app = app
        # self.quad = QuadMesh(self.app)
        # self.triangle = TriangleMesh(self.app)
        # self.chunk = Chunk(self.app)
        self.world = World(app)

    def update(self):
        self.world.update()

    def render(self):
        # self.quad.render()
        # self.triangle.render()
        # self.chunk.render()
        self.world.render()
