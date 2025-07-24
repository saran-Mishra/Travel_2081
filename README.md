# Travel_2081

The goal was to build a SQL procedure which is able to receive details about a new customer and return a stack-ranked list of travel agents (best to worst) who would be the best match for them.

# To run:

(1) Please first initiate the database of sample data by running: init_db.py 
(2) Please run the main.py to see an example run. 
(3) To make changes to the input (i.e. for real-time dynamics) please use the input.json file. 
(4) To see the underlying SQL algorithm please see matched_assignments.sql

# Explanation
My 2 part schema flow is simple but effective:

(1) New Customer Input with the following categories of data: Customer Name, Communication Method, Lead Source, Destination, Launch Location.

(2) The assignment_history + booking tables (pk:AssignmentID) join with the space_travel_agents table (pk:AgendID) to form a CTE taking in the new customers categorical data.

(3) I group by agents and order by the already existing average ratings. I assume that the ratings are done in a different process.

(4) Finally, in descending order, we get the best agents for this particular type of customer

Conclusion: While this may be a simple matching tool, there are obviously ways to expand upon this using predictive methods (clustering, classification, etc) that pair customers with better agent-matches.
