import json
import os

from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

from slack_agent.prompt import AGENT_PROMPT
from dotenv import load_dotenv
load_dotenv()


SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN") 
SLACK_TEAM_ID = os.getenv("SLACK_TEAM_ID") 
SLACK_CHANNEL_IDS = os.getenv("SLACK_CHANNEL_IDS") 


root_agent = Agent(
    model="gemini-2.0-flash",
    name="slack_agent",
    instruction=AGENT_PROMPT,
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command = "npx.cmd",
                args= [
                    "-y",
                    "@modelcontextprotocol/server-slack"
                ],
                env = {
                    "SLACK_BOT_TOKEN": SLACK_BOT_TOKEN,
                    "SLACK_TEAM_ID": SLACK_TEAM_ID,
                    "SLACK_CHANNEL_IDS": SLACK_CHANNEL_IDS
                    },
            )
        ),
    ],
)



