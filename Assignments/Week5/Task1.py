# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the List of parameters.
# You may introduce private/protected utility methods though.
class Calendar:

    def __init__(self, event_id, date_str, start_time, end_time, description):
        self.event_id = event_id
        self.event_id = event_id
        self.date_str = date_str
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        

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