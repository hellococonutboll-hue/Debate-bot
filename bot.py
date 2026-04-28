import discord
from discord import app_commands
import random
import os
from typing import Optional

DEBATE_TOPICS = {
    "food": [
        "Pineapple belongs on pizza",
        "Fast food should be taxed like cigarettes",
        "Vegetarianism should be encouraged globally",
        "Breakfast is the most important meal of the day",
        "Veganism is the only ethical diet",
        "Coffee is better than tea",
        "Spicy food is better than mild food",
        "Cooking at home is always better than eating out",
        "Energy drinks should be banned for people under 18",
        "Alcohol should be treated like other drugs",
        "Dessert should be eaten before dinner",
        "Cereal is a valid dinner",
        "Soda should be banned in schools",
        "Ketchup belongs on eggs",
        "Peanut butter and jelly is overrated",
        "Tap water tastes better than bottled water",
        "Breakfast foods are acceptable for dinner",
        "Vegans are more ethical than meat eaters",
        "Eating insects will become mainstream within 20 years",
        "Fast food chains do more harm than good to communities",
        "Chocolate ice cream is better than vanilla",
        "Cooking is an essential life skill everyone must learn",
        "Ordering takeaway is wasteful",
        "A hot dog is a sandwich",
        "Butter makes everything taste better",
    ],
    "tech": [
        "Social media does more harm than good",
        "Artificial intelligence will destroy more jobs than it creates",
        "Video games cause violence",
        "Technology is making us less social",
        "Everyone should learn to code",
        "The internet has made the world worse",
        "Robots will replace most human jobs within 50 years",
        "Smartphones have ruined childhood",
        "Self-driving cars should replace human drivers",
        "Cryptocurrency is the future of money",
        "Screen time limits should be enforced by law for children",
        "Online privacy is more important than national security",
        "Emojis are ruining written communication",
        "Social media influencers are a bad influence on society",
        "TikTok should be banned",
        "AI-generated art is not real art",
        "Video games are a valid art form",
        "The metaverse will change how we live",
        "Smartphones should be banned in schools",
        "Social media algorithms are dangerous",
        "Electric vehicles are overhyped",
        "Space tourism is a waste of resources",
        "Online anonymity does more harm than good",
        "Automation will create more jobs than it destroys",
        "Big tech companies should be broken up",
        "The 40-hour work week is outdated thanks to technology",
        "Deepfakes are a serious threat to society",
        "Wearable tech will replace smartphones",
    ],
    "education": [
        "Homework should be abolished",
        "College education is overrated",
        "Standardized testing should be eliminated",
        "Grading systems in schools should be eliminated",
        "Physical education should be mandatory in schools",
        "Gap years are a waste of time",
        "Private schools should be banned",
        "Student loan debt should be forgiven",
        "School uniforms are beneficial",
        "Arts and music should be mandatory in schools",
        "Teachers are underpaid",
        "Learning a second language should be required",
        "Financial literacy should be taught in every school",
        "Online learning is just as good as in-person learning",
        "Children are too coddled in modern schools",
        "School start times should be pushed back",
        "Phones should be completely banned during school hours",
        "Students should be allowed to grade their teachers",
        "The school year is too long",
        "History education is biased",
        "Mental health classes should be mandatory",
        "Spelling and grammar still matter in the age of autocorrect",
        "Sports scholarships are unfair",
        "Every student deserves a free university education",
    ],
    "society": [
        "The death penalty should be abolished",
        "Celebrities have too much political influence",
        "Universal basic income should be implemented",
        "The voting age should be lowered to 16",
        "Cancel culture has gone too far",
        "Democracy is the best form of government",
        "Junk food ads should be banned",
        "Violent video games should be banned for minors",
        "Animals should have the same rights as humans",
        "Zoos should be banned",
        "Drug use should be decriminalized",
        "Guns should be banned for civilians",
        "The rich should pay significantly higher taxes",
        "Immigration has a positive impact on society",
        "Affirmative action does more harm than good",
        "Social welfare programs create dependency",
        "The minimum wage should be a living wage",
        "Prisons should focus on rehabilitation, not punishment",
        "Trophy participation is harmful for children",
        "Beauty standards are more harmful than ever",
        "Wealth inequality is the biggest threat to society",
        "The media is biased",
        "Political parties do more harm than good",
        "Jury duty should be optional",
        "Influencers should be regulated like advertisers",
        "Working from home has hurt society",
        "Marriage is an outdated institution",
        "The 4-day work week should be the standard",
        "Dress codes are a form of oppression",
        "Tattoos are still stigmatized unfairly",
    ],
    "environment": [
        "Climate change is the biggest threat facing humanity",
        "Nuclear energy is the best solution to climate change",
        "Space exploration is worth the cost",
        "Zoos do more harm than good to wildlife conservation",
        "Hunting should be completely banned",
        "Single-use plastics should be banned worldwide",
        "Flying should be taxed more heavily due to emissions",
        "Electric cars will save the planet",
        "Humans are responsible for the extinction of many species",
        "Eating less meat is the single best thing for the environment",
        "Geoengineering is too risky to attempt",
        "Individual actions cannot meaningfully fight climate change",
        "Corporations are more responsible for pollution than individuals",
        "Fast fashion is destroying the planet",
        "We should prioritize saving species over human development",
        "National parks should be expanded globally",
        "Carbon taxes are the best way to fight climate change",
        "We have already passed the point of no return on climate",
    ],
    "philosophy": [
        "Humans are naturally good",
        "Money can buy happiness",
        "Luck matters more than skill in success",
        "Aliens almost certainly exist",
        "Free will is an illusion",
        "Life on Earth is a simulation",
        "Morality is subjective",
        "Suffering makes us stronger",
        "Happiness should be the main goal of life",
        "The ends justify the means",
        "A life without risk is not worth living",
        "True altruism does not exist",
        "Ignorance is bliss",
        "You can be both rich and ethical",
        "Humans are inherently selfish",
        "Justice and revenge are the same thing",
        "Dreams reveal something meaningful about us",
        "Consciousness is what makes us human",
        "Death gives life its meaning",
        "Living in the present is more important than planning for the future",
    ],
    "popculture": [
        "Cats are better pets than dogs",
        "Books are better than movies",
        "Morning people are more productive than night owls",
        "Winter is better than summer",
        "Print books are superior to e-books",
        "Remote work is better than working in an office",
        "Sports stars are paid too much",
        "Reality TV is harmful to society",
        "Hip-hop is the most influential music genre",
        "Marvel is better than DC",
        "The movie is always better than the book",
        "Online friendships are just as valid as in-person ones",
        "Introverts make better leaders than extroverts",
        "Streaming services have killed the cinema experience",
        "Sequels are never as good as the original",
        "Celebrity culture does more harm than good",
        "Sports are overrated",
        "Stand-up comedy is the highest form of comedy",
        "Anime is better than Western cartoons",
        "Video game movies are always bad",
        "The 90s was the best decade for music",
        "Social media fame is not real fame",
        "True crime content is harmful",
        "Award shows are pointless",
        "Concert tickets are way too expensive",
        "Reboots and remakes are lazy filmmaking",
        "Going to the gym is overrated",
        "Being an early riser is overrated",
    ],
}

