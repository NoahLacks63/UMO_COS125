# File: simulation.py
# Author: Noah Lacorazza
# Date: 11/22/25
# Section: 1004
# E-mail: noah.lacorazza@maine.edu
# Description:
#   Simulates population dynamics in different scenarios
# Collaboration:
# N/A

import random

# File path constants
CSV_FILE = "weather.csv"
LOG_FILE = "log.txt"
START_DATA_FILE = "start_data.txt"
STATE_FILE = "state.txt"

# Simulation constants
LOW_RAIN = .1
HIGH_RAIN = .9
HIGH_TEMP = .9

BIRTH_RATE = 0.01
DEATH_RATE = 0.005

FARM = "Farm"
CITY = "City"

# Main function to start or resume simulation
def main():
    if input("Would you like to resume a simulation? (y/n): ") == "y":
        resume()
    else:
        new_sim()

# Starts a new simulation
def new_sim():
    weeks = len(open(CSV_FILE).readlines()) - 1

    iterations = min(int(input("Enter the number of iterations you would like to run: ")), weeks)

    init_state = initialize_data()

    simulation_state = {
        "scenario" : input("Enter scenario type (Farm or City): "),
        "week" : 1,
        "weeks" : iterations,
        "people" : init_state["people"],
        "animals" : init_state["animals"],
        "pests" : init_state["pests"],
        "weather" : get_weather(1)
    }

    with open(STATE_FILE, "w") as f:
        f.write(f"{simulation_state["scenario"]}\n")
        f.write(f"{simulation_state["week"]}\n")
        f.write(f"{simulation_state["weeks"]}\n")
        f.write(f"{simulation_state["people"]}\n")
        f.write(f"{simulation_state["animals"]}\n")
        f.write(f"{simulation_state["pests"]}\n")
        f.write(f"{simulation_state["weather"]}\n")
    
    record_data(simulation_state)

    continue_simulation(simulation_state)

# Resumes a previously saved simulation
def resume():
    state = {"weather" : {}}
    with open(STATE_FILE) as f:
        for line in f:
            key, value = line.strip().split(": ")
            if key == "rain" or key == "temp":
                state["weather"][key] = float(value)
            elif key == "scenario":
                state[key] = value
            else:
                state[key] = int(value)
    
    continue_simulation(state)
    


# Continues the simulation from the last turn
#
# Args:
#   state (dict): current state of the simulation
def continue_simulation(state):
    simulation_state = state
    print(f"Week {simulation_state["week"]} of {simulation_state["weeks"]}")

    for key, value in simulation_state.items():
        if key != "weather":
            print(f"{key}: {value}")
        else:
            print(f"rain: {value["rain"]}\ntemp: {value["temp"]}")

    if simulation_state["week"] >= simulation_state["weeks"]:
        print("Simulation complete.")
        return
    else:
        simulation_state = simulation(simulation_state)
        simulation_state["week"] = int(simulation_state["week"]) + 1
        
        record_data(simulation_state)

        save_state(simulation_state)

        if input("Continue simulation? (y/n): ") == "y":
            continue_simulation(simulation_state)
        

# Simulates one week of the simulation
#
# Args:
#   state (dict): current state of the simulation
#
# Returns:
#   simulation_state (dict): updated state after simulation
def simulation(state):
    weather = get_weather(state["week"])
    animals_pop = state["animals"]
    pests_pop = state["pests"]

    if weather["rain"] < LOW_RAIN:
        animals_pop = int(state["animals"] * .9)
    elif weather["rain"] > HIGH_RAIN and weather["temp"] > HIGH_TEMP:
        pests_pop = int(state["pests"] * random.randint(110, 120) / 100)

    simulation_state = {
        "scenario" : state["scenario"],
        "week" : state["week"],
        "weeks" : state["weeks"],
        "people" : state["people"],
        "animals" : animals_pop,
        "pests" : pests_pop,
        "weather" : weather
    }

    simulate_weather(simulation_state)

    return simulation_state

# Simulates pest population changes based on weather
#
# Args:
#   state (dict): current state of the simulation
def simulate_weather(state):
    simulation_state = state

    if simulation_state["pests"] > (simulation_state["animals"] + simulation_state["people"]) * 1.3:
        simulation_state["people"] = int(simulation_state["people"] * .95)
        simulation_state["animals"] = int(simulation_state["animals"] * .95)

    demographic_transition(simulation_state)

# Simulates demographic transition based on birth and death rates
#
# Args:
#   state (dict): current state of the simulation
#
# Returns:   
#   simulation_state (dict): updated state after demographic changes
def demographic_transition(state):
    population_change = 1 + BIRTH_RATE - DEATH_RATE

    people_pop = int(state["people"] * population_change)
    animals_pop = int(state["animals"] * population_change)
    pests_pop = int(state["pests"] * population_change)

    simulation_state = {
        "scenario" : state["scenario"],
        "week" : state["week"],
        "weeks" : state["weeks"],
        "people" : people_pop,
        "animals" : animals_pop,
        "pests" : pests_pop,
        "weather" : state["weather"]
    }

    return simulation_state

# Initializes simulation data
# 
# Returns:
#   init_state (dict): dictionary containing initial populations
def initialize_data():
    with open(START_DATA_FILE) as f:
        lines = f.readlines()
        init_state = {
            "people" : int(lines[1]),
            "animals" : int(lines[2]),
            "pests" : int(lines[3])
        }

    return init_state

# Retrieves weather data for the current week
#
# Args:
#   iteration (int): current week of the simulation
#
# Returns:
#   weather (dict): dictionary containing rain and temperature data
def get_weather(iteration):
    with open(CSV_FILE) as f:
        lines = f.readlines()
        line = lines[iteration - 1].strip().split(",")
        weather = {
            "rain" : int(line[0]),
            "temp" : int(line[1])
        }
    
    return weather
    
# Records the current state of the simulation to a txt file
#
# Args:
#   simulation_state (dict): current state of the simulation
def record_data(simulation_state):
    with open(LOG_FILE, "a") as f:
        f.write(f"Scenario: {simulation_state["scenario"]}\n\tPeople: {simulation_state["people"]}\n")

        if simulation_state["scenario"] == FARM:
            f.write(f"\tLivestock: {simulation_state["animals"]}\n")
        else:
            f.write(f"\tPets: {simulation_state["animals"]}\n")
        
        f.write(f"\tPests: {simulation_state["pests"]}\n")
        f.write(f"\tRain: {simulation_state["weather"]["rain"]}")
        f.write(f"\tTemp: {simulation_state["weather"]["temp"]}\n\n")

# Saves the current state of the simulation to a txt file
#
# Args:
#   state (dict): current state of the simulation
def save_state(state):
    with open(STATE_FILE, "w") as f:
        for key, value in state.items():
            if key == "weather":
                f.write(f"rain: {value["rain"]}\ntemp: {value["temp"]}\n")
            else:
                f.write(f"{key}: {value}\n")
        
# Runs the main simulation loop
main()