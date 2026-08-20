
default_client = None

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
    import os
    from dotenv import load_dotenv
    load_dotenv(override=True)
    model = os.getenv("DEFAULT_MODEL")
    if model is not None:
        openai_client = get_default_client()
        response = openai_client.chat.completions.create(model=model, messages=messages)
        return response
    else:
        print("Cannot get model env variable!")
        raise Exception("Cannot get model env variable")