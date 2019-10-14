# Emergency-mapping

"Emergenсy mapping" is a deeplearning method to detect damaged buildings in remote sensing imagery. Automatic mapping and detection is dedicated to reduce the time for decision making and response.

Here are some useful utils and a sample pipeline for dataset of California region where a lot of buildings were destroyed by wildfires in 2017.

Utils allow to read and write the files (data_handling.py), and also contain a simple convolutional network on Keras (unet.py) with a generator for training and validation, and a Jupyter notebook with a sample pipeline of the data processing.

Datataset is based on Opendata DigitalGlobe (Maxar) imagery and is available for [download](https://minio.aeronetlab.space/public/datasets/emergency/California_2017.zip).
This dataset contains satellite imagery before and after the events and a labeled data.

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
