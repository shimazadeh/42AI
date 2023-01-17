
from tqdm import tqdm
import time

# import timebar=tqdm(range(10),
#       bar_format="{percentage:3.0f}% |{bar}| {elapsed}/{remaining}"
#      )

def ft_progress(listy):
	# for i in tqdm(range(20)):
	# 	time.sleep(0.5)
	t = tqdm(listy, bar_format = "ETA: {remaining} [{percentage:3.0f}%][{bar:30}] elapsed time {elapsed}")
	return (t)

def main():
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		time.sleep(0.01)
	print()
	print(ret)


if __name__ == "__main__":
	main()
