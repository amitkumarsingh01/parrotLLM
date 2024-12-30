class Config:
    PAGE_TITLE = "Chatbot"

    OLLAMA_MODELS = ('llama3.2:latest')

    SYSTEM_PROMPT = f"""You are a helpful chatbot that has access to the following 
                    open-source models {OLLAMA_MODELS}.
                    Answer short and crispy.
                    """
    