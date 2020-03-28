import tensorflow as tf
p1=tf.placeholder(tf.float32)
p2=tf.placeholder(tf.float32)
p3=tf.placeholder(tf.float32)

print(p1)

psum=tf.add_n([p1,p2,p3])
print(psum)
sess= tf.Session()
print(sess.run(psum,feed_dict={p1:100,p2:200,p3:300}))
sess.close()
