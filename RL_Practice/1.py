import gym;
env = gym.make('Taxi-v2');
env.reset();
env.render();
env.env.s = 114;
env.render();
env.step(0);
env.render();
state,reward,done,info = env.step(0);
env.render();
print(state);
print(reward);
print(done);

env.env.s = 114;
env.render();
state,reward,done,info = env.step(1);
env.render();
print(state);
print(reward);
print(done);

env.env.s = 115;
env.render();
state,reward,done,info = env.step(2);
env.render();
print(state);
print(reward);
print(done);

env.env.s = 116;
env.render();
state,reward,done,info = env.step(3);
env.render();
print(state);
print(reward);
print(done);

env.env.s = 117;
env.render();
state,reward,done,info = env.step(0);
env.render();
print(state);
print(reward);
print(done);

env.env.s = 118;
env.render();
state,reward,done,info = env.step(1);
env.render();
print(state);
print(reward);
print(done);


