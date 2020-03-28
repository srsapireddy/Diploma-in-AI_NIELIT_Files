import tensorflow as tf
x=tf.linspace(10.0,20.0,3,name="l")
p=tf.range(10,40,2)

sess=tf.Session()
print(sess.run(x))

