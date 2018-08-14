from nose.tools import *
from ex47.game import Room


def test_room():
    gold=Room("GoldRoom",
        """This Room has gold in it. the door
        jto the north.""")
    assert_equal(gold.name,"GoldRoom")
    assert_equal(gold.paths,{})

def test_room_paths():
    center=Room("Center","Test room in the center.")
    north=Room("North","Test room in the north.")
    south=Room("South","Test room in the south.")

    center.add_paths({'north':north,'south':south})
    assert_equal(center.go('north'),north)
    assert_equal(center.go('south'),south)

def test_map():
    start=Room("Start","You can go westy and down")
    west=Room("Trees","you can go start")
    down=Room("Dungeon","you can go start")

    start.add_paths({"west":west,"down":down})
    west.add_paths({"east":start})
    down.add_paths({'up':start})
    assert_equal(start.go('west'),west)
    assert_equal(west.go('east'),start)
    assert_equal(down.go('up'),start)
