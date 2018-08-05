
from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This is scene is not yet implemented."
        exit(1)

class Death(Scene):
    def enter(self):
        print "Your Died."
        exit(1)
        

class CentralCorridor(Scene):
    def enter(self):
        action=raw_input("Central Corridor>")
        if action=="shoot":
            return "death"
        elif action=="tell a joke":
            return 'laser_weapon_armory'
        else:
            print "Does not computer!"
            return 'central_corridor'

class TheBridge(Scene):
    def enter(self):
        exit(1)

class EscapePod(Scene):
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        code="%d" % (randint(1,9))
        guess=raw_input("Laser Weapon Armory [keypad]> ")
        guesses=0
        while guess!=code and guesses<10:
            print "BZZZZEDDD!"
            guesses+=1
            guess=raw_input("Laser Weapon Armory [keypad]> ")
        if guess==code:
            return "the_bridge"
        else:
            return 'death'


class Engine(object):
    def __init__(self):
        self.scene_map={
            'central_corridor':CentralCorridor(),
            'death':Death(),
            'the_bridge':TheBridge(),
            'escape_pod':EscapePod(),
            'laser_weapon_armory':LaserWeaponArmory()
        }
        self.current_scene=self.scene_map['central_corridor']

    def play(self):
        while True:
            print "\n---------"
            next_scene_name=self.current_scene.enter()
            print "next_scene_name: %s" % next_scene_name
            self.current_scene=self.scene_map[next_scene_name]

game=Engine()
game.play()
