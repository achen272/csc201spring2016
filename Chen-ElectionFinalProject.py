#Alex Chen
#CSC201
#Final Project

import csv
import os
import time

def read_csv(path):
    output = []
    for row in csv.DictReader(open(path)):
        output.append(row)
    return output

def eq(e,a):
    if e ==a:
        return True
    if type(e) == int:
        e = float(e)
    if type(a) == int:
        a = float(a)
    if type(e) != type(a):
        return False
    if type(e) == dict:
        return eq_dict(e,a)
    elif type(e) == float:
        return eq_float(e,a)
    elif type(e) == str:
        return eq_str(e,a)

def eq_dict(e,a):
    if sorted(e.keys()) != sorted(a.keys()):
        return False
    for key in e:
        if not eq(e[key], a[key]):
            return False

def eq_float(e,a):
    epsilon = 0.00001
    return abs(e - a) < epsilon

def eq_str(e,a):
    return e == a

################################################################################
# Problem 1: State edges
################################################################################

def row_to_edge(row):

    row1 = { "Dem": 5, "Rep": 90 }
    assert eq(row_to_edge(row1) == -85)

    row2 = { "Dem": 57.5, "Rep": 77.5 }
    assert eq(row_to_edge(row2) == -20)

    row3 = { "Dem": 52, "Rep": 49, "Lib": 1 }
    assert eq(row_to_edge(row3) == 3)
    return float(row["Dem"]) - float(row["Rep"])  

def state_edges(election_result_rows):

    rows1 = [{'State': 'WA', 'Dem': '1.0', 'Rep': '0.1'}]
    assert eq(state_edges(rows1) == {'WA': 0.9})

    rows2 = [{'State': 'WA', 'Dem': '1.0', 'Rep': '0.1'},
               {'State': 'CA', 'Dem': '0.2', 'Rep': '1.3'}]
    assert eq(state_edges(rows2) == {'WA': 0.9, 'CA': -1.1})
    pass


################################################################################
# Problem 2: Find the most recent poll row
################################################################################

def earlier_date(date1, date2):
    assert earlier_date("Jan 01 2012", "Jan 02 2012")
    assert earlier_date("Jan 31 2012", "Feb 1 2012")
    assert not earlier_date("Dec 31 2012", "Jan 01 2012")
    assert earlier_date("Apr 12 2012", "Jun 12 2012")

    poll_rows1 = [{"ID":1, "State":"WA", "Pollster":"A", "Date":"Jan 07 2010"},
                  {"ID":2, "State":"WA", "Pollster":"B", "Date":"Mar 21 2010"},
                  {"ID":3, "State":"WA", "Pollster":"A", "Date":"Jan 08 2010"},
                  {"ID":4, "State":"OR", "Pollster":"A", "Date":"Feb 10 2010"},
                  {"ID":5, "State":"WA", "Pollster":"B", "Date":"Feb 10 2010"},
                  {"ID":6, "State":"WA", "Pollster":"B", "Date":"Mar 22 2010"}]
    return(time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))

def most_recent_poll_row(poll_rows, pollster, state):

    assert eq(most_recent_poll_row(poll_rows1, "A", "OR") == {"ID":4, "State":"OR", "Pollster":"A", "Date":"Feb 10 2010"})
    assert eq(most_recent_poll_row(poll_rows1, "A", "WA") == {"ID":3, "State":"WA", "Pollster":"A", "Date":"Jan 08 2010"})
    assert eq(most_recent_poll_row(poll_rows1, "B", "WA") == {"ID":6, "State":"WA", "Pollster":"B", "Date":"Mar 22 2010"})
    assert eq(most_recent_poll_row(poll_rows1, "B", "OR") == None)
    assert eq(most_recent_poll_row(poll_rows1, "DoesNotExist", "DoesNotExist") == None)
    pass


################################################################################
# Problem 3: Pollster predictions
################################################################################

def unique_column_values(rows, column_name):

    assert eq(unique_column_values(poll_rows1, "ID") == { 1, 2, 3, 4, 5, 6 })
    assert eq(unique_column_values(poll_rows1, "State") == { "WA", "OR" })
    assert eq(unique_column_values(poll_rows1, "Pollster") == { "A", "B" })
    assert eq(unique_column_values(poll_rows1, "Date") == { "Jan 07 2010", "Jan 08 2010", "Feb 10 2010", "Mar 21 2010", "Mar 22 2010" })
    pass

