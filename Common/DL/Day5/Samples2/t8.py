import tensorflow as tf
x=tf.zeros([3,4],tf.int32)
y=tf.zeros_like([[2,3],[2,5],[4,5]],tf.int32)
sess=tf.Session()
print(sess.run(x))

print(sess.run(y))
x=tf.ones([3,4],tf.int32)
y=tf.ones_like([[2,3],[2,5],[4,5]],tf.int32)
print(sess.run(x))
print(sess.run(y))
