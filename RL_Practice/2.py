import gym;
env = gym.make('Taxi-v2');
env.reset();
env.render();
env.env.s = 114;
env.render();
env.step(0);
env.render();
state,reward,done,info = env.step(2);
env.render();
print(state);
print(reward);
print(done);
print(info);
env.step(2);
env.render();
env.step(2);
env.render();
env.step(0);
env.render();
env.step(0);
env.render();
env.step(4);
env.render();
env.step(1);
env.render();
env.step(1);
env.render();
env.step(3);
env.render();
env.step(3);
env.render();
env.step(3);
env.render();
env.step(0);
env.render();
env.step(0);
env.render();
state,reward,done,info =env.step(5);
env.render();
print(state);
print(reward);
print(done);

