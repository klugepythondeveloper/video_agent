from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI(title="Video Agent API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    print(">>> WebSocket connection attempt")
    await ws.accept()
    print(">>> WebSocket accepted")

    try:
        while True:
            data = await ws.receive_text()
            print(">>> Received:", data)
            await ws.send_text(f"Echo from backend: {data}")
    except WebSocketDisconnect:
        print(">>> WebSocket disconnected")
