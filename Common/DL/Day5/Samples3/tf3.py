import tensorflow as tf
x=tf.constant(5,name='x1')
y=tf.Variable(x+5,name="y1")


model=tf.global_variables_initializer()
sess=tf.Session()
sess.run(model)
print(sess.run(y))

#writer=tf.summary.FileWriter("g3",sess.graph)
#writer.close()




