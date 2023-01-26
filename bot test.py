from rocketgram import Bot, Dispatcher, UpdatesExecutor

from rocketgram import context, commonfilters

from rocketgram import SendMessage

token = f'YOUR_BOT_TOKEN'

router = Dispatcher()

bot = Bot(token, router=router)

@router.handler

@commonfilters.command('/start')

async def start_command():

    await SendMessage(context.user.id, f'Hello there!').send()

    

@router.handler

@commonfilters.command('/help')

async def start_command():

    await SendMessage(context.user.id, f'Some userful help!').send()

    

UpdatesExecutor.run(bot)
