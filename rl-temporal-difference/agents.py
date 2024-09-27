import numpy as np
import numpy.random as rnd

ACTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class SarsaAgent:
    def __init__(self, alpha, epsilon, env):
        self.Q = np.zeros((env.height, env.width, 4))
        self.Q[env.goal_state] = 0

        self.alpha = alpha
        self.epsilon = epsilon

    def get_action(self, state, actions=ACTIONS, greedy=False):
        if greedy or (rnd.rand() >= self.epsilon):
            return np.argmax(self.Q[state[0], state[1]])
        else:
            return rnd.randint(len(actions))

    def update(self, state, action, reward, next_state, next_action):
        self.Q[state[0], state[1], action] += self.alpha * (reward + self.Q[next_state[0], next_state[1], next_action] - self.Q[state[0], state[1], action])

class QLearningAgent:
    def __init__(self, alpha, epsilon, env):
        self.Q = np.zeros((env.height, env.width, 4))
        self.Q[env.goal_state] = 0

        self.alpha = alpha
        self.epsilon = epsilon

    def get_action(self, state, actions=ACTIONS, greedy=False):
        if greedy or (rnd.rand() >= self.epsilon):
            return np.argmax(self.Q[state[0], state[1]])
        else:
            return rnd.randint(len(actions))

    def update(self, state, action, reward, next_state, _):
        self.Q[state[0], state[1], action] += self.alpha * (reward + np.max(self.Q[next_state[0], next_state[1]]) - self.Q[state[0], state[1], action])

class ExpectedSarsaAgent:
    def __init__(self, alpha, epsilon, env):
        self.Q = np.zeros((env.height, env.width, 4))
        self.Q[env.goal_state] = 0

        self.alpha = alpha
        self.epsilon = epsilon

    def get_action(self, state, actions=ACTIONS, greedy=False):
        if greedy or (rnd.rand() >= self.epsilon):
            return np.argmax(self.Q[state[0], state[1]])
        else:
            return rnd.randint(len(actions))

    def update(self, state, action, reward, next_state, _):
        self.Q[state[0], state[1], action] += self.alpha * (reward + self.epsilon * np.sum(self.Q[next_state[0], next_state[1]]) + (1 - self.epsilon) * np.max(self.Q[next_state[0], next_state[1]]) - self.Q[state[0], state[1], action])