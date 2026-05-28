total_revenue = 0
for i in range(7):
    revenue = int(input(f"Nhập doanh thu ngày {i+1}: "))
    total_revenue = total_revenue + revenue
    if revenue >= 5000000:
        day += 1
avg_revenue = total_revenue / 7 

print("--- Báo cáo doanh thu tuần Rikkei Store ---")
print(f"Tổng doanh thu cả tuần: {total_revenue} VND")
print(f"Doanh thu trung bình mỗi ngày: {avg_revenue} VND")
print(f"Số ngày đạt doanh thu mục tiêu (>= 5,000,000 VND): {day} ngày")
