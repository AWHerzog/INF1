# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the List of parameters.
# You may introduce private/protected utility methods though.
from datetime import datetime

class Calendar:

    def __init__(self):
        self.next_event_id = 1
        self.events = []

    def add_event(self, date_str, start_time, end_time, description):
        
        start_time_obj = datetime.strptime(start_time, "%H:%M").time()
        end_time_obj = datetime.strptime(end_time, "%H:%M").time()

        
        if start_time_obj >= end_time_obj:
            raise Exception("Start time cannot be greater or equal to end time")

        
        event = {
            "event_id": self.next_event_id,
            "date_str": date_str,
            "start_time": start_time,
            "end_time": end_time,
            "description": description
        }

        
        self.events.append(event)

        
        self.next_event_id += 1

        
        return event["event_id"]

    def get_events(self, date_str):
        
        filtered_events = [event for event in self.events if event["date_str"] == date_str]
        
        sorted_events = sorted(filtered_events, key=lambda x: x["start_time"])
        
        return [(event["event_id"], event["start_time"], event["end_time"], event["description"]) for event in sorted_events]

    def delete_event(self, event_id):
        
        for event in self.events:
            if event["event_id"] == event_id:
                self.events.remove(event)
                return (event["event_id"], event["start_time"], event["end_time"], event["description"])

        
        raise Exception("Event ID not found")


if __name__ == "__main__":
    cal = Calendar()
    event_id_dinner = cal.add_event("2024-12-24", "18:00", "20:00", "Christmas Dinner with Family")
    event_id_sleep = cal.add_event("2024-12-24", "21:00", "23:59", "Sleep")
    print(cal.get_events("2024-12-24"))
    cal.delete_event(event_id_dinner)
    print(cal.get_events("2024-12-24"))
    cal.delete_event(event_id_sleep)
    print(cal.get_events("2024-12-24"))
