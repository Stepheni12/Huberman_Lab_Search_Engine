import xml.etree.ElementTree as ET
import requests
from tqdm import tqdm

# Path to your XML file
xml_file_path = "hubermanlab.xml"

# Parse XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Find all 'enclosure' elements and extract the 'url' attribute
enclosures = root.findall(".//enclosure")
urls = [enclosure.get("url") for enclosure in enclosures]
    
print("Number of URL's scraped:",len(urls))


def download_mp3_with_progress(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(save_path, 'wb') as file, tqdm(
        desc="Downloading",
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in iter(lambda: response.raw.read(1024), b""):
            file.write(chunk)
            bar.update(len(chunk))