

def test_openai():
    from openai.types.chat import ChatCompletionMessageParam
    from ai_model.Client import create_default_completion_with_tools, handle_tool_calls
    system_message = """You are a precise routing assistant responsible for matching user requests with the appropriate Standard Operating Procedure (SOP) skill. Your goal is to identify the user's intent and retrieve the exact skill required.

**Workflow:**
1. **Initialize Descriptions:** Execute the `get_description` tool once at the start of the session to fetch the static list of all available skill descriptions and their IDs.
2. **Analyze & Match:** Compare incoming user queries against the loaded skill descriptions to identify the single best-fitting skill.
3. **Retrieve Skill:** Call the `get_skill` tool using the exact `Skill ID` corresponding to the selected skill.

**Operating Rules:**
* Run `get_description` only once at initialization; do not re-fetch descriptions for subsequent query evaluations unless instructed.
* Never guess or hardcode a `Skill ID` without matching it against the retrieved descriptions.
* Output tool calls directly and concisely without conversational filler."""

    user_message = """
    How can I transfer files to AVD?
    """
    messages: list[ChatCompletionMessageParam] = [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]
    response = create_default_completion_with_tools(messages)
    while response.choices[0].finish_reason == "tool_calls":
        print(response.choices[0].finish_reason)
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = create_default_completion_with_tools(messages)
    message = response.choices[0].message
    assert message != ""
    print(message)
    print(response.choices[0].finish_reason)

if __name__ == "__main__":
    test_openai()