# Animation and action contracts

Identify the authoritative action, start/loop/end conditions, actual clip inventory, playback mode, socket and interruption policy. A suggestive clip name does not establish a loop; inspect authored intent and the imported clip. State missing clips or approximations explicitly. Preserve compatible rigs and clips.

Map the smallest affected sequence, such as approach → work → carry → return → idle, or anticipate → launch → recoil → recover. Identify ownership: simulation, snapshot, animation state or effect. Use the authoritative clock/event; particles, frame counts and poses should not silently drive game rules.

Diagnose the specific visible defect:

- Sliding: compare displacement, stride, root motion and clip rate before changing movement speed.
- Wrong direction/contact: inspect local/world transforms, socket, target and animated pose.
- Pops/repetition: inspect looping, blends, duplicate events and transition ownership.
- Absent/lingering effects: inspect delivery, visibility, budget admission, lifetime and reused-instance reset. An allocated particle system does not prove it drew.
- Work actions: align work motion, contact cues, cargo state and return motion with the real action, including interruption.

Share state and attachment infrastructure where compatible while preserving distinct authored motion, tool identity and surface response. Do not reopen an accepted model design to repair an event or attachment defect.

Capture the whole affected sequence at normal speed. Keep timestamps and label sampled poses or clips as sampled evidence. Test a useful interruption and affected reuse/death/visibility case. Include the gameplay camera and actual scene lighting; closeups diagnose detail but cannot establish crowd readability.

Use traces alongside images when needed to distinguish simulation from presentation. Follow [runtime verification](runtime-verification.md) for lighting and lifecycle. Promote techniques within tested scope and retain project-owned approval and simulation-review rules.
