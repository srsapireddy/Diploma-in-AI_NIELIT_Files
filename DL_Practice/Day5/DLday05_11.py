#!/usr/bin/env python
import tensorflow as tf

X=tf.constant([[1,2,3],[4,5,6]], tf.int16)
z=tf.random_shuffle(
    X,
    seed=None,
    name=None
)

sess=tf.Session()
output=sess.run(z)
print(output)
sess.close()
