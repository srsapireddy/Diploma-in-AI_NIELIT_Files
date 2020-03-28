import tensorflow as tf
a=tf.placeholder(tf.float32)
b=tf.constant(5,tf.float32)
c=a+b
with tf.Session() as sess:
	print(sess.run(c,feed_dict={a: 1}))