ALL_TOPICS = [topic for topics in DEBATE_TOPICS.values() for topic in topics]

CATEGORY_LABELS = {
    "food": "🍕 Food & Lifestyle",
    "tech": "💻 Technology",
    "education": "📚 Education",
    "society": "🏛️ Society & Politics",
    "environment": "🌍 Environment",
    "philosophy": "🤔 Philosophy",
    "popculture": "🎬 Pop Culture",
}

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("Debate bot is ready!")


@tree.command(name="debate", description="Get a debate topic — pick a category, call someone out, and choose your side!")
@app_commands.describe(
    opponent="The person you want to call out for a debate",
    category="Pick a topic category (leave blank for fully random)",
    your_side="Choose your own side — leave blank to have it randomly assigned"
)
@app_commands.choices(
    category=[
        app_commands.Choice(name="🍕 Food & Lifestyle", value="food"),
        app_commands.Choice(name="💻 Technology", value="tech"),
        app_commands.Choice(name="📚 Education", value="education"),
        app_commands.Choice(name="🏛️ Society & Politics", value="society"),
        app_commands.Choice(name="🌍 Environment", value="environment"),
        app_commands.Choice(name="🤔 Philosophy", value="philosophy"),
        app_commands.Choice(name="🎬 Pop Culture", value="popculture"),
    ],
    your_side=[
        app_commands.Choice(name="✅ For", value="for"),
        app_commands.Choice(name="❌ Against", value="against"),
    ]
)
async def debate(
    interaction: discord.Interaction,
    opponent: Optional[discord.Member] = None,
    category: Optional[str] = None,
    your_side: Optional[str] = None
):
    if category:
        topic = random.choice(DEBATE_TOPICS[category])
        category_label = CATEGORY_LABELS[category]
    else:
        topic = random.choice(ALL_TOPICS)
        category_label = None

    if opponent:
        if your_side == "for":
            for_side, against_side = interaction.user, opponent
            side_note = "You called it — sides locked in!"
        elif your_side == "against":
            for_side, against_side = opponent, interaction.user
            side_note = "You called it — sides locked in!"
        else:
            members = [interaction.user, opponent]
            random.shuffle(members)
            for_side, against_side = members[0], members[1]
            side_note = "Sides randomly assigned. No switching!"

        desc = (
            f"**{interaction.user.mention} has called out {opponent.mention} for a debate!**\n\n"
            f"🗣️ Topic: **{topic}**\n\n"
            f"✅ **FOR** — {for_side.mention}\n"
            f"❌ **AGAINST** — {against_side.mention}"
        )
        if category_label:
            desc += f"\n\n📂 Category: {category_label}"

        embed = discord.Embed(title="⚔️ Debate Callout!", description=desc, color=discord.Color.orange())
        embed.set_footer(text=side_note)
        await interaction.response.send_message(content=f"{opponent.mention}", embed=embed)
    else:
        desc = f"**{topic}**"
        if your_side:
            side_label = "✅ FOR" if your_side == "for" else "❌ AGAINST"
            desc += f"\n\n{side_label} — {interaction.user.mention}"
        if category_label:
            desc += f"\n\n📂 Category: {category_label}"

        embed = discord.Embed(title="🗣️ Debate Topic", description=desc, color=discord.Color.red())
        embed.set_footer(text="Use /debate @someone to call someone out!")
        await interaction.response.send_message(embed=embed)


