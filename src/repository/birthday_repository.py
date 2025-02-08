from sqlalchemy.orm import Session
from sqlalchemy.sql import extract
from datetime import date, timedelta
from src.database.models import Contact

def get_contacts_with_upcoming_birthdays(db: Session, days: int = 7):
    """Retrieve contacts with upcoming birthdays within the specified range"""
    today = date.today()
    end_date = today + timedelta(days=days)

    today_month, today_day = today.month, today.day
    end_month, end_day = end_date.month, end_date.day

    # Якщо діапазон перетинає Новий рік (наприклад, грудень → січень)
    if today_month > end_month:
        return db.query(Contact).filter(
            (extract("month", Contact.birth_date) > today_month) |
            ((extract("month", Contact.birth_date) == today_month) & (extract("day", Contact.birth_date) >= today_day)) |
            (extract("month", Contact.birth_date) < end_month) |
            ((extract("month", Contact.birth_date) == end_month) & (extract("day", Contact.birth_date) <= end_day))
        ).all()

    # Якщо діапазон в межах одного року
    return db.query(Contact).filter(
        (extract("month", Contact.birth_date) > today_month) |
        ((extract("month", Contact.birth_date) == today_month) & (extract("day", Contact.birth_date) >= today_day)),
        (extract("month", Contact.birth_date) < end_month) |
        ((extract("month", Contact.birth_date) == end_month) & (extract("day", Contact.birth_date) <= end_day))
    ).all()
