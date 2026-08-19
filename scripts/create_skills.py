def description_template(skill_id, skill_name):
    return \
f"""---
id: {skill_id}
name: {skill_name}
tags: []
---

## What

## Why

## When

## Who

"""

def skill_template(skill_name):
    return \
f"""# {skill_name}

Describe what the skill does

## Add Custom Sections

## Example

"""

def create_skill():
    import argparse
    import os
    parser = argparse.ArgumentParser(description="Create a new skill")
    parser.add_argument("skill_name", type=str, help="Name of the skill to create")
    args = parser.parse_args()
    skill_id = args.skill_name.lower().replace(" ", "-")
    if os.path.exists(f"skills/{skill_id}"):
        overwrite = input(f"Skill '{skill_id}' already exists, Overwrite? (y/n): ")
        if overwrite.lower() != "y":
            return
    if not os.path.exists(f"skills/{skill_id}"):
        os.makedirs(f"skills/{skill_id}")
    with open(f"skills/{skill_id}/description.md", "w") as f:
        f.write(description_template(skill_id, args.skill_name))

    with open(f"skills/{skill_id}/skill.md", "w") as f:
        f.write(skill_template(args.skill_name))

if __name__ == "__main__":
    create_skill()

