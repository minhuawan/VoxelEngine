from settings import *

import pygame as pg
import moderngl as mgl


class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        # load texture
        self.texture_0 = self.load('frame.png')

        # assign texture unit
        self.texture_0.use(location=0)

    def load(self, filename):
        texture = pg.image.load(f'assets/{filename}')
        # Why flip ?
        texture = pg.transform.flip(texture, flip_x=True, flip_y=False)
        texture = self.ctx.texture(
            size=texture.get_size(),
            components=4,  # What is this
            data=pg.image.tostring(texture, 'RGBA', False)
        )
        texture.anisotropy = 32.0
        texture.build_mipmaps()
        texture.filter = (mgl.NEAREST, mgl.NEAREST)
        return texture
