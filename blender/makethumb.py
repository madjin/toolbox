import bpy
import os


import bpy
import glob
 
for f in glob.glob("*.glb"):
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.view3d.camera_to_view_selected()
    bpy.ops.import_scene.gltf(filepath=f)
    bpy.context.scene.render.filepath = f[:-4] + ".png"
    bpy.ops.render.render(write_still=True)