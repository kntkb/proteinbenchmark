"""List of force fields and water models."""
from pathlib import Path

from proteinbenchmark.utilities import package_data_directory

ff_directory = Path(package_data_directory, "force-fields")

# List of force fields with force field XML file, water model, and water model
# XML file
force_fields = {
    "ff14sb-opc": {
        "force_field_file": Path(
            ff_directory, "nerenberg_ff14sb_c0ala_c0gly_c0val.xml"
        ),
        "water_model": "opc",
    },
    "ff14sb-opc3": {
        "force_field_file": Path(
            ff_directory, "nerenberg_ff14sb_c0ala_c0gly_c0val.xml"
        ),
        "water_model": "opc3",
    },
    "ff14sb-tian-opc": {
        "force_field_file": Path(ff_directory, "tian_ff14sb_c0ala.xml"),
        "water_model": "opc",
    },
    "ff14sb-tian-opc3": {
        "force_field_file": Path(ff_directory, "tian_ff14sb_c0ala.xml"),
        "water_model": "opc3",
    },
    "ff14sb-tian-tip3p": {
        "force_field_file": Path(ff_directory, "tian_ff14sb_c0ala.xml"),
        "water_model": "tip3p",
    },
    "ff14sb-tian-tip3p-fb": {
        "force_field_file": Path(ff_directory, "tian_ff14sb_c0ala.xml"),
        "water_model": "tip3p-fb",
    },
    "ff14sb-tian-tip4p-fb": {
        "force_field_file": Path(ff_directory, "tian_ff14sb_c0ala.xml"),
        "water_model": "tip4p-fb",
    },
    "ff14sb-tip3p": {
        "force_field_file": Path(
            ff_directory, "nerenberg_ff14sb_c0ala_c0gly_c0val.xml"
        ),
        "water_model": "tip3p",
    },
    "ff14sb-tip3p-fb": {
        "force_field_file": Path(
            ff_directory, "nerenberg_ff14sb_c0ala_c0gly_c0val.xml"
        ),
        "water_model": "tip3p-fb",
    },
    "ff14sb-tip4p-fb": {
        "force_field_file": Path(
            ff_directory, "nerenberg_ff14sb_c0ala_c0gly_c0val.xml"
        ),
        "water_model": "tip4p-fb",
    },
    "null-0.0.1-tip3p": {
        "force_field_file": Path(ff_directory, "Protein-Null-0.0.1.offxml"),
        "water_model": "tip3p",
        "water_model_file": None,
    },
    "null-0.0.2-opc": {
        "force_field_file": Path(ff_directory, "Protein-Null-0.0.2-NH2.offxml"),
        "water_model": "opc",
        "water_model_file": "opc-1.0.0.offxml",
    },
    "null-0.0.2-opc3": {
        "force_field_file": Path(ff_directory, "Protein-Null-0.0.2-NH2.offxml"),
        "water_model": "opc3",
        "water_model_file": Path(ff_directory, "opc3-1.0.0.offxml"),
    },
    "null-0.0.2-tip3p": {
        "force_field_file": Path(ff_directory, "Protein-Null-0.0.2-NH2.offxml"),
        "water_model": "tip3p",
        "water_model_file": None,
    },
    "null-0.0.2-tip3p-fb": {
        "force_field_file": Path(ff_directory, "Protein-Null-0.0.2-NH2.offxml"),
        "water_model": "tip3p-fb",
        "water_model_file": Path(ff_directory, "tip3p_fb-1.1.0.offxml"),
    },
    "null-0.0.2-tip4p-fb": {
        "force_field_file": Path(ff_directory, "Protein-Null-0.0.2-NH2.offxml"),
        "water_model": "tip4p-fb",
        "water_model_file": Path(ff_directory, "tip4p_fb-1.0.0.offxml"),
    },
    "specific-0.0.1-tip3p": {
        "force_field_file": Path(ff_directory, "Protein-Specific-0.0.1.offxml"),
        "water_model": "tip3p",
        "water_model_file": None,
    },
    "specific-0.0.2-opc": {
        "force_field_file": Path(ff_directory, "Protein-Specific-0.0.2-NH2.offxml"),
        "water_model": "opc",
        "water_model_file": "opc-1.0.0.offxml",
    },
    "specific-0.0.2-opc3": {
        "force_field_file": Path(ff_directory, "Protein-Specific-0.0.2-NH2.offxml"),
        "water_model": "opc3",
        "water_model_file": Path(ff_directory, "opc3-1.0.0.offxml"),
    },
    "specific-0.0.2-tip3p": {
        "force_field_file": Path(ff_directory, "Protein-Specific-0.0.2-NH2.offxml"),
        "water_model": "tip3p",
        "water_model_file": None,
    },
    "specific-0.0.2-tip3p-fb": {
        "force_field_file": Path(ff_directory, "Protein-Specific-0.0.2-NH2.offxml"),
        "water_model": "tip3p-fb",
        "water_model_file": Path(ff_directory, "tip3p_fb-1.1.0.offxml"),
    },
    "specific-0.0.2-tip4p-fb": {
        "force_field_file": Path(ff_directory, "Protein-Specific-0.0.2-NH2.offxml"),
        "water_model": "tip4p-fb",
        "water_model_file": Path(ff_directory, "tip4p_fb-1.0.0.offxml"),
    },
}

# Add implicit water model files
water_model_files = {
    "tip3p": "amber/tip3p_standard.xml",
    "opc3": Path(ff_directory, "openmm-opc3.xml"),
    "opc": "amber/opc_standard.xml",
    "tip3p-fb": Path(ff_directory, "openmm-tip3p-fb.xml"),
    "tip4p-fb": Path(ff_directory, "openmm-tip4p-fb.xml"),
}

for force_field_name, ff_parameters in force_fields.items():
    if "water_model_file" not in ff_parameters:
        water_model_file = water_model_files[ff_parameters["water_model"]]
        ff_parameters["water_model_file"] = water_model_file
