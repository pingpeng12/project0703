import matplotlib.pyplot as plt
import pandas as pd

# 聖誕樹的高度 (可以調整)
height = 10

# 建立聖誕樹的文字列表
tree_lines = []

# 樹冠部分
for i in range(1, height + 1):
    stars = '*' * (2 * i - 1)
    spaces = ' ' * (height - i)
    tree_lines.append(spaces + stars)

# 樹幹部分
trunk_width = 3
trunk_height = 2
for _ in range(trunk_height):
    spaces = ' ' * (height - (trunk_width // 2) - 1)
    tree_lines.append(spaces + '*' * trunk_width)

# 將文字行合併成一個單一字串
christmas_tree_text = "\n".join(tree_lines)

# 使用 Matplotlib 顯示文字
fig, ax = plt.subplots(figsize=(6, height * 0.5)) # 調整圖形大小以適應文字
ax.text(0.5, 0.5, christmas_tree_text,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=10, # 字體大小可以調整
        fontfamily='monospace', # 使用等寬字體，確保星號對齊
        transform=ax.transAxes)

# 隱藏座標軸
ax.axis('off')

# 將圖形輸出到 Power BI
plt.show()