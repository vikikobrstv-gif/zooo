# === Stage 43: Добавь пагинацию длинных списков ===
# Project: GardenWatch
def paginate(items, page_size=20):
    pages = []
    for i in range(0, len(items), page_size):
        pages.append(items[i:i + page_size])
    return pages

page_index, page_size = 0, 20
print(f"Page {page_index + 1} of {len(paginate(list(range(50)), page_size))}")
for item in paginate(list(range(50)), page_size)[page_index]:
    print(f"  {item}")
