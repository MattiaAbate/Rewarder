"""
Rewarder library
"""

from random import choice

def create_research():
    research = f"{choice(adjectives)} {choice(subjects)} {choice(places)}"
    url = f"https://www.bing.com/search?q={research.replace(' ', '+')}"
    return research, url

adjectives = [
    "Broken",
    "Giant",
    "Strange",
    "Flying",
    "Blue",
    "Fiery",
    "Magical",
    "Space",
    "Destroyer",
    "Red",
    "Paul-like",
    "Invisible",
    "Mysterious",
    "Ancient",
    "Enchanted",
    "Powerful",
    "New",
    "Old",
    "Futuristic",
    "Modern",
    "Colorful",
    "Dark",
    "Light",
    "Cursed",
    "Goofy Ahh",
    "Pixelated",
    "Digital",
    "Delicious",
    "Spicy",
    "Sweet",
    "unbreakable"
]

subjects = [
    "repeater",
    "toaster",
    "antenna",
    "refrigerator",
    "scooter",
    "trampoline",
    "telescope",
    "hat",
    "piano",
    "pillow",
    "easel",
    "balloon",
    "basket",
    "coat",
    "tomato",
    "paul",
    "golden apple",
    "sword",
    "bread",
    "chair",
    "hamburger",
    "pizza",
    "robot",
    "computer",
    "phone",
    "tablet",
    "boat",
    "controller",
    "biscuit",
    "netherite pickaxe",
    "diamond",
    "gorilla"
]

places = [
    "MediaWorld",
    "on the roof",
    "in the parking lot",
    "at the disco",
    "at IKEA",
    "on Mars",
    "on a desert island",
    "at the bar",
    "on Rise of Kingdoms",
    "on Minecraft",
    "on Roblox",
    "in a parallel world",
    "in an alternate universe",
    "in a dystopian future",
    "in the distant past",
    "on Temu",
    "in the mountains",
    "in the forest",
    "in the world",
    "in the sea",
    "in a cave",
    "in a castle",
    "at the restaurant",
    "at the cinema"
]