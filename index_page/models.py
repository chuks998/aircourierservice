from django.db import models

package_status = {
    ('pending','pending'),
    ('active', 'active'),
    ('delivered','delivered'),
    ('delayed', 'delayed'),
}

class PackageDetail(models.Model):
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField(max_length=50)
    client_phone = models.CharField(max_length=20)
    delivery_address = models.CharField(max_length=100, help_text='This is the area for the delivery address')
    status = models.CharField(choices=package_status, default=1, max_length=11, help_text='This section shows the client the status of their item')
    tracking_number = models.CharField(max_length=20, help_text='This is the tracking number you give to your client.')
    content = models.TextField(max_length=100, help_text='This is where you the gift(s) for your client.')
    delivery_day = models.CharField(max_length=5, help_text='this data will be displayed as" your package will be deliverd on or before the number you enter here"')
    first_movement = models.CharField(max_length=100, help_text='example; Your item left qater wherehouse', default='example; Your item arrived poland wherehouse')
    second_movement = models.CharField(max_length=100, help_text='example; Your item arrived poland wherehouse', default='example; Your item arrived poland wherehouse')
    third_movement = models.CharField(max_length=100, help_text='example; Your item left lagos wherehouse', default='example; Your item arrived poland wherehouse')
    fourth_movement = models.CharField(max_length=100, help_text='example; Your item arrived spain wherehouse', default='example; Your item arrived poland wherehouse')

def __str__(self):
    return self.tracking_number
