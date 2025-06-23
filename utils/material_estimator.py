def estimate_materials(detected_elements):
    # Detailed Material Estimation based on detected elements
    material_estimates = {}

    # Example: Walls Material Estimate
    material_estimates["Walls"] = {
        "Material": "Brick or Concrete Blocks (RCC for structural)",
        "Estimated Quantity": f"Approx. {detected_elements.get('Walls', 0)} linear meters",
        "Material Type": "Brick or Concrete Blocks (RCC for structural)",
        "Details": "Walls are typically made of bricks or concrete blocks."
    }

    # Example: Concrete Estimation for Slab, Beams, etc.
    material_estimates["Concrete"] = {
        "Material": "Reinforced Concrete (RCC)",
        "Estimated Quantity": f"Approx. {detected_elements.get('Concrete', 0)} m³",
        "Material Type": "RCC (concrete, steel reinforcement)",
        "Details": "The floor slab is assumed to be made of RCC."
    }

    # Other materials can be added similarly (Steel, Cement, etc.)
    return material_estimates

def generate_image_description(detected_elements):
    # Generate a simple description of the detected elements
    description = "Material Estimation Based on AutoCAD Drawing\n\n"
    description += "### Structural Elements\n"
    description += f"Walls: {detected_elements.get('Walls', 0)} linear meters\n"
    description += f"Concrete: {detected_elements.get('Concrete', 0)} m³\n"

    # Add descriptions for detected elements like windows, doors, etc.
    description += "\n### Architectural Elements\n"
    description += f"Estimated Quantity for Windows: {detected_elements.get('Windows', 0)} windows\n"
    description += f"Estimated Quantity for Doors: {detected_elements.get('Doors', 0)} doors\n"

    return description
