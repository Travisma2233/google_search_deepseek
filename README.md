# 📌 Google Search & SiliconFlow API | Google 搜索 & 硅基流动 API

## 🌟 Project Introduction | 项目简介

This project utilizes **Google Search API (SerpAPI)** and **SiliconFlow API** to create a simple **intelligent search assistant**. It extracts keywords from user input, performs a Google search, and returns relevant results.

本项目使用 **Google Search API (SerpAPI)** 和 **SiliconFlow API** 实现了一个简单的 **智能搜索助手**，能够从用户输入中解析关键词，并进行 Google 搜索，最终返回相关的搜索结果。

---

## 🚀 Features | 功能

✅ Extract keywords from user input 🔍 | 解析用户输入的关键词 🔍  
✅ Perform Google search 🌍 | 通过 Google 进行搜索 🌍  
✅ Parse Google search results 📄 | 解析 Google 搜索结果 📄  
✅ Use SiliconFlow API for intelligent completion 🤖 | 调用 SiliconFlow API 进行智能补全 🤖  
✅ Store results as JSON file 📝 | 结果存储为 JSON 文件 📝

---

## 🛠️ Dependencies | 依赖

Make sure you have installed the following Python libraries:

请确保你的环境已安装以下 Python 库：

```bash
pip install requests
```

---

## 🎯 Usage | 使用方法

1️⃣ **Set API Keys | 设置 API Key**

- Replace `SERPAPI_API_KEY` and `SILICONFLOW_API_KEY` with your API keys.
- 替换 `SERPAPI_API_KEY` 和 `SILICONFLOW_API_KEY` 为你的 API 密钥。

2️⃣ **Run the script | 运行代码**

```bash
python script.py
```

3️⃣ **Check results | 查看结果**

- Search results will be saved as JSON files, named `google_search_YYYYMMDD_HHMMSS.json`.
- 搜索结果将保存为 JSON 文件，命名格式为 `google_search_YYYYMMDD_HHMMSS.json`。

---

## ⚠️ Notes | 注意事项

⚡ Ensure your API keys have the correct permissions; otherwise, requests may fail.  
⚡ 请确保你的 API Key 具有正确的权限，否则请求可能会失败。

⚡ Google Search API may require a proxy; set it according to your network environment.  
⚡ Google 搜索 API 可能需要代理，请根据你的网络环境进行设置。

⚡ You may encounter `JSONDecodeError` while running; check if the API returns correctly formatted data.  
⚡ 运行时可能会遇到 `JSONDecodeError`，请检查 API 返回的数据格式是否正确。

---

## 📄 License | 许可证

This project follows the **MIT License**.  
本项目遵循 **MIT License**。