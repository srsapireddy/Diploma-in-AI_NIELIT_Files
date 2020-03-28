#!/usr/bin/env python
import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = tf.placeholder(tf.float32)

x = tf.add_n([a, b, c])

sess = tf.Session()
output = sess.run(x, feed_dict = {a:3, b:5, c:7})
print(output)
sess.close()
