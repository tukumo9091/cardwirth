import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("親父さんおはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            reply = f'{message.author.mention}' # 返信メッセージの作成
            ohayou = reply + " おはよう、" + message.author.name + "。"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(ohayou)

    # 「こんにちは」で始まるか調べる
    if message.content.startswith("親父さんこんにちは"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            reply = f'{message.author.mention}' # 返信メッセージの作成
            konnnitiha = " こんにちは、" + message.author.name + "。"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(konnnitiha)

    # 「こんにちは」で始まるか調べる
    if message.content.startswith("親父さんこんばんは"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            reply = f'{message.author.mention}' # 返信メッセージの作成
            konnnitiha = " こんにちは、" + message.author.name + "。"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(konnnitiha)

#張り紙紹介「依頼」
    if message.content.startswith("親父さん依頼"):
        #レスポンスされる張り紙のリストを作成
        harigami = ["街中で出来そうなお使い系の依頼はどうだ？", "どこかの街に出かけて見るのはどうだ？", "ゴブリンの洞窟に関係する依頼がオススメだぞ。", "ちょいと難易度の高そうなダンジョンに挑んでみたらどうだ。", "危険な敵に関する仕事の受け手を求めている依頼があるようだぞ。", "店で買物でもして装備を整えるのも悪くはないんじゃないか？"]
        reply = f'{message.author.mention}　' # 返信メッセージの作成
        choice = reply + message.author.name + "か。" + random.choice(harigami) #randomモジュール使用
        await message.channel.send(choice)



client.run(TOKEN)
