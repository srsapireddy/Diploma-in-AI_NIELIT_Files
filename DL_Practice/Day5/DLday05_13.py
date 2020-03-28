#!/usr/bin/env python
import tensorflow as tf

X=tf.constant([[-1,-2,-3],[0,1,2]], tf.int32)  
Y=tf.zeros(X.shape, tf.int32) 
out= tf.not_equal(X, Y)
sess=tf.Session()
output=sess.run(out)
print(output)
sess.close()
