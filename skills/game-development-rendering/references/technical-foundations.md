# Technical foundations and tool selection

Use primary sources for mechanisms and version-specific APIs. Resolve the installed executable/version first, then use matching documentation and actual exporter/importer behavior. Record documentation version and retrieval date when a decision depends on it. Documentation does not establish artistic acceptance or a successful project roundtrip.

## Interchange and authoring

- [Khronos glTF 2.0 specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html): skin palettes, inverse binds, animation targets and accessors must remain coherent. Base-color RGB is sRGB; metallic/roughness data are linear, with roughness in green and metallic in blue. Verify bindings and deformation, not only retained names or images.
- [Blender manual](https://docs.blender.org/manual/en/latest/) and [Python API](https://docs.blender.org/api/current/): select the installed version for mesh, armature, action, normal, bake and export work. Inspect operator support instead of assuming current examples apply to older binaries.
- [Blender glTF documentation](https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html): inspect material restrictions, action/NLA handling and actual exported animation identities. Internal action names need not equal exported clip identities.
- [Blender render baking](https://docs.blender.org/manual/en/latest/render/cycles/baking.html): validate installed operators and representative projection results before baking a whole asset.
- [MikkTSpace implementation](https://github.com/mmikk/MikkTSpace): useful when reproducing a tangent-generation defect. Diagnose the exact triangle, normals and UVs rather than treating all tangent errors as UV collapse.

## Engine examples

Apply these only to projects using that engine and match its installed version:

- [Godot 3D import pipeline](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/index.html): the shipped importer and effective runtime asset are the compatibility authority.
- [Godot materials](https://docs.godotengine.org/en/stable/tutorials/3d/standard_material_3d.html): overrides can replace material assignments; overlays add rendering layers. Trace effective bindings before editing a source map.
- [Godot environment and post-processing](https://docs.godotengine.org/en/stable/tutorials/3d/environment_and_post_processing.html): camera environments, tone mapping and renderer support affect the result; preview lights do not automatically become runtime lights.
- [Godot general optimization](https://docs.godotengine.org/en/stable/tutorials/performance/general_optimization.html): sustained slowness, spikes and loading stalls require distinct hypotheses and equivalent-workload measurements.

## Introduce tools for demonstrated needs

[NVIDIA Texture Tools](https://developer.nvidia.com/texture-tools-exporter) may help with measured compression, mip, alpha or normal-map problems. Verify channel/color-space preservation and final imports. Compression and upscaling do not create authored detail. [Nsight Graphics](https://developer.nvidia.com/nsight-graphics) may help with a demonstrated GPU bottleneck or binding defect; verify device/driver/API support and separate profiling overhead from ordinary measurements.

New integrations should resolve a concrete unmet need. Vendor provenance does not make arbitrary executed code safe for project data. Read documentation without adding execution dependencies; review permissions, compatibility and project tool boundaries before introducing an add-on or automation server. Do not migrate engines because another engine offers a new tool.
