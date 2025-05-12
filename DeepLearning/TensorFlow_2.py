import tensorflow as tf

size = [150, 160, 170, 180]
ssize = [152, 162, 172, 182]

# w 값
x1 = tf.Variable(0.1)
x2 = tf.Variable(0.5)

# optimizer : 손실값을 최소화하기 위해서 w값을 어떻게 업데이트할건지 결정하는 알고리즘
# learning rate : w값을 변경할 때 어느 정도로 바꿀지
opt = tf.keras.optimizers.Adam(learning_rate=0.001)

for i in range(1000):
    # 기울기, 손실계산식을 넣으면 알아서 미분해줌, tape에 기울기가 담겨져 있음
    with tf.GradientTape() as tape:
        prediction = size * x1 + x2
        loss = (prediction - ssize)**2
        # loss 값이 list기 때문에 4개의 loss 값 생성 그래서 평균을 내주고 그걸 다시 저장해서 사용
        loss = tf.reduce_mean(loss)
        
    # 기울기 출력
    data = tape.gradient(loss, [x1, x2])
    # print(data)

    # info 역전파, local minimum을 피하기 위해서 0.0001곱하기
    # x1.assign_sub(data[0] * 0.00001)
    # x2.assign_sub(data[1] * 0.00001)
    
    # info 계산된 기울기를 x1, x2. 즉, w 값에 업데이트해줌
    opt.apply_gradients([[data[0], x1], [data[1], x2]])
    print(x1.numpy(), x2.numpy())

