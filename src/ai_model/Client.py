
import os
from dotenv import load_dotenv
load_dotenv(override=True)
import ai_model.tool_get_description as get_description
import ai_model.tool_get_skill as get_skill
import json

default_client = None
tools = [{"type": "function", "function": get_description.get_description_json},
        {"type": "function", "function": get_skill.get_skills_json}]
tool_payload = {"get_description": get_description.toolcall_get_description, "get_skill": get_skill.toolcall_get_skill}

def get_default_client():
    global default_client
    if default_client is None:
        from openai import OpenAI
        import os
        from dotenv import load_dotenv
        load_dotenv(override=True)
        api_key = os.getenv("ANSPIRE_API_KEY")
        endpoint = os.getenv("ANSPIRE_ENDPOINT")
        default_client = OpenAI(api_key=api_key, base_url=endpoint)
    return default_client

def create_default_completion(messages):
    model = os.getenv("DEFAULT_MODEL")
    if model is not None:
        openai_client = get_default_client()
        response = openai_client.chat.completions.create(model=model, messages=messages)
        return response
    else:
        print("Cannot get model env variable!")
        raise Exception("Cannot get model env variable")

def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        tool = tool_payload.get(tool_name)
        result = tool(**arguments) if tool else {}
        results.append({"role": "tool","content": json.dumps(result),"tool_call_id": tool_call.id})
    return results

def create_default_completion_with_tools(messages):
    model = os.getenv("DEFAULT_MODEL")
    if model is not None:
        openai_client = get_default_client()
        response = openai_client.chat.completions.create(model=model, messages=messages, tools=tools)
        return response
    else:
        print("Cannot get model env variable!")
        raise Exception("Cannot get model env variable")
