"""
Run initial setup/population of default data
"""

from classes.Company import Company
from classes.Contents import Contents
from classes.Disk import Disk
from classes.Employee import Employee
from classes.Memory import Memory
from classes.Menu import Menu
from classes.Network import Network
from classes.Processor import Processor
from classes.Qualification import Qualification
from classes.Server import Server

# ACCOUNTS = []
# BADGES = []
# BANK_ACCOUNTS = []
from classes.Workstation import Workstation

COMPANIES = []
# CONTENTS = []
DISKS = []
EMPLOYEES = []
# HACKERS = []
MEMORY = []
MENUS = []
# MISSIONS = []
NETWORKS = []
PROCESSORS = []
QUALIFICATIONS = []
SERVERS = []
WORKSTATIONS = []
# WORKSTATION_COMPONENTS = []

# Company List
COMPANIES.append(Company(1, "Bob's Computer Repair", "", 4, 100000, 1992))
COMPANIES.append(Company(2, "Jim's Software Services", "", 3, 32000, 2001))
COMPANIES.append(Company(3, "NanoTech Software", "", 23, 2100000, 2003))
COMPANIES.append(Company(4, "Herb's Hardware", "", 2, 140000, 1985))

# Disks List (Space is in GB)
DISKS.append(Disk("Basic HDD", "No Frills 5400RPM HDD", 50, 1, 5400, 1000))
DISKS.append(Disk("Basic HDD", "No Frills 5400RPM HDD", 50, 1, 5400, 2000))
DISKS.append(Disk("Basic HDD", "No Frills 5400RPM HDD", 50, 1, 5400, 4000))
DISKS.append(Disk("Basic HDD", "No Frills 5400RPM HDD", 50, 1, 5400, 8000))
DISKS.append(Disk("Standard HDD", "No Frills 7200RPM HDD", 50, 1, 7200, 1000))
DISKS.append(Disk("Standard HDD", "No Frills 7200RPM HDD", 50, 1, 7200, 2000))
DISKS.append(Disk("Standard HDD", "No Frills 7200RPM HDD", 50, 1, 7200, 4000))
DISKS.append(Disk("Standard HDD", "No Frills 7200RPM HDD", 50, 1, 7200, 8000))
DISKS.append(Disk("Performance SSD", "Performance SSD Drive", 50, 1, 15000, 500))
DISKS.append(Disk("Performance SSD", "Performance SSD Drive", 50, 1, 15000, 1000))
DISKS.append(Disk("Performance SSD", "Performance SSD Drive", 50, 1, 15000, 1500))
DISKS.append(Disk("Performance SSD", "Performance SSD Drive", 50, 1, 15000, 2000))
DISKS.append(Disk("Performance SSD", "Performance SSD Drive", 50, 1, 15000, 4000))

# Employee List
EMPLOYEES.append(Employee(1, "Jim", "Bond", "999-88-7777", "123-123-1234", "9876 Somewhere St.", "St. Louis", "MO",
                          "11111", None, None, 0, None))
EMPLOYEES.append(Employee(2, "Bob", "Smith", "111-22-3333", "111-222-3333", "123 Anywhere Rd.", "Orlando", "FL",
                          "32830", None, "Network Engineer", 123200.00, None))

# Memory List (Size in MB)
MEMORY.append(Memory("Dynamix DDR 2100 RAM", "1x1GB Kit - Older but common RAM", 100, 1, 2100, 1024))
MEMORY.append(Memory("Dynamix DDR 2100 RAM", "1x2GB Kit - Older but common RAM", 200, 1, 2100, 2048))
MEMORY.append(Memory("Dynamix DDR 2100 RAM", "2x2GB Kit - Older but common RAM", 450, 2, 2100, 4096))
MEMORY.append(Memory("Dynamix DDR 2100 RAM", "2x4GB Kit - Older but common RAM", 950, 2, 2100, 8192))
MEMORY.append(Memory("Ballistix DDR 3000 RAM", "1x2GB Kit - Performance RAM", 300, 1, 3000, 2048))
MEMORY.append(Memory("Ballistix DDR 3000 RAM", "1x4GB Kit - Performance RAM", 600, 1, 3000, 4096))
MEMORY.append(Memory("Ballistix DDR 3000 RAM", "2x4GB Kit - Performance RAM", 1500, 2, 3000, 8192))
MEMORY.append(Memory("Ballistix DDR 3000 RAM", "2x8GB Kit - Performance RAM", 3500, 2, 3000, 16384))

