# roughnessToAlpha
A python utility script to copy roughness texture to alpha channel of metallic texture
Because the smoothness of each point on the surface is a single value, only a single channel of an image texture is required for the data. Therefore, in Unity, the smoothness data is assumed to be stored in the Alpha Channel of the same image texture used for the Metallic or Specular texture map (depending which of these two modes you are using).

#usage
usage: MetallicToRought.py [-h] [--met METALLIC_MAP_PATH]
                           (--rough ROUGHNESS_MAP_PATH | --smooth SMOOTHNESS_MAP_PATH)

Add roughness map to alpha channel of metallic map.

optional arguments:
  -h, --help            show this help message and exit
  --met METALLIC_MAP_PATH
                        metallic texture path
  --rough ROUGHNESS_MAP_PATH
                        roughness texture path
  --smooth SMOOTHNESS_MAP_PATH
                        smoothness texture path
