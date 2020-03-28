#!/usr/bin/env python
import tensorflow as tf

X=tf.random_normal([10,10,3],mean=0.0,stddev=2.0)
z=tf.random_crop(
    X,[5,5,3])
  

sess=tf.Session()
output=sess.run(z)
print(output)
sess.close()
