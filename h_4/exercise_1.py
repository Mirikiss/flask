import requests
import time
import argparse
import concurrent.futures
import asyncio
import aiohttp


def download_image_thread(url):
	response = requests.get(url)
	filename = url.split("/")[-1]
	with open(filename, "wb") as f:
		f.write(response.content)
	print(f"Downloaded {filename}")


def download_image_process(url):
	response = requests.get(url)
	filename = url.split("/")[-1]
	with open(filename, "wb") as f:
		f.write(response.content)
	print(f"Downloaded {filename}")


async def download_image_async(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as response:
			filename = url.split("/")[-1]
			with open(filename, "wb") as f:
				f.write(await response.read())
			print(f"Downloaded {filename}")


def download_images_thread(urls):
	start_time = time.time()
	with concurrent.futures.ThreadPoolExecutor() as executor:
		executor.map(download_image_thread, urls)
	end_time = time.time()
	total_time = end_time - start_time
	print(f"Total time taken: {total_time} seconds")


def download_images_process(urls):
	start_time = time.time()
	with concurrent.futures.ProcessPoolExecutor() as executor:
		executor.map(download_image_process, urls)
	end_time = time.time()
	total_time = end_time - start_time
	print(f"Total time taken: {total_time} seconds")


async def download_images_async(urls):
	start_time = time.time()
	tasks = []
	for url in urls:
		tasks.append(download_image_async(url))
	await asyncio.gather(*tasks)
	end_time = time.time()
	total_time = end_time - start_time
	print(f"Total time taken: {total_time} seconds")


def get_urls_from_command_line():
	parser = argparse.ArgumentParser()
	parser.add_argument("urls", nargs="+", help="List of image URLs")
	args = parser.parse_args()
	return args.urls


def main():
	urls = get_urls_from_command_line()

	download_images_thread(urls)

	download_images_process(urls)

	asyncio.run(download_images_async(urls))


if __name__ == "__main__":
	main()