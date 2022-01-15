dice1=(1,2,3,4,5,6)
dice2=(2,3,5,7,11,13)

dice_sum=set()

#i로 인덱스 바로 읽어오잖아~~
for i in dice1:
    for k in dice2:
        dice_sum.add(i+k)

print(dice_sum)