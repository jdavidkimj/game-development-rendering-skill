# Blender migration, bevel experiments and benchmarks

## Pin provenance and preserve the old path

Use an official [Blender download](https://www.blender.org/download/) or [release archive](https://download.blender.org/release/). Record exact version, platform, package origin and hash. Compare the package with the official checksum; validate a publisher signature when the distribution provides one. A valid checksum establishes the downloaded artifact's identity, not compatibility with a project.

Install or extract new and legacy runtimes side by side in project-approved tool locations. Pin the executable in each invocation and retain a working rollback path. Do not overwrite a known-good runtime or automatically migrate every authoring file. Keep downloaded executables, add-ons and project assets out of the skill package.

Build an explicit version adapter where APIs differ. Choose supported branches from the detected version/capabilities and fail clearly on unsupported versions. Do not silently fall back to a legacy binary when a candidate fails; that produces a false successful migration. Keep legacy execution selectable and labeled.

## Verify semantics, not just successful execution

Check installed operators and arguments before scripting. Version changes may affect action slots, NLA/clip selection, shader socket names, normal/smoothing APIs, evaluated meshes, exporter options and joint ordering. Use Python exception exit handling supported by the binary, inspect logs, require expected artifacts and audit their contents.

First run an unchanged reference asset through import/export. Compare both the retained known-good runtime artifact and the original source; the known-good pipeline may itself lose information. A roundtrip can exit successfully while dropping a texture channel, image, clip, attachment or mesh. Count inventories as an initial signal, then inspect semantic bindings and runtime output. Equivalent image counts do not prove equivalent material response.

For skinned interchange, explicitly inspect skin joint palettes. In glTF, `JOINTS_n` values index the associated `skin.joints` array, rather than globally identifying nodes. Import/export can reorder that palette. If merging candidate geometry into a retained skin, derive a verified candidate-palette → retained-palette mapping using stable joint identity, remap every affected `JOINTS_n` accessor, retain corresponding weights and validate bounds. Account for instancing or primitives shared across skins; do not mutate a shared accessor under incompatible mappings. Check inverse binds, hierarchy, animation targets, sockets and representative deformation after the remap. Do not drop a joint-order guard or assume names alone establish compatibility.

Audit relevant mesh/node instances, topology, UV sets, split normals/tangents, material assignments, packed texture channels and color spaces, transparency, joints/inverse binds, clips and sockets. Distinguish intentional transformation from lost data. Require exact export receipts plus evidence in the actual engine/import path. A DCC render alone does not prove runtime compatibility.

## Bevel as reusable construction

Blender 5.2 introduces the [Mesh Bevel Geometry Node](https://docs.blender.org/manual/en/5.2/modeling/geometry_nodes/mesh/operations/mesh_bevel.html). Verify availability and socket names in the installed 5.2 build before automating it; do not apply this API to earlier versions. The versioned manual is the feature reference, not proof a project's exporter preserves its result.

Use a representative hard-surface region to compare the node, an existing bevel modifier or authored edge treatment. Expose width, segment count, profile and edge selection in a reusable authoring setup. Choose width relative to physical scale, reference construction and gameplay pixel coverage; extra segments are useful only if they improve silhouette or shading at the relevant cost.

Preserve defining silhouette, panel clearances, UV boundaries, material regions, skin weights and normal/tangent quality. Inspect acute corners and overlap handling, including deformed poses for skinned work. Avoid a global bevel that rounds intentional sharp boundaries or destroys narrow construction.

A real bevel must survive evaluated mesh export to become runtime geometry. Confirm the exported topology and imported result; saving a node group or modifier is insufficient. A shader bevel changes shading and is not exported geometry. A bake can transfer a shading cue but does not change silhouette. Choose the route based on the needed visible result and supported runtime.

Review matched close and gameplay views, with fixed lighting as geometry changes. Check source-resolution edges, silhouette, UV seams and material boundaries. Keep a candidate reversible until the engine result establishes improvement. Do not generalize one successful width/profile to unrelated scales or materials.

## Controlled performance comparison

Accept the visual and semantic output before claiming a performance improvement. Use identical source inputs and hashes, immutable source-derived camera/framing, pose/time, object scale, resolution, renderer, device, samples, color management, lighting and output format. A camera recalculated from candidate bounds can change workload and invalidate an apparent speedup. Explicitly label unavoidable differences such as changed shader response.

Separate import, script/geometry processing, export, engine import and render stages. State whether startup, warmup, disk/cache work and instrumentation are included. Use the same quiet machine/workload, record hardware/tool versions, repeat comparable runs and report medians with spread or individual samples. Change ordering or repeat when cache/order effects are consequential. Retain failed runs and explain exclusions.

If visual outputs differ, report measured stage timings as timings of those specific outputs; withhold an equivalent-quality speed claim until output is accepted. Do not turn faster import/export or offline CPU/GPU rendering into a game FPS claim. Runtime FPS requires its own matched engine workload and frame-time evidence. Never invent measurements from release notes or hardware capability.
