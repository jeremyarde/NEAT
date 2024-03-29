import gym

env = gym.make("CartPole-v1")
observation = env.reset()


def test_population(population):
    # results = []
    # networks = [create_network(g) for g in population]

    for _ in population:
        # observation = [0,0,0,0,]/
        fitness = 0
        for _ in range(1000):
            env.render()
            action = env.action_space.sample()  # your agent here (this takes random actions)
            # action = network.feed(observation) # your agent here (this takes random actions)
            observation, reward, done, info = env.step(action)
            fitness += reward

            if done:
                pass
        # results.append((network, fitness))

    env.close()


# g1 = GenomeFactory.create_genome(4,2)
# pop = create_population(g1)


def test_gym():
    import gym
    env = gym.make("CartPole-v1")
    for _ in range(1000):
        env.render()
        action = env.action_space.sample()  # your agent here (this takes random actions)
        observation, reward, done, info = env.step(action)

        if done:
            pass
    env.close()


test_gym()
