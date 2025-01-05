# Generated by Django 4.0.4 on 2023-02-08 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('slug', models.SlugField(null=True)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('diagnosis_date', models.DateField()),
                ('surgery_date', models.DateField()),
                ('histopath_result', models.ImageField(blank=True, null=True, upload_to='')),
                ('gleason_score', models.IntegerField(blank=True, null=True)),
                ('date_of_treatment', models.DateField()),
                ('type_of_treatment', models.CharField(choices=[('Hormonal Treatment', 'Hormonal Treatment'), ('Radiation Therapy', 'Radiation Therapy'), ('Chemotherapy', 'Chemotherapy'), ('Others', 'Others')], max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psa', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('creatinine', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('wbc', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('rbc', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('hemoglobin', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('hematocrit', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('platelet', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('lactate_hydrogenase', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('alkaline_phosphatase', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('sgpt', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('sgot', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bilirubins', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('salivary_gland_status', models.CharField(choices=[('Normal', 'Normal'), ('Left Obstruction', 'Left Obstruction'), ('Right Obstruction', 'Right Obstruction')], max_length=120)),
                ('salivary_gland_image', models.ImageField(blank=True, upload_to='')),
                ('bone_metastasis_status', models.CharField(blank=True, choices=[('Metastasis', 'Metastasis'), ('No Metastasis', 'No Metastasis')], max_length=120, null=True)),
                ('bone_scan_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('renal_scintigraphy', models.ImageField(blank=True, null=True, upload_to='')),
                ('gapsma_choices', models.CharField(blank=True, choices=[('GA-68', 'GA-68'), ('F-18 PSMA', 'F-18 PSMA')], max_length=120, null=True)),
                ('gapsma_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('gapsma_prostate_lesion_status', models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Prostate Lesion Status')),
                ('gapsma_prostate_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Prostate Location')),
                ('gapsma_prostate_suv', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Prostate SUV')),
                ('gapsma_prostate_size', models.IntegerField(blank=True, null=True, verbose_name='Prostate Lesion Size')),
                ('gapsma_lymph_node_lesion_status', models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Lymph Node Lesion Status')),
                ('gapsma_lymph_node_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Lymph Node Location')),
                ('gapsma_lymph_node_suv', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Lymph Node SUV')),
                ('gapsma_lymph_node_size', models.IntegerField(blank=True, null=True, verbose_name='Lymph Node Lesion Size')),
                ('gapsma_bone_lesion_status', models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Bone Lesion Status')),
                ('gapsma_bone_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bone Lesion Location')),
                ('gapsma_bone_suv', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Bone SUV')),
                ('gapsma_bone_size', models.IntegerField(blank=True, null=True, verbose_name='Bone Lesion Size')),
                ('gapsma_brain_lesion_status', models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Brain Lesion Status')),
                ('gapsma_brain_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Brain Lesion Location')),
                ('gapsma_brain_suv', models.DecimalField(blank=True, null=True, verbose_name='Brain SUV')),
                ('gapsma_brain_size', models.IntegerField(blank=True, null=True, verbose_name='Brain Lesion Size')),
                ('gapsma_lung_lesion_status', models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Lung Lesion Status')),
                ('gapsma_lung_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Lung Lesion Location')),
                ('gapsma_lung_suv', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Lung SUV')),
                ('gapsma_lung_size', models.IntegerField(blank=True, null=True, verbose_name='Lung Lesion Size')),
                ('gapsma_liver_lesion_status', models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Liver Lesion Status')),
                ('gapsma_liver_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Liver Lesion Location')),
                ('gapsma_liver_suv', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Liver SUV')),
                ('gapsma_liver_size', models.IntegerField(blank=True, null=True, verbose_name='Liver Lesion Size')),
                ('fdgpetct_img', models.ImageField(blank=True, upload_to='')),
                ('fdgpetct_prostate_lesion_status', models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Prostate Lesion Status')),
                ('fdgpetct_prostate_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Prostate Location')),
                ('fdgpetct_prostate_suv', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Prostate SUV')),
                ('fdgpetct_prostate_size', models.IntegerField(blank=True, null=True, verbose_name='Prostate Lesion Size')),
                ('fdgpetct_lymph_node_lesion_status', models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Lymph Node Lesion Status')),
                ('fdgpetct_lymph_node_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Lymph Node Location')),
                ('fdgpetct_lymph_node_suv', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Lymph Node SUV')),
                ('fdgpetct_lymph_node_size', models.IntegerField(blank=True, null=True, verbose_name='Lymph Node Lesion Size')),
                ('fdgpetct_bone_lesion_status', models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Bone Lesion Status')),
                ('fdgpetct_bone_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bone Lesion Location')),
                ('fdgpetct_bone_suv', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Bone SUV')),
                ('fdgpetct_bone_size', models.IntegerField(blank=True, null=True, verbose_name='Bone Lesion Size')),
                ('fdgpetct_brain_lesion_status', models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Brain Lesion Status')),
                ('fdgpetct_brain_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Brain Lesion Location')),
                ('fdgpetct_brain_suv', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Brain SUV')),
                ('fdgpetct_brain_size', models.IntegerField(blank=True, null=True, verbose_name='Brain Lesion Size')),
                ('fdgpetct_lung_lesion_status', models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Lung Lesion Status')),
                ('fdgpetct_lung_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Lung Lesion Location')),
                ('fdgpetct_lung_suv', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Lung SUV')),
                ('fdgpetct_lung_size', models.IntegerField(blank=True, null=True, verbose_name='Lung Lesion Size')),
                ('fdgpetct_liver_lesion_status', models.CharField(blank=True, choices=[('Absent', 'Absent'), ('Present', 'Present')], max_length=120, null=True, verbose_name='Liver Lesion Status')),
                ('fdgpetct_liver_location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Liver Lesion Location')),
                ('fdgpetct_liver_suv', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Liver SUV')),
                ('fdgpetct_liver_size', models.IntegerField(blank=True, null=True, verbose_name='Liver Lesion Size')),
                ('assessment', models.CharField(blank=True, choices=[('Low Risk', 'Low Risk'), ('Intermediate Risk', 'Intermediate Risk'), ('High Risk', 'High Risk')], max_length=120, null=True)),
                ('plan', models.CharField(blank=True, max_length=120, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part_1.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecog_score', models.IntegerField(blank=True)),
                ('height', models.IntegerField(blank=True)),
                ('weight', models.IntegerField(blank=True)),
                ('bmi', models.IntegerField(blank=True)),
                ('bp', models.CharField(blank=True, max_length=120)),
                ('hr', models.IntegerField(blank=True)),
                ('pain_score', models.IntegerField(blank=True)),
                ('local_symptoms', models.CharField(blank=True, max_length=300)),
                ('systemic_symptoms', models.CharField(blank=True, max_length=300)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='part_1.patient')),
            ],
        ),
    ]
