get_description_json = {
    "name": "get_description",
    "description": "Read all the skills description created by the user and decide which one is needed",
}

def toolcall_get_description():
    import os
    skill_directory = os.path.join(os.getcwd(), "skills")
    skill_ids = os.listdir(skill_directory)
    result = []
    for i, skill_id in enumerate(skill_ids):
        description_file = os.path.join(skill_directory, skill_id,"description.md")
        if os.path.exists(description_file):
            with open(description_file, "r") as f:
                description_content = f.read()
                result.append(description_content)

    return "\n\n".join(result)

if __name__ == "__main__":
    print(toolcall_get_description())