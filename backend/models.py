from pydantic import BaseModel

class ScheduleInput(BaseModel):
    class_name: str
    subject: str
    teacher: str
    sessions: int
