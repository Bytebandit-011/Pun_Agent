from agno.agent import  Agent 
from agno.models.google import Gemini
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Fun to Pun Agent", page_icon="")
st.title("Pun Agent")

subject = st.text_input("Enter a Subject to generate pun")
generate_button = st.button("Generate Pun", disabled=(subject.strip()== ""))

if generate_button:
    if subject.strip() == "":
        st.warning("Please enter a subject first")
    else:
        with st.spinner("Generating your pun..."):
            try:
                pun_agent = Agent(
                    name='Pun Agent',
                    agent_id="pun_agent",
                    model=Gemini(id="gemini-2.0-flash"),
                    description="You are an AI agent that can Generate Pun",
                    instructions=[ """
                        You are a witty pun generator. Always respond with jokes, wordplay, and puns.
                        - Keep answers short, funny, and clever.
                        - If the user asks a normal question, twist it into a pun.
                        - Try to use puns related to the user’s topic.
                        - Example: If the user asks about coding, make programming puns.
                        - Example: If they ask about food, use food puns.
                        - Always keep the tone lighthearted and humorous.
                    """ ],
                    markdown=True,
                    debug_mode=True,
                )

                pun = pun_agent.run(
                    f"Make a funny pun about: {subject}"
                )

                # Handle different response object structures
                st.success("Here's your pun:")
                st.write(pun.content)
                
                

            except Exception as e:
                st.error(f"Error generating pun: {e}")
                
                st.write("Debug info:", str(e))
