# DS Condition-Based Waiting

## Overview

Notebook and pipeline debugging often fail because analysts guess when data is ready: "the extract should be there by now", "the cache probably refreshed", "rerunning one more time will fix it".

**Core principle:** Wait for the analytical condition you need, not for an arbitrary amount of time.

## When to Use

- Waiting for a table, extract, or file to appear
- Waiting for asynchronous job output before rerunning analysis
- Verifying a notebook export or cached dataset is actually refreshed
- Polling for a known readiness condition in a data workflow

## Core Pattern

```python
# Wrong: arbitrary sleep
time.sleep(60)
df = read_parquet(path)

# Better: wait for the condition
wait_for(lambda: Path(path).exists(), "extract file exists")
df = read_parquet(path)
```

## Minimal Helper

```python
import time

def wait_for(condition, description, timeout_s=300, poll_s=5):
    start = time.time()
    while True:
        if condition():
            return
        if time.time() - start > timeout_s:
            raise TimeoutError(f"Timeout waiting for {description}")
        time.sleep(poll_s)
```

## Common Mistakes

- Sleeping first, checking later
- Polling an already-stale DataFrame instead of reloading state
- Waiting forever without timeout

## Important Limit

Do not use this to hide broken reproducibility. If the pipeline needs repeated waiting because state is unclear, fix the upstream process.
