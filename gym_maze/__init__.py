from gym.envs.registration import register

register(
    id='maze-v0',
    entry_point='gym_maze.envs:mazeEnv',
)
register(
    id='maze-extrahard-v0',
    entry_point='gym_maze.envs:mazeExtraHardEnv',
)
