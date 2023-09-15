import discord
from discord.ext import commands

# Konfiguration
token = ''
prefix = '!'

# Spielfeld
board = [' ' for _ in range(9)]
current_player = 'X'
players = {}

# Intents konfigurieren
intents = discord.Intents.default()
intents.message_content = True  # Aktiviert das Ereignis für Nachrichteninhalte

# Bot-Client erstellen
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_error(event, *args, **kwargs):
    import traceback
    error_message = traceback.format_exc()
    print(f'Fehler im Event {event}: {error_message}')

@bot.event
async def on_ready():
    print(f'Bot ist eingeloggt als {bot.user.name}')

@bot.command(name='neu')
async def new_game(ctx):
    global board, current_player, players
    board = [' ' for _ in range(9)]
    current_player = 'X'
    players = {}
    await ctx.send('Neues Tic-Tac-Toe-Spiel gestartet!\n' + draw_board())
    await ctx.send('Spieler X, gib `!beitreten` ein, um dem Spiel beizutreten!')

@bot.command(name='zug')
async def make_move(ctx, position: int):
    global board, current_player

    if ctx.author.id in players and current_player == players[ctx.author.id]:
        if 1 <= position <= 9 and board[position - 1] == ' ':
            board[position - 1] = current_player

            if check_winner():
                await ctx.send(draw_board())
                await ctx.send(f'Spieler {current_player} gewinnt!')
            elif ' ' not in board:
                await ctx.send(draw_board())
                await ctx.send('Unentschieden!')
            else:
                current_player = 'O' if current_player == 'X' else 'X'
                await ctx.send(draw_board())
                await ctx.send(f'Spieler {current_player} ist am Zug.')
        else:
            await ctx.send('Ungültiger Zug! Bitte wähle eine freie Position von 1 bis 9.')
    else:
        await ctx.send('Du bist nicht am Zug!')

@bot.command(name='beitreten')
async def join_game(ctx):
    global players

    if ctx.author.id not in players:
        players[ctx.author.id] = 'X' if len(players) % 2 == 0 else 'O'
        await ctx.send(f'Spieler {players[ctx.author.id]} ist beigetreten!')
    else:
        await ctx.send('Du bist bereits im Spiel!')

def draw_board():
    rows = [board[i:i + 3] for i in range(0, len(board), 3)]
    board_str = '\n'.join([' | '.join(row) for row in rows])
    return f'```\n{board_str}```'

def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False

@bot.event
async def on_message(message):
    # Prüfe, ob die Nachricht im gewünschten Kanal ist (nach Channel-ID überprüft)
    target_channel_id = '1151479089656504354'  # Ersetze DEINE_CHANNEL_ID durch die tatsächliche Channel-ID
    if message.channel.id == target_channel_id:
        if message.content.startswith('!neu'):
            await new_game(message.channel)
        elif message.content.startswith('!zug'):
            try:
                position = int(message.content.split()[1])
                await make_move(message.channel, position)
            except ValueError:
                await message.channel.send('Ungültiger Zug! Verwende `!zug [Position]`, um einen Zug zu machen.')
    await bot.process_commands(message)


bot.run(token)
