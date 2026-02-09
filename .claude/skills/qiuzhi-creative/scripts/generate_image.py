#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
秋芝餐厅品牌物料生成脚本
使用 Gemini API 生成符合品牌视觉规范的图片
"""

import os
import sys
import json
import google.generativeai as genai
from PIL import Image
import io

# 设置标准输出编码，解决Windows控制台乱码问题
if os.name == 'nt':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

try:
    import google.generativeai as genai
except ImportError:
    print("错误：未安装 google-generativeai，请运行：pip install google-gemini")
    sys.exit(1)

# 从环境变量读取 API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("错误：请设置 GOOGLE_API_KEY 环境变量")
    sys.exit(1)

# 初始化模型
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash-exp-image-generation')

# 品牌视觉关键词（始终包含在 prompt 中）
BRAND_STYLE = """ 
Style requirements:
- 3D cartoon gourd mascot with mint green color (#5DDEB5) and white stripes
- Fresh, healthy, youthful, modern aesthetic
- High-quality 3D rendering with soft lighting
- Clean, minimalist background
- Appetizing food presentation if applicable
- Friendly and inviting atmosphere
"""

def generate_image(prompt, output_path="./output", reference_images=None):
    """
    生成符合品牌规范的图像
    
    Args:
        prompt (str): 用户的创意描述
        output_path (str): 输出路径
        reference_images (list): 参考图片路径列表
    """
    try:
        # 组合最终提示词
        final_prompt = f"{prompt}\n\n{BRAND_STYLE}"
        
        print(f"正在生成图像...")
        print(f"提示词: {final_prompt[:100]}...")
        
        # 准备参考图片
        images = []
        if reference_images:
            for img_path in reference_images:
                if os.path.exists(img_path):
                    with Image.open(img_path) as img:
                        img_bytes = io.BytesIO()
                        img.save(img_bytes, format='PNG')
                        img_bytes.seek(0)
                        images.append(Image.open(img_bytes))
        
        # 调用模型生成图像
        response = model.generate_content([
            f"Generate an image based on the following description: {final_prompt}",
            *images
        ])
        
        # 保存生成的图像
        os.makedirs(output_path, exist_ok=True)
        
        # 这里简化处理，实际的 Gemini API 可能有不同的响应格式
        # 在实际应用中，需要根据 API 的实际响应格式来处理
        if hasattr(response, 'images'):
            for i, img in enumerate(response.images):
                img_path = os.path.join(output_path, f"qiuzhi_creative_{i+1}.png")
                img.save(img_path)
                print(f"图像已保存到: {img_path}")
        else:
            print("警告：API 响应中未包含图像数据")
            print(f"响应内容: {response}")

    except Exception as e:
        print(f"图像生成过程中发生错误: {str(e)}")

if __name__ == "__main__":
    # 示例用法
    if len(sys.argv) < 2:
        print("用法: python generate_image.py \"<创意描述>\" [输出路径] [参考图片路径1] [参考图片路径2] ...")
        sys.exit(1)
    
    user_prompt = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "./output"
    reference_images = sys.argv[3:] if len(sys.argv) > 3 else []
    
    generate_image(user_prompt, output_path, reference_images)