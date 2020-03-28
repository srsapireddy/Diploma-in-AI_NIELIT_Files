#!/usr/bin/env python
import tensorflow as tf
x=tf.random.normal([3,2],mean=0.0,stddev=2.0,dtype=tf.dtypes.float32,seed=None,name=None)
sess=tf.Session()
print(sess.run(x))
sess.close()

