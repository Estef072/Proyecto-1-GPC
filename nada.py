rend.glLoadModel("buff.obj",
                 translate = V3(-6, -2, -10),
                 scale = V3(2,2,2),
                 rotate = V3(2,0,0))
rend.active_shader = hologram
rend.active_shader = invertedcolor

rend.glLoadModel("model.obj",
                 translate = V3(0, 3, -10),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))

rend.active_shader = randomstatic

rend.glLoadModel("model.obj",
                 translate = V3(4, -1, -10),
                 scale = V3(2,2,2),
                 rotate = V3(0,0,0))