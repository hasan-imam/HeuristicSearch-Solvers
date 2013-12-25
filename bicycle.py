
'''
bicycle STATESPACE 
'''

from search import *
from math import *

class bicycle(StateSpace):
    StateSpace.n = 0

    # Class variables
    job_list = None
    max_time = 1140 # (7:00 pm)
    min_time = 420 # (7:00 am)
    
    def __init__(self, action, gval, location, time, pending_jobs, latest_delivery, parent = None):
        """
        Initialize a bicycle search state object. 
        self.gval === lost earning or opportunity cost (search tries to minimize this)
        self.location === current location
        self.time === current time 
        self.pending_jobs === same structure as job_list, but contains only pending jobs
        """
        #init the base class members.
        StateSpace.__init__(self, action, gval, parent)

        self.location = location
        self.time = time
        self.pending_jobs = pending_jobs
        self.latest_delivery = latest_delivery

    def successors(self) :
        """Implements the transitions of the bicycle search space.
        State transition === taking action === making a delivery"""
        States = list()
        for job in self.pending_jobs:
            # New list of pending jobs with this job removed
            pending_jobs = [tmp_job for tmp_job in self.pending_jobs if tmp_job != job]
            # Time after finishing
            time = self.time + bicycle.get_ETA(self.location, job[1]) 
            if time < bicycle.to_minutes(job[2]): # If arrive before pick-up time
                time = bicycle.to_minutes(job[2])
            time = time + bicycle.get_ETA(job[1], job[3])
            if time > bicycle.max_time:
                continue # Avoid expanding on action that exceeds latest time
            # Location after the job
            location = job[3]
            
            # gval += lost earning: best payment - payment for doing it now 
            gval = self.gval
            payment = 0
            if job.__len__() >= 5:
                # Find the payment we get for delivering at 'time'
                payment = bicycle.earning(job[4:], time) 
                gval = gval + (job[4][1] - payment)
            # Now gval is either the same (if we have achieved the best
            # payment) or increased due to new lost earning
            
            # Informaiton on this delivery 
            # delivery = [job_name, initial_location, start_time, final_location, end_time, payment]
            delivery = [job[0], # job name
                        self.location, # initial location
                        bicycle.get_readable_time(self.time), # when started this job
                        location, # final location after delivery
                        bicycle.get_readable_time(time), # time after delivery
                        payment] # payment from this delivery
            # If starting from home, then don't need to start till the pick up time
            # So start time is set to the first pick up time.
            if self.parent is None:
                delivery[2] = bicycle.get_readable_time(job[2])
            
            States.append(bicycle(job[0], gval, location, time, pending_jobs, delivery, self))
        return States

    def hashable_state(self) :
        #Return a hashable data item representing the state. 
        # hash = location-time:job1.job2.job3...
        h = str(self.location) + "-" + str(self.time) + ":"
        for job in self.pending_jobs:
            h = h + job[0] + "."
        return h

    def print_state(self):
    #    so that we can trace the search during debugging.
        if self.parent:
            print "Action= \"{}\", S{}, g-value = {}, (From S{})".format(self.action, self.index, self.gval, self.parent.index)
        else:
            print "Action= \"{}\", S{}, g-value = {}, (Initial State)".format(self.action, self.index, self.gval)
    
    def get_deliveries(self):
        '''Return the sequence of deliveries made to reach self'''
        state = self
        deliveries = []
        while state is not None and state.latest_delivery is not None:
            deliveries.insert(0, state.latest_delivery)
            state = state.parent
        return deliveries

    @staticmethod
    def get_ETA(source, dest):
        '''Return the time it takes to go from source to dest'''
        if source != 'home':
            eta = bicycle.routes[bicycle.location_names.index(source)][bicycle.location_names.index(dest)]
            assert eta is not None
        else: 
            eta = 0 # Takes 0 time to go from home to any location
        return eta
        
    @staticmethod
    def to_minutes(time):
        '''Convert time of format hh.mm to minutes.
        Due to this format of input, times like 08.30 effectively
        becomes 8.3 (float). This funciton takes care of that.'''
        if isinstance(time, int):
            return time
        else: 
            tok = str(time).split('.')
            if tok[1].__len__() == 1:
                tok[1] = tok[1] + '0'
            return int(tok[0]) * 60 + int(tok[1])
        
    @staticmethod
    def get_readable_time(minutes):
        '''Convert minutes to time of format hh.mm and return as string'''
        return str(int(minutes/60)) + '.' + str(int(round((minutes/60.0-minutes/60)*60)))
    
    @staticmethod
    def earning(payments, time):
        '''Given a list of <time, payment> and delivery time, 
        returns the first achieveable payment or 0 if none achieveable.'''
        for payment in payments:
            if time <= payment[0]:
                return payment[1]
        return 0
        
def h0(state):
    '''Null Heuristc'''
    return 0
        
def h1(state):
    '''Logisitics Heuristic 1: optimistic approximation of lost earning,
    given the current time and list of pending jobs. Heuristic assumes that 
    we can get the max payment for each job after excluding the payments that 
    has been already missed. Then count the lost earning from that. 
    '''
    h = 0
    for job in state.pending_jobs:
        h = h + job[4][1] - bicycle.earning(job[4:], state.time)
    return h

#################################################################
#   Functions which will define an interface to the
#   search space routines and allow us to automatically test the
#   implementation.
#################################################################

