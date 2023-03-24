list1 = [45,100,50,200,100]
total = list1[0]+list1[1]+list1[2]+list1[3]+list1[4]
if total>10000:
    discount=(total*25)/100
    price=total-discount
    print('the discounted total price is %d'%(price))
elif total>5000:
    discount=(total*18)/100
    price=total-discount
    print('the discounted total price is %d'%(price))
elif total>2000:
    discount=(total*12)/100
    price=total-discount
    print('the discounted total price is %d'%(price))
else:
    print('total price is %d'%(total))
