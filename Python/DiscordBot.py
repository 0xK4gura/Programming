#   Discord Bot untuk suggest makanan biasa-biasa
#   Jangan lupa follow GitHub saya di https://github.com/0xK4gura
#   Terima kasih kerana mencuba bot dan program mudah ini
#   Sengaja saya buat untuk improve skill Python
#   Jika ada sebarang masalah boleh hubungi saya
#

import random
import discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='$')   # Config untuk set prefix
tok = 'LetakBotTokenDiSini'  # Dapatkan 'Bot Token' dan bubuh di sini untuk client.run()

@client.event # nak check bot online ke tak
async def on_ready():
    print('Selamat Datang {0.user}'.format(client))

@client.command(brief='Echoes back what user says.') 
async def echo(ctx, *, user_message): # 'echo' adalah command yang diberikan kepada discord nanti; contoh di sini; $echo | ' $echo helo helo ' akan buat bot send mesej balik sebagai "User says helo helo"
    await ctx.send('User says ' + user_message)

@client.command(brief='Await input from user.')
async def makanan(ctx):

    #   Jangan lupa untuk check out https://github.com/0xK4gura
    #   If ada problem boleh try create issue or tanya direct dekat discord juga di 'k4gura #1611'
    #   Or boleh e-mel dekat kaguramaru11@gmail.com
    #   Hasil kompilasi biasa biasa untuk kegunaan harian 
    # 

    Sarapan = ["Nasi Goreng Telur", "Roti Pita Ayam", "Sandwich Ikan", "Mongolian Foldover", "Roti Telur", "Roti Sapu Kaya", "Nasi Lemak", "Nasi Kerabu", "Kuey Teow Goreng", "Mee Goreng"] 
    Lunch = ["Spaghetti Ayam", "Nasi Berlauk", "Nasi Goreng USA", "Makaroni Cheese", "Keuy Teow Kungfu", "Meatball Ikea", "Mee Bandung", "Nasi Kangkang 👀", "Nasi Kukus"]

    senarai = []    #   Nak simpan dalam list for anything
    noList = 3      #   Nak tukar berapa kali dia send mesej

    SarapanL = len(Sarapan)     # Nombor item yang ada dalam Sarapan
    RandomSarapan = random.randint(0,int(SarapanL)) # Nombor rawak untuk panggil array, daripada array tersebut boleh panggil String Makanan

    LunchL = len(Lunch)
    RandomLunch = random.randint(0,int(LunchL))
    
    await ctx.send("> Halo Awak Mesti Lapar Kan!! 😋🧆🥙 \n\n> Total Menu Sarapan: {}\n> Total Menu Lunch: {}\n\n> 1 : Sarapan\n> 2 : Lunch\n\n> 0 : Exit\n\n> Makan Untuk Apa Hari Ni: \n> (Pilih Nombor) \n\n> (Timeout: 30s)".format(SarapanL, LunchL))

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content in ["1", "2", "3", "0"] # Check mesej betul ke tak mengikut siapa yang hantar so tak ada clash antara pengguna yang lain.
    
    try:
        msg = await client.wait_for("Message", check=check, timeout=30) # Masa diberikan untuk hantar mesej pilihan 1,2,3,0
        if msg.content == "1":
            await ctx.send("✅ Anda Pilih Sarapan! 🥣")
            for i in range(noList):
                SarapanL = len(Sarapan)
                RandomSarapan = random.randint(0,int(SarapanL-1))
                x = Sarapan[int(RandomSarapan)]
                await ctx.send("> " + x)
            await ctx.send("Selamat Menjamu Selera! 😋😋")
        elif msg.content == "2":
            await ctx.send("✅ Anda Pilih Lunch 🕛")
            for i in range(noList):
                LunchL = len(Lunch)
                RandomLunch = random.randint(0,int(LunchL-1))
                x = Lunch[int(RandomLunch)]
                await ctx.send("> " + x)
            await ctx.send("Selamat Menjamu Selera! 😋😋")
        else:
            await ctx.send("❗❗ Sila Pilih Nombor Berkenaan 😠")
    except asyncio.TimeoutError:
        await ctx.send("❗❗ Tamat! Sila Cuba Lagi 😤")


client.run(tok) # Sila pastikan command ni run di bawah sekali

#   Follow saya di GitHub https://github.com/0xK4gura
#   Sila hubungi jika ada masalah atau tidak faham
#   Terima kasih sekali lagi kerana mencuba
#