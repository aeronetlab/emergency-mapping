Emergency-mapping
-----------------

*"Emergenсy mapping"* is a deeplearning method to detect damaged buildings in remote sensing imagery. Automatic mapping and detection is needed to reduce the time for decision making and response.

# California 2017

Here are some useful utils and a sample pipeline for dataset of California region where a lot of buildings were destroyed by wildfires in 2017.

Utils allow to read and write the files (data_handling.py), and also contain a simple convolutional network on Keras (unet.py) with a generator for training and validation, and a Jupyter notebook with a sample pipeline of the data processing.

Datataset is based on Opendata DigitalGlobe (Maxar) imagery and is available for [download](https://minio.aeronetlab.space/public/datasets/emergency/California_2017.zip).

The dataset contains satellite imagery before and after the events and a labeled data.

Data:
1. Images with the labels:
- ventura_train
- santa_rosa_train

contain 2 RGB images (pre- and post- event) organized in 3 seaprate bands each (pre_r, pre_g, pre_b etc.)
and 3 raster masks of hte ground truth for the classes:
- all: all the buildings present in the pre_ image
- non_burned: all the buildings present in both pre_ and post_ images
- burned: all the buildings present in the pre_ image, but burned down in the post_ image.

All the masks are doubled by geojson vector files (convenient for preview in [GIS](https://qgis.org/en/site/))
All the images are georeferenced (web mercator / EPSG:3857)

2. Images wihtour labels:
- ventura_test
- santa_rosa_test
contain 2 RGB images organized as described above, without any ground truth. The images contain both burned and non-burned buildings.

raw satellite data fot the Santa Rosa area: 

santa_rosa_raw.zip
2 large RGB files covering santa_rosa_test and santa_rosa_train areas as well as much more. They are georeferenced (lat-lon) and aligned to each other.

#Docker instructions

1. Image creation:

docker build -t <image_name> .
or if there is NVidia GPU and nvidia-docker:
nvidia-docker build -t <image_name> .

the Dockerfile can be used to create Docker container with all librares for DL analysis of aerial images.
run of the image will open jupyter notebook server automatically.

2. Run image 

PASSWORD FOR JUPYTER NOTEBOOK: aeronet

to start a container as background process use:
docker run -d --rm -p <port_on_host>:8888 --name $(whoami) -v <your_folder>:<folder_in_container> -e "UID=$(id -u)" -e "GID=$(id -g)" <image_name>

or if there is NVidia GPU and nvidia-docker:

nvidia-docker run -d --rm -p <port_on_host>:8888 --name $(whoami) -v <your_folder>:<folder_in_container> -e "UID=$(id -u)" -e "GID=$(id -g)" <image_name>


#License

MIT License

Data is licensed by DigitalGlobe under the terms of their Opendata programm: "The Open Data Program supports non-commercial use only" (https://www.digitalglobe.com/opendata/)


# Florida 2018

This dataset (~12K buildings with damage classes) is based on Google open aerial imagery after hurricane Michael hitted Florida coast. [download](https://minio.aeronetlab.space/public/datasets/emergency/Florida_2018.zip).

Each of the labeled buildings has a geometrical contour and the appropirate class assignment whether it has no visible damages or was fully destroyed or partly damaged. 
<table>
  <tr>
   <td><strong>ID</strong>
   </td>
   <td><strong>CLASS_NAME</strong>
   </td>
   <td><strong>Description</strong>
   </td>
   <td width="130px"><strong>Visual</strong>
   </td>
   <td><strong>Application domains</strong>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
0</p>

   </td>
   <td>clutter
   </td>
   <td>
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td colspan="5" >
<h2>Buildings and Construction</h2>


   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
101</p>

   </td>
   <td>Residential building
   </td>
   <td>Roofs (not footprints) of apartment buildings. Multistorey building 
   </td>
   <td><img src="https://aeronetlab.space/img/class_img/101.png"/>
   </td>
   <td>
   </td>
  </tr>

  <tr>
   <td><p style="text-align: right">
102</p>

   </td>
   <td>House
   </td>
   <td>
   </td>
   <td><img src="https://aeronetlab.space/img/class_img/102.png" />
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
103</p>

   </td>
   <td>Industrial building
   </td>
   <td>Plants, etc.
   </td>
   <td><img src="https://aeronetlab.space/img/class_img/103.png" />
   </td>
   <td>
   </td>
  </tr>
 
  <tr>
   <td><p style="text-align: right">
105</p>

   </td>
   <td>Other non-residential buildings
   </td>
   <td>Garages, hangars, etc. - mostly small non-residential buildings
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>


  <tr>
   <td colspan="5" >
<h2>Emergency and risk management</h2>


   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
801</p>

   </td>
   <td>Destroyed building
   </td>
   <td>
   </td>
   <td><img src="https://aeronetlab.space/img/class_img/801.png" />
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
802</p>

   </td>
   <td>Damaged building
   </td>
   <td>
   </td>
   <td><img src="https://aeronetlab.space/img/class_img/802.png" />
   </td>
   <td>
   </td>
  </tr>
 </table>
