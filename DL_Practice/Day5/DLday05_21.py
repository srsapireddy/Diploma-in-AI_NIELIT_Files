#!/usr/bin/env python
import tensorflow as tf

x = tf.Variable(initial_value=1.0, name='x')
y = tf.Variable(initial_value=1.0, name='y')
z = tf.Variable(initial_value=1.0, name='z')

x = x.assign(1)
y = y.assign(2)
z = z.assign(3)

out = tf.add_n([x, y, z])

tf.global_variables_initializer()

sess = tf.Session()
output = sess.run(out)
print(output)
sess.close()

