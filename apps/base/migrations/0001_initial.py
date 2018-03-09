# Generated by Django 2.0.2 on 2018-03-09 03:54

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(blank=True, max_length=6, verbose_name='姓名')),
                ('mobile', models.CharField(blank=True, max_length=11, verbose_name='手机号码')),
                ('gender', models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], max_length=6, verbose_name='性别')),
                ('avatar', models.ImageField(blank=True, default='avatar/default.jpg', null=True, upload_to='avatar', verbose_name='头像')),
                ('experience', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='经验')),
                ('score', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='积分')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=256, verbose_name='名称')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='base.Area', verbose_name='上级区域')),
            ],
            options={
                'verbose_name': '区域',
                'verbose_name_plural': '区域',
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=256, verbose_name='名称')),
                ('address', models.CharField(blank=True, max_length=128, verbose_name='地址')),
                ('tel', models.CharField(blank=True, max_length=32, verbose_name='联系电话')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='base.Department', verbose_name='上级部门')),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门',
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=256, verbose_name='名称')),
                ('hx_group_id', models.CharField(blank=True, editable=False, max_length=128, verbose_name='环信聊天群组id')),
            ],
            options={
                'verbose_name': '团队',
                'verbose_name_plural': '团队',
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='名称')),
                ('address', models.CharField(blank=True, max_length=256, verbose_name='地址')),
                ('tel', models.CharField(blank=True, max_length=32, verbose_name='联系电话')),
                ('users_limit', models.PositiveIntegerField(blank=True, default=100, null=True, verbose_name='用户数限制')),
                ('is_supertenant', models.BooleanField(default=False, verbose_name='是否超级租户')),
            ],
            options={
                'verbose_name': '租户',
                'verbose_name_plural': '租户',
                'db_table': 'tenant',
            },
        ),
        migrations.CreateModel(
            name='UserTeamRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Team')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Tenant', verbose_name='所属租户')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户团队关系',
                'verbose_name_plural': '用户团队关系',
                'db_table': 'user_team_relation',
            },
        ),
        migrations.AddField(
            model_name='team',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Tenant', verbose_name='所属租户'),
        ),
        migrations.AddField(
            model_name='department',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Tenant', verbose_name='所属租户'),
        ),
        migrations.AddField(
            model_name='area',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Tenant', verbose_name='所属租户'),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='base.Department', verbose_name='所属部门'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='teams',
            field=models.ManyToManyField(blank=True, related_name='users', through='base.UserTeamRelation', to='base.Team', verbose_name='团队'),
        ),
        migrations.AddField(
            model_name='user',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Tenant', verbose_name='所属租户'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='userteamrelation',
            unique_together={('user', 'team')},
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together={('parent', 'name'), ('tenant', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='area',
            unique_together={('parent', 'name'), ('tenant', 'name')},
        ),
    ]
