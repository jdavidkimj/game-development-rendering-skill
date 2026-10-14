# Game Development & Rendering Skill

A reusable Codex skill for creating and refining game models, materials, animation, lighting and effects, with evidence from the actual runtime.

The workflow connects selected references and playtest feedback to small experiments, matched before/after captures, semantic asset checks and scoped lessons. Focused guides cover multi-view review, skin/animation preservation, Blender migrations, geometry bevels and controlled benchmarks. It is engine-agnostic, with optional Godot documentation examples.

## Install

Ask Codex to install the skill with its skill installer:

```text
Use $skill-installer to install the skill at skills/game-development-rendering
from https://github.com/jdavidkimj/game-development-rendering-skill.
```

Alternatively, download or clone this repository and copy `skills/game-development-rendering` into your Codex skills directory, normally `~/.codex/skills/`. Preserve the complete folder, including `references/` and `agents/`. If `CODEX_HOME` is configured, use its `skills/` directory. Follow your client's instructions to reload skills if the new entry does not appear.

## Use

```text
Use $game-development-rendering to refine this model against the selected
reference, preserve its rig and materials, and verify the engine result.
```

Normal automatic skill discovery remains enabled. The entrypoint loads focused guides only when they apply. The skill follows project instructions and existing learning records; it does not supply assets or install a renderer, engine, Blender, add-on or executable dependency.

Keep proprietary references, models, captures and project-specific preferences in your own project. The package contains only general instructions, metadata and public documentation links. It makes no measured performance or game-FPS claims.

## Package

- `skills/game-development-rendering/SKILL.md`: discovery and shared workflow.
- `skills/game-development-rendering/agents/openai.yaml`: display metadata.
- `skills/game-development-rendering/references/`: task-specific guidance.

Instructions are provided under the [MIT License](LICENSE). Linked external documentation remains subject to its own terms.
