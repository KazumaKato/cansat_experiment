import red_detect_lib as red
import matplotlib.pyplot as plt


occ_list = []
distance_list = []
for i in range(4, 51):
    image = f'{i}.jpg'
    #red.image_output(red.red_masks_get(f'{i}.jpg'),f'red{i}.jpg')
    occ = red.occ_get(image)
    occ_list.append(occ)
    distance_list.append(i/10)

print (occ_list, distance_list)

WSIZE = 5

occ_list_2 = []
for i in range(len(occ_list)):
    s = 0
    n = 0
    for j in range(i-WSIZE//2,i+WSIZE//2+1):
        if j>=0 and j<len(occ_list):
            s = s + occ_list[j]
            n = n + 1
    occ_list_2.append(s/n)


plt.plot(distance_list,occ_list,marker='.', color = 'blue')
plt.plot(distance_list,occ_list_2,marker='.', color = 'orange')
plt.savefig('result_i.jpg')


