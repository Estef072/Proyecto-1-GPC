from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, greyscale, hologram, invertedcolor, randomstatic, unlit, gourad, toon, glow, textureBlend, pinkjelly, toongreyscale, heatmap

width = 1240
height = 1240

rend = Renderer(width, height)

rend.background = Texture("fondo.bmp")
rend.glClearBackground()

rend.active_texture = Texture("model.bmp")
rend.active_shader = randomstatic
rend.glLoadModel("model.obj",
                 translate = V3(-4, 3.5, -10),
                 scale = V3(1.5,1.5,1.5),
                 rotate = V3(0,0,0))


rend.active_texture = Texture("poke.bmp")
rend.dirLight = V3(0,1,0)
rend.active_shader = hologram
rend.glLoadModel("Pokemon.obj",
                 translate = V3(-.1, 2.5, -10),
                 scale = V3(1.4,1.4,1.4),
                 rotate = V3(5,-180,0))

rend.active_shader = greyscale
rend.glLoadModel("Mask.obj",
                 translate = V3(4, 3.6, -10),
                 scale = V3(11.5,11.5,1.5),
                 rotate = V3(0,0,0))


rend.active_texture = Texture("tree.bmp")
rend.active_shader = pinkjelly
rend.glLoadModel("arbolito.obj",
                 translate = V3(-4, -1.6, -10),
                 scale = V3(.135,.135,.135),
                 rotate = V3(5,-180,0))


rend.dirLight = V3(0,1,0)
rend.active_shader = invertedcolor
rend.glLoadModel("bolita.obj",
                 translate = V3(-.1, -.5, -10),
                 scale = V3(.4,.4,.4),
                 rotate = V3(5,-180,0))


rend.active_shader = toongreyscale
rend.glLoadModel("flor.obj",
                 translate = V3(4, -1.6, -10),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))
#rend.active_texture = Texture("models/model.bmp")
#rend.active_shader = gourad
#rend.glLoadModel("models/model.obj",
#                 translate = V3(-4, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

#rend.active_shader = toon
#rend.glLoadModel("models/model.obj",
#                 translate = V3(0, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))

#rend.active_shader = glow
#rend.glLoadModel("models/model.obj",
#                 translate = V3(4, 0, -10),
#                 scale = V3(3,3,3),
#                 rotate = V3(0,0,0))



rend.glFinish("output.bmp")
