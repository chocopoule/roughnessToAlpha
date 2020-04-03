import sys
import os
from PIL import Image
import PIL.ImageOps 
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add roughness map to alpha channel of metallic map.')
    parser.add_argument('--met', dest="metallic_map_path", help='metallic texture path')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--rough', dest="roughness_map_path",  help='roughness texture path')
    group.add_argument('--smooth', dest="smoothness_map_path", help='smoothness texture path')                    
    args = parser.parse_args()

    if(args.roughness_map_path):
        roughness_map = Image.open(args.roughness_map_path).convert('L')
        smoothness_map = PIL.ImageOps.invert(roughness_map)
    else:
        smoothness_map = Image.open(args.smoothness_map_path).convert('L')

    width, height = smoothness_map.size
    if(not args.metallic_map_path):
        metallic_map  = Image.new("RGBA",smoothness_map.size,"#000000")
    else:
        metallic_map = Image.open(args.metallic_map_path).convert('RGBA')

    metallic_map.putalpha(smoothness_map)
    filename, file_extension = os.path.splitext(args.roughness_map_path or args.smoothness_map_path)
    metallic_map.save(os.path.basename(filename+"_Metallic_result"+".png"))