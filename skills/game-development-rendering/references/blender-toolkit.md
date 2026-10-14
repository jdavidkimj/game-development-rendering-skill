# Blender tools: choose by the visible problem

Official documentation reviewed October 13, 2026, primarily Blender 5.2. Some indexed pages resolve to earlier versions or another manual locale with English content; verify the installed API rather than treating a search result as a compatibility test. These are researched mechanisms and proposed applications, not claims of production success.

## Shape and construction

| Visible need | Candidate tool | Decision and failure to watch |
|---|---|---|
| Wrong overall proportions across several connected parts | Lattice, proportional editing, reference-aligned cross sections | Change the full assembly before adding detail. A lattice can reshape several objects together; it does not automatically retarget a skeleton, sockets or clips. |
| Symmetric armor with deliberate openings | Mirror, Boolean, Solidify, Bevel | Establish connected volumes, then openings, thickness and edge treatment. Preserve purposeful asymmetry. Inspect thin walls, acute corners, intersections and evaluated topology before skinning. |
| Hard armor that reads as razor-sharp or inflated | Selective Bevel and Weighted Normal | Bevel changes geometry; weighted normals change shading. Use scale-aware edge widths and intentional sharp boundaries. Normals cannot repair a wrong silhouette or self-intersection. |
| Repeated vents, ribs, cables, scales or modular plates | Array, curves and Geometry Nodes | Expose dimensions, spacing, seed and material regions as parameters. Follow the selected construction instead of scattering arbitrary detail. Verify realized/exported geometry and material assignments. |
| Organic forms assembled from disconnected pieces | Sculpting and voxel remesh on an isolated authoring copy | Explore connected anatomy at coarse resolution first. Remeshing changes topology; do not assume original UVs, skin weights, shape keys or vertex correspondence survive. |
| Fine organic detail on established anatomy | Multiresolution, retopology, Shrinkwrap | Use sculpt detail on a suitable base or project a new surface carefully. Shrinkwrap projection limits and direction matter around lips, folded shells and neighboring limbs. Inspect inner surfaces and silhouette; nearest surface is not necessarily the intended surface. |

