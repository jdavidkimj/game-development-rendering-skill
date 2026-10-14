# Reference matching and visual production

## Shape and construction

Save the selected reference version and later corrections. Compare silhouette and negative space first, then projected proportions, limb/tool lengths, structural overlaps and material boundaries, then fine detail. Measurements from perspective images carry camera and pose uncertainty. Identify consequential hidden-surface assumptions.

Maintain a fixed comparison camera; label additional reference-angle studies. Inspect close construction and ordinary gameplay scale. Clay isolates shape but cannot establish material quality. A flattering angle or brighter light does not prove geometry improved.

Inventory active meshes, UVs, maps, joints, inverse binds, weights, clips, sockets and effect cards before modifying an asset. Preserve useful detail and behavior, replacing the demonstrated mismatch. Fit additions to local curved or tilted surfaces and articulated segments. Include thickness, edge treatment, articulation clearance and functional housings instead of stacking disconnected plates.

For a visible intersection or occlusion, trace the captured region through the complete posed assembly, including neighboring components with different bindings. A ray against only a new shell can miss the part actually blocking it. Derive an outside silhouette separately from a circular mechanism inside it.

Audit geometry referenced by active scene nodes and instances. Interchange files may retain unused mesh definitions; distinguish those from rendered surfaces. Separate numeric clearance envelopes from visible geometry so retained placeholder cores do not dominate a finished silhouette.

Inspect triangle interiors as well as vertices when fitting armor to curved supports. Linear faces can penetrate a curved surface even when their corners clear it. Triangulate concave polygons correctly; an assumed centroid fan can introduce invalid faces. Use measured failures to choose subdivision, refitting or weight corrections.

## Deformation and interchange

When changing rest anatomy, inspect vertices, normals, inverse binds, descendants, animation channels and attachment transforms together. Matching joint names alone is insufficient. Verify exported/imported clip identities and representative deformed poses, tool/socket alignment and recoil clearance. Reproduce the retained baseline before attributing a new defect to the candidate; builder drift can invalidate comparisons.

Full authoring-tool roundtrips can alter animation or material channels. Geometry-only export and tested merging into the original asset may reduce disruption but require their own preservation proof. Read logs, expected output receipts and semantic checks as well as exit status. Do not weaken a guard until the exact expected/actual difference is understood. Consult [migration](blender-migration.md) for joint-palette and version changes.

Separate editable authoring sources from engine-importable outputs. Some engines automatically import authoring files through external tools. Use project-supported excluded authoring locations and correct manifests rather than changing global editor settings to conceal an unintended import.

## Surface response and baking

Solve proportions, intermediate construction and then fine surfaces. Distinguish metal, paint, ceramic, organic shell, tissue, glass and emissive response. Tie details to function: fasteners, recesses, flexible connections, growth and restrained irregularity. Repeated decorative strips or uniformly bright seams can obscure believable construction.

Trace effective materials through maps, importer, node/mesh overrides, shader samplers, packed channels, color space, UVs and tangent frame. A retained image file does not prove its shader channel remains bound. Preserve native UVs on retained faces; unwrap new broad surfaces instead of stretching an unrelated atlas fragment.

When a material boundary crosses coarse faces, split geometry at that boundary or use a suitable continuous mask. Whole-face assignment by face-center location can create a sawtooth boundary. Inspect source-resolution pixels before judging a reduced contact sheet.

For invalid tangents, retain the failing triangle's positions, UVs and split normals. Nonzero UV area does not exclude geometric degeneracy: extremely acute bevel corners can lose angle-weighted tangent contributions in finite precision. Reproduce the installed generator's behavior before repairing. Correct demonstrated slivers narrowly with bounded displacement and manifold checks, then recompute and retain the tangent gate. Avoid invented tangents or broad welding of preserved meshes. Release temporary tangent data before mutating mesh layers when required by the installed API.

For high-to-low baking, keep editable source, low mesh/UVs and reproducible settings. Test a representative patch first. Inspect projection misses, seams, tangent consistency, mips and final engine bindings. Planned normal or occlusion maps are not completed detail. Choose resolution and geometry from visible need and measured cost.

## Terrain and expansion

Terrain needs broad form, physical texture scale, intermediate accumulation and filtered fine detail. Displaced normals/tangents, footing, contact geometry and picking should use compatible height information. Preserve defining canopy coverage when simplifying distant vegetation. Transfer the cause of a successful biome treatment rather than its literal color or optical settings.

Keep previous candidates and reproducible builders. Show matched reference/baseline/candidate views and the largest remaining mismatch. Test a representative second subject before broad reuse; rigid-shell methods may fail on deforming anatomy. Review [runtime integration](runtime-verification.md) before declaring an asset ready for play.

For player-color materials, preserve an explicit ownership-paint mask separately from fixed finishes, including painted weapon surfaces. For construction, deformation and baking tool choices, use [Blender toolkit](blender-toolkit.md); availability alone is not proof of runtime improvement.

## Imported material staging

When newly extracted models export with placeholder textures, inspect which stage is missing: raw texture, decoded/processed image, material relink, or engine import. An exported mesh can be structurally valid while embedding placeholder pixels. Preserve the texture gate; prepare the missing maps and verify the new export. A file created by a failed extractor may be empty, so existence alone must not promote an asset to ready.
