def freetables(tables):
    freetablelist = []
    for t in tables:
        if not t["occupied"]:
            freetablelist.append(t["tableid"])
    return freetablelist

def opentables(tables, partysize):
    for t in tables:
        if not t["occupied"] and t["capacity"] >= partysize:
            return t["tableid"]
    return None

def suitabletables(tables, partysize):
    avail_tables = []
    for t in tables:
        if not t["occupied"] and t["capacity"] >= partysize:
            avail_tables.append(t["tableid"])
    return avail_tables

def posscombs(tables, partysize):
    validoptions = []
    for t in tables:
        if not t["occupied"] and t["capacity"] >= partysize:
            validoptions.append((t["tableid"],))
        if t["neighbors"] and not t["occupied"]:
            for n in t["neighbors"]:
                adj_table = next((tb for tb in tables if tb["tableid"] == n), None)
                if adj_table and not adj_table["occupied"]:
                    combinedcapacity = t["capacity"] + adj_table["capacity"]
                    if combinedcapacity >= partysize:
                        validoptions.append(tuple(sorted([t["tableid"], adj_table["tableid"]])))
    return validoptions

def tableoptions(tables, options):
    for opt in options:
        if len(opt) == 1:
            tid = opt[0]
            table = next(tb for tb in tables if tb["tableid"] == tid)
            print(f"Table {tid} is open and seats {table['capacity']} people.")
        else:
            t1, t2 = opt
            tb1 = next(tb for tb in tables if tb["tableid"] == t1)
            tb2 = next(tb for tb in tables if tb["tableid"] == t2)
            capacity = tb1["capacity"] + tb2["capacity"]
            print(f"Tables {t1} and {t2} together can seat {capacity} guests.")

if __name__ == "__main__":
    sample = [
        {"tableid": 1, "capacity": 2, "occupied": False, "neighbors": [2]},
        {"tableid": 2, "capacity": 4, "occupied": True, "neighbors": [1, 3]},
        {"tableid": 3, "capacity": 2, "occupied": False, "neighbors": [2, 4]},
        {"tableid": 4, "capacity": 6, "occupied": False, "neighbors": [3]}
    ]
    print("Open Tables:", freetables(sample))
    print("Best single table for group of 2:", opentables(sample, 2))
    print("All suitable tables for group of 2:", suitabletables(sample, 2))
    combinations = posscombs(sample, 5)
    print("Possible table combinations for group of 5:", combinations)
    tableoptions(sample, combinations)
