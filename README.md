# Qiuzhi Project (OpenClaw Skill Demo)

这是一个简单、易于 Fork 且支持 Codespace 的 Python 项目，用于演示 **Google Gemini API** 的集成。

## 🚀 快速开始 (仅需 30 秒)

如果您使用 GitHub Codespaces，则无需安装任何环境！

1.  **Fork 此仓库**
    点击页面右上角的 **Fork** 按钮。

2.  **在 Codespaces 中打开**
    - 点击绿色的 **Code** 按钮。
    - 切换到 **Codespaces** 标签页。
    - 点击 **Create codespace on main**。

3.  **运行演示**
    终端准备好后，运行以下命令：

    ```bash
    # 安装依赖
    pip install google-generativeai

    # 运行演示 (需要 GOOGLE_API_KEY)
    export GOOGLE_API_KEY="您的_API_KEY"
    python3 start_here.py
    ```

## 🔑 必要条件

运行此项目需要：

-   **Google Gemini API Key**: 可在 [Google AI Studio](https://aistudio.google.com/) 免费获取。

## 📂 项目结构

-   `start_here.py`: 入口脚本。从这里开始！
-   `demo_system.py`: 演示系统交互。
-   `test_image_gen.py`: 测试图像生成能力（如果可用）。
-   `test_skill.py`: 验证技能集成。

## 🤝 贡献

欢迎 Fork 并提交 Pull Request！本项目旨在作为您 AI 实验的一个简单起点。
