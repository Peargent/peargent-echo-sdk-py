# peargent-echo

Official Python SDK for [Peargent Echo](https://echo.peargent.online) — persistent memory for AI agents.

## Installation

```bash
pip install peargent-echo
```

## Quick Start

```python
from peargent_echo import PeargentEcho

client = PeargentEcho(api_key="YOUR_API_KEY")  # Get from https://echo.peargent.online/dashboard

# Store a memory
client.add_memory("User prefers Python over JavaScript.")

# Search memories
results = client.search("programming preferences")
print(results)

# Get user profile
profile = client.get_profile()
print(profile)
```

## API Reference

### `add_memory(content, **options)`

Store a new memory. Similar memories are automatically merged.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `filter` | bool | `True` | Filter irrelevant content |
| `extract` | bool | `True` | Extract entities & facts |
| `agent_id` | str | - | Agent identifier |
| `run_id` | str | - | Conversation run ID |
| `metadata` | dict | - | Custom JSON metadata |

### `search(query, **options)`

Semantically search through stored memories.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `limit` | int | `10` | Max results to return |
| `include_graph` | bool | `False` | Include related memories |

### `get_profile()`

Get the auto-generated user profile from stored memories.

## License

MIT
