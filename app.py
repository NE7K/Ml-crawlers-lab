리스트 = ['삼성전자', '카카오', '네이버', '신풍제약']
f = open('z.txt', 'w')
for i in range(4):
    for x in range(4):
        f.write( 리스트[x] + '\n')
f.close()