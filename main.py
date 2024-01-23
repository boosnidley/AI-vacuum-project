from environments import TrivialVacuumEnvironment
from agent_programs import model_based_vacuum_agent

env = TrivialVacuumEnvironment()
vacuum = model_based_vacuum_agent()
env.add_thing(vacuum)

print(f'env status: {env.status}')
env.run()
print(f'perf. score = {vacuum.performance}')
print(f'env status: {env.status}')
