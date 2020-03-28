import tensorflow as tf
x=tf.constant(35,name='x1')
y=tf.constant(5,name='y1')
z=tf.add(x,y)
model=tf.global_variables_initializer()
with tf.Session() as session:
	session.run(model)
	print(session.run(z))
	writer=tf.summary.FileWriter('g1',session.graph)


