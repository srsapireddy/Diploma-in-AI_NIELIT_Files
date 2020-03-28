#!/usr/bin/env python
import tensorflow as tf

p = tf.placeholder(tf.float32)

sess = tf.Session()
output = sess.run(p, feed_dict = {p : 5})
print(output)
sess.close()
