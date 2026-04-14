import gymnasium as gym
import numpy as np



env = gym.make("CartPole-v1", render_mode="rgb_array")
obs, _ = env.reset(seed=123)

total_reward = 0
for i in range(500):
    env.render()
    
    if obs[2] + obs[3] > 0:
        action = 1
    else:
        action = 0
    

    obs, reward, terminated, truncated, _ = env.step(action)
    total_reward = total_reward + reward
    if terminated or truncated:
        break

env.close()
print(f"Score: {total_reward}")