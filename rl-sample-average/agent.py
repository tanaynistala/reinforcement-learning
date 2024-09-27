#
# agent.py
# Tanay Nistala
# 2022-09-26
# 
# Epsilon-Greedy Agent Class
#

import numpy as np
import numpy.random as random
from environment import Environment

class Agent:
    def __init__(self, num_arms: int, e: float, a: float, q0: float = 0):
        # Parameters
        self.num_arms = num_arms
        self.e = e
        self.a = a

        # Value Function + Pull Counts
        self.Q = [ (random.normal() if q0 < 0 else q0) for _ in range(num_arms) ]
        self.N = [ 0 for _ in range(num_arms) ]

    def pull_arm(self, env: Environment):
        if (random.random() < self.e):
            # Random Policy
            arm = random.randint(self.num_arms)
        else:
            # Greedy Policy
            best_arms = np.argwhere(self.Q == np.max(self.Q)).reshape(-1)
            arm = random.choice(best_arms) if best_arms.size > 1 else best_arms[0]

        # Pull the arm and get the reward
        reward = env.pull(arm)

        # Update value function
        self.N[arm] += 1
        step_size = self.a if self.a > 0 else (1.0 / self.N[arm])
        self.Q[arm] += step_size * (reward - self.Q[arm])

