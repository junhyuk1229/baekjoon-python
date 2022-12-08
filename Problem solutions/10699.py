from datetime import datetime


def main():
    now = datetime.now()
    print(now.strftime("%Y-%m-%d"))


if __name__ == "__main__":
    main()