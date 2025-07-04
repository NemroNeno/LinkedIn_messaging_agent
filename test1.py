# linkedin_connection_messenger.py
import asyncio, os, time, json, random
from browser_use import Agent, BrowserSession
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use.llm import ChatGoogle
LOG_FILE = "sent_messages.log"
CONNECTIONS_URL = "https://www.linkedin.com/mynetwork/invite-connect/connections/"
# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    model_kwargs={"automatic_function_calling": {"disable": True}},
    api_key="AIzaSyBc_vgT-svDtj1b2BJa1tAFPyPVlp5-uw8"
)

# Saved login session
browser_session = BrowserSession(storage_state="linkedin_auth.json")

# Task template with placeholder for each connection
TASK_TEMPLATE = """
1. Navigate to: {connections_url}
2. Identify the {num} visible connection.
3. Click "Message" for that connection.
4. Send the exact message: "{fact}"
5. Close the message pane.
"""

def generate_fact():
    prompt = (
        "Provide one interesting and unique fact about business, technology, "
        "or data science. It should be concise and engaging for a professional audience."
    )
    return llm.invoke(prompt).content.strip()

async def main():
    sent_count = 0
    with open(LOG_FILE, "a") as log:
        while sent_count < 5:  # Adjust to 5 for full requirement
            fact = generate_fact()
            print("3333333333333333333333333333333333333333333333333333333333333")
            print(f"Generated Fact: {fact}")
            task_str = TASK_TEMPLATE.format(connections_url=CONNECTIONS_URL, fact=fact, num=sent_count + 2)

            agent = Agent(
                name=f"linkedin_msg_{sent_count+1}",
                task=task_str,
                llm=ChatGoogle(model='gemini-2.0-flash-exp'),
                browser_session=browser_session,
                
            )

            await agent.run()
            log.write(json.dumps({
                "timestamp": time.time(),
                "fact": fact
            }) + "\n")

            sent_count += 1
            await asyncio.sleep(random.uniform(2, 5))

    print(f"✅ Done: Sent {sent_count} messages. See {LOG_FILE}")

if __name__ == "__main__":
    asyncio.run(main())
