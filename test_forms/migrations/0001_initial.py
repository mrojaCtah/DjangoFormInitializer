# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-18 04:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('customer_pk', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=140, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspection_date', models.DateField(default=datetime.date.today)),
                ('inspection_time', models.TimeField(default=datetime.time(23, 27, 32, 645701))),
                ('slug', models.SlugField(max_length=140, unique=True)),
                ('customer_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.CustomerAddress')),
            ],
        ),
        migrations.CreateModel(
            name='Section1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=10000)),
                ('property_address', models.CharField(max_length=10000)),
                ('property_description', models.CharField(max_length=10000)),
                ('property_representative', models.CharField(max_length=10000)),
                ('pr_address', models.CharField(max_length=10000)),
                ('pr_phone', models.CharField(max_length=10)),
                ('pr_fax', models.CharField(max_length=10)),
                ('pr_email', models.EmailField(max_length=254)),
                ('authority_with_jurisdiction', models.CharField(max_length=10000)),
                ('aj_phone', models.CharField(max_length=10)),
                ('aj_fax', models.CharField(max_length=10)),
                ('aj_email', models.EmailField(max_length=254)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section10_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspector_signature', models.CharField(max_length=255)),
                ('inspector_name', models.CharField(max_length=255)),
                ('inspector_organization', models.CharField(max_length=255)),
                ('inspector_title', models.CharField(max_length=255)),
                ('inspector_phone', models.CharField(max_length=10)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section10_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_signature', models.CharField(max_length=255)),
                ('owner_name', models.CharField(max_length=255)),
                ('owner_date', models.DateField(auto_now_add=True)),
                ('owner_organization', models.CharField(max_length=255)),
                ('owner_title', models.CharField(max_length=255)),
                ('owner_phone', models.CharField(max_length=10)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_test_service', models.CharField(max_length=10000)),
                ('ots_address', models.CharField(max_length=10000)),
                ('ots_phone', models.CharField(max_length=10)),
                ('ots_fax', models.CharField(max_length=10)),
                ('ots_email', models.EmailField(max_length=254)),
                ('service_technician', models.CharField(max_length=10000)),
                ('test_frequency', models.CharField(max_length=250)),
                ('monitor_org', models.CharField(max_length=10000)),
                ('mo_address', models.CharField(max_length=10000)),
                ('mo_phone', models.CharField(max_length=10)),
                ('mo_fax', models.CharField(max_length=10)),
                ('mo_email', models.EmailField(max_length=254)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fas_nonvoice', models.BooleanField(default=False)),
                ('evacs', models.BooleanField(default=False)),
                ('mns', models.BooleanField(default=False)),
                ('system_combo', models.BooleanField(default=False)),
                ('fas_nonvoice_combo', models.BooleanField(default=False)),
                ('evacs_combo', models.BooleanField(default=False)),
                ('mns_combo', models.BooleanField(default=False)),
                ('two_way_combo', models.BooleanField(default=False)),
                ('other', models.BooleanField(default=False)),
                ('specify', models.CharField(blank=True, max_length=10000, null=True)),
                ('manufacturer', models.CharField(max_length=255)),
                ('model_number', models.CharField(max_length=255)),
                ('sys_docs', models.BooleanField(default=False)),
                ('sys_docs_location', models.CharField(blank=True, max_length=500, null=True)),
                ('site_specific_software', models.BooleanField(default=False)),
                ('revision_number', models.CharField(blank=True, max_length=255, null=True)),
                ('last_update', models.DateField(blank=True, default=None, null=True)),
                ('site_software_copy', models.BooleanField(default=False)),
                ('copy_location', models.CharField(blank=True, max_length=10000, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section4_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp_input_voltage', models.FloatField(max_length=255)),
                ('cp_amps', models.FloatField(max_length=255)),
                ('generator', models.BooleanField(default=False)),
                ('generator_location', models.CharField(blank=True, max_length=10000, null=True)),
                ('generator_fuel_location', models.CharField(blank=True, max_length=500, null=True)),
                ('generator_fuel_type', models.CharField(blank=True, max_length=255, null=True)),
                ('ups', models.BooleanField(default=False)),
                ('ups_powered_equipment', models.CharField(blank=True, max_length=10000, null=True)),
                ('ups_location', models.CharField(blank=True, max_length=10000, null=True)),
                ('ups_battery_standby', models.FloatField(blank=True, max_length=255, null=True)),
                ('ups_battery_alarm', models.FloatField(blank=True, max_length=255, null=True)),
                ('battery_location', models.CharField(max_length=100)),
                ('battery_type', models.CharField(max_length=100)),
                ('battery_voltage', models.FloatField(max_length=100)),
                ('battery_amp_hour', models.CharField(max_length=100)),
                ('battery_standby', models.FloatField(max_length=100)),
                ('battery_alarm', models.FloatField(max_length=100)),
                ('battery_mark', models.BooleanField(default=False)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section4_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power_extender_panels', models.BooleanField(default=False)),
                ('pep_voltage', models.FloatField(blank=True, max_length=255, null=True)),
                ('pep_amps', models.FloatField(blank=True, max_length=255, null=True)),
                ('generator', models.BooleanField(default=False)),
                ('generator_location', models.CharField(blank=True, max_length=10000, null=True)),
                ('generator_fuel_location', models.CharField(blank=True, max_length=500, null=True)),
                ('generator_fuel_type', models.CharField(blank=True, max_length=255, null=True)),
                ('ups', models.BooleanField(default=False)),
                ('ups_powered_equipment', models.CharField(blank=True, max_length=10000, null=True)),
                ('ups_location', models.CharField(blank=True, max_length=10000, null=True)),
                ('ups_battery_standby', models.FloatField(blank=True, max_length=255, null=True)),
                ('ups_battery_alarm', models.FloatField(blank=True, max_length=255, null=True)),
                ('battery_location', models.CharField(max_length=100)),
                ('battery_type', models.CharField(max_length=100)),
                ('battery_voltage', models.FloatField(max_length=100)),
                ('battery_amp_hour', models.CharField(max_length=100)),
                ('battery_standby', models.FloatField(max_length=100)),
                ('battery_alarm', models.FloatField(max_length=100)),
                ('battery_mark', models.BooleanField(default=False)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anunciators', models.BooleanField(default=False)),
                ('anunciator1', models.CharField(blank=True, max_length=10000, null=True)),
                ('anunciator2', models.CharField(blank=True, max_length=10000, null=True)),
                ('anunciator3', models.CharField(blank=True, max_length=10000, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitor_contact', models.CharField(blank=True, max_length=10000, null=True)),
                ('monitor_time', models.CharField(blank=True, max_length=10000, null=True)),
                ('management_contact', models.CharField(blank=True, max_length=10000, null=True)),
                ('management_time', models.CharField(blank=True, max_length=10000, null=True)),
                ('occupant_contact', models.CharField(blank=True, max_length=10000, null=True)),
                ('occupant_time', models.CharField(blank=True, max_length=10000, null=True)),
                ('authority_contact', models.CharField(blank=True, max_length=10000, null=True)),
                ('authority_time', models.CharField(blank=True, max_length=10000, null=True)),
                ('other_contact', models.CharField(blank=True, max_length=10000, null=True)),
                ('other_time', models.CharField(blank=True, max_length=10000, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section7_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cu_vi', models.BooleanField(default=False)),
                ('cu_ft', models.BooleanField(default=False)),
                ('cu_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('lighting_vi', models.BooleanField(default=False)),
                ('lighting_ft', models.BooleanField(default=False)),
                ('lighting_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('fuse_vi', models.BooleanField(default=False)),
                ('fuse_ft', models.BooleanField(default=False)),
                ('fuse_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('trouble_signal_vi', models.BooleanField(default=False)),
                ('trouble_signal_ft', models.BooleanField(default=False)),
                ('trouble_signal_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('disconnect_switches_vi', models.BooleanField(default=False)),
                ('disconnect_switches_ft', models.BooleanField(default=False)),
                ('disconnect_switches_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('gf_monitoring_vi', models.BooleanField(default=False)),
                ('gf_monitoring_ft', models.BooleanField(default=False)),
                ('gf_monitoring_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('supervision_vi', models.BooleanField(default=False)),
                ('supervision_ft', models.BooleanField(default=False)),
                ('supervision_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('local_annunciator_vi', models.BooleanField(default=False)),
                ('local_annunciator_ft', models.BooleanField(default=False)),
                ('local_annunciator_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('remote_annunciator_vi', models.BooleanField(default=False)),
                ('remote_annunciator_ft', models.BooleanField(default=False)),
                ('remote_annunciator_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('pep_vi', models.BooleanField(default=False)),
                ('pep_ft', models.BooleanField(default=False)),
                ('pep_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('iso_mods_vi', models.BooleanField(default=False)),
                ('iso_mods_ft', models.BooleanField(default=False)),
                ('iso_mod_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('other_vi', models.BooleanField(default=False)),
                ('other_ft', models.BooleanField(default=False)),
                ('other_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section7_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volt_120_vi', models.BooleanField(default=False)),
                ('volt_120_ft', models.BooleanField(default=False)),
                ('volt_120_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('generator_ups_vi', models.BooleanField(default=False)),
                ('generator_ups_ft', models.BooleanField(default=False)),
                ('generatorcomments', models.CharField(blank=True, max_length=10000, null=True)),
                ('battery_condition_vi', models.BooleanField(default=False)),
                ('battery_condition_ft', models.BooleanField(default=False)),
                ('battery_condition_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('load_voltage_vi', models.BooleanField(default=False)),
                ('load_voltage_ft', models.BooleanField(default=False)),
                ('load_voltage_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('discharge_vi', models.BooleanField(default=False)),
                ('discharge_ft', models.BooleanField(default=False)),
                ('discharge_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('charger_vi', models.BooleanField(default=False)),
                ('charger_ft', models.BooleanField(default=False)),
                ('charger_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('other_vi', models.BooleanField(default=False)),
                ('other_ft', models.BooleanField(default=False)),
                ('other_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section7_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('light_vi', models.BooleanField(default=False)),
                ('light_ft', models.BooleanField(default=False)),
                ('light_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('fuse_vi', models.BooleanField(default=False)),
                ('fuse_ft', models.BooleanField(default=False)),
                ('fuse_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('primary_power_vi', models.BooleanField(default=False)),
                ('primary_power_ft', models.BooleanField(default=False)),
                ('primary_power_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('secondary_power_vi', models.BooleanField(default=False)),
                ('secondary_power_ft', models.BooleanField(default=False)),
                ('secondary_power_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('trouble_signals_vi', models.BooleanField(default=False)),
                ('trouble_signals_ft', models.BooleanField(default=False)),
                ('trouble_signals_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('gf_monitoring_vi', models.BooleanField(default=False)),
                ('gf_monitoring_ft', models.BooleanField(default=False)),
                ('gf_monitoring_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('panel_super_vi', models.BooleanField(default=False)),
                ('panel_super_ft', models.BooleanField(default=False)),
                ('panel_super_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('other_vi', models.BooleanField(default=False)),
                ('other_ft', models.BooleanField(default=False)),
                ('other_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section7_4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('femds_vi', models.BooleanField(default=False)),
                ('femds_ft', models.BooleanField(default=False)),
                ('femds_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('cmds_vi', models.BooleanField(default=False)),
                ('cmds_ft', models.BooleanField(default=False)),
                ('cmds_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('combo_fs_vi', models.BooleanField(default=False)),
                ('combo_fs_ft', models.BooleanField(default=False)),
                ('combo_fs_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('other_vi', models.BooleanField(default=False)),
                ('other_ft', models.BooleanField(default=False)),
                ('other_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section7_5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shs_1_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('shs_1_vi', models.BooleanField(default=False)),
                ('shs_1_ft', models.BooleanField(default=False)),
                ('shs_1_comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('shs_2_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('shs_2_vi', models.BooleanField(default=False)),
                ('shs_2_ft', models.BooleanField(default=False)),
                ('shs_2_comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('shs_3_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('shs_3_vi', models.BooleanField(default=False)),
                ('shs_3_ft', models.BooleanField(default=False)),
                ('shs_3_comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section7_6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generator_vi', models.BooleanField(default=False)),
                ('generator_ft', models.BooleanField(default=False)),
                ('generator_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('fire_pump_vi', models.BooleanField(default=False)),
                ('fire_pump_ft', models.BooleanField(default=False)),
                ('fire_pump_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('sus_vi', models.BooleanField(default=False)),
                ('sus_ft', models.BooleanField(default=False)),
                ('sus_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('other_vi', models.BooleanField(default=False)),
                ('other_ft', models.BooleanField(default=False)),
                ('other_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section7_7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door_releasing_devices_vi', models.BooleanField(default=False)),
                ('door_releasing_devices_ft', models.BooleanField(default=False)),
                ('door_releasing_devices_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('fan_shutdown_vi', models.BooleanField(default=False)),
                ('fan_shutdown_ft', models.BooleanField(default=False)),
                ('fan_shutdown_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('smoke_control_vi', models.BooleanField(default=False)),
                ('smoke_control_ft', models.BooleanField(default=False)),
                ('smoke_control_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('smoke_damper_vi', models.BooleanField(default=False)),
                ('smoke_damper_ft', models.BooleanField(default=False)),
                ('smoke_damper_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('smoke_shutter_vi', models.BooleanField(default=False)),
                ('smoke_shutter_ft', models.BooleanField(default=False)),
                ('smoke_shutter_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('door_unlocking_vi', models.BooleanField(default=False)),
                ('door_unlocking_ft', models.BooleanField(default=False)),
                ('door_unlocking_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('elevator_recall_vi', models.BooleanField(default=False)),
                ('elevator_recall_ft', models.BooleanField(default=False)),
                ('elevator_recall_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('elevator_shunt_trip_vi', models.BooleanField(default=False)),
                ('elevator_shunt_trip_ft', models.BooleanField(default=False)),
                ('elevator_shunt_trip_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('other_vi', models.BooleanField(default=False)),
                ('other_ft', models.BooleanField(default=False)),
                ('other_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section7_8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(max_length=100)),
                ('device_address', models.CharField(max_length=100)),
                ('device_inspection_type', models.CharField(choices=[('V', 'Visual Inspection'), ('F', 'Functional Test')], max_length=1)),
                ('device_inspection_cycle', models.CharField(max_length=5)),
                ('device_location', models.CharField(max_length=1000)),
                ('device_test_results', models.CharField(max_length=255)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section7_9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarm_signal_vi', models.BooleanField(default=False)),
                ('alarm_signal_ft', models.BooleanField(default=False)),
                ('alarm_signal_time', models.FloatField(blank=True, max_length=30, null=True)),
                ('alarm_signal_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('alarm_restoration_vi', models.BooleanField(default=False)),
                ('alarm_restoration_ft', models.BooleanField(default=False)),
                ('alarm_restoration_time', models.FloatField(blank=True, max_length=30, null=True)),
                ('alarm_restoration_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('trouble_signal_vi', models.BooleanField(default=False)),
                ('trouble_signal_ft', models.BooleanField(default=False)),
                ('trouble_signal_time', models.FloatField(blank=True, max_length=30, null=True)),
                ('trouble_signal_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('trouble_restoration_vi', models.BooleanField(default=False)),
                ('trouble_restoration_ft', models.BooleanField(default=False)),
                ('trouble_restoration_time', models.FloatField(blank=True, max_length=30, null=True)),
                ('trouble_restoration_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('supervisory_signal_vi', models.BooleanField(default=False)),
                ('supervisory_signal_ft', models.BooleanField(default=False)),
                ('supervisory_signal_time', models.FloatField(blank=True, max_length=30, null=True)),
                ('supervisory_signal_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('supervisory_restoration_vi', models.BooleanField(default=False)),
                ('supervisory_restoration_ft', models.BooleanField(default=False)),
                ('supervisory_restoration_time', models.FloatField(blank=True, max_length=30, null=True)),
                ('supervisory_restoration_comments', models.CharField(blank=True, max_length=10000, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitor_contact', models.CharField(blank=True, max_length=10000, null=True)),
                ('monitor_time', models.CharField(blank=True, max_length=10000, null=True)),
                ('management_contact', models.CharField(blank=True, max_length=10000, null=True)),
                ('management_time', models.CharField(blank=True, max_length=10000, null=True)),
                ('occupant_contact', models.CharField(blank=True, max_length=10000, null=True)),
                ('occupant_time', models.CharField(blank=True, max_length=10000, null=True)),
                ('authority_contact', models.CharField(blank=True, max_length=10000, null=True)),
                ('authority_time', models.CharField(blank=True, max_length=10000, null=True)),
                ('other_contact', models.CharField(blank=True, max_length=10000, null=True)),
                ('other_time', models.CharField(blank=True, max_length=10000, null=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
        migrations.CreateModel(
            name='Section9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_restore_date', models.DateField(auto_now_add=True)),
                ('system_restore_time', models.TimeField(auto_now_add=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Inspection')),
            ],
        ),
    ]
