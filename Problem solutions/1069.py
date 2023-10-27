import math
import sys


def main() -> None:
	input_x, input_y, tele_dist, tele_time = map(int, sys.stdin.readline().rstrip().split(sep=' '))

	total_dist = math.sqrt(input_x ** 2 + input_y ** 2)

	if tele_dist <= tele_time:
		print(total_dist)
		return

	if tele_dist > total_dist:
		print(
			min(
				2 * tele_time,
				total_dist,
				tele_dist - total_dist + tele_time
			)
		)
		return

	output_time = 0

	while total_dist >= 2 * tele_dist:
		output_time += tele_time
		total_dist -= tele_dist

	print(output_time + min(
		2 * tele_time,
		total_dist,
		total_dist - tele_dist + tele_time
	))

	return


if __name__ == '__main__':
	main()
