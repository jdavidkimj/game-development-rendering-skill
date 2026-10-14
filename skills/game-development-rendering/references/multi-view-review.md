# Consistent multi-view review

## Reference prerequisite before modeling

When the user or project requires multiple reference angles, establish those references before new geometry work. Record the selected source identity, required named views, saved image paths (or sheet regions), later corrections, inferred hidden details, and a visual consistency verdict. A file count is not a visual verdict: duplicated angles, contradictory silhouettes or a drifted design keep the reference unresolved. Reuse valid existing references; do not regenerate them merely because a new session starts.

Check this record before assigning a modeling task, and include it in the brief. Where tooling supports it, fail the unit's authoring/review preflight on missing evidence, changed source hashes or an unresolved reference verdict. Such a check verifies recorded evidence and freshness; it cannot judge visual fidelity or prevent arbitrary manual edits. Block only dependent geometry work; independent gameplay fixes, diagnostics and reference preparation may continue. A changed reference or correction requires re-review of affected views.

Track reference readiness, implementation evidence and user approval independently. Engine captures belong to implementation evidence and must never be substituted for design references. The original selected design and explicit later corrections remain authoritative over inferred views. This rule does not require an extra user approval unless the project or user already calls for it.

Use when matching a character or prop reference, or when a single attractive angle conceals construction problems. Choose coverage and resolution for the ambiguity; there is no universal minimum view count.

Write a compact target brief: selected reference, defining proportions, part layout, materials, pose/camera and allowed inference. Derive useful front, rear, side and three-quarter views from that design. Label invented hidden construction. Generated views can retain perspective or disagree on details; they are not measured orthographic plans. Do not redesign an approved front to accommodate an inconsistent generated rear.

Track important components as missing, implemented but unverified, inspected in named views, or rejected with a specific defect. A concept image, successful build or large polygon count does not change an implementation's visual status. Retain exact generation prompts and parameters when useful, with the accepted capture recipe; do not promise approval on the first attempt.

Capture the actual engine model with controlled pose/time, projection, distance, object scale, lighting and exposure. Reuse comparison cameras. Record effective internal rendering resolution and upscaling, not only window dimensions. Mark differently posed or independently framed comparisons as approximate.

Use a compact contact sheet for proportions and preserve full-resolution originals or unscaled crops for seams and fit. Inspect sides and rear before presentation: front geometry can hide block-like depth, floating cuffs, unfinished backs and disconnected limbs. A reduced sheet can conceal the defect under review.

Calibrate custom previews before using them as construction gates: equal world-to-pixel scale across axes, orthogonal view bases, common framing and real per-pixel depth. Triangle painter sorting can invent surface stripes. State omitted meshes and approximated bevels, materials or lights. If calibration was wrong, qualify earlier judgments and reassess with corrected previews or matched engine views.

Separate shape, intersections, material response and sampling/shadow defects. Shadow-map resolution is independent of color-framebuffer resolution. Preserve a fixed-light comparison while geometry changes. Follow requested review stages; encouragement about progress does not automatically approve final materials or movement.

Retain reference, inferred-view labels, editable source, builder/capture configuration, baseline/candidate images, rejected evidence, verdict and open gaps. Link one compact experiment in existing project records. Standardize helpers after demonstrated reuse rather than building a framework around one failure.

## Two passes: construction first, fine detail second

For detailed reference-matching work, complete the proportions and construction pass
before advancing fine detail. First check overall silhouette, relative volumes, major
part placement, armor overlaps, thickness, negative spaces and physical connections.
Then check smaller features, seams, bevels, surface relief, trim, maps and material
response. If a later detail view reveals a structural defect, reopen the first pass for
that part and its dependencies. More surface detail does not close a shape mismatch.

### Grid and part review

When details are repeatedly missed, use a stable numbered grid on the selected reference
and actual engine view, with synchronized cell selection and source-resolution close-ups.
Choose a useful grid density for the subject; a fixed cell count is not a universal rule.
Keep a whole-model view beside the cell review so local repairs cannot silently distort
the silhouette. Review physical parts crossing cell boundaries together, including
their neighboring supports and occluding layers.

Match the reference's viewing direction and angle before reference-to-model grid
comparison. Both subjects facing right (or left) is not enough: match model rotation
relative to the camera, camera azimuth/yaw, elevation/pitch and roll, then projection
and framing. A front view and a three-quarter view remain incompatible even when both
face the same side. Recapture the actual model; do not mirror it, since asymmetric
equipment would swap sides. Match the relevant pose and limb/weapon orientations too.

Verify alignment visually using anatomical landmarks, visible front/side/top surfaces,
foreshortening and occlusion before enabling linked cells. Matching camera parameter
numbers alone is insufficient when models use different forward axes. For concept art
without camera metadata, infer and refine the view; do not claim an exact measured angle.
Keep the grid gated while the angle is unresolved. An "approximate" label or a coarse
silhouette comparison does not satisfy this gate. Once the view is matched, mark any
remaining pose-limited cells uncertain and obtain a matched pose before judging them.

Register the images before judging cells. Record source identity, angle, pose/time,
camera, crop bounds, scale and lighting. Preserve image aspect ratio; do not stretch,
warp or independently fit every part to manufacture agreement. Reuse the same crop and
camera for matched engine before/after views. If alignment must change, version it and
recheck affected cell findings instead of reusing their old coordinates. An unmatched
concept angle can support a separate overview study, but not the linked grid. Mark perspective,
pose, occlusion or inferred hidden construction as uncertain where they prevent judgment.

Use linked zoom and a blink or opacity overlay for genuinely matched engine captures.
Overlays expose changes; a difference image alone cannot distinguish a correction from
a regression. Never treat blank, hidden or uninspected cells as passing. Preserve full
resolution sources and inspect the relevant pixels rather than relying only on thumbnails.

Maintain a compact cell/part ledger with: view and stable cell ID, part, expected feature,
observed difference, status, evidence, reviewer and next correction. Separate structural
and detail findings. Useful statuses are unreviewed, mismatch, uncertain and observed
match; the last means the named evidence supports that feature, not user approval.
Keep unresolved findings visible across candidates. Recheck changed cells, adjoining
parts and the whole silhouette; broaden the review only when the change has wider effects.

Measure silhouette and landmark ratios only when framing, projection and pose support
the comparison. State landmarks, coordinate convention, normalization and uncertainty;
do not report precise 3D agreement from uncalibrated concept art. Prefer separate
part-level findings to an overall similarity score that can hide a defining defect.

Before advancing a reference-faithful candidate, use a second independent visual review
when available and authorized. Give the reviewer the selected references, later user
corrections and exact engine evidence before showing the first review's verdict. Compare
findings afterward; resolve disagreements with closer or additional views. Record when
an independent review was unavailable instead of claiming one. Neither review grants
user acceptance or motion/publication clearance.

Track review time and revision count when evaluating efficiency. Grid inspection adds
upfront work and may reduce rework; treat that benefit as a hypothesis until measured.
Keep scripts and image data in the project's existing evidence system. Browser draft
notes or exported annotations are not canonical decisions until reconciled there.
