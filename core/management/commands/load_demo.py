import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
import faker

from job.models import Job, Category, Application, Tag, Location, Company


class Command(BaseCommand):
    help = 'Load demo data into database'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of fake data to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = faker.Faker()

        for _ in range(total):
            user_model = get_user_model()
            user = user_model.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                bio=fake.text(),
                user_type=fake.random_element(elements=['Applicant', 'Employeer']),
            )
            user.set_password('12345678')
            user.save()

        self.stdout.write(self.style.SUCCESS('[+] Users created successfully'))

        for _ in range(total):
            Category.objects.create(
                name=fake.job(),
                description=fake.text(),
                slug=fake.slug(),
            )
        
        self.stdout.write(self.style.SUCCESS('[+] Categories created successfully'))

        for _ in range(total):
            users = get_user_model().objects.all()
            Company.objects.create(
                user=users[random.randint(0, len(users) - 1)],
                name=fake.company(),
                description=fake.text(),
                website=fake.url(),
                logo=fake.image_url(),
                slug=fake.slug(),
            )

        self.stdout.write(self.style.SUCCESS('[+] Companies created successfully'))

        for _ in range(total):
            Tag.objects.create(
                name=fake.job(),
                slug=fake.slug(),
            )

        self.stdout.write(self.style.SUCCESS('[+] Tags created successfully'))

        for _ in range(total):
            Location.objects.create(
                name=fake.city(),
                slug=fake.slug(),
            )

        self.stdout.write(self.style.SUCCESS('[+] Locations created successfully'))

        for _ in range(total):
            users = get_user_model().objects.all()
            companies = Company.objects.all()
            tags = Tag.objects.all()
            locations = Location.objects.all()
            categories = Category.objects.all()
            applications = Application.objects.all()
            applicants = Application.objects.all()
            job = Job(
                employer=users[random.randint(0, len(users) - 1)],
                company=companies[random.randint(0, len(companies) - 1)],
                # applicants=applicants.set(users[random.randint(0, len(users) - 1)]),
                # tags=tags[random.randint(0, len(tags) - 1)],

                title=fake.job(),
                description=fake.text(),
                location=locations[random.randint(0, len(locations) - 1)],
                # User .add() to add multiple in many to many fields
                # applications = applications[random.randint(0, len(applications) - 1)],
                # applications=self.job.add(applications[random.randint(0, len(applications) - 1)]),
                views=random.randint(0, 100),
                job_type=fake.random_element(elements=['Full Time', 'Part Time', 'Remote', 'Internship', 'Contract', 'Temporary']),
                category=categories[random.randint(0, len(categories) - 1)],
                vacancy=random.randint(1, 10),
                salary=random.randint(10000, 100000),
                experience=random.randint(0, 10),
                image=fake.image_url(),
                slug=fake.slug(),
                is_published=True,
                is_approved=True,
            )
            job.save()
            # Set the many-to-many fields using .set()
            job.tags.set(tags[random.randint(0, len(tags) - 1)])
            job.applicants.set(applicants[random.randint(0, len(applicants) - 1)])
            # job.save()

        self.stdout.write(self.style.SUCCESS('[+] Jobs created successfully'))


        for _ in range(total):
            jobs = Job.objects.all()
            Application.objects.create(
                applicant=users[random.randint(0, len(users) - 1)],
                status=fake.random_element(elements=['Pending', 'Shortlisted', 'Approved', 'Rejected']),
                message=fake.text(),
            )
        self.stdout.write(self.style.SUCCESS('[+] Applications created successfully'))

        self.stdout.write(self.style.SUCCESS('[+] Data generated successfully'))
    
