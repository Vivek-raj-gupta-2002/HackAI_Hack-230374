# The city whose temperature is to be monitored
CITY: str = 'Indore'

# the alerting max temperature
MAX_TEMP: float = 20.0

# the alerting min temperature
MIN_TEMP: float = 26.0

# should be notified or not
NOTIFICATION: bool = True 

# The file name that will save all the log data or temperature data
FILENAME: str = './data.txt'#


if __name__ == '__main__':
    # running the agent
    from uagents import Bureau
    from agents.monitor import monitor

    server = Bureau()

    server.add(monitor.agent)

    server.run()

