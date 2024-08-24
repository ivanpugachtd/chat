from typing import List
from fastapi import APIRouter, FastAPI
import os

class App:
    def __init__(self, routers: List[APIRouter], port: int):
        self.app = FastAPI()
        self.routers = routers
        self.port = port
        
    def initialize_routers(self):
        for router in self.routers:
            self.app.include_router(router)
            
    def initialize_middleware(self):
        pass
    
    def run(self):
        import uvicorn
        stage = os.getenv("STAGE", "LOCAL")
        uvicorn.run("main:app", host="0.0.0.0", port=self.port, reload=stage == "local")
    