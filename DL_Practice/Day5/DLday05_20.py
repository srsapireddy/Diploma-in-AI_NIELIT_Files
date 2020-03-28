#!/usr/bin/env python
import tensorflow as tf

w = tf.Variable(initial_value=1.0, name='w')
w=w.assign(1)
sess = tf.Session()
output = sess.run(w)
print(output)
sess.close()
