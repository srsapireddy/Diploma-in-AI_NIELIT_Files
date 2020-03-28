import tensorflow as tf
x=tf.Variable(0,name="y1")


model=tf.global_variables_initializer()
sess=tf.Session()
sess.run(model)
for i in range(5):
	x=x+1
	print(sess.run(x))




