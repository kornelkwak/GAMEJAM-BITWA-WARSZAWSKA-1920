import pyglet, time

pic = pyglet.image.load('images/plansza.png')

window = pyglet.window.Window(fullscreen = True)

@window.event
def on_draw():
    window.clear()
    pic.blit(0,0, width = window.width, height = window.height)

def close(event):
    window.close()

pyglet.clock.schedule_once(close, 5)

pyglet.app.run()


