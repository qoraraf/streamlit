import streamlit as st
import gym
from stable_baselines3 import PPO

def create_environment_and_agent():
    env = gym.make('CartPole-v1')
    model = PPO("MlpPolicy", env, verbose=1)
    return env, model

def train_agent(env, model, timesteps):
    model.learn(total_timesteps=timesteps)
    return model

def test_agent(env, model, episodes):
    for episode in range(episodes):
        obs = env.reset()
        done = False
        score = 0
        while not done:
            action, _states = model.predict(obs, deterministic=True)
            obs, reward, done, info = env.step(action)
            score += reward
        st.write(f"Episode: {episode + 1}, Score: {score}")
        
def main():
    st.title("Stable Baselines and Streamlit Example")
    timesteps = st.sidebar.slider("Training Timesteps", 1000, 10000, 5000, step=1000)
    test_episodes = st.sidebar.slider("Test Episodes", 1, 10, 5, step=1)

    if st.button("Train and Test Agent"):
        st.write("Training the agent...")
        env, model = create_environment_and_agent()
        model = train_agent(env, model, timesteps)
        st.write("Testing the agent...")
        test_agent(env, model, test_episodes)

if __name__ == "__main__":
    main()
