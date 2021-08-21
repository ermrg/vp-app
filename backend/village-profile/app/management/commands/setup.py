from django.core.management import call_command
from django.core.management.base import BaseCommand
from tqdm import tqdm


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating Table, could take upto 5 min'))
        call_command('migrate')
        self.stdout.write(self.style.SUCCESS('Table created successfully'))

        self.stdout.write(self.style.SUCCESS('Running Basic Setup'))
        progress_bar = tqdm(desc="Processing", total=9)
        call_command('loaddata', 'app/fixtures/FiscalYear.json')  # Fiscal Year
        call_command('loaddata', 'app/fixtures/Province.json')  # Province
        call_command('loaddata', 'app/fixtures/District.json')  # District
        call_command('loaddata', 'app/fixtures/Ward.json')  # Ward
        # call_command('loaddata', 'app/fixtures/LocalLevel.json')  # Local Level
        call_command('loaddata', 'app/fixtures/AnimalType.json')  # household_animal Type
        call_command('loaddata', 'app/fixtures/Basti.json')  # Basti
        call_command('loaddata', 'app/fixtures/BusinessType.json')  # Business Type
        call_command('loaddata', 'app/fixtures/CookingFuel.json')  # Cooking Fuel
        call_command('loaddata', 'app/fixtures/Country.json')  # Country
        call_command('loaddata', 'app/fixtures/DeathReason.json')  # Death Reason
        call_command('loaddata', 'app/fixtures/DisabilityType.json')  # Disability Type
        call_command('loaddata', 'app/fixtures/Disaster.json')  # Disaster
        call_command('loaddata', 'app/fixtures/EducationLevel.json')  # Education Level
        call_command('loaddata', 'app/fixtures/EducationStatus.json')  # Education Status
        call_command('loaddata', 'app/fixtures/Facility.json')  # Facility
        call_command('loaddata', 'app/fixtures/Festival.json')  # Festival
        call_command('loaddata', 'app/fixtures/ForeignReason.json')  # Foreign Reason
        call_command('loaddata', 'app/fixtures/GarbageManagement.json')  # Garbage Management
        call_command('loaddata', 'app/fixtures/Gender.json')  # Gender
        call_command('loaddata', 'app/fixtures/HouseDamageStatus.json')  # House Damage Status
        call_command('loaddata', 'app/fixtures/HouseType.json')  # House Type
        call_command('loaddata', 'app/fixtures/IncomeSource.json')  # Income Source
        call_command('loaddata', 'app/fixtures/Jaati.json')  # Jaati
        call_command('loaddata', 'app/fixtures/LandType.json')  # Land Type
        call_command('loaddata', 'app/fixtures/LightFuel.json')  # Light Fuel
        call_command('loaddata', 'app/fixtures/MainOccupation.json')  # Main Occupation
        call_command('loaddata', 'app/fixtures/MaritalStatus.json')  # Marital Status
        # call_command('loaddata', 'app/fixtures/Marga.json')  # Marga
        call_command('loaddata', 'app/fixtures/MotherTongue.json')  # Mother Tongue
        call_command('loaddata', 'app/fixtures/Relation.json')  # Relation
        call_command('loaddata', 'app/fixtures/Religion.json')  # Religion
        call_command('loaddata', 'app/fixtures/RoofType.json')  # Roof Type
        call_command('loaddata', 'app/fixtures/SewageType.json')  # Sewage Type
        call_command('loaddata', 'app/fixtures/ToiletType.json')  # Toilet Type
        call_command('loaddata', 'app/fixtures/TechnicalSkill.json')  # Technical Skill
        call_command('loaddata', 'app/fixtures/VaccineName.json')  # Vaccine Names
        call_command('loaddata', 'app/fixtures/VehicleType.json')  # Vehicle Type
        call_command('loaddata', 'app/fixtures/WaterSource.json')  # Water Resource
        progress_bar.update(4)

        self.stdout.write(self.style.SUCCESS('Running User Setup'))
        call_command('loaddata', 'app/fixtures/User.json')  # User
        call_command('loaddata', 'app/fixtures/Group.json')  # Group
        call_command('loaddata', 'app/fixtures/UserGroups.json')  # User Group
        call_command('loaddata', 'app/fixtures/Office.json')  # Office
        call_command('loaddata', 'app/fixtures/UserProfile.json')  # User Profile
        progress_bar.update(5)
        self.stdout.write(self.style.SUCCESS('Data added successfully'))
        progress_bar.close()
