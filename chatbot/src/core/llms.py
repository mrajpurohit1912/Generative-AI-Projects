from autogen_ext.models.ollama import OllamaChatCompletionClient


class LLMS:
    def get_ollama_llm(self,model_name:str="codellama:latest"):
        llm = OllamaChatCompletionClient(model=model_name,host="http://localhost:11434",model_info={
                "description": "ollam model running locally on ollama server",
                "json_output": False  ,
                "vision":False,
                "function_calling":True
            })
        
        return llm
