#!/usr/bin/env python
import tensorflow as tf
a=tf.random_uniform([3,2],minval=0,maxval=2)
sess=tf.Session()
print(sess.run(a))
sess.close()
