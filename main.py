from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


img_filename = input("please enter path of your image: ")

def histogram(image, pros_type):
    a = np.array(image.getdata())
    fig, ax = plt.subplots(figsize=(10,4))
    n,bins,patches = ax.hist(a, bins=range(256), edgecolor='none')
    ax.set_title("histogram")
    ax.set_xlim(0,255)
    cm = plt.cm.get_cmap('cool')
    norm = matplotlib.colors.Normalize(vmin=bins.min(), vmax=bins.max())
    for b,p in zip(bins,patches):
        p.set_facecolor(cm(norm(b)))
    plt.savefig('plots/input_plot.png') if pros_type == 1 else plt.savefig('plots/result_plot.png')


image = Image.open(img_filename)
histogram(image.convert(mode='L'), 1)
img_array = np.asarray(image.convert(mode='L'))
histogram_array = np.bincount(img_array.flatten(), minlength=256)
count_pixel = np.sum(histogram_array)
histogram_array = histogram_array / count_pixel
chistogram_array = np.cumsum(histogram_array)
transform_map = np.floor(255 * chistogram_array).astype(np.uint8)
image_to_list = list(img_array.flatten())
eq_imgage_list = [transform_map[i] for i in image_to_list]
eq_img_array = np.reshape(np.asarray(eq_imgage_list), img_array.shape)
eq_img = Image.fromarray(eq_img_array, mode='L')
eq_img.save('results/output.jpg')
histogram(eq_img, 2)