def pollster_predictions(poll_rows):

    rows1 = [{'State': 'WA', 
                'Dem': '1.0', 
                'Rep': '0.1', 
                'Date': 'Nov 04 2008', 
                'Pollster': 'PPP'}]
    assert eq(pollster_predictions(rows1) == {'PPP': {'WA': 0.9}})

    rows2 = [
      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
      {'State': 'CA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'}]
    assert eq(pollster_predictions(rows2) == {'PPP': {'WA': 0.9, 'CA': -9.3}})

    rows3 = [
      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
      {'State': 'CA', 'Dem': '2.1', 'Rep': '3.2', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'},
      {'State': 'WA', 'Dem': '9.1', 'Rep': '7.1', 'Date': 'Nov 05 2008', 'Pollster': 'IPSOS'},
      {'State': 'CA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'IPSOS'}]
    assert eq(pollster_predictions(rows3) == {'PPP': {'WA': 0.9, 'CA': -1.1}, 
                                             'IPSOS': {'WA': 2.0, 'CA': -9.3}})
                                             
    rows4 = [
      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
      {'State': 'WA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'}]
    assert eq(pollster_predictions(rows4) == {'PPP': {'WA': 0.9}})

    rows5 = [
      {'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
      {'State': 'CA', 'Dem': '2.1', 'Rep': '3.2', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'},
      {'State': 'OR', 'Dem': '9.1', 'Rep': '7.1', 'Date': 'Nov 05 2008', 'Pollster': 'IPSOS'}]

    assert eq(pollster_predictions(rows5) == {'PPP': {'CA': -1.1, 'WA': 0.9}, 'IPSOS': {'OR': 2.0}})
    pass

            
################################################################################
# Problem 4: Pollster errors
################################################################################

def average_error(state_edges_predicted, state_edges_actual):

    state_edges_pred_1 = {'WA': 1.0, 'CA': -2.3, 'ID': -20.1}
    state_edges_act_1 = {'WA': 2.1, 'CA': -1.4, 'ID': -19.1}
    assert eq(average_error(state_edges_pred_1, state_edges_act_1) == 1.0)

    state_edges_pred_2 = {'WA': 1.0, 'CA': 2.0}
    state_edges_act_2 = {'WA': 2.0, 'CA': 1.0}
    assert eq(average_error(state_edges_pred_2, state_edges_act_2) == 1.0)

    state_edges_pred_3 = {'WA': 1.0, 'CA': 2.0}
    state_edges_act_3 = {'WA': 2.0, 'CA': 1.0, 'MA': 2.4, 'OR': -3.9}
    assert eq(average_error(state_edges_pred_3, state_edges_act_3) == 1.0)

    state_edges_pred_4 = {'WA': 1.0}
    state_edges_act_4 = {'WA': 0.0}
    assert eq(average_error(state_edges_pred_4, state_edges_act_4) == 1.0)
    pass

def pollster_errors(pollster_predictions, state_edges_actual):

    predictions = {
      'PPP': {'WA': 1.0, 'CA': -2.0, 'ID': -20.0}, 
      'ISPOP': {'WA': 2.0, 'ID': -19.0} 
      }
    actual = {'WA': 2.0, 'CA': -1.0, 'ID': -19.0, 'OR': 2.2, 'DC': 0.1}
    assert eq(pollster_errors(predictions, actual) == {'PPP': 1.0, 'ISPOP': 0.0})
    pass


################################################################################
# Problem 5: Pivot a nested dictionary
################################################################################

def pivot_nested_dict(nested_dict):

    us_wars_by_name = {
        "Revolutionary" : { "start": 1775, "end": 1783 },
        "Mexican" : { "start": 1846, "end": 1848 },
        "Civil" : { "start": 1861, "end": 1865 }
        }
    us_wars_by_start_and_end = {
        'start': {'Revolutionary': 1775, 'Civil': 1861, 'Mexican': 1846},
        'end': {'Revolutionary': 1783, 'Civil': 1865, 'Mexican': 1848}
        }
    assert eq(pivot_nested_dict(us_wars_by_name) == us_wars_by_start_and_end)

    pnd_input = { "a" : { "x": 1, "y": 2 },
                  "b" : { "x": 3, "z": 4 } }
    pnd_output = {'y': {'a': 2},
                  'x': {'a': 1, 'b': 3},
                  'z': {'b': 4} }
    assert eq(pivot_nested_dict(pnd_input) == pnd_output)
    pass


################################################################################
# Problem 6: Average the edges in a single state
################################################################################

def average_error_to_weight(error):

    assert eq(average_error_to_weight(.25) == 16.0)
    assert eq(average_error_to_weight(1) == 1.0)
    assert eq(average_error_to_weight(2) == 0.25)
    assert eq(average_error_to_weight(4) == 0.0625)
    return error ** (-2)

def pollster_to_weight(pollster, pollster_errors):

    pollster_errors = {"Gallup":4, "Rasmussen":10, "SurveyUSA":.25}
    assert eq(pollster_to_weight("Gallup", pollster_errors) == 0.0625)
    assert eq(pollster_to_weight("SurveyUSA", pollster_errors) == 16)
    assert eq(pollster_to_weight("Google", pollster_errors) == 0.04)

    if pollster not in pollster_errors:
        weight = average_error_to_weight(DEFAULT_AVERAGE_ERROR)
    else:
        weight = average_error_to_weight(pollster_errors[pollster])
    return weight


def weighted_average(items, weights):

    assert eq(weighted_average([3, 4, 5], [1, 1, 1]) == 4)
    assert eq(weighted_average([3, 4], [1, 1]) == 3.5)
    assert eq(weighted_average([2, 4, 4, 6], [1, 1, 1, 5]) == 5)
    assert eq(weighted_average([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]) == 3)
    assert eq(weighted_average([1, 2, 1], [3, 2, 5]) == 1.2)
    assert len(items) > 0
    assert len(items) == len(weights)
    pass


def average_edge(pollster_edges, pollster_errors):

    assert eq(average_edge({"p1":3, "p2":4, "p3":5}, {"p1":1, "p2":1, "p3":1}) == 4)
    assert eq(average_edge({"p1":3, "p2":4, "p3":5}, {"p1":1, "p2":1, "p3":1, "p4":2, "p5": -8}) == 4)
    assert eq(average_edge({"p1":3, "p2":4}, {"p1":1, "p2":1}) == 3.5)
    assert eq(average_edge({"p1":2, "p2":4, "p3":4, "p4":6}, {"p1":1, "p2":1, "p3":1, "p4":5}) == 3.3684210526315788)
    assert eq(average_edge({"p1":1, "p2":2, "p3":3, "p4":4, "p5":5},
                        {"p1":1, "p2":2, "p3":3, "p4":4, "p5":5}) == 1.560068324160182)
    assert eq(average_edge({"p1":3, "p2":4, "p3":5}, {"p1":5, "p2":5}) == 4)
    assert eq(average_edge({"p1":3, "p2":4, "p3":5}, {}) == 4)
    pass

    
################################################################################
# Problem 7: Predict the 2012 election
################################################################################

def predict_state_edges(pollster_predictions, pollster_errors):

    pollster_predictions = {
      'PPP': { 'WA': -11.2, 'CA': -2.0, 'ID': -1.1 },
      'IPSOS': { 'WA': -8.7, 'CA': -3.1, 'ID': 4.0 },
      'SurveyUSA': { 'WA': -9.0, 'FL': 0.5 },
      }
    pollster_errors = {'PPP': 1.2, 'IPSOS': 4.0, 'SurveyUSA':3.5, 'NonExistant':100.0}
    assert eq(predict_state_edges(pollster_predictions, pollster_errors) == {'CA':
    -2.0908256880733944, 'FL': 0.5, 'ID': -0.6788990825688075, 'WA': -10.799509886766941})
    pass
    

################################################################################
# Electoral College, Main Function, etc.
################################################################################

def electoral_college_outcome(ec_rows, state_edges):

    electoral_college = [
      {'State': 'AK', 'Name': 'Alaska', 'Electors': 2, 'Population': 710000},
      {'State': 'AL', 'Name': 'Alabama', 'Electors': 8, 'Population': 4780000},
      {'State': 'AR', 'Name': 'Arkansas', 'Electors': 4, 'Population': 2916000}
    ]
    state_edges = {'AK': -4.0, 'AL': 2.0, 'AR': 1.0}
    assert eq(electoral_college_outcome(electoral_college, state_edges) == {'Rep': 2.0, 'Dem': 12.0})
    
    state_edges = {'AK': -4.0, 'AL': 0.0, 'AR': 1.0}
    assert eq(electoral_college_outcome(electoral_college, state_edges) == {'Rep': 6.0, 'Dem': 8.0})

    ec_votes = {}           
    for row in ec_rows:
        ec_votes[row["State"]] = float(row["Electors"])

    outcome = {"Dem": 0, "Rep": 0}
    for state in state_edges:
        votes = ec_votes[state]
        if state_edges[state] > 0:
            outcome["Dem"] += votes
        elif state_edges[state] < 0:
            outcome["Rep"] += votes
        else:
            outcome["Dem"] += votes/2.0
            outcome["Rep"] += votes/2.0
    return outcome


def print_dict(dictionary):
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if type(value) == float:
            value = round(value, 8)
        print(key, value)


def main():
    edges_2008 = state_edges(read_csv("data/2008-results.csv"))
    
    polls_2008 = pollster_predictions(read_csv("data/2008-polls.csv"))
    polls_2012 = pollster_predictions(read_csv("data/2012-polls.csv"))
    
    error_2008 = pollster_errors(polls_2008, edges_2008)
    
    prediction_2012 = predict_state_edges(polls_2012, error_2008)
    
    ec_2012 = electoral_college_outcome(read_csv("data/2012-electoral-college.csv"),
                                        prediction_2012)
    
    print("Predicted 2012 election results:",print_dict(prediction_2012))
    
    print("Predicted 2012 Electoral College outcome:",print_dict(ec_2012))   

if __name__ == "__main__":
    main()
    read_csv()
    row_to_edge()
    state_edges()
    earlier_date()
    most_recent_poll_row()
    unique_column_values()
    pollster_predictions()
    average_error()
    pollster_errors()
    pivot_nested_dict()
    weighted_average()
    pollster_to_weight()
    average_error_to_weight()
    average_edge()
    predict_state_edges()
    electoral_college_outcome()
