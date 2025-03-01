import json
import requests
from urllib.parse import quote
import os
import datetime

SERPAPI_API_KEY = ""
SILICONFLOW_API_KEY = "sk-"

def googleSearch(keyword):
    url = f"https://serpapi.com/search.json?q={keyword}&api_key={SERPAPI_API_KEY}"
    # Google搜索使用代理
    proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890"
    }
    response = requests.get(url, proxies=proxies)
    return response.json()

def get_completion(messages):
    url = "https://api.siliconflow.cn/v1/chat/completions"
    
    payload = {
        "model": "Pro/deepseek-ai/DeepSeek-V3",
        "messages": messages,
        "temperature": 0.7
    }
    
    headers = {
        "Authorization": f"Bearer {SILICONFLOW_API_KEY}",
        "Content-Type": "application/json"
    }

    # 硅基流动API直接访问，显式设置空代理
    session = requests.Session()
    session.trust_env = False  # 禁用环境变量中的代理设置
    response = session.post(url, json=payload, headers=headers)
    
    # 打印原始响应和状态码
    print("Response status code:", response.status_code)
    print("Raw response:", response.text)
    
    return response.json()

# 系统提示词
system_prompt = """
Please parse the "keyword" from user's message to be used in a Google search and output them in JSON format. 

EXAMPLE INPUT: 
What's the weather like in New York today?

EXAMPLE JSON OUTPUT:
{
    "keyword": "weather in New York"
}
"""

user_prompt = "伦敦今天天气怎么样?"

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

try:
    # 获取关键词
    response = get_completion(messages)
    print("API Response:", response)
    
    if 'choices' in response and len(response['choices']) > 0:
        content = response['choices'][0]['message']['content']
        json_str = content.replace('```json', '').replace('```', '').strip()
        keyword = json.loads(json_str)["keyword"]
        
        # 进行Google搜索
        googleResponse = googleSearch(keyword)
        
        # 保存完整的Google搜索结果到文件
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"google_search_{timestamp}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(googleResponse, f, ensure_ascii=False, indent=2)
        print(f"Google search results saved to {filename}")
        
        answer_box = googleResponse.get("answer_box")
        answer_box_to_string = json.dumps(answer_box, indent=2)

        if answer_box:
            messages = [
                {"role": "system", "content": "Answer the question from user with provided information: " + answer_box_to_string},
                {"role": "user", "content": user_prompt}
            ]
            
            response = get_completion(messages)
            print(response['choices'][0]['message']['content'])
        else:
            print("No answer box found")
    else:
        print("Invalid API response format")
except Exception as e:
    print("Error occurred:", str(e))



