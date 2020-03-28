import tensorflow as tf
a=tf.placeholder(tf.float32,shape=[3])
b=tf.constant([5,5,5],tf.float32)
c=a+b
with tf.Session() as sess:
	print(sess.run(c,feed_dict={a:[1,2,3]}))
	

x=tf.placeholder(tf.float32)
x=tf.add(2,3)
c=tf.multiply(x,3)
with tf.Session() as sess:
	print(sess.run(c))
	print(sess.run(c,feed_dict={x:15}))

