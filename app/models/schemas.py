from pydantic import BaseModel
from typing import Optional

class AdFrequencyInput(BaseModel):
    user_key_id: str
    country: str
    age: int
    sex: str
    easy_completion_rate: float
    medium_completion_rate: float
    hard_completion_rate: float
    session_count: int
    total_session_time: int
    total_ad_viewed: int
    total_earned_reward_amount_in_usd: float

class ChurnInput(BaseModel):
    user_key_id: str
    country: str
    age: int
    sex: str
    first_time_login: str
    session_count: int
    total_session_time_x: int
    total_ad_viewed: int
    total_spent_in_usd: float
    total_spent_time: float
    total_session_time_y: int
    level_completion_count: int
    avg_level_completion_time: float
    easy_completion_rate: float
    medium_completion_rate: float
    hard_completion_rate: float

class IAPPackInput(BaseModel):
    user_key_id: str
    country: str
    age: int
    sex: str
    total_spent_in_usd: float
    total_spent_time: float
    session_count: int
    total_session_time: int
    easy_completion_rate: float
    medium_completion_rate: float
    hard_completion_rate: float

class LevelDifficultyInput(BaseModel):
    user_key_id: str
    country: str
    age: int
    sex: str
    total_spent_in_usd: float
    total_spent_time: float
    avg_daily_session: float
    avg_weekly_session: float
    easy_completion_rate: float
    medium_completion_rate: float
    hard_completion_rate: float