# Menus List
MENUS.append(Menu("Main Menu", "Welcome to Blackhat.NULL! Here's your opportunity to get a piece of the black market "
                               "profits as a security consultant. Please see the options below and let the games begin!",
                  [[1, "Log-in to Console", "login"], [2, "Settings", "settings"], [3, "Exit", "exit"]]))
MENUS.append(Menu("Settings", "Customize your game settings below", [[1, "Enable Debug", "debug"], [2, "Show Help", "help"], [3, "Back", "back"]]))
MENUS.append(Menu("Play", "Welcome to your terminal. Select from the options below to get started",
                  [[1, "Jobs Board", "jobs"],
                   [2, "Banking", "bank"],
                   [3, "Shop", "shop"],
                   [4, "Terminal", "terminal"],
                   [5, "Logout", "logout"]]))

# Network List
NETWORKS.append(Network("10MB Network Card", "Basic Network Card", 100, 1, 10, 10))
NETWORKS.append(Network("100MB Network Card", "Standard Network Card", 1000, 1, 100, 100))
NETWORKS.append(Network("1GB Network Card", "Advanced Network Card", 10000, 1, 1000, 1000))
NETWORKS.append(Network("10GB Network Card", "High Speed Network Card", 100000, 2, 10000, 10000))

# Processor List
PROCESSORS.append(Processor("Insmell PC2000", "Basic Consumer Processor", 100, 1, 2000))
PROCESSORS.append(Processor("Insmell PC3000", "Standard Consumer Processor", 300, 1, 3000))
PROCESSORS.append(Processor("Insmell PC4000", "Standard Consumer Processor w/ Turbo", 600, 1, 4000))
PROCESSORS.append(Processor("Insmell PC6000", "Advanced Consumer Processor", 700, 1, 6000))
PROCESSORS.append(Processor("Insmell PC8000", "Advanced Consumer Processor w/ Turbo", 1500, 1, 8000))
PROCESSORS.append(Processor("Insmell PC10000", "Ultra Industrial Processor", 3000, 1, 10000))

# Qualifications
QUALIFICATIONS.append(Qualification("Network Security", "Class 1"))
QUALIFICATIONS.append(Qualification("Network Security", "Class 2"))
QUALIFICATIONS.append(Qualification("Network Security", "Class 3"))
QUALIFICATIONS.append(Qualification("Network Security", "Class 4"))
QUALIFICATIONS.append(Qualification("Software Developer", "Class 1"))
QUALIFICATIONS.append(Qualification("Software Developer", "Class 2"))
QUALIFICATIONS.append(Qualification("Software Developer", "Class 3"))
QUALIFICATIONS.append(Qualification("Software Developer", "Class 4"))

# Servers
SERVERS.append(Server(1, "Server A", "file", "192.192.192.192", 1,
                      Contents(["File A.txt", "File B.txt", "File C.jpg"])))
SERVERS.append(Server(2, "Server B", "bank", "10.10.10.10", 2,
                      Contents([["1234", "John Smith", 123.45], ["2345", "Suzie Sanders", 524.12]])))
SERVERS.append(Server(3, "Server C", "database", "10.80.3.18", 2,
                      Contents([["Steve", "Smith", "9876 Somewhere St.", "St. Louis", "MO"],
                                ["Jim", "Jones", "123 Middle Rd.", "Indianapolis", "IN"]])))

# Workstations
WORKSTATIONS.append(Workstation("Standard Desktop PC", "Standard performance PC", 500, 4, [DISKS[1], MEMORY[1], NETWORKS[1], PROCESSORS[1]]))
WORKSTATIONS.append(Workstation("Mid-range Desktop PC", "Moderate performance PC", 1000, 5, [DISKS[5], MEMORY[2], NETWORKS[2], PROCESSORS[2]]))
WORKSTATIONS.append(Workstation("High-End Gaming PC", "High-speed gaming performance PC", 2000, 8, [DISKS[8], MEMORY[4], NETWORKS[3], PROCESSORS[3]]))
WORKSTATIONS.append(Workstation("High-End Workstation", "High performance Workstation", 3500, 16, [DISKS[11], MEMORY[6], NETWORKS[3], PROCESSORS[4]]))
