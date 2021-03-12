import pyglet

music = pyglet.resource.media('musica.mp3', streaming=False)
music.play()


pyglet.app.run()