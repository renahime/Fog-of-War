"""empty message

Revision ID: 1500b7ee8209
Revises: 
Create Date: 2023-06-22 09:04:42.573005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1500b7ee8209'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('about', sa.String(length=500), nullable=True),
    sa.Column('signature', sa.Text(), nullable=True),
    sa.Column('profile_image', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('subcategories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('categoryId', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['categoryId'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('threads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=255), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=255), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('thread_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['thread_id'], ['threads.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('thread_categories',
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('thread_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['thread_id'], ['threads.id'], )
    )
    op.create_table('thread_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('threadId', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['threadId'], ['threads.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('thread_sub_categories',
    sa.Column('sub_category_id', sa.Integer(), nullable=True),
    sa.Column('thread_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sub_category_id'], ['subcategories.id'], ),
    sa.ForeignKeyConstraint(['thread_id'], ['threads.id'], )
    )
    op.create_table('post_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('postId', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['postId'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reply',
    sa.Column('replyer', sa.Integer(), nullable=False),
    sa.Column('replied', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['replied'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['replyer'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('replyer', 'replied')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reply')
    op.drop_table('post_images')
    op.drop_table('thread_sub_categories')
    op.drop_table('thread_images')
    op.drop_table('thread_categories')
    op.drop_table('posts')
    op.drop_table('threads')
    op.drop_table('subcategories')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###