from langchain_core.callbacks.base import BaseCallbackHandler

class APICallLogger(BaseCallbackHandler):
    def __init__(self):
        self.call_count = 0

    def on_llm_start(self, serialized: dict, prompts: list[str], **kwargs) -> None:
        self.call_count += 1
        print(f"{'='*60}\n📡 LLM API CALL STARTED: {self.call_count}\n{'='*60}")
        for i, prompt in enumerate(prompts):
            print(f"🔹 Prompt {i+1}:\n{prompt}\n")
        
        print(kwargs['invocation_params']['tools'])
        print('\n')

    def on_llm_end(self, response, **kwargs):
        print(f"✅ LLM API CALL COMPLETED: {self.call_count}")
        print(f"Response:\n{response.generations}\n")