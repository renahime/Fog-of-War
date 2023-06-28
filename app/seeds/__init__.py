from flask.cli import AppGroup
from .users import seed_users, undo_users
from .category import seed_category, undo_category
from .anime_threads import seed_threads, undo_thread
from .anime_posts import seed_posts, undo_posts
from .lit_posts import seed_lit_posts, undo_lit_posts
from .lit_threads import seed_lit_threads, undo_lit_thread
from .higu_seeds import seed_higu_threads, undo_higu_thread
from .higu_posts import seed_higu_posts, undo_higu_posts
from .monster_threads import seed_monster_threads, undo_monster_thread
from .monster_posts import seed_monster_posts, undo_monster_posts
from .boys_threads import seed_boys_threads
from .boys_posts import seed_boys_posts
from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_posts()
        undo_lit_posts()
        undo_lit_thread()
        undo_thread()
        undo_category()

    seed_users()
    seed_category()
    seed_threads()
    seed_posts()
    seed_lit_threads()
    seed_lit_posts()
    seed_higu_threads()
    seed_higu_posts()
    seed_monster_threads()
    seed_monster_posts()
    seed_boys_threads()
    seed_boys_posts()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_posts()
    undo_lit_posts()
    undo_thread()
    undo_lit_thread()
    undo_category()
    # Add other undo functions here
