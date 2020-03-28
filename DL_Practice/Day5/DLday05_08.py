#!/usr/bin/env python
import tensorflow as tf
start=5 
limit=10
delta=0.0816
x=tf.range(start,limit,delta)
sess=tf.Session()
print(sess.run(x))
sess.close()

