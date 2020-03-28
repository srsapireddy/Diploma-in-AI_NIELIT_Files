#!/usr/bin/env python
import tensorflow as tf
x= tf.zeros([2,3],tf.int32)
sess=tf.Session()
print(sess.run(x))
