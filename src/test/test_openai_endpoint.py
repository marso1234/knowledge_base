

def test_openai():
    from openai.types.chat import ChatCompletionMessageParam
    from ai_model.Client import create_default_completion
    system_message = """
    You are a cat. You don't speak. Just meow
    """

    user_message = """
    Hi, kitty!
    """

    messages: list[ChatCompletionMessageParam] = [{"role": "system", "content": system_message}, {"role": "user", "content": user_message}]

    response = create_default_completion(messages)
    
    message = response.choices[0].message
    assert message != ""
    print(message)
    print(response.choices[0].finish_reason)

if __name__ == "__main__":
    test_openai()