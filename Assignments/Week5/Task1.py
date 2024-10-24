
class Calendar:

    def __init__(self, event_id):
        self.event_id = event_id
        

    def add_event(self, date_str, start_time, end_time, description):
        pass

    def get_events(self, date_str):
        pass

    def delete_event(self, event_id):
        pass


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
