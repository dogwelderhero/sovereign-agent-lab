"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = [
    "check_pub_availability",
    "calculate_catering_cost",
    "get_edinburgh_weather",
    "generate_event_flyer",
]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

# Optional — anything unexpected.
# If you used a non-default model via RESEARCH_MODEL env var, note it here.
# Example: "Used nvidia/nemotron-3-super-120b-a12b for the agent loop."
TASK_A_NOTES = "The agent completed the task successfully, but it only checked The Albanach and did not check The Haymarket Vaults even though the prompt asked for both venues."

# ── Task B ─────────────────────────────────────────────────────────────────
#
# The scaffold ships with a working generate_event_flyer that has two paths:
#
#   - Live mode: if FLYER_IMAGE_MODEL is set in .env, the tool calls that
#     model and returns a real image URL.
#   - Placeholder mode: otherwise (the default) the tool returns a
#     deterministic placehold.co URL with mode="placeholder".
#
# Both paths return success=True. Both count as "implemented" for grading.
# This is not the original Task B — the original asked you to write a direct
# FLUX image call, but Nebius removed FLUX on 2026-04-13. See CHANGELOG.md
# §Changed for why we pivoted the task.

# Did your run of the flyer tool produce a success=True result?
# (This will be True for both live and placeholder mode — both are valid.)
TASK_B_IMPLEMENTED = True   # True or False

# Which path did your run take? "live" or "placeholder"
# Look for the "mode" field in the TOOL_RESULT output of Task B.
# If you didn't set FLYER_IMAGE_MODEL in .env, you will get "placeholder".
TASK_B_MODE = "placeholder"

# The image URL returned by the tool. Copy exactly from your terminal output.
# In placeholder mode this will be a placehold.co URL.
# In live mode it will be a provider CDN URL.
TASK_B_IMAGE_URL = "https://placehold.co/1200x628/1a1a2e/eaeaea?text=The+Haymarket+Vaults+%7C+160+guests&id=2ef939fbbaf6"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# Why did the agent's behaviour NOT change when Nebius removed FLUX?
# One sentence. This is the point of the lesson.
TASK_B_WHY_AGENT_SURVIVED = """
The agent survived because the flyer tool was implemented with graceful fallback, returning a structured placeholder result instead of crashing when no live image model was available.
"""

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The pivot happened right after the first tool result showed that The Bow Bar had capacity 80, status full, and meets_all_constraints false, after which the agent immediately called check_pub_availability for The Haymarket Vaults.
"""

SCENARIO_1_FALLBACK_VENUE = "The Haymarket Vaults"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
<think>
Okay, let's see. The user is looking for a venue in Edinburgh that can accommodate 300 people with vegan options. They provided a list of known venues: The Albanach, The Haymarket Vaults, The Guilford Arms, and The Bow Bar. I checked each one using the check_pub_availability function.

First, The Albanach had a capacity of 180, which is under 300. The Haymarket Vaults had 160, also too small. The Guilford Arms had 200, still not enough. The Bow Bar has 80, which is way below. All of them except The Guilford Arms had vegan options, but even that one didn't meet the capacity. None of the venues can handle 300 people. So, I need to inform the user that none of the known venues meet their requirements. They might need to look for another place or adjust their capacity needs.
</think>

None of the known Edinburgh venues can accommodate 300 people with vegan options. The maximum capacities are:
- The Albanach: 180
- The Haymarket Vaults: 160
- The Guilford Arms: 200 (no vegan options)
- The Bow Bar: 80

Would you like to:
1. Search for alternative venues outside this list?
2. Adjust the capacity requirements?
3. Remove the vegan dietary constraint?
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "I don't have access to real-time train schedules or transportation data."

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Yes, this behaviour is acceptable and preferable to hallucinating. The agent recognized that train schedules were outside its toolset, made no unsupported tool call, and clearly stated its limitation instead of inventing a departure time.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
\t__start__([<p>__start__</p>]):::first
\tagent(agent)
\ttools(tools)
\t__end__([<p>__end__</p>]):::last
\t__start__ --> agent;
\tagent -.-> __end__;
\tagent -.-> tools;
\ttools --> agent;
\tclassDef default fill:#f2f0ff,line-height:1.2
\tclassDef first fill-opacity:0
\tclassDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/flows.yml. Min 30 words.
TASK_D_COMPARISON = """
The LangGraph graph is very compact: one agent node decides at runtime whether to call tools again or finish. In contrast, Rasa flows.yml describes behaviour explicitly as predefined flows. LangGraph is more dynamic and loop-based, while Rasa is more structured and prescriptive.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
The most unexpected behaviour was that in Task A the agent did not follow the instruction literally to check both The Albanach and The Haymarket Vaults. It found that The Albanach worked, then moved on to catering, weather, and flyer generation. So it solved the task efficiently, but not completely faithfully.
"""