"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh"
QUERY_2_FINAL_ANSWER  = "It seems there are no Edinburgh venues currently available that can accommodate 300 people *and* offer vegan options. Would you like me to:\n\n1. Search for venues with a lower minimum capacity (e.g., 250)?\n2. Look for non-vegan venues that can accommodate 300 people?\n3. Check for multiple smaller venues that could be combined?\n\nLet me know how you'd like to proceed!"

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
After changing The Albanach's status from available to full in
sovereign_agent/tools/mcp_venue_server.py and rerunning the client, the agent's
best match changed from The Albanach to The Haymarket Vaults. I did not need to
change exercise4_mcp_client.py or the agent loop at all. Only the MCP server
data changed, and the client automatically picked up the new result through the
same discovered tools. After the test, I reverted the venue status back.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 4
LINES_OF_TOOL_CODE_EX4 = 0

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP gives a stable interface between the agent and the tools. The client does
not need hardcoded knowledge of venue logic or venue data. When the server-side
data or implementation changes, the same agent can keep working without code
changes in the client. It also makes reuse easier, because both LangGraph and
Rasa can connect to the same MCP server instead of duplicating tool logic in
two separate places.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────

WEEK_5_ARCHITECTURE = """
- The Planner is a stronger reasoning model that takes a raw user goal and turns it into ordered subgoals; it lives in the autonomous-loop half of PyNanoClaw.
- The Executor is the LangGraph ReAct agent that carries out subgoals using tools and MCP-connected services; it lives in the autonomous-loop half.
- The Memory store keeps task history, preferences, and reusable facts across steps and sessions; it lives in the shared layer between both halves.
- The Handoff bridge routes tasks between the autonomous LangGraph side and the structured Rasa side when a conversational or voice workflow is better suited; it lives in the shared layer.
- The Rasa structured agent handles guided conversational flows, slot-filling, and predictable voice interactions; it lives in the structured-agent half.
- The MCP gateway exposes shared tools like venue search, venue details, and later file or web operations to both LangGraph and Rasa; it lives in the shared layer.
- The Observability layer records traces, tool calls, errors, and cost usage so the system can be debugged and governed; it lives across both halves.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The LangGraph research-style agent feels right for open-ended discovery and
tool-based reasoning. In Exercise 4 it searched venues, fetched details, and
adapted to MCP-served data with minimal client logic. In Exercise 2 it also
handled ambiguity and failure cases by trying tools, observing outputs, and
changing course. A call-oriented agent should instead be the structured Rasa
side, because live calls need predictable turns, explicit flows, and tighter
control over what happens next. Swapping them feels wrong because the research
agent is flexible but loose, while voice or call handling needs consistency,
guardrails, and a clearer conversation structure.
"""