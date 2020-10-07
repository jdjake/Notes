def parse_games(steam_string, humble_string):
	steam_lines = steam_string.split("\n")
	humble_lines = humble_string.split("\n")

	for line in humble_lines:
		print(line.split("|")[0])

f1 = open("SteamGameJacob.txt","r").read()
f2 = open("HumbleBundleJacob.txt","r").read()

print("Hello world")
print(f1)