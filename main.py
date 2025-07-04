from browser_use.llm import ChatGoogle
from browser_use import Agent, BrowserSession
import asyncio

llm = ChatGoogle(model='gemini-2.0-flash-lite')

browser_session = BrowserSession(
    storage_state='linkedin_auth.json',
)

agent = Agent(
    task="""
1. Go to https://www.linkedin.com/feed
find some interesting posts related to AI, ML, or Data Science.
2. Summarize the posts in a concise manner.
3. Provide insights or key takeaways from the posts.
4. If any post is particularly interesting, provide a brief analysis of why it stands out.
""",
    llm=llm,
    browser_session=browser_session,
)

async def main():
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
