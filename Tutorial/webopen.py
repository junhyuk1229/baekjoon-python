import sys
import webbrowser


def submit(number):
    webbrowser.open('https://www.acmicpc.net/submit/' + str(number))


def main():
    submit(1550)


if __name__ == "__main__":
    main()
