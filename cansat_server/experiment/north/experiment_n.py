import red_detect_lib as red
import matplotlib.pyplot as plt


occ_list = []
distance_list = []
for i in range(50, 1050, 50):
    image = f'n{i}.jpg'
    red.image_output(red.red_masks_get(f'n{i}.jpg'),f'red_n{i}.jpg')
    occ = red.occ_get(image)
    occ_list.append(occ)
    distance_list.append(i/100)

print (occ_list, distance_list)

plt.plot(distance_list,occ_list,marker='.')
plt.xlim(0, 10)
plt.ylim(0, 0.3)
plt.savefig('result_n.jpg')