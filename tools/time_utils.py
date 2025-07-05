from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def get_six_months_ago_at_midnight(months_back: int = 6, result_format: str = "%A, %B %d at %I:%M %p") -> str:
    """
    Returns a formatted string of the date that was `months_back` months ago from now, set at midnight.
    Example: "Tuesday, January 16 at 12:00 AM"
    """
    try:
        if months_back < 0 or months_back > 12:
            raise ValueError("Invalid month range: must be between 0 and 12")
        
        now = datetime.now()
        past = now - relativedelta(months=months_back)
        midnight = past.replace(hour=0, minute=0, second=0, microsecond=0)
        return midnight.strftime(result_format)
    except Exception as e:
        return f"Error calculating date: {str(e)}"
