import tensorflow as tf
a=tf.constant(5,name="a")
b=tf.constant(6,name="b")
c=tf.add(a,b, name="add")
print(c)
sess=tf.Session()
output=sess.run(c)
print(output)

writer=tf.summary.FileWriter('b1',sess.graph)
writer.close()
sess.close()


