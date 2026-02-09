# Qiuzhi Project (Clawdbot Skill Demo) / 求知项目

A simple, fork-able, and Codespace-ready Python project to demonstrate **Google Gemini API** integration.
一个简单、易于 Fork 且支持 Codespace 的 Python 项目，用于演示 **Google Gemini API** 的集成。

---

## 🚀 Quick Start (30 Seconds) / 快速开始

No installation required if you use GitHub Codespaces!
如果您使用 GitHub Codespaces，则无需安装任何环境！

1.  **Fork this Repository** / **Fork 此仓库**
    Click the **Fork** button at the top right of this page.
    点击页面右上角的 **Fork** 按钮。

2.  **Open in Codespaces** / **在 Codespaces 中打开**
    - Click the green **Code** button.
    - Switch to the **Codespaces** tab.
    - Click **Create codespace on main**.
    - 点击绿色的 **Code** 按钮 -> 切换到 **Codespaces** 标签页 -> 点击 **Create codespace on main**。

3.  **Run the Demo** / **运行演示**
    Once the terminal is ready, run:
    终端准备好后，运行以下命令：

    ```bash
    # Install dependencies / 安装依赖
    pip install google-generativeai

    # Run the demo (Requires GOOGLE_API_KEY) / 运行演示 (需要 API Key)
    export GOOGLE_API_KEY="your_api_key_here"
    python3 start_here.py
    ```

---

## 🔑 Requirements / 必要条件

To run this project, you need:
运行此项目需要：

-   **Google Gemini API Key**: Get one for free at [Google AI Studio](https://aistudio.google.com/).
-   **Google Gemini API Key**: 可在 [Google AI Studio](https://aistudio.google.com/) 免费获取。

---

## 📂 Project Structure / 项目结构

-   `start_here.py`: The entry point script. Start here! / 入口脚本。从这里开始！
-   `demo_system.py`: Demonstrates system interactions. / 演示系统交互。
-   `test_image_gen.py`: Tests image generation capabilities (if available). / 测试图像生成能力。
-   `test_skill.py`: Validates skill integration. / 验证技能集成。

---

## 🤝 Contributing / 贡献

Feel free to fork and submit Pull Requests! This project is designed to be a simple starting point for your own AI experiments.
欢迎 Fork 并提交 Pull Request！本项目旨在作为您 AI 实验的一个简单起点。
