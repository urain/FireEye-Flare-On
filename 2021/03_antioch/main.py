import binascii


color_tab = [0xB59395A9, 0x1BB5AB29, 0x0000000E, 0x5EFDD04B, 0x3F8468C8, 0x00000012, 0xECED85D0, 0x82D23D48, 0x00000002, 0xD8549214, 0x00472EE5, 0x0000001D, 0x2C2F024D, 0xC9A060AA, 0x0000000C, 0x018A5232, 0x0024D235, 0x0000000D, 0x72B88A33, 0x81576613, 0x00000014, 0x674404E2, 0x5169E129, 0x0000000B, 0x307A73B5, 0xE560E13E, 0x0000001C, 0x13468704, 0x2358E4A9, 0x00000015, 0x94F6471B, 0xD6341A53, 0x00000005, 0xEDA1CF75, 0xBAFA91E5, 0x00000018, 0xBBAC124D, 0xA697641D, 0x00000019, 0xF707E4C3, 0xEF185643, 0x00000007, 0xD702596F, 0x79C28915, 0x0000000A, 0x86A10848, 0x59108FDC, 0x00000001, 0xD640531C, 0xEF3DE1E8, 0x00000013, 0x7B665DB3, 0xA3A903B0, 0x00000003, 0xAB1321CC, 0xEEEDEAD7, 0x00000004, 0x4F6066D8, 0x9C8A3D07, 0x00000011, 0x256047CA, 0x4085BE9E, 0x00000009, 0x3FC91ED3, 0x379549C9, 0x00000008, 0xA424AFE4, 0xEF871347, 0x0000001B, 0x550901DA, 0x01FCEC6B, 0x00000010, 0x10A29E2D, 0xE76056AA, 0x00000016, 0x56CBC85F, 0x356F1A68, 0x0000000F, 0x80DFE3A6, 0x9D0AB536, 0x0000001E, 0xE657D4E1, 0xB4E9FD30, 0x00000017, 0x2BA1E1D4, 0xBE66D918, 0x0000001A, 0x7D33089B, 0x67C1F585]
color = ["Black ", "Night", "Charcoal", "Oil", "Dark Gray", "Black Cat", "Iridium", "Black Eel", "Black Cow", "Gray Wolf", "Vampire Gray", "Iron Gray", "Gray Dolphin", "Carbon Gray", "Ash Gray", "Cloudy Gray", "DimGray or DimGrey ", "Smokey Gray", "Alien Gray", "Sonic Silver", "Platinum Gray", "Granite", "Gray or Grey ", "Battleship Gray", "DarkGray or DarkGrey ", "Gray Cloud", "Silver ", "Pale Silver", "Gray Goose", "Platinum Silver", "LightGray or LightGrey ", "Gainsboro ", "Platinum", "Metallic Silver", "Blue Gray", "Roman Silver", "LightSlateGray or LightSlateGrey ", "SlateGray or SlateGrey ", "Rat Gray", "Slate Granite Gray", "Jet Gray", "Mist Blue", "Marble Blue", "Slate Blue Grey", "Light Purple Blue", "Azure Blue", "Blue Jay", "Dark Blue Grey", "Dark Slate", "Deep Sea Blue", "Night Blue", "MidnightBlue ", "Navy ", "Denim Dark Blue", "DarkBlue ", "Lapis Blue", "New Midnight Blue", "Earth Blue", "Cobalt Blue", "MediumBlue ", "Blueberry Blue", "Canary Blue", "Blue ", "Bright Blue", "Blue Orchid", "Sapphire Blue", "Blue Eyes", "Bright Navy Blue", "Balloon Blue", "RoyalBlue ", "Ocean Blue", "Blue Ribbon", "Blue Dress", "Neon Blue", "DodgerBlue ", "Glacial Blue Ice", "SteelBlue ", "Silk Blue", "Windows Blue", "Blue Ivy", "Blue Koi", "Columbia Blue", "Baby Blue", "CornflowerBlue ", "Sky Blue Dress", "Iceberg", "Butterfly Blue", "DeepSkyBlue ", "Midday Blue", "Crystal Blue", "Denim Blue", "Day Sky Blue", "LightSkyBlue ", "SkyBlue ", "Jeans Blue", "Blue Angel", "Pastel Blue", "Light Day Blue", "Sea Blue", "Heavenly Blue", "Robin Egg Blue", "PowderBlue ", "Coral Blue", "LightBlue ", "LightSteelBlue ", "Gulf Blue", "Pastel Light Blue", "Lavender Blue", "Lavender ", "Water", "AliceBlue ", "GhostWhite ", "Azure ", "LightCyan ", "Light Slate", "Electric Blue", "Tron Blue", "Blue Zircon", "Aqua or Cyan ", "Bright Cyan", "Celeste", "Blue Diamond", "Bright Turquoise", "Blue Lagoon", "PaleTurquoise ", "Pale Blue Lily", "Tiffany Blue", "Blue Hosta", "Cyan Opaque", "Northern Lights Blue", "Blue Green", "MediumAquaMarine ", "Magic Mint", "Aquamarine ", "Light Aquamarine", "Turquoise ", "MediumTurquoise ", "Deep Turquoise", "Jellyfish", "Blue Turquoise", "DarkTurquoise ", "Macaw Blue Green", "LightSeaGreen ", "Seafoam Green", "CadetBlue ", "Deep Sea", "DarkCyan ", "Teal ", "Medium Teal", "Deep Teal", "DarkSlateGray or DarkSlateGrey ", "Gunmetal", "Blue Moss Green", "Beetle Green", "Grayish Turquoise", "Greenish Blue", "Aquamarine Stone", "Sea Turtle Green", "Dull Sea Green", "Deep Sea Green", "SeaGreen ", "Dark Mint", "Earth Green", "Emerald", "Mint", "MediumSeaGreen ", "Camouflage Green", "Sage Green", "Hazel Green", "Venom Green", "OliveDrab ", "Olive ", "DarkOliveGreen ", "Army Green", "Fern Green", "Fall Forest Green", "Pine Green", "Medium Forest Green", "Jungle Green", "ForestGreen ", "Green ", "DarkGreen ", "Deep Emerald Green", "Dark Forest Green", "Seaweed Green", "Shamrock Green", "Green Onion", "Green Pepper", "Dark Lime Green", "Parrot Green", "Clover Green", "Dinosaur Green", "Green Snake", "Alien Green", "Green Apple", "LimeGreen ", "Pea Green", "Kelly Green", "Zombie Green", "Frog Green", "DarkSeaGreen ", "Green Peas", "Dollar Bill Green", "Iguana Green", "Acid Green", "Avocado Green", "Pistachio Green", "Salad Green", "YellowGreen ", "Pastel Green", "Hummingbird Green", "Nebula Green", "Stoplight Go Green", "Neon Green", "Jade Green", "Lime Mint Green", "SpringGreen ", "MediumSpringGreen ", "Emerald Green", "Lime ", "LawnGreen ", "Bright Green", "Chartreuse ", "Yellow Lawn Green", "Aloe Vera Green", "Dull Green Yellow", "GreenYellow ", "Chameleon Green", "Yellow Green Grosbeak", "Tea Green", "Slime Green", "Algae Green", "LightGreen ", "Dragon Green", "PaleGreen ", "Mint Green", "Green Thumb", "Organic Brown", "Light Jade", "Light Rose Green", "HoneyDew ", "MintCream ", "LemonChiffon ", "Parchment", "Cream", "LightGoldenRodYellow ", "LightYellow ", "Beige ", "Cornsilk ", "Blonde", "Champagne", "AntiqueWhite ", "PapayaWhip ", "BlanchedAlmond ", "Bisque ", "Wheat ", "Moccasin ", "Peach", "Light Orange", "PeachPuff ", "NavajoWhite ", "Golden Silk", "Vanilla", "Tan Brown", "PaleGoldenRod ", "Khaki ", "Cardboard Brown", "Harvest Gold", "Sun Yellow", "Corn Yellow", "Pastel Yellow", "Yellow ", "Canary Yellow", "Banana Yellow", "Mustard Yellow", "Golden Yellow", "Bold Yellow", "Rubber Ducky Yellow", "Gold ", "Bright Gold", "Golden Brown", "Deep Yellow", "Macaroni and Cheese", "Saffron", "Beer", "Yellow Orange or Orange Yellow", "Cantaloupe", "Orange ", "Brown Sand", "SandyBrown ", "Brown Sugar", "Camel Brown", "Deer Brown", "BurlyWood ", "Tan ", "Light French Beige", "Sand", "Sage", "Fall Leaf Brown", "Ginger Brown", "DarkKhaki ", "Olive Green", "Brass", "Cookie Brown", "Metallic Gold", "Bee Yellow", "School Bus Yellow", "GoldenRod ", "Orange Gold", "Caramel", "DarkGoldenRod ", "Cinnamon", "Peru ", "Bronze", "Tiger Orange", "Copper", "Wood", "Oak Brown", "Antique Bronze", "Hazel", "Dark Yellow", "Dark Moccasin", "Bullet Shell", "Army Brown", "Sandstone", "Taupe", "Mocha", "Milk Chocolate", "Gray Brown", "Dark Coffee", "Old Burgundy", "Bakers Brown", "Dark Brown", "Coffee", "Brown Bear", "Red Dirt", "Sepia", "Sienna ", "SaddleBrown ", "Dark Sienna", "Sangria", "Blood Red", "Chestnut", "Chestnut Red", "Mahogany", "Red Fox", "Dark Bisque", "Light Brown", "Rust", "Copper Red", "Orange Salmon", "Chocolate ", "Sedona", "Papaya Orange", "Halloween Orange", "Neon Orange", "Bright Orange", "Pumpkin Orange", "Carrot Orange", "DarkOrange ", "Construction Cone Orange", "Sunrise Orange", "Mango Orange", "Coral ", "Basket Ball Orange", "Light Salmon Rose", "LightSalmon ", "DarkSalmon ", "Tangerine", "Light Copper", "Salmon ", "LightCoral ", "Pastel Red", "Pink Coral", "Bean Red", "Valentine Red", "IndianRed ", "Tomato ", "Shocking Orange", "OrangeRed ", "Red ", "Scarlet", "Ruby Red", "Ferrari Red", "Fire Engine Red", "Lava Red", "Love Red", "Grapefruit", "Cherry Red", "Chilli Pepper", "FireBrick ", "Brown ", "Carbon Red", "Cranberry", "Red Wine or Wine Red", "DarkRed ", "Maroon ", "Burgundy", "Deep Red", "Red Blood", "Blood Night", "Black Bean", "Chocolate Brown", "Midnight", "Purple Lily", "Purple Maroon", "Plum Pie", "Plum Velvet", "Velvet Maroon", "Rosy Finch", "Dull Purple", "Puce", "Rose Dust", "Rosy Pink", "RosyBrown ", "Khaki Rose", "Pink Brown", "Lipstick Pink", "Rose", "Silver Pink", "Rose Gold", "Deep Peach", "Pastel Orange", "Desert Sand", "Unbleached Silk", "Pig Pink", "Pink Bubble Gum", "MistyRose ", "Light Red", "Light Rose", "Deep Rose", "Pink ", "LightPink ", "Donut Pink", "Baby Pink", "Flamingo Pink", "Pastel Pink", "Pink Rose", "Pink Daisy", "Cadillac Pink", "Carnation Pink", "Blush Red", "PaleVioletRed ", "Purple Pink", "Tulip Pink", "Bashful Pink", "Dark Pink", "Dark Hot Pink", "HotPink ", "Watermelon Pink", "Violet Red", "Hot Deep Pink", "DeepPink ", "Neon Pink", "Pink Cupcake", "Dimorphotheca Magenta", "Pink Lemonade", "Crimson ", "Bright Maroon", "Rose Red", "Rogue Pink", "Burnt Pink", "Pink Violet", "MediumVioletRed ", "Dark Carnation Pink", "Pink Plum", "Orchid ", "Deep Mauve", "Violet ", "Bright Neon Pink", "Fuchsia or Magenta ", "Crimson Purple", "Heliotrope Purple", "Tyrian Purple", "MediumOrchid ", "Purple Flower", "Orchid Purple", "Pastel Violet", "Mauve Taupe", "Viola Purple", "Eggplant", "Plum Purple", "Grape", "Purple Navy", "SlateBlue ", "Blue Lotus", "Light Slate Blue", "MediumSlateBlue ", "Purple Amethyst", "Bright Purple", "DarkSlateBlue ", "Purple Haze", "Purple Iris", "Dark Purple", "Deep Purple", "Purple Monster", "Indigo ", "Blue Whale", "RebeccaPurple ", "Purple Jam", "DarkMagenta ", "Purple ", "French Lilac", "DarkOrchid ", "DarkViolet ", "Purple Violet", "Jasmine Purple", "Purple Daffodil", "Clemantis Violet", "BlueViolet ", "Purple Sage Bush", "Lovely Purple", "Purple Plum", "Aztech Purple", "Lavender Purple", "MediumPurple ", "Light Purple", "Crocus Purple", "Purple Mimosa", "Pale Lilac", "Mauve", "Bright Lilac", "Rich Lilac", "Purple Dragon", "Lilac", "Plum ", "Blush Pink", "Pastel Purple", "Blossom Pink", "Wisteria Purple", "Purple Thistle", "Thistle ", "Periwinkle", "Cotton Candy", "Lavender Pinocchio", "Ash White", "White Chocolate", "Soft Ivory", "Off White", "LavenderBlush ", "Pearl", "Egg Shell", "OldLace ", "Linen ", "SeaShell ", "Rice", "FloralWhite ", "Ivory ", "Light White", "WhiteSmoke ", "Cotton", "Snow ", "Milk White", "White", "White", "Yellow", "Blue", "Red", "Green", "Black", "Brown", "Azure", "Ivory", "Teal", "Silver", "Purple", "Navy blue", "Pea green", "Gray", "Orange", "Maroon", "Charcoal", "Aquamarine", "Coral", "Fuchsia", "Wheat", "Lime", "Crimson", "Khaki", "Hot pink", "Magenta", "Olden", "Plum", "Olive", "Cyan", "amber", "ash", "asphalt", "auburn", "avocado", "aquamarine", "azure", "beige", "bisque", "black", "blue", "bone", "bordeaux", "brass", "bronze", "brown", "burgundy", "camel", "caramel", "canary", "celeste", "cerulean", "champagne", "charcoal", "chartreuse", "chestnut", "chocolate", "citron", "claret", "coal", "cobalt", "coffee", "coral", "corn", "cream", "crimson", "cyan", "denim", "desert", "ebony", "ecru", "emerald", "feldspar", "fuchsia", "gold", "gray", "green", "heather", "indigo", "ivory", "jet", "khaki", "lime", "magenta", "maroon", "mint", "navy", "olive", "orange", "pink", "plum", "purple", "red", "rust", "salmon", "sienna", "silver", "snow", "steel", "tan", "teal", "tomato", "violet", "white", "yellow"]
colors = []
for i in color:
    if i.strip().lower() not in colors:
        colors.append(i.strip().lower())
