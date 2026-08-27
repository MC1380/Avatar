from .agent import run_agent
from .state import AgentState


state = AgentState()


print("USER: سلام")
print("AVATAR:", run_agent("سلام", state))


print("\nUSER: میخوام با محمد ارتباط برقرار کنم")
print(
    "AVATAR:",
    run_agent(
        "میخوام با محمد ارتباط برقرار کنم",
        state,
    )
)


print("\nUSER: اسمم علی هست")
print(
    "AVATAR:",
    run_agent(
        "اسمم علی هست",
        state,
    )
)