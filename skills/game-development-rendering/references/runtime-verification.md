# Runtime verification and playability

Select checks affected by the change; avoid turning a local adjustment into a full test matrix.

| Area | Observe in the running game | Insufficient evidence |
|---|---|---|
| Environment | Day/night transitions, shadow, contact, material response and identity | Studio lighting alone |
| Attached lights | Credible source, color, falloff, spill, motion and crowded budget | Bloom or floating lamps alone |
| Exposure/glow | Bright core, softer diffusion, controlled clipping and stable transitions | Raising global exposure to hide a weak cue |
| Animation | Start, loop, recovery, contact, turn, recoil and interruption | A correct single pose |
| Effects | Anticipation, launch, travel, impact, aftermath and cleanup | A generic glow or damage counter |
| Lifecycle | Relevant visibility, death, transform, pooling, pause and low-frame states | One successful spawn |
| Tactical view | Identity, selection feedback and action hierarchy in a crowd | Closeups alone |

## Lighting and visibility

Separate emissive surface color, post-process glow and scene illumination. A luminous surface may not illuminate the ground; an unattached scene light may lack a credible source. Inspect active camera environment/attributes, world settings and renderer support. Preserve accepted endpoints unless the requested correction and evidence call for changing them; scope such changes and capture controls.

Check attachments during motion and recoil. When pooling or retirement changes, verify reset on the exact reused instance. Shared light budgets should preserve spatial and readability priorities. An isolated exemplar does not justify one real light per object in a crowd. Capture after budget updates: a brief admitted flash can expire before any displayed frame.

Effects communicate gameplay information. Respect project visibility policy for fog, concealment and hidden objects. Scope intentional family exceptions and use control cases rather than raising brightness everywhere.

## Action and effect evidence

Classify an ambiguous missing cue: luminous geometry, moving tracer, impact, illumination or the underlying action. Trace command/event through snapshot/state, renderer hook, socket, spawned visual and cleanup. Delivery routes may emit different events. Recipient state establishes gameplay results; timed frames establish visible cues. Reproduce the current runtime before assuming an older test still covers it.

Keep effect identity: short dashes, sustained beams, solid projectiles and thrown objects require different motion and surface treatment. For branching energy, separate core width and brightness from branch density and diffusion. Judge decay, illumination and timing in motion.

Capture relevant before/launch/travel/impact/fade frames plus continuous normal-speed footage for motion claims. Preserve timestamps and missing intervals. Sparse stills interpolated into a smooth clip invent evidence. Check framing early before long captures.

## Frame delivery and integration

Reproduce the player's symptom before changing logic. Missing flashes can make working actions appear broken; low hardware utilization can coexist with interpolation stutter. Separate simulation cadence, snapshot consumption, animation progress, camera movement and delivered frames.

Compare equivalent builds, maps, population, view, rendering settings, resolution and capture mode. Use frame-time distributions and spikes as well as average FPS. Bounded light or draw-call counts are design constraints, not proof of acceptable performance. Use a quiet representative workload; distinguish instrumented/profiler captures from ordinary measurements.

Keep presentation and authoritative game rules separate according to the architecture. Tests should cover meaningful changed behavior; visual-policy changes need representative controls and affected lifecycle routes. Reuse passing evidence when conditions remain applicable. State remaining integration, performance and acceptance gaps.
