import tensorflow as tf

# tensor 자료형
tensor = tf.constant([1, 3, 2])
tensor2 = tf.constant([-1, 2, 2])

# 행렬 ㄱㄴ
tensor3 = tf.constant([[2, 3], [2, 1]])

print(tensor + tensor2)

# note tf.subtract, tf.divide, tf.multiply도 존재, 행렬의 곱은 tf.matmul 
data = tf.add(tensor, tensor2)

print(data)

# 0이 10개
tf.zeros(10)
print(tf.zeros( [2, 2, 3] ))

# info 데이터를 해석할 때에는 뒤에서부터 해석 (2,3)이면 3개의 데이터를 갖는 2개의 행렬
print(tensor.shape)

# df cast는 데이터 타입 변경 가능

# w 값 : weight, print해보고 싶을 때에는 numpy사용
w = tf.Variable(1.0)
# Variable Fix
w = w.assign(2)
print(w.numpy())