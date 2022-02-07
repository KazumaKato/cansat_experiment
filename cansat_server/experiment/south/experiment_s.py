import red_detect_lib as red
import matplotlib.pyplot as plt


occ_list = []
distance_list = []
for i in (200, 250, 300, 320, 340, 360, 380, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000):
    image = f's{i}.jpg'
    occ = red.occ_get(image)
    occ_list.append(occ)
    distance_list.append(i/100)

print (occ_list, distance_list)

plt.plot(distance_list,occ_list,marker='.')
plt.xlim(0, 10)
plt.ylim(0, 0.3)
plt.savefig('result_s.jpg')