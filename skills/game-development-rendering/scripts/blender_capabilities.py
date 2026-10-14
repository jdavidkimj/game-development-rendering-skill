"""Inventory installed Blender authoring APIs; does not prove evaluation or export.

Run in a fresh background process:
blender --background --factory-startup --python-exit-code 1 --python this.py -- --output receipt.json
No project files are opened, rendered, or saved. Only the requested JSON is written.
"""
import argparse
import json
from pathlib import Path
import sys

import bpy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    if args.output.exists():
        raise FileExistsError(f"Preserve the previous receipt; choose a fresh path: {args.output}")
    report = {"version": bpy.app.version_string,
              "build_hash": bpy.app.build_hash.decode(),
              "scope": "API construction/introspection only; no geometry evaluation, export, render, or artistic validation",
              "modifiers": {}, "geometry_nodes": {}, "operators": {}, "shader_inputs": []}
    mesh = bpy.data.meshes.new("CapabilityProbe")
    obj = bpy.data.objects.new("CapabilityProbe", mesh)
    group = bpy.data.node_groups.new("CapabilityProbe", "GeometryNodeTree")
    material = bpy.data.materials.new("CapabilityProbe")
    try:
        for kind in ("MIRROR", "ARRAY", "BEVEL", "WEIGHTED_NORMAL", "BOOLEAN", "SOLIDIFY",
                     "SUBSURF", "MULTIRES", "REMESH", "SHRINKWRAP", "LATTICE", "CURVE",
                     "DATA_TRANSFER", "ARMATURE", "CORRECTIVE_SMOOTH", "TRIANGULATE", "DECIMATE", "NODES"):
            try:
                modifier = obj.modifiers.new(kind, kind)
                report["modifiers"][kind] = {"available": True}
                obj.modifiers.remove(modifier)
            except Exception as exc:
                report["modifiers"][kind] = {"available": False, "error": str(exc)}
        for kind in ("GeometryNodeMeshBevel", "GeometryNodeCurveToMesh", "GeometryNodeInstanceOnPoints",
                     "GeometryNodeRealizeInstances", "GeometryNodeSetMaterial"):
            try:
                node = group.nodes.new(kind)
                report["geometry_nodes"][kind] = {"available": True,
                    "inputs": [{"name": s.name, "identifier": s.identifier} for s in node.inputs]}
                group.nodes.remove(node)
            except Exception as exc:
                report["geometry_nodes"][kind] = {"available": False, "error": str(exc)}
        for namespace, name in (("object", "bake"), ("object", "voxel_remesh"),
                                ("nla", "bake"), ("export_scene", "gltf")):
            label = namespace + "." + name
            try:
                rna = getattr(getattr(bpy.ops, namespace), name).get_rna_type()
                report["operators"][label] = {"available": True,
                    "properties": [p.identifier for p in rna.properties if p.identifier != "rna_type"]}
            except Exception as exc:
                report["operators"][label] = {"available": False, "error": str(exc)}
        material.use_nodes = True
        shader = material.node_tree.nodes.new("ShaderNodeBsdfPrincipled")
        report["shader_inputs"] = [s.name for s in shader.inputs]
    finally:
        bpy.data.materials.remove(material)
        bpy.data.node_groups.remove(group)
        bpy.data.objects.remove(obj)
        bpy.data.meshes.remove(mesh)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"receipt": str(args.output), "version": report["version"], "scope": report["scope"]}))


if __name__ == "__main__":
    main()
