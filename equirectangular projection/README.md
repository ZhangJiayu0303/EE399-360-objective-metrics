#Reference: https://github.com/bingsyslab/360projection

# 360-degree Projection

This repo includes code for rendering 360-degree images/video frames and converting these images among different types of spherical projections.

## Equirectangular Projection

In equirectangular projection, angles on the sphere given by yaw and pitch values(in degrees) are discretized and mapped to pixels on a rectangular image with x = (yaw + 180)/360 * width and y = (90 - pitch)/180 * height. 

The size of the equirectangular image (width, height). The center of the equirectangular image is at: ```<yaw = 0, pitch = 0>```.

**equirectangular.py** contains code for rendering view at a specific angle, vertical and horizontal field of view, and view resolution, given an image in equirectangular projection. It also contains code for converting the equirectangular projection to the standard cubic projection.


# Usage
```
usage: main.py [-h] config_f img_f

positional arguments:
  config_f    path to config file
  img_f       path to input image

optional arguments:
  -h, --help  show this help message and exit
```
config is a json formatted file. A few example config files as well as a `config_template` have been provided in this repo.

For example, to render an equirectangular image, example parameters can be found at `config_equi_render`, then run
```
python main.py config_equi_render equi_image.jpg
```
