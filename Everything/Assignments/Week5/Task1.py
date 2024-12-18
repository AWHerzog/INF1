from datetime import datetime

class Calendar:
    def __init__(self):
        self.events = []
        self.next_event_id = 1

    def add_event(self, date_str, start_time, end_time, description):
        start_dt = datetime.strptime(f"{date_str} {start_time}", "%Y-%m-%d %H:%M")
        end_dt = datetime.strptime(f"{date_str} {end_time}", "%Y-%m-%d %H:%M")
        
        if start_dt >= end_dt:
            raise Exception("Start time must be before end time.")
        
        event = (self.next_event_id, start_time, end_time, description)
        self.events.append((date_str, event))
        self.next_event_id += 1
        
        return event[0]

    def get_events(self, date_str):
        events_for_date = [event for date, event in self.events if date == date_str]
        sorted_events = sorted(events_for_date, key=lambda x: x[1])
        return sorted_events

    def delete_event(self, event_id):
        for i, (date, event) in enumerate(self.events):
            if event[0] == event_id:
                return self.events.pop(i)[1]
        raise Exception("Event ID does not exist.")


# You can play around with your implementation in the following body.
# The contained statements will be ignored while evaluating your solution.
if __name__ == "__main__":
    cal = Calendar()
    event_id_dinner = cal.add_event("2024-12-24", "18:00", "20:00", "Christmas Dinner with Family")
    event_id_sleep = cal.add_event("2024-12-24", "21:00", "23:59", "Sleep")
    print(cal.get_events("2024-12-24"))
    cal.delete_event(event_id_dinner)
    print(cal.get_events("2024-12-24"))
    cal.delete_event(event_id_sleep)
    print(cal.get_events("2024-12-24"))
