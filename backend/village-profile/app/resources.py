from django.forms import forms
from import_export import resources, fields

from app.models.vp.house_detail import HouseDetail
from app.models.vp.household import Household
from app.models.vp.household_animal import HouseholdAnimal
from app.models.vp.household_business import HouseholdBusiness
# from app.models.vp.household_child_labor import HouseholdHelper
from app.models.vp.household_helper import HouseholdHelper
from app.models.vp.household_expenses import HouseholdExpenses
from app.models.vp.household_facility import HouseholdFacility
from app.models.vp.household_festival import HouseholdFestival
from app.models.vp.household_income import HouseholdIncome
from app.models.vp.household_infrastructure import HouseholdInfrastructure
from app.models.vp.household_land import HouseholdLand
from app.models.vp.household_vehicle import HouseholdVehicle
from app.models.vp.member import Member
from app.models.vp.member_deceased import MemberDeceased
from app.models.vp.rent_member import RentMember
from app.xls import ExcelDateWidget, ExcelDataset


class HouseholdResource(resources.ModelResource):
    hoh_name = fields.Field(attribute='hoh_name', column_name='hoh_name', widget=ExcelDataset())
    # birth_date = fields.Field(attribute='birth_date', column_name='birth_date', widget=ExcelDateWidget())

    class Meta:
        model = Household


class HouseheadResource(resources.ModelResource):
    name_eng = fields.Field(attribute='name_eng', column_name='name_eng', widget=ExcelDataset())
    # dob_bs = fields.Field(attribute='dob_bs', column_name='dob_bs')

    class Meta:
        model = Member
        # fields = ('name_eng', 'gender', 'dob_bs', 'education_status_id', 'main_occupation_id','citizenship_num', 'id')


class MemberResource(resources.ModelResource):
    # name_eng = fields.Field(attribute='name_eng', column_name='name_eng', widget=ExcelDataset())
    dob_bs = fields.Field(attribute='dob_bs', column_name='dob_bs', widget=ExcelDateWidget())

    class Meta:
        model = Member


class DeceasedResource(resources.ModelResource):
    name_eng = fields.Field(attribute='name', column_name='name', widget=ExcelDataset())
    dob_bs = fields.Field(attribute='dob', column_name='dob', widget=ExcelDateWidget())

    class Meta:
        model = MemberDeceased


class HouseDetailsResource(resources.ModelResource):
    house_type = fields.Field(attribute='house_type', column_name='house_type', widget=ExcelDataset())
    map_pass_date_bs = fields.Field(attribute='map_pass_date_bs', column_name='map_pass_date_bs', widget=ExcelDateWidget())

    class Meta:
        model = HouseDetail


class RentMemberResource(resources.ModelResource):
    rent_member_head = fields.Field(attribute='rent_member_head', column_name='khadadevi-rent_member-rent_member_owner_name', widget=ExcelDataset())
    no_of_member = fields.Field(attribute='migrated_from', column_name='khadadevi-rent_member-rent_member_room_count', widget=ExcelDataset())
    room_no = fields.Field(attribute='migrated_from', column_name='khadadevi-rent_member-rent_member_member_count', widget=ExcelDataset())
    migrated_from = fields.Field(attribute='migrated_from', column_name='khadadevi-rent_member-rent_member_from_place', widget=ExcelDataset())
    reason_for_migration = fields.Field(attribute='migrated_from', column_name='khadadevi-rent_member-rent_member_reason', widget=ExcelDataset())
    # dob_bs = fields.Field(attribute='dob_bs', column_name='dob_bs', widget=ExcelDateWidget())

    class Meta:
        model = RentMember


class LandResource(resources.ModelResource):
    land_type = fields.Field(attribute='land_type', column_name='land_type', widget=ExcelDataset())
    dob_bs = fields.Field(attribute='dob_bs', column_name='dob_bs', widget=ExcelDateWidget())

    class Meta:
        model = HouseholdLand


class AnimalResource(resources.ModelResource):
    animal_type = fields.Field(attribute='animal_type', column_name='animal_type', widget=ExcelDataset())
    dob_bs = fields.Field(attribute='dob_bs', column_name='dob_bs', widget=ExcelDateWidget())

    class Meta:
        model = HouseholdAnimal


