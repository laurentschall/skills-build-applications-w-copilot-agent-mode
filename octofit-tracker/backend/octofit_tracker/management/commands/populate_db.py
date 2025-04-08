from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Add test data
        users = [
            User(username="john_doe", email="john@example.com"),
            User(username="jane_smith", email="jane@example.com"),
        ]
        User.objects.bulk_create(users)

        teams = [
            Team(name="Team Alpha", description="Alpha team description"),
            Team(name="Team Beta", description="Beta team description"),
        ]
        Team.objects.bulk_create(teams)

        activities = [
            Activity(name="Running", description="Running activity"),
            Activity(name="Cycling", description="Cycling activity"),
        ]
        Activity.objects.bulk_create(activities)

        leaderboard = [
            Leaderboard(user=users[0], team=teams[0], points=100),
            Leaderboard(user=users[1], team=teams[1], points=150),
        ]
        Leaderboard.objects.bulk_create(leaderboard)

        workouts = [
            Workout(user=users[0], activity=activities[0], duration=30),
            Workout(user=users[1], activity=activities[1], duration=45),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Test data successfully populated!'))
