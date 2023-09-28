from uagents import Agent, Context
from utills import weather, getTime, notification, saveData
from main import CITY, MAX_TEMP, MIN_TEMP, NOTIFICATION, FILENAME

agent = Agent(name='monitor')

@agent.on_interval(period=300)
async def interval(ctx: Context):
    """
    get the temperature 
    check if the temperature is write or not if not the sends some thing
    and then check if the temperature lies b/w a perticular range or not if not 
    check if notifications are on or not if on then notify the user
    
    """
    # get the temperature
    ctx.logger.info(f"[{getTime.getTime()}]:  Checking....")
    temp = weather.getTemp(CITY)

    status = 'Normal'

    # check if we are getting wright data that is float value
    if type(temp) == str:
        status = 'Error'
        ctx.logger.info(f"[{getTime.getTime()}]:  Some thing is wrong with CITY name or yout Network")

    elif type(temp) == float:

        # now lets check temperature
        if temp > MAX_TEMP:# if more than MAX_TEMP
            # now check if notification is on or off

            status = 'High Temperature'

            if NOTIFICATION:
                notification.showNotification(
                    title='High Temperature Alert',
                    message=f'The temperature in {CITY} has Crossed {MAX_TEMP} temperature. The temperature is {temp}'
                )
            else:
                ctx.logger.info(f'[{getTime.getTime()}]:  Crossed high temperature {temp}')

        if temp < MIN_TEMP:
            status ='Low Temprature'
            # now check if notification is on or off
            if NOTIFICATION:

                # sending the notification
                notification.showNotification(
                    title='Low Temperature Alert',
                    message=f'The temperature in {CITY} is below {MIN_TEMP} temperature. The temperature is {temp}'
                )
            else:
                ctx.logger.info(f'[{getTime.getTime()}]:  Crossed high temperature {temp}')
        # the task completed

        # format the log message
        save_mess = f"[{getTime.getTime()}]:  City: '{CITY}' Temperature: '{temp}' Status: {status}"
        saveData.save(FILENAME, save_mess)

        ctx.logger.info(f"[{getTime.getTime()}]:  Successfull")