class BusinessTypesResource(resources.ModelResource):
    business_type = fields.Field(attribute='business_type', column_name='business_type', widget=ExcelDataset())
    dob_bs = fields.Field(attribute='dob_bs', column_name='dob_bs', widget=ExcelDateWidget())

    class Meta:
        model = HouseholdBusiness


class FestivalResource(resources.ModelResource):
    festival = fields.Field(attribute='festival', column_name='festival', widget=ExcelDataset())
    dob_bs = fields.Field(attribute='dob_bs', column_name='dob_bs', widget=ExcelDateWidget())

    class Meta:
        model = HouseholdFestival


class ChildLabourResource(resources.ModelResource):
    child_name = fields.Field(attribute='child_name', column_name='khadadevi-hhis_childlabour-childlabour_name', widget=ExcelDataset())
    age = fields.Field(attribute='age', column_name='khadadevi-hhis_childlabour-childlabour_age', widget=ExcelDataset())
    gender = fields.Field(attribute='gender', column_name='khadadevi-hhis_childlabour-childlabour_sex', widget=ExcelDataset())
    remarks = fields.Field(attribute='remarks', column_name='khadadevi-hhis_childlabour-childlabour_remarks', widget=ExcelDataset())
    status = fields.Field(attribute='status', column_name='khadadevi-hhis_childlabour-childlabour_status', widget=ExcelDataset())
    start_date_bs = fields.Field(attribute='start_date_bs', column_name='khadadevi-hhis_childlabour-childlabour_fromdategrp-childlabour_fromdate_day', widget=ExcelDataset())

    class Meta:
        model = HouseholdHelper


class IncomeResource(resources.ModelResource):
    source = fields.Field(attribute='source', column_name='source', widget=ExcelDataset())
    dob_bs = fields.Field(attribute='dob_bs', column_name='dob_bs', widget=ExcelDateWidget())

    class Meta:
        model = HouseholdIncome


class ExpensesResource(resources.ModelResource):
    food_expenses = fields.Field(attribute='food_expenses', column_name='food_expenses', widget=ExcelDataset())
    health_expenses = fields.Field(attribute='health_expenses', column_name='health_expenses', widget=ExcelDataset())
    education_expenses = fields.Field(attribute='education_expenses', column_name='education_expenses', widget=ExcelDataset())
    dob_bs = fields.Field(attribute='dob_bs', column_name='dob_bs', widget=ExcelDateWidget())

    class Meta:
        model = HouseholdExpenses


class VehicleResource(resources.ModelResource):

    vehicle_type_id = fields.Field(attribute='vehicle_type_id', column_name='khadadevi-hhis_vehicles-vehicles_type_id', widget=ExcelDataset())
    count = fields.Field(attribute='count', column_name='khadadevi-hhis_vehicles-vehicles_count', widget=ExcelDataset())
    remarks = fields.Field(attribute='remarks', column_name='khadadevi-hhis_vehicles-vehicles_remarks', widget=ExcelDataset())

    # vehicle_type = fields.Field(attribute='name_eng', column_name='name_eng', widget=ExcelDataset())
    # vehicle_type = fields.Field(attribute='name_eng', column_name='name_eng', widget=ExcelDataset())
    # dob_bs = fields.Field(attribute='dob_bs', column_name='dob_bs', widget=ExcelDateWidget())

    class Meta:
        model = HouseholdVehicle


class FacilityResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='name', widget=ExcelDataset())
    dob_bs = fields.Field(attribute='dob_bs', column_name='dob_bs', widget=ExcelDateWidget())

    class Meta:
        model = HouseholdFacility


class InfrastructureResource(resources.ModelResource):
    household_watersource = fields.Field(attribute='household_watersource', column_name='water_source', widget=ExcelDataset())
    household_natural_disaster = fields.Field(attribute='household_natural_disaster', column_name='natural_disaster', widget=ExcelDataset())
    # dob_bs = fields.Field(attribute='dob_bs', column_name='dob_bs', widget=ExcelDateWidget())

    class Meta:
        model = HouseholdInfrastructure
