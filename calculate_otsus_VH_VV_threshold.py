# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 13:15:19 2022

@author: FALAH FAKHRI


Model calculate_otsus_VH_VV_threshold.py
==============================================================================================================================================
This model has been extracted and edited from the following two resources,
 
https://muthu.co/otsus-method-for-image-thresholding-explained-and-implemented/

https://scikit-image.org/docs/0.12.x/auto_examples/segmentation/plot_local_otsu.html

In order to calculate the VH, and VV threshold of Interferometric Wide Swath IW, Ground Range Detected High Resolution (HR) GRDHR, 

https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-1-sar/products-algorithms/level-1-algorithms/ground-range-detected/iw

But a preperation to an image is needed beforehand, 

running this model, the preperation is mentioned within this repository as well under the name, 

Intensity_GRD.xml, it's possible to run this *.xml file suing SNAP, or using gpt luncher in the

other repository within my github in the following link,

https://github.com/falahfakhri-Iraq/gpt_launcher/blob/main/gpt_launcher.py 

==============================================================================================================================================
"""

try:
    import time
    import rasterio as rio
    from skimage.morphology import disk
    from skimage.filters import threshold_otsu, rank
    from skimage.util import img_as_ubyte
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.rcParams['font.size'] = 9
    import sys
    from termcolor import colored
    
except ModuleNotFoundError:
    print('Module improt error')
    sys.exit()
else:
    print(colored('\nAll libraries properly loaded. Ready to start!!!', 'green'), '\n')    

def Otsus_VH_VV_thr(input_file_path:str):
        
    """Returns thresshold of VH, or VV
    parameters
    ----------
    input_file_path: str
        path directory to VH or VV with tif extension file'
    
    """
    start_time = time.time()
    
    vvvh = rio.open(input_file_path)
    
    print('layer_count\n:', vvvh.count)
    print('layer_shape\n: ', vvvh.shape)
    print('layer_type\n:', vvvh.dtypes)
    print('Lyer_NAN\n:', vvvh.nodatavals)

    vvvh = vvvh.read()

    img = img_as_ubyte(vvvh)

    print('Layer_shape_after_converted_to_unit8',img.shape)

    img = img[0, :, :]

    radius = 15

    selem = disk(radius)

    local_otsu = rank.otsu(img, selem)

    threshold_global_otsu = threshold_otsu(img)

    print('The layer threshold is\n:',threshold_global_otsu)

    global_otsu = img >= threshold_global_otsu


    fig, ax = plt.subplots(2, 2, figsize=(8, 5), sharex=True, sharey=True,
                           subplot_kw={'adjustable': 'box'})
    ax0, ax1, ax2, ax3 = ax.ravel()
    plt.tight_layout()


    fig.colorbar(ax0.imshow(img, cmap=plt.cm.gray),
                 ax=ax0, orientation='horizontal')
    ax0.set_title('Original')
    ax0.axis('off')

    fig.colorbar(ax1.imshow(local_otsu, cmap=plt.cm.gray),
                 ax=ax1, orientation='horizontal')
    ax1.set_title('Local Otsu (radius=%d)' % radius)
    ax1.axis('off')

    ax2.imshow(img >= local_otsu, cmap=plt.cm.gray)
    ax2.set_title('Original >= Local Otsu' % threshold_global_otsu)
    ax2.axis('off')

    ax3.imshow(global_otsu, cmap=plt.cm.gray)
    ax3.set_title('Global Otsu (threshold = %d)' % threshold_global_otsu)
    ax3.axis('off')

    plt.show()
    
    end_time = time.time()
    hours, rem = divmod(end_time-start_time, 3600)
    minutes, seconds = divmod(rem, 60)
    
    if __name__ == '__main__':
        print("Total time is: \n", "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

    