# have to include the line return from CLI to get correct crc32
count = 0
for c in colors:
    clr = c[0].upper() + c[1:] + "\x0a"
    #print(hex((binascii.crc32(b'King Arthur\x0a'))))
    colorCrc = binascii.crc32(clr.encode("utf-8"))
    if colorCrc in color_tab:
        print("%02d %-10s %s"%(count,hex(colorCrc),clr[:-1]))
        count += 1
"""
I think I did this the absolute dumbest/longest/manual way possible.
There are 2 primary commands in the main binary. approach+consult
approach asks you questions to include a name, quest, and favorite color.
This is from monty python's holy grail. In the binary the quest doesn't
actually resolve to anything, but the name and color are crc32 hashed.
In each of the sha256 docker folders there is an author in each json file.
Giving these names to the approach command succeeds but you need to guess
the correct color for each name. How the fuck are you supposed to know this?
I simply scavanged for color names and put in a python list, crc32 hashed each one
and then debugged the binary with each of the 30 names to match the expected
hash to the hashes of colors I made. Giving the correct name/color combo
outputs a number. I assumed this was the order in which each of the names
archive files are to be copied into the docker image/instance...I dunno
the terminology...I don't fucking understand docker at all...so I did this
shit the hard fucking way. Not all archives have a.dat through z.dat and the
consult command reads in a-z.dat. I think what we were supposed to do 
is add commands to the docker configs/images/instance...I don't fucking know
because I don't understand docker. But if that is the case then if we
went in order the files would overwrite any previous files of the same name.
So, I just started at the end and started going backward until I had a 
full alphabet. Then ran the consult command and got the flag.

I attempted to run this in docker and could do so by doing 
docker load -i antioch.tar 
and then 
docker run -i antioch
but in the end I just ran the binary by itself.

01  Miss Islington          Brown
02  Sir Bors                Coral
03  Tim the Enchanter       Orange
04  Dragon of Angnor        Khaki
05  Brother Maynard         Crimson
06  Sir Bedevere            Teal
07  Sir Robin               Red
08  Zoot                    Tan
09  Squire Concorde         Periwinkle
10  Green Knight            Green 
11  Trojan Rabbit           Beige
12  Chicken of Bristol      Mint
13  Roger the Shrubber      Tomato
14  Bridge Keeper           Indigo
15  Sir Gawain              Azure
16  Legendary Black Beast of Argh   Silver
17  A Famous Historian      Pink
18  Sir Lancelot            Blue
19  Lady of the Lake        Gold
20  Rabbit of Caerbannog    Salmon

22  Prince Herbert          Wheat
23  King Arthur             Purple
24  Inspector End Of Film   Gray
25  Sir Ector               Bisque
26  Squire Patsy            Chartreuse
27  Dennis the Peasant      Orchid
28  Dinky                   Turquoise
29  Black Knight            Black
30  Sir Gallahad            Yellow

Sir Not-Appearing-in-this-Film  2358e4a9 UNKNOWN
"""

























