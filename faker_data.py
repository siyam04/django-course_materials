import os, django, random

from faker import Faker
from blog.models import Post
# Configure settings for project
# Need to run this before calling models from application!


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'source.settings')
django.setup()

faker_generating = Faker()
topics = ['Search', 'Social', 'Blog', 'Articles', 'News']


def add_topic():
    t = Post.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    """Create n Entries of Dates Accessed"""
    for entry in range(n):
        # Get Topic for Entry
        top = add_topic()
        # Create Fake Data for entry
        f_title = faker_generating.title()
        f_details = faker_generating.details()
        f_author = faker_generating.author()
        # Create Fake Access Record for that page
        data = Post.objects.get_or_create(topic=top, title=f_title, details=f_details, author=f_author)


if __name__ == '__main__':
    print("Populating the database...Please Wait")
    populate(20)
    print('Populating Complete!')