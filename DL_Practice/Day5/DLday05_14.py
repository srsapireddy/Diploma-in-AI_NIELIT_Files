#!/usr/bin/env python
import tensorflow as tf
x=tf.constant([4,3,2])
y=tf.constant([3,2,1])
z=tf.constant([1,1,1])

out=tf.add(x,y)
dot=tf.tensordot(x,y,1)
sub=tf.subtract(x,y,name=None)
add=tf.add(out,z)
sm=tf.multiply(x,5)
sess=tf.Session()
print(sess.run(out))
print(sess.run(dot))
print(sess.run(sub))
print(sess.run(add))
print(sess.run(sm))
sess.close()