Mechanism sources: [Lattice](https://docs.blender.org/manual/en/latest/modeling/modifiers/deform/lattice.html), [Bevel](https://docs.blender.org/manual/en/4.4/modeling/modifiers/generate/bevel.html), [Weighted Normal](https://docs.blender.org/manual/en/5.2/modeling/modifiers/normals/weighted_normal.html), [remeshing](https://docs.blender.org/manual/en/5.0/modeling/meshes/retopology.html), [Multiresolution](https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/multiresolution.html), [Shrinkwrap](https://docs.blender.org/manual/en/5.2/modeling/modifiers/deform/shrinkwrap.html).

[Boolean](https://docs.blender.org/manual/en/5.2/modeling/modifiers/generate/booleans.html) results depend on input geometry and solver; closed manifold operands provide the reliable case. [Solidify](https://docs.blender.org/manual/nl/5.2/modeling/modifiers/generate/solidify.html) computes thickness in local coordinates, so nonuniform object scale changes apparent wall thickness. Resolve transforms deliberately on an authoring copy; do not blindly apply transforms to an existing skinned asset.

The 5.2 [Mesh Bevel node](https://docs.blender.org/manual/id/5.2/modeling/geometry_nodes/mesh/operations/mesh_bevel.html) supports explicit selection and varying offsets; it is not a drop-in copy of the modifier. Edge bevel operates on manifold edges, and some modifier options require helper nodes. Inspect the installed sockets before scripting. Prefer the simpler modifier for a one-off shell; choose a node group when controlled reuse offers a concrete benefit. See [migration and bevels](blender-migration.md) for export and comparison gates.

A 5.2.2 API probe exposed `Affect Kind` where the reviewed manual labels the control `Affect Type`. Discover socket identifiers on the active binary; do not add an unverified name alias merely to make a script run. This observation establishes an API difference, not bevel quality.

## Surface detail and materials

Use high-to-low baking when detail is smaller than the required silhouette and dense geometry would be wasteful. Start with one representative region. A [Cycles bake](https://docs.blender.org/manual/en/latest/render/cycles/baking.html) needs destination UVs and an active image target; selected-to-active projection may require a controlled cage. Check cage misses and neighboring-part bleed, seams, padding under mip filtering, tangent convention and the actual engine sampler. Normal maps carry shading detail, not a new outline. Keep portable material properties separate from baked scene illumination when lighting changes at runtime.

Use [Principled BSDF](https://docs.blender.org/manual/sr/5.2/render/shader_nodes/shader/principled.html) to distinguish paint, metal, ceramic, flesh, shell and glass. Coat, roughness, transmission and subsurface are separate mechanisms; stronger specularity alone does not make a surface more realistic. Confirm which features the export format and game shader reproduce. Procedural node networks often need baking or a deliberate engine equivalent.

When the product uses player colors, author ownership paint as an explicit mask/material semantic, separate from fixed metal, trim, wear and emission. Painted weapon parts are still paint. Verify contrasting player colors on the same asset and preserve roughness/normal response. Do not infer ownership paint from a broad runtime RGB threshold or globally tint the model. This is an asset contract, not a Blender default.

## Rigging, deformation and animation

- [Data Transfer](https://docs.blender.org/manual/en/5.1/modeling/modifiers/modify/data_transfer.html) can seed compatible weights, UVs or normals. Choose mapping and destination layers deliberately. Nearby geometry can belong to the wrong limb; transferred weights require joint-pose inspection and cleanup.
- [Corrective Smooth](https://docs.blender.org/manual/id/5.2/modeling/modifiers/deform/corrective_smooth.html) can reduce armature-induced distortion. Bind/rest-state choice and topology matter; smoothing can lose volume. It is an authoring aid, not proof that a corrective deformation exports as an ordinary skeletal clip.
- [IK](https://docs.blender.org/manual/id/5.2/animation/constraints/tracking/ik_solver.html), constraints and pose tools help author hand/foot contact and mechanical alignment. Use shape keys or corrective poses where a joint needs authored volume preservation, then verify supported morph/animation export. Bake evaluated bone motion where the exporter requires it; do not assume constraint graphs survive.
- Ground contact on changing game terrain also needs engine-side sampling, locomotion/IK and transition handling. A Blender walk cycle alone cannot solve arbitrary slopes, terrain penetration or unit collisions.

Treat [glTF export](https://docs.blender.org/manual/en/latest/addons/import_export/scene_gltf2.html) as a separate contract: inspect evaluated mesh, supported material channels, joint palettes, action/clip identities, morphs and attachment relationships. Exported transforms or sampled bone motion do not reproduce every Blender modifier, driver or physics simulation. Inspect the actual imported result; follow the semantic audits in [migration](blender-migration.md).

## Reuse and learning

[Asset libraries](https://docs.blender.org/manual/en/5.2/files/asset_libraries/introduction.html) can retain useful node groups, materials, objects and poses. Promote a method after representative evidence, with a second compatible example before broad use where the project requires it. Keep private art outside a public skill. Store generic guidance or small helpers in the skill; keep source assets, receipts, presets and measured project-specific values in project-owned storage.

Record each evaluated technique with: the visible hypothesis; tool/build; input identity; relevant parameters; baseline/candidate evidence; evaluation/export/runtime result; time or cost only if measured; failure and next decision. Use distinct states: **documented**, **API available**, **evaluated/exported**, **engine-observed**, and **artistically accepted**. Availability is not a quality rating.

For installed API discovery, run `scripts/blender_capabilities.py` in a fresh background Blender process using the project's normal wrapper and a fresh `--output` receipt. It opens no project and only writes that JSON. It constructs temporary API objects and inventories operator arguments; it does not execute modifiers, bake, export or render. Read its per-tool results, not just its exit code. Probe again after a runtime upgrade or a tool-specific incompatibility, not every session.

For a major reference-matching rework, satisfy reference readiness first, choose tools for the largest structural discrepancy, and compare a representative region before multiplying detail. A newer Blender release expands options; it does not itself improve the model.
