import requests
from bs4 import BeautifulSoup
import json

def extract_articles_from_html(html_content):
    # 解析HTML内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 找到包含JSON数据的<script>标签
    script_tag = soup.find('script', id='__APP_DATA')
    if not script_tag:
        print("无法找到包含JSON数据的<script>标签")
        return []

    # 提取JSON数据
    json_data = script_tag.string
    data = json.loads(json_data)

    # 提取catalogs数组
    catalogs = []
    try:
        catalogs = data['appState']['loader']['dataByRouteId']['d9b2']['catalogs']
    except KeyError as e:
        print(f"提取catalogs数组时出错: {e}")

    return catalogs

# 输入目标URL
url = 'https://www.binance.com/zh-CN/support/announcement/%E6%95%B0%E5%AD%97%E8%B4%A7%E5%B8%81%E5%8F%8A%E4%BA%A4%E6%98%93%E5%AF%B9%E4%B8%8A%E6%96%B0?c=48&navId=48'  # 替换为实际的目标URL

# 发送HTTP请求获取网页内容
response = requests.get(url)
response.raise_for_status()  # 检查请求是否成功

# 提取articles数组中的内容
articles = extract_articles_from_html(response.text)
for article in articles:
    print(article)