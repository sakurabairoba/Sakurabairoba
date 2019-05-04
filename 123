class Socialusers(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    # Field name made lowercase.
    chinesename = models.CharField(db_column='chineseName', max_length=64, blank=True, null=True)  
    email = models.CharField(max_length=64, blank=True, null=True)
    # Field name made lowercase.
    qq = models.CharField(db_column='QQ', max_length=15, blank=True, null=True)  
    weibo = models.CharField(max_length=300, blank=True, null=True)
    identity_number = models.CharField(max_length=25, blank=True, null=True)
    cell_phone = models.CharField(max_length=20, blank=True, null=True)
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    college = models.CharField(max_length=60, blank=True, null=True)
    living_place = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'SocialUsers'
