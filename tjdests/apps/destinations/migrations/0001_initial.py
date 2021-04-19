# Generated by Django 3.2 on 2021-04-19 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceeb_code', models.PositiveSmallIntegerField(verbose_name='CEEB Code')),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TestScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(choices=[('ACT_ENGL', 'ACT English (Grammar)'), ('ACT_MATH', 'ACT Math'), ('ACT_READ', 'ACT Reading'), ('ACT_SCI', 'ACT Science'), ('ACT_COMP', 'ACT Composite'), ('SAT_EBRW', 'SAT Verbal'), ('SAT_MATH', 'SAT Math'), ('SAT_TOTAL', 'SAT Total'), ('SAT2_MATH1', 'SAT Subject Test Math 1'), ('SAT2_MATH2', 'SAT Subject Test Math 2'), ('SAT2_BIO', 'SAT Subject Test Biology'), ('SAT2_CHEM', 'SAT Subject Test Chemistry'), ('SAT2_PHYS', 'SAT Subject Test Physics'), ('SAT2_ENGL', 'SAT Subject Test English'), ('SAT2_USH', 'SAT Subject Test U.S. History'), ('SAT2_WH', 'SAT Subject Test World History'), ('SAT2_ES', 'SAT Subject Test Spanish'), ('SAT2_ESL', 'SAT Subject Test Spanish with Listening'), ('SAT2_FR', 'SAT Subject Test French'), ('SAT2_FRL', 'SAT Subject Test French with Listening'), ('SAT2_ZHL', 'SAT Subject Test Chinese with Listening'), ('SAT2_IT', 'SAT Subject Test Italian'), ('SAT2_DE', 'SAT Subject Test German'), ('SAT2_DEL', 'SAT Subject Test German with Listening'), ('SAT2_HE', 'SAT Subject Test Modern Hebrew'), ('SAT2_LA', 'SAT Subject Test Latin'), ('SAT2_JAL', 'SAT Subject Test Japanese with Listening'), ('SAT2_KOL', 'SAT Subject Test Korean with Listening'), ('AP_RSRCH', 'AP Research'), ('AP_SMNR', 'AP Seminar'), ('AP_ART2D', 'AP Art and Design: 2-D Design'), ('AP_ART3D', 'AP Art and Design: 3-D Design'), ('AP_ARTDRAW', 'AP Art and Design: Drawing'), ('AP_ARTHIST', 'AP Art History'), ('AP_BIO', 'AP Biology'), ('AP_CALCAB', 'AP Calculus AB'), ('AP_CALCBC', 'AP Calculus BC'), ('AP_CHEM', 'AP Chemistry'), ('AP_ZHLANG', 'AP Chinese Language and Culture'), ('AP_CSA', 'AP Computer Science A'), ('AP_CSP', 'AP Computer Science Principles'), ('AP_ENLANG', 'AP English Language and Composition'), ('AP_ENLIT', 'AP English Literature and Composition'), ('AP_ENVSCI', 'AP Environmental Science'), ('AP_EUROHIST', 'AP European History'), ('AP_FRLANG', 'AP French Language and Culture'), ('AP_DELANG', 'AP German Language and Culture'), ('AP_GOVCOMP', 'AP Comparative Government and Politics'), ('AP_GOVUS', 'AP U.S. Government and Politics'), ('AP_HUG', 'AP Human Geography'), ('AP_ITLANG', 'AP Italian Language and Culture'), ('AP_JALANG', 'AP Japanese Language and Culture'), ('AP_LATIN', 'AP Latin'), ('AP_MACRO', 'AP Macroeconomics'), ('AP_MICRO', 'AP Microeconomics'), ('AP_MUSTHRY', 'AP Music Theory'), ('AP_PHYSICS1', 'AP Physics 1: Algebra-Based'), ('AP_PHYSICS2', 'AP Physics 2: Algebra-Based'), ('AP_PHYSICSCEM', 'AP Physics C: Electricity and Magnetism'), ('AP_PHYSICSCM', 'AP Physics C: Mechanics'), ('AP_PSYCH', 'AP Psychology'), ('AP_ESLANG', 'AP Spanish Language and Culture'), ('AP_ESLIT', 'AP Spanish Literature and Culture'), ('AP_STAT', 'AP Statistics'), ('AP_USH', 'AP US History'), ('AP_WHM', 'AP World History: Modern')], max_length=20)),
                ('exam_score', models.PositiveSmallIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Decision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decision_type', models.CharField(choices=[('ED', 'Early Decision'), ('ED2', 'Early Decision 2'), ('EA', 'Early Action'), ('EA2', 'Early Action 2'), ('RD', 'Regular Decision'), ('RL', 'Rolling')], max_length=20, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.college')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
