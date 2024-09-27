import numpy as np

ACTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
WIND    = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

class CliffWalk:
    def __init__(self, height=4, width=12, start_state=(3, 0), goal_state=(3, 11), actions=ACTIONS):
        self.height      = height
        self.width       = width
        self.start_state = start_state
        self.goal_state  = goal_state
        self.actions     = actions

        self.reset()

    def reset(self):
        self.state = self.start_state
        return self.state

    def step(self, action_index):
        action = self.actions[action_index]
        next_state = (self.state[0] + action[0], self.state[1] + action[1])
        next_state = (np.clip(next_state[0], 0, self.height - 1), np.clip(next_state[1], 0, self.width - 1))

        reward = -1
        done = False

        if self.state[0] == self.height - 1 and self.state[1] > 0 and self.state[1] < self.width - 1:
            next_state = self.start_state
            reward = -100

        self.state = next_state
        done = next_state == self.goal_state
        return self.state, reward, done

    def render(self):
        grid = np.zeros((self.height, self.width))
        grid[self.goal_state] = 0.9
        grid[self.height - 1, 1:self.width - 1] = 0.25
        grid[self.state] = 0.5

        return grid

OBSTACLES = [
    (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10)
]

BONUSES = [
    # (1, 2), (1, 6), (1, 10)
    (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10)
]

class ObstacleCourse:
    def __init__(self, height=4, width=12, start_state=(3, 0), goal_state=(3, 11), actions=ACTIONS, obstacles=OBSTACLES, bonuses=BONUSES):
        self.height      = height
        self.width       = width
        self.start_state = start_state
        self.goal_state  = goal_state
        self.actions     = actions

        self.obstacles   = obstacles
        self.bonuses     = bonuses
        self.active_bonuses = bonuses.copy()

        self.reset()

    def reset(self):
        self.state = self.start_state
        return self.state

    def step(self, action_index):
        action = self.actions[action_index]
        next_state = (self.state[0] + action[0], self.state[1] + action[1])
        next_state = (np.clip(next_state[0], 0, self.height - 1), np.clip(next_state[1], 0, self.width - 1))

        reward = -1
        done = False

        if self.state in self.obstacles:
            next_state = self.start_state
            reward = -100
        elif self.state in self.active_bonuses:
            reward = 100
            self.active_bonuses.remove(self.state)

        self.state = next_state
        done = next_state == self.goal_state
        return self.state, reward, done

    def render(self):
        grid = np.zeros((self.height, self.width))
        grid[:,:] = 0.25
        grid[self.goal_state] = 0.9
        for obstacle in self.obstacles:
            grid[obstacle] = 0
        for bonus in self.bonuses:
            grid[bonus] = 0.75
        grid[self.state] = 0.5

        return grid