@tree.command(name="debate_custom", description="Start a debate with your own topic — optionally call someone out!")
@app_commands.describe(
    topic="The debate topic you want to use",
    opponent="The person you want to call out",
    your_side="Choose your side (optional)"
)
@app_commands.choices(your_side=[
    app_commands.Choice(name="✅ For", value="for"),
    app_commands.Choice(name="❌ Against", value="against"),
])
async def debate_custom(
    interaction: discord.Interaction,
    topic: str,
    opponent: Optional[discord.Member] = None,
    your_side: Optional[str] = None
):
    topic = topic.strip()
    if len(topic) < 5:
        await interaction.response.send_message("That topic is too short!", ephemeral=True)
        return
    if len(topic) > 200:
        await interaction.response.send_message("That topic is too long! Keep it under 200 characters.", ephemeral=True)
        return

    if opponent:
        if your_side == "for":
            for_side, against_side = interaction.user, opponent
            side_note = "You called it — sides locked in!"
        elif your_side == "against":
            for_side, against_side = opponent, interaction.user
            side_note = "You called it — sides locked in!"
        else:
            members = [interaction.user, opponent]
            random.shuffle(members)
            for_side, against_side = members[0], members[1]
            side_note = "Sides randomly assigned. No switching!"

        desc = (
            f"**{interaction.user.mention} has called out {opponent.mention} for a debate!**\n\n"
            f"🗣️ Topic: **{topic}**\n\n"
            f"✅ **FOR** — {for_side.mention}\n"
            f"❌ **AGAINST** — {against_side.mention}"
        )
        embed = discord.Embed(title="⚔️ Custom Debate Callout!", description=desc, color=discord.Color.orange())
        embed.set_footer(text=side_note)
        await interaction.response.send_message(content=f"{opponent.mention}", embed=embed)
    else:
        desc = f"**{topic}**"
        if your_side:
            side_label = "✅ FOR" if your_side == "for" else "❌ AGAINST"
            desc += f"\n\n{side_label} — {interaction.user.mention}"
        embed = discord.Embed(title="🗣️ Custom Debate Topic", description=desc, color=discord.Color.red())
        embed.set_footer(text="Use /debate_custom @someone to call someone out!")
        await interaction.response.send_message(embed=embed)


@tree.command(name="debate_list", description="See all available categories and topic counts")
async def debate_list(interaction: discord.Interaction):
    lines = "\n".join(
        f"{CATEGORY_LABELS[cat]} — **{len(topics)} topics**"
        for cat, topics in DEBATE_TOPICS.items()
    )
    embed = discord.Embed(
        title="📋 Debate Categories",
        description=f"{lines}\n\n**Total: {len(ALL_TOPICS)} topics**\n\nUse `/debate` for a random topic, `/debate_custom` to use your own!",
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed)


token = os.environ.get("DISCORD_BOT_TOKEN")
if not token:
    raise ValueError("DISCORD_BOT_TOKEN environment variable is not set.")

client.run(token)
