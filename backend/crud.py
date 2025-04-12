def generate_schedule(data):
    # Giả lập sắp xếp thời khóa biểu (sẽ nâng cấp sau)
    return {
        "class": data.class_name,
        "schedule": [
            {"day": "Monday", "subject": data.subject, "teacher": data.teacher}
        ]
    }
