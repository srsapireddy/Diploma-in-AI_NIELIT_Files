import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist =input_data.read_data_sets("/tmp/data/",one_hot=True)
Xtr,Ytr=mnist.train.next_batch(5000)
Xte,Yte=mnist.test.next_batch(10)
print(Xtr.shape)
xtr=tf.placeholder("float",[5000,784])
xte=tf.placeholder("float",[784])

distance=tf.reduce_sum(tf.abs(tf.add(xtr,tf.negative(xte))),1)
pred=tf.arg_min(distance,0)
print(pred)
accuracy=0.
init=tf.global_variables_initializer()

sess=tf.Session()
sess.run(init)
for i in range(len(Xte)):
	nn_index=sess.run(pred,feed_dict={xtr:Xtr,xte:Xte[i,:]})
	print(nn_index)
	print("Prediction",np.argmax(Ytr[nn_index]))
	print("True Class",np.argmax(Yte[i]))
	




