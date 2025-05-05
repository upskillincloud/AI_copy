from langchain import OpenAI
import os
os.setenv("OPENAI_API_KEY") = "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"

llm = OpenAI()
text = "What would be a good company name for a company that makes toy for kids"

print(llm.invoke(text))
