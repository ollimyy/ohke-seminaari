from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse

from .price_estimator import estimate_price_from_condition

app = FastAPI()

@app.get("/estimate-price")
async def estimate_price(
    item_description: str = Query(..., description="Description of the item"),
    condition: int = Query(..., description="Condition of the item (1-5)", ge=1, le=5)
):

    try:
        price_estimate = estimate_price_from_condition(condition, item_description)
        # placeholders, replace with proper calculation
        min_price = int(price_estimate * 0.7)
        max_price = int(price_estimate * 1.2)

        return JSONResponse(content={
            "min_price": min_price,
            "estimated_price": price_estimate,
            "max_price": max_price
        }, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")