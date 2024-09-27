# README

The code for the project is included in `code.zip`, which contains the following files:

* `environment.py`: Contains the environment class for the multi-armed bandit
* `agent.py`: Contains the agent class for the multi-armed bandit
* `project1.ipynb`: Contains the code for the experiments and plots in the report

The project uses the `numpy` and `matplotlib` libraries. The code was tested with Python 3.9.6. As with most Python notebooks, Jupyter is required to run the code in the notebook.

To run the code, one may simply run the included notebook. Alternatively, the environment and agent classes may be used as follows:

```python
from environment import Environment
from agent import Agent

# Create environment
env = Environment(num_arms=10, mode=1)

# Create agent
agent = Agent(num_arms=10, e=0.1, a=0.1, q0=0)

# Run agent
for step in range(1000):
    agent.pull_arm(env)
```