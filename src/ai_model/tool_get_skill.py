get_skills_json = {
    "name": "get_skill",
    "description": "Providing the Skill ID, show the corresponding skill to user",
    "parameters": {
        "type": "object",
        "properties": {
            "skill_id": {
                'type': 'string',
                'title': 'Skill ID'
                }
            },
        "required": ["skill_id"],
        "additionalProperties": False
    }
}

def toolcall_get_skill(skill_id):
    import os
    skill_directory = os.path.join(os.getcwd(), "skills")
    skill_file = os.path.join(skill_directory, skill_id,"skill.md")
    if os.path.exists(skill_file):
        with open(skill_file, "r", encoding="utf-8") as f:
            skill_content = f.read()
            print(skill_content)
            return f"Skill has shown to user"
    else:
        return f"Skill with ID '{skill_id}' not found."

if __name__ == "__main__":
    print(toolcall_get_skill("add-new-user-and-assign-group-to-instace"))