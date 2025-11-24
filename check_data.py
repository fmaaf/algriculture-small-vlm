# import os

# file_path = '/media/fmaaf/新加卷/agriculture_dataset/Jute_Pest_Dataset/Jute_Pest_Dataset/train/qwen_labeled_data.json'

# print(f"正在扫描文件行号: {file_path}")

# try:
#     with open(file_path, 'r', encoding='utf-8') as f:
#         # 逐行读取文件
#         for line_num, line in enumerate(f, 1):
#             # 查找错误的 Key，通常是带双引号的 "从":
#             if '"从":' in line:
#                 print(f"-> [行号 {line_num}] 发现错误: {line.strip()}")

# except Exception as e:
#     print(f"读取错误: {e}")



import json

# 修改为你的数据集路径
JSON_FILE = "/media/fmaaf/新加卷/agriculture_dataset/Jute_Pest_Dataset/Jute_Pest_Dataset/train/qwen_labeled_data.json"

def check_dataset():
    print(f"正在检查文件: {JSON_FILE} ...")
    
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ JSON 文件无法读取: {e}")
        return

    error_count = 0
    
    for index, item in enumerate(data):
        # 1. 检查是否有 conversations
        if "conversations" not in item:
            print(f"⚠️ [Index {index}] ID: {item.get('id', 'Unknown')} -> 缺少 'conversations' 字段")
            error_count += 1
            continue
            
        # 2. 遍历每一轮对话
        for turn_idx, turn in enumerate(item["conversations"]):
            # 检查是否有 'value' 键
            if "value" not in turn:
                print(f"❌ [Index {index}] ID: {item.get('id', 'Unknown')}")
                print(f"   第 {turn_idx+1} 轮对话出错: {turn}")
                print(f"   缺少 'value' 键。现有的键: {list(turn.keys())}")
                print("-" * 30)
                error_count += 1
    
    if error_count == 0:
        print("✅ 恭喜！数据格式完美，没有发现缺少 'value' 的情况。")
    else:
        print(f"🚫 检查结束，共发现 {error_count} 处错误。请根据 ID 修正 JSON 文件。")

if __name__ == "__main__":
    check_dataset()