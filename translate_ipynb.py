import os
import json
import requests
import time
import hashlib
import hmac
import nbformat
from tqdm import tqdm
import re

# 腾讯翻译API配置信息
SECRET_ID = 'AKIDjMqBMSM6h8OUPJ4byEI8rOhlcJtGSSIx'
SECRET_KEY = 'WrCOPDmEcu33ubLzVq01ta2IMEtPl8f2'
REGION = 'ap-guangzhou'
ENDPOINT = 'tmt.tencentcloudapi.com'
SERVICE = 'tmt'
VERSION = '2018-03-21'
ACTION = 'TextTranslate'

# 请求间隔时间（秒）
REQUEST_INTERVAL = 0.5
# 最大重试次数
MAX_RETRIES = 5
# 每次翻译的最大字符数
MAX_CHARS_PER_REQUEST = 2000

def sign_request(secret_id, secret_key, method, endpoint, uri, params):
    timestamp = int(time.time())
    date = time.strftime('%Y-%m-%d', time.gmtime(timestamp))
    
    # 1. Build Canonical Request String
    http_request_method = method
    canonical_uri = uri
    canonical_querystring = ''
    canonical_headers = f'content-type:application/json\nhost:{endpoint}\n'
    signed_headers = 'content-type;host'
    payload_hash = hashlib.sha256(json.dumps(params).encode('utf-8')).hexdigest()
    canonical_request = (http_request_method + '\n' + 
                        canonical_uri + '\n' + 
                        canonical_querystring + '\n' + 
                        canonical_headers + '\n' + 
                        signed_headers + '\n' + 
                        payload_hash)
    
    # 2. Build String to Sign
    algorithm = 'TC3-HMAC-SHA256'
    credential_scope = f"{date}/{SERVICE}/tc3_request"
    string_to_sign = (algorithm + '\n' + 
                     str(timestamp) + '\n' + 
                     credential_scope + '\n' + 
                     hashlib.sha256(canonical_request.encode('utf-8')).hexdigest())
    
    # 3. Sign String
    def sign(key, msg):
        return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()
    
    secret_date = sign(('TC3' + secret_key).encode('utf-8'), date)
    secret_service = sign(secret_date, SERVICE)
    secret_signing = sign(secret_service, 'tc3_request')
    signature = hmac.new(secret_signing, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()
    
    # 4. Build Authorization Header
    authorization = (f"{algorithm} "
                    f"Credential={secret_id}/{credential_scope}, "
                    f"SignedHeaders={signed_headers}, "
                    f"Signature={signature}")
    
    return authorization, timestamp

def translate_to_chinese(text):
    # 确保text是字符串类型
    if not isinstance(text, str):
        text = str(text)
    

    # 如果文本过长，分段翻译
    if len(text) > MAX_CHARS_PER_REQUEST:
        chunks = [text[i:i+MAX_CHARS_PER_REQUEST] for i in range(0, len(text), MAX_CHARS_PER_REQUEST)]
        translated_chunks = []
        for chunk in chunks:
            translated_chunks.append(_translate_chunk(chunk))
            time.sleep(REQUEST_INTERVAL)  # 控制请求频率
        return ''.join(translated_chunks)
    else:
        return _translate_chunk(text)

def _translate_chunk(text):
    params = {
        "SourceText": text,
        "Source": "en",
        "Target": "zh",
        "ProjectId": 0
    }

    method = 'POST'
    uri = '/'
    
    for attempt in range(MAX_RETRIES):
        try:
            authorization, timestamp = sign_request(SECRET_ID, SECRET_KEY, method, ENDPOINT, uri, params)

            headers = {
                'Content-Type': 'application/json',
                'Host': ENDPOINT,
                'X-TC-Action': ACTION,
                'X-TC-Timestamp': str(timestamp),
                'X-TC-Version': VERSION,
                'X-TC-Region': REGION,
                'Authorization': authorization
            }

            response = requests.post(f'https://{ENDPOINT}{uri}', headers=headers, data=json.dumps(params))
            result = response.json()
            
            if 'Response' in result and 'TargetText' in result['Response']:
                return result['Response']['TargetText']
            else:
                print(f"翻译API响应错误: {result}")
                if attempt < MAX_RETRIES - 1:
                    time.sleep(REQUEST_INTERVAL * 2)  # 重试前等待更长时间
                    continue
                return text  # 如果翻译失败，返回原文
        except Exception as e:
            print(f"翻译请求失败: {str(e)}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(REQUEST_INTERVAL * 2)
                continue
            return text
    
    return text

def fix_markdown_format(text):
    # 修复Markdown标题格式
    text = re.sub(r'^(#{1,6})([^#\s])', r'\1 \2', text, flags=re.MULTILINE)
    # 修复Markdown链接格式
    text = re.sub(r'\[([^\]]+)\]\s*（([^)]+)）', r'[\1] (\2)', text)
    # 修复列表格式
    text = re.sub(r'^\s*([*+-])\s*([^\s])', r'\1 \2', text, flags=re.MULTILINE)
    # 修复代码块格式
    text = re.sub(r'```\s*([^\n]+)', r'```\1', text)
    # 修复引用格式
    text = re.sub(r'^>\s*([^\s])', r'> \1', text, flags=re.MULTILINE)
    # 修复图片链接格式
    text = re.sub(r'!\[([^\]]*)\]\s*（([^)]+)）', r'![\1] (\2)', text)
    # 修复表格格式
    text = re.sub(r'\|([^|]+)\|', lambda m: '|' + '|'.join(cell.strip() for cell in m.group(1).split('|')) + '|', text)
    # 修复多余的逗号
    text = text.replace(',,,', '')
    # 修复JSON拼写错误
    text = text.replace('SON', 'JSON')
    # 删除多余的空格
    text = re.sub(r'\s+', ' ', text)
    return text

def translate_markdown_file(md_path):
    """翻译Markdown文件"""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 分段翻译
    sections = content.split('\n\n')
    translated_sections = []
    
    for section in tqdm(sections, desc=f"翻译 {os.path.basename(md_path)}"):
        translated = translate_to_chinese(section)
        translated = fix_markdown_format(translated)
        translated_sections.append(translated)
        time.sleep(REQUEST_INTERVAL)
    
    # 保存翻译后的文件
    output_path = md_path.replace('.md', '_zh.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(translated_sections))
    
    print(f"已翻译并保存: {output_path}")

def translate_notebook(notebook_path):
    # 使用nbformat读取原始notebook
    notebook = nbformat.read(notebook_path, as_version=4)
    
    total_cells = len(notebook.cells)
    print(f"开始翻译: {notebook_path} ({total_cells}个单元格)")
    
    with tqdm(total=total_cells, desc="翻译进度") as pbar:
        for cell in notebook.cells:
            if cell.cell_type == 'markdown' or cell.cell_type == 'code':
                # 翻译markdown内容和代码注释
                if cell.cell_type == 'code':
                    # 翻译代码注释
                    source_lines = cell.source.splitlines()
                    translated_lines = []
                    for line in source_lines:
                        if line.strip().startswith('#'):
                            translated_line = translate_to_chinese(line)
                            time.sleep(REQUEST_INTERVAL)  # 控制请求频率
                            translated_lines.append(translated_line)
                        else:
                            translated_lines.append(line)
                    cell.source = '\n'.join(translated_lines)
                else:
                    # 翻译markdown内容
                    cell.source = translate_to_chinese(cell.source)
                    # 修复Markdown格式
                    cell.source = fix_markdown_format(cell.source)
                    time.sleep(REQUEST_INTERVAL)
            pbar.update(1)
    
    # 保存翻译后的notebook
    output_path = notebook_path.replace('.ipynb', '_zh.ipynb')
    nbformat.write(notebook, output_path)
    print(f"\n已翻译并保存: {output_path}")

def main():
    base_dir = 'teachopencadd/talktorials'
    
    # 获取所有教程目录
    tutorial_dirs = [d for d in os.listdir(base_dir)
                    if os.path.isdir(os.path.join(base_dir, d))
                    and d.startswith('T')]
    
    for tutorial_dir in tutorial_dirs:
        dir_path = os.path.join(base_dir, tutorial_dir)
        
        # 翻译README.md
        readme_path = os.path.join(dir_path, 'README.md')
        if os.path.exists(readme_path):
            translate_markdown_file(readme_path)

if __name__ == '__main__':
    main()