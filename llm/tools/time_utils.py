from datetime import datetime
from pydantic import BaseModel, Field

class TimeInput(BaseModel):
    past: str = Field(..., description="The past datetime in ISO format (e.g., 2024-06-18T14:30:00)")
    timespan: str = Field("seconds", description="Timespan to return: seconds, minutes, hours, or days")
    result_format: str = Field(
        "%Y-%m-%d %H:%M:%S",
        description="(Optional) Format to return the past time as a string. Follows Python's datetime strftime format.",
    )

def getElapsedTimeFrom(past: str, timespan: str = "seconds", result_format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Calculates the elapsed time between the current time and a past datetime.
    """
    try:
        past_dt = datetime.fromisoformat(past)
        now = datetime.now()
        delta = now - past_dt

        if timespan == "seconds":
            result = delta.total_seconds()
        elif timespan == "minutes":
            result = delta.total_seconds() / 60
        elif timespan == "hours":
            result = delta.total_seconds() / 3600
        elif timespan == "days":
            result = delta.days
        else:
            return f"Invalid timespan: {timespan}. Use seconds, minutes, hours, or days."

        formatted_past = past_dt.strftime(result_format)
        return f"Elapsed time since {formatted_past}: {round(result, 2)} {timespan}"

    except ValueError as e:
        return f"Invalid datetime format. Please use ISO format. Error: {e}"
