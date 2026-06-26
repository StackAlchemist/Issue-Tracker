import time
from fastapi import Request

async def timing_middleware(request: Request, call_next):
    start = time.perf_counter() #high res counter to measure elapsed time
    response = await call_next(request)
    response.headers["X-Process-Time"] =  f"{time.perf_counter() - start:.4f}s"
    return response

