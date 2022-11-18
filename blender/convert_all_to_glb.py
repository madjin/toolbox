import bpy
import os
 
def convert_to_glb(filename):
    bpy.ops.import_scene.obj(filepath=filename)
    bpy.ops.export_scene.gltf(filepath=filename)
 
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".obj") or filename.endswith(".dae") or filename.endswith(".fbx"):
        convert_to_glb(filename)