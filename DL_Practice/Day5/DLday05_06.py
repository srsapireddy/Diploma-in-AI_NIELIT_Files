#!/usr/bin/env python
import tensorflow as tf
x=tf.constant([[1,3,5],[4,6,8]],dtype='float32')
sess=tf.Session()
print(sess.run(x))

