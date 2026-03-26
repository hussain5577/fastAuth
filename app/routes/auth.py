from fastapi import APIRouter, HTTPException, Depends
from app.services.google_auth import get_google_user_data
from app.auth.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.get("/google/login")
def google_login():
    # Redirect user to Google's OAuth page
    return {
        "url": f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={settings.GOOGLE_CLIENT_ID}&redirect_uri={settings.GOOGLE_REDIRECT_URI}&scope=openid%20email%20profile"
    }

@router.get("/google/callback")
async def google_callback(code: str):
    user_info = await get_google_user_data(code)
    if not user_info:
        raise HTTPException(status_code=400, detail="Failed to fetch user from Google")
    
    # Here you would typically check if user exists in DB; if not, create them.
    # For now, we just issue a JWT.
    token = create_access_token(data={"sub": user_info["email"]})
    return {"access_token": token, "token_type": "bearer"}