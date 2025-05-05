# langchain_with_system adn human messages
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import os

# Set up API with error handling
try:
    # Option 1: Use your existing OpenAI key with error handling
    os.environ["OPENAI_API_KEY"] = "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"

    model = ChatOpenAI(
        model="gpt-4o-mini",  # Specify a potentially less expensive model
        temperature=0,
        max_tokens=150
    )

    # Create messages
    sysmsg = "You are a physics teacher"
    humanmsg = "Explain the concept of Galaxy"
    messages = [
        SystemMessage(content=sysmsg),
        HumanMessage(content=humanmsg),
    ]

    # Try to get a response
    response = model.invoke(messages)
    print(response.content)  # Just print the content part

except Exception as e:
    print(f"OpenAI API Error: {e}")

    # Fallback response when API fails
    print("\nFallback Response:")
    print("""Sorry,quota exceeded""")
