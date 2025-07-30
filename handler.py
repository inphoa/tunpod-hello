def handler(event):
    return {
        "message": "Hello, world!",
        "input": event.get("input", {})
    }
