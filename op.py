# install dependencies if needed:
# pip install langchain openai

from langchain import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from langchain_openai import ChatOpenAI

# # Set your API key
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
#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
# # Initialize the OpenAI model (e.g., GPT-3.5)
# llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.7,api_key="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")

# 2. Initialize ChatOpenAI model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=150,
    api_key="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"
    
)

# 3. Prepare a prompt template
template = PromptTemplate(
    input_variables=["name"],
    template="Write a friendly greeting to {name}."
)

# 4. Create the LLMChain
chain = LLMChain(prompt=template, llm=llm)

# 5. Run the chain
if __name__ == "__main__":
    name = "Alice"
    result = chain.invoke({"name": name})
    print(result)