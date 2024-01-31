from vacuum_grid import VacuumGrid
from vacuum_planning_agent_program import VacuumPlanningAgentProgram
from environments import Agent

env = VacuumGrid(10, 10)
agent = Agent(VacuumPlanningAgentProgram())
env.add_thing(agent)
env.run()
print('Final State')
agent.program.show_state()
