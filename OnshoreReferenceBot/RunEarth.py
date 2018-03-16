import random
import sys
import traceback
import battlecode as bc

from MapController import MapController
from PathfindingController import PathfindingController
from UnitController import UnitController
from MissionController import MissionController
from UnitController import UnitController


class RunEarth:
    """This is how we run Earth"""
    # Initialize controllers
    # Initialize all class variables
    # Only include code that should be initialized once at the beginning of the match
    def __init__(self, gameController):
        self.game_controller = gameController
        self.map_controller = MapController(gameController)
        # self.enemy_tracking_controller = EnemyTrackingController(gameController)
        # self.strategy_controller = StrategyController(gameController, \
        # self.map_controller, self.enemy_tracking_controller)
        # self.research_tree_controller = ResearchTreeController(gameController, \
        # self.strategy_controller)
        # self.build_controller = BuildController(gameController, self.map_controller, \
        # self.strategy_controller)
        self.pathfinding_controller = PathfindingController(gameController, self.map_controller)
        self.mission_controller = MissionController(gameController, self.map_controller)
        self.unit_controller = UnitController(gameController, self.pathfinding_controller, self.mission_controller, self.map_controller)
        # self.targetting_controller = TargettingController(gameController, \
        # self.map_controller, self.strategy_controller, self.unit_controller, self.enemy_tracking_controller)
        self.game_controller.queue_research(bc.UnitType.Rocket)
        self.game_controller.queue_research(bc.UnitType.Ranger)
        self.game_controller.queue_research(bc.UnitType.Ranger)
        self.game_controller.queue_research(bc.UnitType.Ranger)
        self.game_controller.queue_research(bc.UnitType.Worker)
        self.game_controller.queue_research(bc.UnitType.Worker)
        self.game_controller.queue_research(bc.UnitType.Worker)
        self.game_controller.queue_research(bc.UnitType.Worker)

    # Runs once per turn for this planet only
    def Run(self):
        """This runs on Earth once per turn"""
        print("Karbonite: {}".format(self.game_controller.karbonite()))
        self.round = self.game_controller.round()
        if self.round == 1:
            print("First round on Earth.  Initializing map")
            self.map_controller.InitializeEarthMap()
            print("First round on Mars.  Initializing map")
            self.map_controller.InitializeMarsMap()

        else:
            print("Round {}".format(self.round))

        #print("Update research queue")
        # self.research_tree_controller.update_queue()

        #print("Updating units.  Synching between game units and player entities.")
        self.unit_controller.update_units()

        #print("Running all units")
        self.unit_controller.run_units()
