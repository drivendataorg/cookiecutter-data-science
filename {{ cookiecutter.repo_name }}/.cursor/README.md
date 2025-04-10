# Cursor Integration

- `artifacts` -- Similar to Claude artifacts, these are temporary files (typically markdown) created and updated by LLMs where the chat interface is not enough. Managed by `rules/302_artifacts.mdc`
- `mem` -- Memory bank for LLMs to update a knowledge base of your repository. Currently not functioning. Managed by `rules/301_memory.mdc`
- `notes` -- Agentic note taking system. This is described in `rules/303_note-taking.mdc`
- `rules` -- This is part of the cursor rules system. This is context that is applied selectively when you have a certain file open or the agent decides to read it in from a description. This is kind of an automatically or manually applied prompt bank.

## Model Context Protocol (MCP)

GOTem recommneds using [ComposeIO](https://mcp.composio.dev/). These make adding tools to your model extremely easy.
