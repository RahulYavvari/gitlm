from gitlm.model_interface import model

VALID_GIT_COMMANDS = [
    "add", "commit", "push", "pull", "status", "checkout", 
    "branch", "merge", "rebase", "log", "diff", "clone", 
    "fetch", "reset", "stash", "tag"
]

def is_valid_git_command(cmd):
    parts = cmd.strip().split()
    if len(parts) < 2 or parts[0] != "git":
        return False
    if parts[1] not in VALID_GIT_COMMANDS:
        return False
    return True

def explain(cmd):
    print("[Explanation]")

    if is_valid_git_command(cmd):
        prompt = f"""
        Explain this Git command.
Stop after explanation.

Command: {cmd}
        """
        stream_output = model.model_inference(
            messages=[{"role": "user", "content": prompt}]
        )

        for chunk in stream_output:
            delta = chunk["choices"][0]["delta"]
            if "content" in delta:
                print(delta["content"], end="", flush=True)
    else:
        print("Invalid git command!")