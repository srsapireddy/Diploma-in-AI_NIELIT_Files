import tensorflow as tf
#x=tf.ones_like([[2,4],[4,5]],tf.int32)
#x=tf.ones([2,4],tf.int32)
#x=tf.linspace(10.0,20.0,4)
x=tf.range(10,40,2)
sess =tf.Session()
print(sess.run(x))

sess.close()

