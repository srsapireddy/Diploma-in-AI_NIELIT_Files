import tensorflow as tf
x=tf.constant(5,name='x1')
y=tf.constant(4,name='y1')

z=tf.add(x,y,name="z1")

#model=tf.global_variables_initializer()
sess=tf.Session()
#sess.run(model)
print(sess.run(z))

#writer=tf.summary.FileWriter("g3",sess.graph)
#writer.close()




