import pandas as pd

# 엑셀 파일 읽기 (4번째 시트만 읽기)
file_path = 'material_process.xlsx'
df = pd.read_excel(file_path, sheet_name=3, header=None)  # 0부터 시작하는 인덱스, 세 번째 시트를 의미

# 필요한 열만 선택 (3번째, 4번째, 6번째, 8번째 열)
selected_columns = [2, 3, 5, 7]  # 0부터 시작하는 인덱스
df_selected = df.iloc[3:, selected_columns]

# 열 이름 설정
column_names = ['Material', 'LCA_Process', 'Unit', 'Result']
df_selected.columns = column_names

# 새로운 엑셀 파일로 저장
output_file_path = 'filtered_data.xlsx'
df_selected.to_excel(output_file_path, index=False)
