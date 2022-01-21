# Otsus-method-for-GRDHR-VH-VV-thresholding
Calculate the VH, VV threshold of GRDHR VH, and VV
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

It's worth mentioning that, 

Thresholding works best when backscatter tiles are provided on a decibel scale 
to get Gaussian distribution that is scaled to a range of 0-255, 
and performed on a small tile that is likely to have a transition between water and not water.

Implement the model.
--------------------
dirpath = 'D://WATER_MAP_TEST/'
vv = dirpath + 'VV/S1A_IW_GRDH_1SDV_20210324T191554_045F93_21DF_VV_NR_Orb_TC_res.tif'   
vh = dirpath + 'VH/S1A_IW_GRDH_1SDV_20210324T191554_045F93_21DF_VH_NR_Orb_TC_res.tif'
Otsus_VH_VV_thr(vh)
Otsus_VH_VV_thr(vh)
layer_count
: 1
layer_shape
:  (21494, 25689)
layer_type
: ('float32',)
Lyer_NAN
: (None,)
Layer_shape_after_converted_to_unit8 (1, 21494, 25689)
The layer threshold is
: 18
Total time is: 
 00:07:01.82


