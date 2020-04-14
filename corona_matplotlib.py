import matplotlib.pyplot as plt
dict = {"USA": 22115,
        "SPAIN": 17489,
        "ITLY": 19899,
        "FRA": 14393,
        "GERM": 3022,
        "UK": 11329,
        "CHINA": 3341,
        "IRAN": 4585,
        "TURKY": 1198,
        "BEL": 3903,
        "NETHER": 2823,
        "SWITZ": 1117,
        "CANADA": 717,
        "BRAZ": 1241,
        "RAUSSIA": 148,
        "INDIA": 331}
country = list(dict.keys())
number_of_deaths = list(dict.values())

plt.title("Corona Death Analysis", fontsize=15)
plt.plot(country, number_of_deaths, 'ro-', label="Number of Deaths")
plt.xlabel("Countries", fontsize=10, color="blue")
plt.ylabel("Number of Deaths", fontsize=10, color="blue")
plt.legend(loc=0)
plt.show()