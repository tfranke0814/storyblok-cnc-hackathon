Quick localhost dev runtime for backend API. Command should be in the backend directory.

```sh
pip install uv # If you have not done so already!
uv run uvicorn foodapi.api:app --reload --host 127.0.0.1 --port 8000
```
