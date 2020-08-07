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
    flight_path = {}
    route = [None] * length
    # check for the start destination of our trip
    for ticket in tickets:
        if ticket.source == "NONE":
            # add it to our `route` array as the first element
            route[0] = ticket.destination
        else:
         # hash each ticket with the source as key and destination as value
            flight_path[ticket.source] = ticket.destination
    # if the tickets are greater than 1 then we need to check other wise we know our flight path
    if length > 1:
        # loop through our object, grabbing the source's associated destination and adding it to our route
        for i in range(1, length):
            route[i] = flight_path[route[i-1]]

    return route
