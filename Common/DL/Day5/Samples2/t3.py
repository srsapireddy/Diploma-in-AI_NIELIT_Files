import tensorflow as tf
x=tf.constant(35,name='x1')
p=tf.constant(5,name='y1')
k=tf.add(x,p,name='k1')
z=tf.add(k,3,name='z1')
model=tf.global_variables_initializer()
with tf.Session() as session:
	session.run(model)
	print(session.run(z))
	writer=tf.summary.FileWriter('g5',session.graph)


