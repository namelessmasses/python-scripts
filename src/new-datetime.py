import datetime
import argparse

def main():
    parser = argparse.ArgumentParser(description="Parse and display a datetime string in ISO 8601 format and display it as POSIX timestamp.")
    parser.add_argument('--string', type=str, required=True, help='Datetime string in ISO 8601 format (e.g., 2024-06-01T12:34:56)')    
    args = parser.parse_args()
    
    dt = datetime.datetime.fromisoformat(args.string)
    print(f"Parsed datetime: {dt.isoformat()}")
    print(f"POSIX timestamp: {dt.timestamp()}")

if __name__ == "__main__":
    main()