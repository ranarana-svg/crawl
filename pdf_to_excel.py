import pdfplumber
import pandas as pd
import sys
import os

def pdf_to_excel(pdf_path, excel_path):
    """
    将PDF文件转换为Excel文件，所有数据放在一个工作表中
    """
    all_data = []
    
    print(f"正在读取PDF文件: {pdf_path}")
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"PDF共有 {total_pages} 页")
            
            for page_num, page in enumerate(pdf.pages, 1):
                print(f"正在处理第 {page_num}/{total_pages} 页...")
                
                # 提取表格
                tables = page.extract_tables()
                
                if tables:
                    for table in tables:
                        if table:
                            # 跳过空行
                            for row in table:
                                if row and any(cell and str(cell).strip() for cell in row):
                                    all_data.append(row)
                else:
                    # 如果没有表格，尝试提取文本并转换为表格格式
                    text = page.extract_text()
                    if text:
                        lines = text.split('\n')
                        for line in lines:
                            if line.strip():
                                all_data.append([line.strip()])
        
        if not all_data:
            print("警告: 未从PDF中提取到任何数据")
            return False
        
        print(f"共提取到 {len(all_data)} 行数据")
        
        if not all_data:
            print("警告: 未提取到任何数据")
            return False
        
        # 创建DataFrame
        # 找到最大列数
        max_cols = max(len(row) for row in all_data) if all_data else 0
        
        # 确保所有行都有相同的列数
        normalized_data = []
        for row in all_data:
            # 清理数据：将None转换为空字符串，去除前后空格
            cleaned_row = [str(cell).strip() if cell is not None else '' for cell in row]
            normalized_row = cleaned_row + [''] * (max_cols - len(cleaned_row))
            normalized_data.append(normalized_row[:max_cols])
        
        # 去除重复的表头行（如果第一行和第二行相同，则删除第二行）
        if len(normalized_data) > 1:
            first_row_str = str(normalized_data[0])
            filtered_data = [normalized_data[0]]  # 保留第一行
            
            for i in range(1, len(normalized_data)):
                current_row_str = str(normalized_data[i])
                # 如果当前行与第一行不完全相同，则保留
                if current_row_str != first_row_str:
                    filtered_data.append(normalized_data[i])
                else:
                    print(f"检测到重复表头，已跳过第 {i+1} 行")
            
            normalized_data = filtered_data
        
        df = pd.DataFrame(normalized_data)
        
        # 如果第一行看起来像表头，可以将其作为列名
        if len(df) > 0:
            # 检查第一行是否可能是表头（包含非空值）
            first_row = df.iloc[0]
            if first_row.notna().sum() > 0 and first_row.astype(str).str.strip().ne('').sum() > 0:
                # 使用第一行作为列名，数据从第二行开始
                df.columns = [str(col) if pd.notna(col) else f'列{i+1}' for i, col in enumerate(first_row)]
                df = df[1:].reset_index(drop=True)
        
        print(f"正在保存Excel文件: {excel_path}")
        
        # 保存为Excel文件
        df.to_excel(excel_path, index=False, engine='openpyxl')
        
        print(f"转换完成！Excel文件已保存到: {excel_path}")
        return True
        
    except Exception as e:
        print(f"错误: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # 桌面路径
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # PDF文件路径
    pdf_file = os.path.join(desktop_path, "高校一流课程建设数据.pdf")
    
    # 如果主文件不存在，尝试其他变体
    if not os.path.exists(pdf_file):
        pdf_file_alt1 = os.path.join(desktop_path, "高校一流课程建设数据 (2).pdf")
        pdf_file_alt2 = os.path.join(desktop_path, "高校一流课程建设数据.html.pdf")
        
        if os.path.exists(pdf_file_alt1):
            pdf_file = pdf_file_alt1
        elif os.path.exists(pdf_file_alt2):
            pdf_file = pdf_file_alt2
    
    if not os.path.exists(pdf_file):
        print(f"错误: 找不到PDF文件")
        print(f"请确保桌面上存在 '高校一流课程建设数据.pdf' 文件")
        sys.exit(1)
    
    # Excel输出文件路径
    excel_file = os.path.join(desktop_path, "高校一流课程建设数据.xlsx")
    
    # 执行转换
    success = pdf_to_excel(pdf_file, excel_file)
    
    if success:
        print("\n转换成功！")
    else:
        print("\n转换失败！")
        sys.exit(1)
