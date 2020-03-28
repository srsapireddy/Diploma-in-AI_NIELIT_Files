#!/usr/bin/env python
import tensorflow as tf
x=tf.ones([3,2],dtype='int32')
y=tf.constant(5,dtype='int32')
res=tf.multiply(x,y)
sess=tf.Session()
print(sess.run(res))
