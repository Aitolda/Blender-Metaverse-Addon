import bpy

class WEIGHTPAINT_PT_MVT_TOOLSET(bpy.types.Panel):
    """ Panel for Weight paint related tools """
    bl_label = "Weight Paint Tools"
    bl_region_type = "TOOLS"
    bl_space_type = "VIEW_3D"

    @classmethod
    def poll(self, context):
        print(context.mode + "SWAP")
        return context.mode == "PAINT_WEIGHT"

    def draw(self):
        layout = self.layout
        layout.operator(WEIGHTPAINT_PT_MVT_TOOLSET.bl_idname, icon='MOD_VERTEX_WEIGHT', emboss=False)
        return None


class WEIGHTPAINT_OT_MVT_TOOLSET_Smooth_Vertex_Group(bpy.types.Operator):
    """ UI Shortcut for weight smoothing """
    bl_idname = "metaverse_toolset.smooth_vertex_shortcut"
    bl_label = "Smooth Vertex"
    bl_region_type = "TOOLS"
    bl_space_type = "VIEW_3D"

    def execute(self):
        bpy.ops.paint.vertex_color_smooth()
        return {'FINISHED'}


classes = (
    WEIGHTPAINT_PT_MVT_TOOLSET,
    WEIGHTPAINT_OT_MVT_TOOLSET_Smooth_Vertex_Group
)

module_register, module_unregister = bpy.utils.register_classes_factory(classes)