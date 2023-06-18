
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.axis('off')

img_idx = '2'

img = cv2.imread('/ailab_mat/dataset/MetaGraspNet/dataset_sim/'+image_fn)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



## save image
plt.imshow(img); plt.savefig(f'/ailab_mat/personal/rho_heeseon/graduation/part1/InstaOrder+Meta/{img_idx}_image.png')



## save bbox
fig, ax = plt.subplots()
ax.imshow(img)
plt.axis('off')
for box in bboxes:
    print(box)
    rect = patches.Rectangle((box[0], box[1]), box[2], box[3], linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
plt.show(); plt.savefig(f'/ailab_mat/personal/rho_heeseon/graduation/part1/InstaOrder+Meta/{img_idx}_gt_box.png', bbox_inches='tight',transparent=True, pad_inches=0);




## save mask
for i, mask in enumerate(modal):
    plt.imshow(mask); plt.savefig(f'/ailab_mat/personal/rho_heeseon/graduation/part1/InstaOrder+Meta/{img_idx}_modal{i}.png', bbox_inches='tight',transparent=True, pad_inches=0)


f = open(f'/ailab_mat/personal/rho_heeseon/graduation/part1/InstaOrder+Meta/{img_idx}_rel_mat.txt', 'w')
f.write(f'gt_rel_mat\n{gt_occ_matrix}')
f.close()


