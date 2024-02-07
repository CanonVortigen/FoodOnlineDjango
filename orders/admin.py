from django.contrib import admin
from . models import Payment, Order, OrderedFood

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'transaction_id', 'payment_method', 'amount', 'status', 'created_at']

class OrderedFoodInline(admin.TabularInline):
    model = OrderedFood
    readonly_fields = ('order', 'payment', 'user', 'fooditem', 'quantity', 'price', 'amount')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment', 'order_number', 'name', 'phone', 'email', 'country', 'state', 'city', 'total', 'payment_method', 'status', 'order_placed_to', 'is_ordered']
    inlines = [OrderedFoodInline]

class OrderedFoodAdmin(admin.ModelAdmin):
    list_display = ['order', 'payment', 'user', 'fooditem', 'quantity', 'price', 'amount']

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedFood, OrderedFoodAdmin)
