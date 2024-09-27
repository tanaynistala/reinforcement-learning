#
# environment.py
# Tanay Nistala
# 2022-09-26
# 
# Multi-Armed, Non-Stationary Bandit Environment
#

import numpy as np
import numpy.random as random

class Environment:
    def __init__(self, num_arms: int, mode: int = 1):
        """
        Mode 0: Zero initial values
        Mode 1: Random initial values
        """

        # Parameters
        self.num_arms = num_arms

        # Generators
        self.means = [ (0 if mode == 0 else random.normal()) for _ in range(num_arms) ]

        # Statistics
        self.total_reward = 0
        self.optim_pulls  = 0
        self.total_pulls  = 0

    def pull(self, arm: int) -> float:
        # Generate the reward
        reward = random.normal(self.means[arm])

        # Update statistics
        self.total_reward += reward
        self.optim_pulls  += 1 if arm == np.argmax(self.means) else 0
        self.total_pulls  += 1

        return reward
    
    def update(self, mode: int = 0) -> None:
        if mode == 0:
            # No change
            return
        elif mode == 1:
            # Random walk (best arm only)
            best_arm = np.argmax(self.means)
            self.means[best_arm] += random.normal(0, 0.01)
        elif mode == 2:
            # Random walk (all arms)
            for i in range(self.num_arms):
                self.means[i] += random.normal(0, 0.01)

    
    def get_optimal_pulls_pct(self) -> float:
        return self.optim_pulls / self.total_pulls * 100

    def get_average_reward(self) -> float:
        return self.total_reward / self.total_pulls