def make_start_state(map, job_list):
    # map:  is a list of two lists 
    #
    # [[location-names], [location-travel-time-pairs]]
    #    location-names
    #          is a list of strings specifying
    #          the locations for the deliveries. Each location has a unique name.
    #    location-travel-time-pairs
    #          a list of location-travel-time-pair-items 
    #        each location-travel-time-pair-item is
    #           a list of three elements [location1, location2, traveltime]
    #           where location1 and location2 are members of location-names
    #           and travel time is a positive integer specifying the time 
    #           it takes to go from location1 to location2 in minutes.
    #           a. The travel time from location2 to location1 is the same
    #              as the travel time from location1 to location2
    #           b. The travel time from a location back to itself is zero
    #    The location-travel-time-pairs along with rules (a) and (b) must
    #    determine the travel time between every pair of locations in location-names
    #
    #  Example: 
    #  map = [
    #         ['locA', 'locB', 'locC', 'locD'],
    #         [['locA', 'locB', 15], ['locA', 'locC', 25], ['locA', 'locD', 10], 
    #          ['locB', 'locC', 10], ['locB', 'locD', 13], ['locC', 'locD', 20]]
    #        ]
    # 
    # job_list: a list of jobs
    #    each job is a list of 5 or more items
    #    1. a string that is the job name. Each job has a unique name.
    #    2. Pickup location, a location from location-names
    #    3. pickup time. A number in the format hh.mm (h=hour, m=minute)
    #    4. Dropoff location, a location from location-names
    #    5. A time-payoff pair
    #    6,7,..: the job-list can contain an arbitrary number of time-payoff pairs.
    #
    #       time-payoff pair:
    #       a list of two items, [time, payoff]
    #       time is a number in the format hh.mm
    #       payoff is an integer specifying the number of dollars paid. 
    #    You may assume that each subsequent time-payoff pair in the job-list has
    #      a higher time and a lower payoff. 
    # 
    # Example:
    # job_list = [['Job1', 'locA', 8.00, 'locC', [8.30, 25], [9.30, 20], [10.00, 10], [11.00, 5]],
    #             ['Job2', 'locB', 10.00, 'locC', [10.30, 25], [12.00, 5]],
    #             ['Job3', 'locC', 9.00, 'locD', [9.05, 50], [9.30, 25], [10.00, 5]]
    #             ]
    '''Input a map list and a job_list. Return a bicycle StateSpace object
       with action "START", gval = 0, and initial location "home" that represents the 
       starting configuration for the scheduling problem specified'''
    
    # Assign argumnets to class variables.
    # Assigned once since there will be only one root START state
    # This funciton must be called once at the beginning for the state variables to work
    
    # Full list of all jobs
    # Iterate over to convert time values to minutes
    # TODO: remove payments that are not possible to achieve 
    bicycle.job_list = list()
    for job in job_list:
        tmp = list(job)
        tmp[4:] = [[bicycle.to_minutes(payment[0]), payment[1]] for payment in job[4:]]
        tmp[2] = bicycle.to_minutes(tmp[2])
        bicycle.job_list.append(tmp)
    # List of location names
    bicycle.location_names = map[0]
    # 2D array of point-to-point travelling time
    bicycle.routes = [None] * bicycle.location_names.__len__()
    for i in range(0, bicycle.location_names.__len__()):
        bicycle.routes[i] = [None] * bicycle.location_names.__len__()
        bicycle.routes[i][i] = 0 # cost to itself === 0
    # Populate the array with times
    for i, route in enumerate(map[1]):        
        # These costs are symmetric
        bicycle.routes[bicycle.location_names.index(route[0])][bicycle.location_names.index(route[1])] = route[2]
        bicycle.routes[bicycle.location_names.index(route[1])][bicycle.location_names.index(route[0])] = route[2]
    
#     # Print status.
#     print 'Initialized bicycle problem. Parameters:'
#     print 'job list: ', bicycle.job_list
#     print 'locations: ', bicycle.location_names
#     print 'routes: ', bicycle.routes
#     print 'Returning START state'
    
    # Return the starting state
    return bicycle('START', 0, 'home', bicycle.min_time, bicycle.job_list, None, None)

def bicycle_goal_fn(state):
    # Goal is met when pending job list is empty before the time has exceeded.
    if not state.pending_jobs and (state.time <= bicycle.max_time):
        return True
    return False

def solve(bicycle_start_state):
    '''Compute a delivery schedule given an initial bicycle search state that has been
       computed from make_start_state (above). Output the computed sequence of deliveries'''
    # This function invokes the search routines to find a solution to the delivery
    # scheduling problem that executes all of the delivery jobs specified by the
    # bicycle_start_state
    # It returns a list of deliveries
    # deliveries = [delivery1, delivery2, ... ]
    # 
    # each delivery is a list
    # [job_name, initial_location, start_time, final_location, end_time, payment]
    #  job_name: the job name from job_list
    #  initial_location: your location when you started working on the job
    #  start_time: the time when you started riding from initial_location to 
    #              the job's pickup location
    #  final_location: the delivery location of the job
    #  end_time: the time when you delivered the job's package 
    #  payment: the money earned for this job
    #
    # For example, the returned list of deliveries
    # for the schedule given in the assignment specification would be
    # [ ['Job1', 'home', 8.00, 'locC', 8.25, 25]
    #   ['Job3', 'locC', 8.25, 'locD', 9.20, 25]
    #   ['Job2', 'locD', 9.20, 'locC', 10:10, 25]
    # ]
    
    engine = SearchEngine('astar', 'full')
    goal_node = engine.search(bicycle_start_state, bicycle_goal_fn, h1)
    if goal_node is False:
        print '\nNo Solution found: cannot finish all jobs before 19.01'
        return []
    else:
        deliveries = goal_node.get_deliveries()
        return deliveries
