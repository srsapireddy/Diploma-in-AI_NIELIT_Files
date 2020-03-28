#!/usr/bin/env python
import tensorflow as tf
X=tf.constant([[1,2,3],[4,5,6]],dtype=tf.int32)
y=tf.zeros(tf.shape(X),X.dtype,name="Y")
sess=tf.Session()
print(sess.run(y))

