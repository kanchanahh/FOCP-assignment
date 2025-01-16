import sys
import os

def parse_driver_details(filename):
    """Parse the driver details from the given file."""
    drivers = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    drivers[parts[1]] = {"name": parts[2], "team": parts[3]}
    return drivers

def parse_lap_times(filename):
    """Parse lap times from the given file."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Lap times file '{filename}' not found.")
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    if not lines:
        raise ValueError(f"Lap times file '{filename}' is empty.")

    race_location = lines[0].strip()
    lap_data = {}

    for line in lines[1:]:
        if len(line.strip()) < 4:
            continue
        driver_code = line[:3]
        try:
            lap_time = float(line[3:].strip())
        except ValueError:
            continue
        lap_data.setdefault(driver_code, []).append(lap_time)
    
    return race_location, lap_data

def calculate_driver_stats(lap_data):
    """Calculate statistics for each driver."""
    stats = {}
    for driver, times in lap_data.items():
        stats[driver] = {
            "fastest_time": min(times),
            "average_time": sum(times) / len(times)
        }
    return stats

def format_table(headers, rows, col_widths):
    """Format data into a neatly aligned table."""
    separator = "+" + "+".join("-" * w for w in col_widths) + "+"
    formatted_table = [separator]
    header_row = "|" + "|".join(h.center(w) for h, w in zip(headers, col_widths)) + "|"
    formatted_table.append(header_row)
    formatted_table.append(separator)

    for row in rows:
        formatted_row = "|" + "|".join(str(cell).ljust(w) for cell, w in zip(row, col_widths)) + "|"
        formatted_table.append(formatted_row)
    formatted_table.append(separator)
    return "\n".join(formatted_table)

def display_results(lap_filename, driver_filename):
    """Display race results in a formatted table."""
    drivers = parse_driver_details(driver_filename)
    race_location, lap_data = parse_lap_times(lap_filename)
    driver_stats = calculate_driver_stats(lap_data)

    print(f"Race Location: {race_location}\n")

    headers = ["Driver Code", "Name", "Team", "Fastest Lap", "Average Lap"]
    rows = []

    for driver_code, stats in driver_stats.items():
        driver_info = drivers.get(driver_code, {"name": "Unknown", "team": "Unknown"})
        rows.append([
            driver_code,
            driver_info["name"],
            driver_info["team"],
            f"{stats['fastest_time']:.3f}",
            f"{stats['average_time']:.3f}"
        ])
    
    col_widths = [15, 25, 20, 15, 15]
    print(format_table(headers, rows, col_widths))

    overall_fastest_driver = min(driver_stats, key=lambda d: driver_stats[d]["fastest_time"])
    fastest_time = driver_stats[overall_fastest_driver]["fastest_time"]
    print(f"\nOverall Fastest Lap: {fastest_time:.3f} by {overall_fastest_driver} ({drivers.get(overall_fastest_driver, {}).get('name', 'Unknown')})")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python timingboard.py <lap_times_filename> <drivers_filename>")
    else:
        try:
            display_results(sys.argv[1], sys.argv[2])
        except Exception as e:
            print(f"Error: {e}")