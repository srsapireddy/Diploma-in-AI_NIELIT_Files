import tensorflow as tf
a=tf.constant(35,name='a1')
b=tf.constant(5,name='b1')
c=tf.add(a,b,name='c1')
d=tf.constant(3,name='d1')
e=tf.add(c,d,name="e1")
model=tf.global_variables_initializer()
with tf.Session() as session:
	session.run(model)
	print(session.run(e))
	writer=tf.summary.FileWriter('g2',session.graph)


