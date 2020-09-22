from setup import *
from play import *

# Print Setup Details
print(
    f"Loading data set into blackhat.null...\n"
    f"Companies:\t\t{len(COMPANIES)}\n"
    f"Employees:\t\t{len(EMPLOYEES)}\n"
    f"Store Items:\t{len(DISKS) + len(MEMORY) + len(NETWORKS) + len(PROCESSORS) + len(WORKSTATIONS)}\n"
    f"- Disks:\t\t{len(DISKS)}\n"
    f"- Memory:\t\t{len(MEMORY)}\n"
    f"- Network:\t\t{len(NETWORKS)}\n"
    f"- Processors:\t{len(PROCESSORS)}\n"
    f"- Workstations:\t{len(WORKSTATIONS)}\n"
    f"Qualifications:\t{len(QUALIFICATIONS)}\n"
    f"Servers:\t\t{len(SERVERS)}\n"
    f"Data loaded successfully!"
)

# Start at main menu
display_menu(0)
