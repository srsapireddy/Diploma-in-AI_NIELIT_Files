#!/usr/bin/env python
import tensorflow as tf
x= tf.constant([[1,2,3],[4,5,6]],dtype=tf.int32)
sess=tf.Session()
print(sess.run(x))
tf.shape(x)
tf.rank(x)

