from langsmith import traceable

PROMPT_TEMPLATE = """
You are a helpful assistant.
Here is the context:
{documents_as_context}

Here is the query:
{query}
"""


@traceable
class Prompt:
    def __init__(self, prompt_template: str = PROMPT_TEMPLATE):
        self.prompt_template = prompt_template

    def populate(self, query: str, documents_as_context: str) -> str:
        return self.prompt_template.format(query=query, documents_as_context=documents_as_context)
