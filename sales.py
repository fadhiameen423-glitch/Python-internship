x=0
sales=[1200,1500,900,1800,2200,1700,1300]
total_sales=sum(sales)
highest_sales=max(sales)
lowest_sales=min(sales)
average_sales=(total_sales)/len(sales)
for i in sales:
    if i>1500:
        x+=1
print("Total sales: " + str(total_sales))
print("Average sales: " + str(average_sales))
print("Highest sales: " + str(highest_sales))
print("Lowest sales: " + str(lowest_sales))
print("Number of days with sales above 1500: " + str(x))