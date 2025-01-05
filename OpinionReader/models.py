from django.db import models


class Combineddata(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=100)  # Field name made lowercase.
    author_name = models.CharField(db_column='Author_Name', max_length=100)  # Field name made lowercase.
    author_id = models.CharField(db_column='Author_Id', max_length=100, blank=True, null=True)  # Field name made lowercase.
    author_type = models.CharField(db_column='Author_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    domain = models.CharField(db_column='Domain', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rank = models.FloatField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=200, blank=True, null=True)  # Field name made lowercase.
    read_count = models.IntegerField(db_column='ReadCount', blank=True, null=True)  # Field name made lowercase.
    like_count = models.IntegerField(db_column='LikeCount', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=200, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    comment_count = models.IntegerField(db_column='CommentCount', blank=True, null=True)  # Field name made lowercase.
    forward_count = models.IntegerField(db_column='ForwardCount', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CombinedData'


class Keywords(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    key_name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'Keywords'


class KeywordsAssociation(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    keyword = models.ForeignKey('Keywords', models.DO_NOTHING)
    data = models.ForeignKey('Combineddata', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'keywords_association'
        unique_together = (('data', 'keyword'),)
