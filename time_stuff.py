def get_hour():
    from datetime import datetime
    from pytz import timezone
    tz = timezone('EST')
    today = datetime.now(tz)
    hour = today.strftime('%H')
    hours = (datetime(1900, 1, 1, int(hour), 0), datetime(1900, 1, 1, 20, 0))