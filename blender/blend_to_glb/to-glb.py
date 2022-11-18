import bpy
import os

filepath = os.path.basename(bpy.data.filepath)
basepath = os.path.splitext(filepath)
output_file_path = basepath[0] + ".glb"

bpy.ops.export_scene.gltf(filepath=output_file_path, export_format="GLB")
