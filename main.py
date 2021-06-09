import pyglet
import random
import math
import os

class Browser:
    def __init__(self):
        self.disk_img = pyglet.image.load('imgs/disk.png')
        self.padding = 10

        self.widgets = []

    def update(self, dt):
        self.widgets = []

        sprite = pyglet.sprite.Sprite(
            self.disk_img,
            x = window.width / 2 - 55,
            y = window.height / 2- 55,
        )

        sprite.scale = 110/256.0

        self.widgets.append(
            sprite
        )

    def draw(self):
        pyglet.gl.glClearColor(0.5, 0.5, 0.5, 1)
        for widget in self.widgets:
            widget.draw()

class ParticleSystem:
    def __init__(self, x, y, radius, particle_radius, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

        self.particles = []
        for i in range(0, 7):
            self.particles.append(pyglet.shapes.Circle(x, y, radius=particle_radius, color=color))
            self.particles[i].speed = random.randrange(50, 100) / 20.0
            self.particles[i].rot = 0

    def update(self, dt):
        for particle in self.particles:
            particle.rot += particle.speed * dt

            particle.x = self.x + math.cos(particle.rot) * self.radius
            particle.y = self.y + math.sin(particle.rot) * self.radius

    def draw(self):
        for particle in self.particles:
            particle.draw()

class MainMenu:
    def __init__(self):
        self.font_name = 'Helvetica'
        self.font_size = 20
        self.help_font_size = 15
        self.padding = 5
        self.selected_color = (80, 157, 178, 255)
        self.unselected_color = (128, 128, 128, 255)
        self.help_color = (200, 200, 200, 255)
        self.x_img = pyglet.image.load('imgs/cross.png')
        self.triangle_img = pyglet.image.load('imgs/triangle.png')

        self.browser_label = pyglet.text.Label(
            'Browser',
            font_name = self.font_name,
            font_size = self.font_size,
            color = self.selected_color,
            x = window.width/2,
            y = window.height/2,
            anchor_x = 'center',
            anchor_y = 'center')

        self.conf_label = pyglet.text.Label(
            'System Configuration',
            font_name = self.font_name,
            font_size = self.font_size,
            color = self.unselected_color,
            x = window.width/2,
            y = window.height/2 - self.font_size - self.padding,
            anchor_x = 'center',
            anchor_y = 'center')

        self.enter_label = pyglet.text.Label(
            'Enter',
            font_name = self.font_name,
            font_size = self.help_font_size,
            color = self.help_color,
            x = window.width/4,
            y = window.height/10,
            anchor_x = 'center',
            anchor_y = 'center')

        self.enter_button = pyglet.sprite.Sprite(
            self.x_img,
            x = window.width/4 - (len('Enter')/2)*self.help_font_size - self.padding,
            y = window.height/10 - self.help_font_size / 2,
        )

        self.enter_button.scale = self.help_font_size/512

        self.version_label = pyglet.text.Label(
            'Version',
            font_name = self.font_name,
            font_size = self.help_font_size,
            color = self.help_color,
            x = window.width - window.width/4,
            y = window.height/10,
            anchor_x = 'center',
            anchor_y = 'center')

        self.version_button = pyglet.sprite.Sprite(
            self.triangle_img,
            x = (window.width - window.width/4) - (len('Version')/2)*self.help_font_size,
            y = window.height/10 - self.help_font_size / 2,
        )

        self.version_button.scale = self.help_font_size/512

        self.widgets = [
            self.browser_label,
            self.conf_label,
            self.enter_label,
            self.enter_button,
            self.version_label,
            self.version_button
        ]

        self.particle_system = ParticleSystem(
            window.width / 2 - (len('Browser') / 2) * self.font_size - self.padding * 8,
            window.height / 2,
            50,
            5,
            (100, 177, 198))

    def update(self, dt):
        self.particle_system.update(dt)

    def draw(self):
        self.particle_system.draw()

        for widget in self.widgets:
            widget.draw()

window = pyglet.window.Window()

main_menu = MainMenu()
browser = Browser()

def update(dt):
    main_menu.update(dt)
    browser.update(dt)

@window.event
def on_draw():
    window.clear()

    #main_menu.draw()
    browser.draw()


pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
