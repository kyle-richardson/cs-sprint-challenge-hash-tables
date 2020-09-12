#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    for ticket in tickets:
        source = ticket.source
        dest = ticket.destination
        d[source] = dest
    current = d["NONE"]
    route = []
    while current is not "NONE":
        route.append(current)
        current = d[current]
    route.append(current)
    return route
