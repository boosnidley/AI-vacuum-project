
from environments import XYEnvironment, Wall, Obstacle, Dirt, Agent
import random


class VacuumGrid(XYEnvironment):
    def __init__(self, width, height):
        super().__init__(width, height)

        # walls around the exterior
        self.add_walls()

        # arrange some obstacles.
        for i in range(1, width // 2):
            self.add_thing(Obstacle(), (i, 3))
            self.add_thing(Obstacle(), (width - i - 1, height - 4))

        # toss in some dirt
        for _ in range(width * height // 4):
            self.add_thing(Dirt(), (random.randrange(1, width - 1), random.randrange(1, height - 1)), empty_only=True)

    def thing_classes(self):
        return [Wall, Dirt, Obstacle, Agent]

    def percept(self, agent):
        # the agent can see the entire environment. How does this work:
        return {
            'agent': self.agents[0].location,
            'obstacles': [o.location for o in self.things if isinstance(o, Obstacle)],
            'dirts': [d.location for d in self.things if isinstance(d, Dirt)]
        }

    def execute_action(self, agent, action):
        if action == 'Suck':
            dirt_list = self.list_things_at(agent.location, Dirt)
            if dirt_list:
                dirt = dirt_list[0]
                agent.performance += 1
                self.delete_thing(dirt)
        else:
            new_loc = None
            if action == 'Left':
                new_loc = (agent.location[0]-1, agent.location[1])
            elif action == 'Right':
                new_loc = (agent.location[0]+1, agent.location[1])
            elif action == 'Up':
                new_loc = (agent.location[0], agent.location[1]+1)
            elif action == 'Down':
                new_loc = (agent.location[0], agent.location[1]+1)

            if new_loc and (not self.some_things_at(new_loc, Obstacle)
                            and not self.some_things_at(new_loc, Wall)):
                agent.location = new_loc
