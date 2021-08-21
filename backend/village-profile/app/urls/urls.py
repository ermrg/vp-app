from django.urls import path, include

from app.views import home_controller
from app.views.settings import user_controller, fiscal_year_controller, province_controller, district_controller, \
    local_level_controller, designation_controller, feedback_controller, office_controller, setting_controller, \
    collector_controller
from app.views.vp import household_controller, individual_controller, import_controller, reports_controller, \
    analysis_controller
from app.views.vp.analytics import animal_analytics_controller, business_analytics_controller, deceased_analytics_controller, \
    income_analytics_controller, househead_analytics_controller, infrastructure_analytics_controller, member_analytics_controller, \
    house_analytics_controller, land_analytics_controller, rent_analytics_controller
from app.views.vp.analytics.animal_analytics_controller import AnimalLineChartJSONView
from app.views.vp.analytics.business_analytics_controller import BusinessLineChartJSONView
from app.views.vp.analytics.deceased_analytics_controller import DeceasedLineChartJSONView
from app.views.vp.analytics.income_analytics_controller import IncomeLineChartJSONView
from app.views.vp.analytics.househead_analytics_controller import HouseheadLineChartJSONView
from app.views.vp.analytics.infrastructure_analytics_controller import InfrastructureLineChartJSONView
from app.views.vp.analytics.member_analytics_controller import MemberLineChartJSONView
from app.views.vp.analytics.house_analytics_controller import HouseLineChartJSONView
from app.views.vp.analytics.land_analytics_controller import LandLineChartJSONView
from app.views.vp.analytics.rent_analytics_controller import RentLineChartJSONView

urlpatterns = [

    path('', home_controller.index, name='dashboard'),
    # path('signup/', home_controller.SignUp.as_view(), name='signup'),

    #  User
    path('setting/user/create', user_controller.create_user, name='create_user'),
    path('setting/user/list', user_controller.list_user, name='list_user'),
    path('setting/user/delete/<int:user_id>', user_controller.delete_user, name='delete_user'),
    path('setting/user/edit/<int:user_id>', user_controller.edit_user, name='edit_user'),


    # Fiscal Year
    path('setting/fiscal-year/list', fiscal_year_controller.list_fiscal_year, name='fiscal_year'),
    path('setting/fiscal-year/create', fiscal_year_controller.create_fiscal_year, name='create_fiscal_year'),
    path('setting/fiscal-year/change-status', fiscal_year_controller.change_status, name='fy_change_status'),


    # Province
    path('setting/province/list', province_controller.list_province, name='province'),
    path('setting/province/create', province_controller.create_province, name='create_province'),

    # District
    path('setting/district/list', district_controller.list_district, name='district'),
    path('setting/district/create', district_controller.create_district, name='create_district'),

    # Local Level
    path('setting/local_level/list', local_level_controller.list_local_level, name='local_level'),
    path('setting/local_level/create', local_level_controller.create_local_level, name='create_local_level'),

    # designation
    path('setting/designation/list', designation_controller.list_designation, name='designation'),
    path('setting/designation/create', designation_controller.create_designation, name='create_designation'),

    # office
    path('setting/office/list', office_controller.list_office, name='office'),
    path('setting/office/create', office_controller.create_office, name='create_office'),

    # household
    path('household/list', household_controller.list_household, name='household'),
    path('household/create', household_controller.create_household, name='create_household'),
    path('household/create/<int:hh_id>', household_controller.create_household, name='create_household'),
    path('household/create/<int:hh_id>/<int:step_>', household_controller.create_household, name='create_household'),
    # path('household/delete/<int:hh_id>', household_controller.delete_household, name='delete_household'),

    # path('household/store', household_controller.store_household, name='store_household'),
    # path('household/store/<int:hh_id>/<slug:step>', household_controller.store_household, name='store_household'),

    # individual
    path('individual/list', individual_controller.list_individual, name='individual'),
    path('individual/create', individual_controller.create_individual, name='create_individual'),

    # Feedback
    path('setting/feedback/list', feedback_controller.list_feedback, name='feedback'),
    path('setting/feedback/create', feedback_controller.create_feedback, name='create_feedback'),

    # reports
    path('household/reports', reports_controller.report, name='report'),
    # path('household/reports', reports_controller.line_chart_json, name='line_chart_json'),

    # household_animal Type
    path('setting/animal-type/list', setting_controller.animal_type, name='setting.animal_type'),
    path('setting/animal-type/create', setting_controller.animal_type_create, name='setting.animal_type.create'),
    path('setting/animal-type/delete/<int:id>', setting_controller.delete_animal,
         name='setting.delete_animal'),
    path('setting/animal-type/edit/<int:id>', setting_controller.edit_animal, name='setting.edit_animal'),
    path('setting/animal-type/update/<int:id>', setting_controller.update_animal, name='setting.update_animal'),

    # Basti
    path('setting/basti-name/list', setting_controller.basti, name='setting.basti_name'),
    path('setting/basti-name/create', setting_controller.basti_create, name='setting.basti.create'),
    path('setting/basti-name/delete/<int:id>', setting_controller.delete_basti, name='setting.delete_basti'),
    path('setting/basti-name/edit/<int:id>', setting_controller.edit_basti, name='setting.edit_basti'),
    path('setting/basti-name/select/<int:id>', setting_controller.get_basti_by_ward, name='setting.get_bastis_by_ward'),
    path('setting/basti-name/update/<int:id>', setting_controller.update_basti, name='setting.update_basti'),


    # Business Type
    path('setting/business-type/list', setting_controller.business_type, name='setting.business_type'),
    path('setting/business-type/create', setting_controller.business_type_create, name='setting.business_type.create'),
    path('setting/business-type/delete/<int:id>', setting_controller.delete_business_type,
         name='setting.delete_business_type'),
    path('setting/business-type/edit/<int:id>', setting_controller.edit_business_type, name='setting.edit_business_type'),
    path('setting/business-type/update/<int:id>', setting_controller.update_business_type,
         name='setting.update_business_type'),

    # Cooking Fuel
    path('setting/cooking-fuel/list', setting_controller.cooking_fuel, name='setting.cooking_fuel'),
    path('setting/cooking-fuel/create', setting_controller.cooking_fuel_create, name='setting.cooking_fuel.create'),
    path('setting/cooking-fuel/delete/<int:id>', setting_controller.delete_cooking_fuel,
         name='setting.delete_cooking_fuel'),
    path('setting/cooking-fuel/edit/<int:id>', setting_controller.edit_cooking_fuel, name='setting.edit_cooking_fuel'),
    path('setting/cooking-fuel/updaet/<int:id>', setting_controller.update_cooking_fuel,
         name='setting.update_cooking_fuel'),

    # Country Name
    path('setting/country/list', setting_controller.country, name='setting.country'),
    path('setting/country/create', setting_controller.country_create, name='setting.country.create'),
    path('setting/country/delete/<int:id>', setting_controller.delete_country, name='setting.delete_country'),
    path('setting/country/edit/<int:id>', setting_controller.edit_country, name='setting.edit_country'),
    path('setting/country/update/<int:id>', setting_controller.update_country, name='setting.update_country'),

    # Death Reason
    path('setting/death-reason/list', setting_controller.death_reason, name='setting.death_reason'),
    path('setting/death-reason/create', setting_controller.death_reason_create, name='setting.death_reason.create'),
    path('setting/death-reason/delete/<int:id>', setting_controller.delete_death_reason,
         name='setting.delete_death_reason'),
    path('setting/death-reason/edit/<int:id>', setting_controller.edit_death_reason,
         name='setting.edit_death_reason'),
    path('setting/death-reason/update/<int:id>', setting_controller.update_death_reason,
         name='setting.update_death_reason'),

    # Disability Type
    path('setting/disability-type/list', setting_controller.disability_type, name='setting.disability_type'),
    path('setting/disability-type/create', setting_controller.disability_type_create,
         name='setting.disability_type.create'),
    path('setting/disability-type/delete/<int:id>', setting_controller.delete_disability_type,
         name='setting.delete_disability_type'),
    path('setting/disability-type/edit/<int:id>', setting_controller.edit_disability_type,
         name='setting.edit_disability_type'),
     path('setting/disability-type/update/<int:id>', setting_controller.update_disability_type,
         name='setting.update_disability_type'),

    # Disaster Name
    path('setting/disaster-name/list', setting_controller.disaster_name, name='setting.disaster_name'),
    path('setting/disaster-name/create', setting_controller.disaster_name_create, name='setting.disaster_name.create'),
    path('setting/disaster-name/delete/<int:id>', setting_controller.delete_disaster, name='setting.delete_disaster'),
    path('setting/disaster-name/edit/<int:id>', setting_controller.edit_disaster, name='setting.edit_disaster'),
    path('setting/disaster-name/update/<int:id>', setting_controller.update_disaster, name='setting.update_disaster'),

    # Education Level
    path('setting/education-level/list', setting_controller.education_level, name='setting.education_level'),
    path('setting/education-level/create', setting_controller.education_level_create,
         name='setting.education_level.create'),
    path('setting/education-level/delete/<int:id>', setting_controller.delete_education_level,
         name='setting.delete_education_level'),
    path('setting/education-level/edit/<int:id>', setting_controller.edit_education_level,
         name='setting.edit_education_level'),
    path('setting/education-level/update/<int:id>', setting_controller.update_education_level,
         name='setting.update_education_level'),

    # Education Status
    path('setting/education-status/list', setting_controller.education_status, name='setting.education_status'),
    path('setting/education-status/create', setting_controller.education_status_create,
         name='setting.education_status.create'),
    path('setting/education-status/delete/<int:id>', setting_controller.delete_education_status,
         name='setting.delete_education_status'),
    path('setting/education-status/edit/<int:id>', setting_controller.edit_education_status,
         name='setting.edit_education_status'),
    path('setting/education-status/update/<int:id>', setting_controller.update_education_status,
         name='setting.update_education_status'),

    # Facility
    path('setting/facility/list', setting_controller.facility, name='setting.facility'),
    path('setting/facility/create', setting_controller.facility_create, name='setting.facility.create'),
    path('setting/facility/delete/<int:id>', setting_controller.delete_facility, name='setting.delete_facility'),
    path('setting/facility/edit/<int:id>', setting_controller.edit_facility, name='setting.edit_facility'),
    path('setting/facility/update/<int:id>', setting_controller.update_facility, name='setting.update_facility'),


    # Festival
    path('setting/festival/list', setting_controller.festival, name='setting.festival'),
    path('setting/festival/create', setting_controller.festival_create, name='setting.festival.create'),
    path('setting/festival/delete/<int:id>', setting_controller.delete_festival, name='setting.delete_festival'),
    path('setting/festival/edit/<int:id>', setting_controller.edit_festival, name='setting.edit_festival'),
    path('setting/festival/update/<int:id>', setting_controller.update_festival, name='setting.update_festival'),

    # Foreign Reason
    path('setting/foreign-reason/list', setting_controller.foreign_reason, name='setting.foreign_reason'),
    path('setting/foreign-reason/create', setting_controller.foreign_reason_create, name='setting.foreign_reason.create'),
    path('setting/foreign-reason/delete/<int:id>', setting_controller.delete_foreign_reason,
         name='setting.delete_foreign_reason'),
    path('setting/foreign-reason/edit/<int:id>', setting_controller.edit_foreign_reason,
         name='setting.edit_foreign_reason'),
    path('setting/foreign-reason/update/<int:id>', setting_controller.update_foreign_reason,
         name='setting.update_foreign_reason'),

    # Garbage Management
    path('setting/garbage-management/list', setting_controller.garbage_management, name='setting.garbage_management'),
    path('setting/garbage-management/create', setting_controller.garbage_management_create,
         name='setting.garbage_management.create'),
    path('setting/garbage-management/delete/<int:id>', setting_controller.delete_garbage_management,
         name='setting.delete_garbage_management'),
    path('setting/garbage-management/edit/<int:id>', setting_controller.edit_garbage_management,
         name='setting.edit_garbage_management'),
    path('setting/garbage-management/update/<int:id>', setting_controller.update_garbage_management,
         name='setting.update_garbage_management'),

    # House Damage Status
    path('setting/house-damage-status/list', setting_controller.house_damage_status, name='setting.house_damage_status'),
    path('setting/house-damage-status/create', setting_controller.house_damage_status_create,
         name='setting.house_damage_status.create'),
    path('setting/house-damage-status/delete/<int:id>', setting_controller.delete_house_damage_status,
         name='setting.delete_house_damage_status'),
    path('setting/house-damage-status/edit/<int:id>', setting_controller.edit_house_damage_status,
         name='setting.edit_house_damage_status'),
    path('setting/house-damage-status/update/<int:id>', setting_controller.update_house_damage_status,
         name='setting.update_house_damage_status'),

    # House Type
    path('setting/house-type/list', setting_controller.house_type, name='setting.house_type'),
    path('setting/house-type/create', setting_controller.house_type_create, name='setting.house_type.create'),
    path('setting/house-type/delete/<int:id>', setting_controller.delete_house_type,name='setting.delete_house_type'),
    path('setting/house-type/edit/<int:id>', setting_controller.edit_house_type, name='setting.edit_house_type'),
    path('setting/house-type/update/<int:id>', setting_controller.update_house_type,name='setting.update_house_type'),

    # Income Source
    path('setting/income-source/list', setting_controller.income_source, name='setting.income_source'),
    path('setting/income-source/create', setting_controller.income_source_create, name='setting.income_source.create'),
    path('setting/income-source/delete/<int:id>', setting_controller.delete_income_source,
         name='setting.delete_income_source'),
    path('setting/income-source/edit/<int:id>', setting_controller.edit_income_source,
         name='setting.edit_income_source'),
    path('setting/income-source/update/<int:id>', setting_controller.update_income_source,
         name='setting.update_income_source'),

    # Jaati
    path('setting/ethnics/list', setting_controller.jaati, name='setting.jaati'),
    path('setting/ethnics/create', setting_controller.jaati_create, name='setting.jaati.create'),
    path('setting/ethnics/delete/<int:id>', setting_controller.delete_jaati, name='setting.delete_jaati'),
    path('setting/ethnics/edit/<int:id>', setting_controller.edit_jaati, name='setting.edit_jaati'),
    path('setting/ethnics/update/<int:id>', setting_controller.update_jaati, name='setting.update_jaati'),

    # Land Type
    path('setting/land-type/list', setting_controller.land_type, name='setting.land_type'),
    path('setting/land-type/create', setting_controller.land_type_create, name='setting.land_type.create'),
    path('setting/land-type/delete/<int:id>', setting_controller.delete_land_type,
         name='setting.delete_land_type'),
    path('setting/land-type/edit/<int:id>', setting_controller.edit_land_type,
         name='setting.edit_land_type'),
    path('setting/land-type/update/<int:id>', setting_controller.update_land_type,
         name='setting.update_land_type'),

    # Light Fuel
    path('setting/light-fuel/list', setting_controller.light_fuel, name='setting.light_fuel'),
    path('setting/light-fuel/create', setting_controller.light_fuel_create, name='setting.light_fuel.create'),
    path('setting/light-fuel/delete/<int:id>', setting_controller.delete_light_fuel,
         name='setting.delete_light_fuel'),
    path('setting/light-fuel/edit/<int:id>', setting_controller.edit_light_fuel,
         name='setting.edit_light_fuel'),
    path('setting/light-fuel/update/<int:id>', setting_controller.update_light_fuel,
         name='setting.update_light_fuel'),

    # Main Occupation
    path('setting/main-occupation/list', setting_controller.main_occupation, name='setting.main_occupation'),
    path('setting/main-occupation/create', setting_controller.main_occupation_create,
         name='setting.main_occupation.create'),
    path('setting/main-occupation/delete/<int:id>', setting_controller.delete_main_occupation,
         name='setting.delete_main_occupation'),
    path('setting/main-occupation/edit/<int:id>', setting_controller.edit_main_occupation,
         name='setting.edit_main_occupation'),
    path('setting/main-occupation/update/<int:id>', setting_controller.update_main_occupation,
         name='setting.update_main_occupation'),

    # Marga
    path('setting/marga/list', setting_controller.marga, name='setting.marga'),
    path('setting/marga/create', setting_controller.marga_create, name='setting.marga.create'),
    path('setting/marga/delete/<int:id>', setting_controller.delete_marga, name='setting.delete_marga'),
    path('setting/marga/edit/<int:id>', setting_controller.edit_marga, name='setting.edit_marga'),
    path('setting/marga/update/<int:id>', setting_controller.update_marga, name='setting.update_marga'),

    # Marital Status
    path('setting/marital-status/list', setting_controller.marital_status, name='setting.marital_status'),
    path('setting/marital-status/create', setting_controller.marital_status_create,
         name='setting.marital_status.create'),
    path('setting/marital-status/delete/<int:id>', setting_controller.delete_marital_status,
         name='setting.delete_marital_status'),
    path('setting/marital-status/edit/<int:id>', setting_controller.edit_marital_status,
         name='setting.edit_marital_status'),
    path('setting/marital-status/update/<int:id>', setting_controller.update_marital_status,
         name='setting.update_marital_status'),

    # Mother Tongue
    path('setting/mother-tongue/list', setting_controller.mother_tongue, name='setting.mother_tongue'),
    path('setting/mother-tongue/create', setting_controller.mother_tongue_create,
         name='setting.mother_tongue.create'),
    path('setting/mother-tongue/delete/<int:id>', setting_controller.delete_mother_tongue,
         name='setting.delete_mother_tongue'),
    path('setting/mother-tongue/edit/<int:id>', setting_controller.edit_mother_tongue,
         name='setting.edit_mother_tongue'),
    path('setting/mother-tongue/update/<int:id>', setting_controller.update_mother_tongue,
         name='setting.update_mother_tongue'),

    # Relation With HouseHead
    path('setting/relation-with-hoh/list', setting_controller.relation_with_hoh, name='setting.relation_with_hoh'),
    path('setting/relation-with-hoh/create', setting_controller.relation_with_hoh_create,
         name='setting.relation_with_hoh.create'),
    path('setting/relation-with-hoh/delete/<int:id>', setting_controller.delete_relation_with_hoh,
         name='setting.delete_relation_with_hoh'),
    path('setting/relation-with-hoh/edit/<int:id>', setting_controller.edit_relation_with_hoh,
         name='setting.edit_relation_with_hoh'),
    path('setting/relation-with-hoh/update/<int:id>', setting_controller.update_relation_with_hoh,
         name='setting.update_relation_with_hoh'),

    # Religion
    path('setting/religion/list', setting_controller.religion, name='setting.religion'),
    path('setting/religion/create', setting_controller.religion_create, name='setting.religion.create'),
    path('setting/religion/delete/<int:id>', setting_controller.delete_religion, name='setting.delete_religion'),
    path('setting/religion/edit/<int:id>', setting_controller.edit_religion, name='setting.edit_religion'),
    path('setting/religion/update/<int:id>', setting_controller.update_religion, name='setting.update_religion'),

    # Roof Type
    path('setting/roof-type/list', setting_controller.roof_type, name='setting.roof_type'),
    path('setting/roof-type/create', setting_controller.roof_type_create, name='setting.roof_type.create'), # Roof Type
    path('setting/roof-type/delete/<int:id>', setting_controller.delete_roof_type, name='setting.delete_roof_type'),
    path('setting/roof-type/edit/<int:id>', setting_controller.edit_roof_type, name='setting.edit_roof_type'),
    path('setting/roof-type/update/<int:id>', setting_controller.update_roof_type, name='setting.update_roof_type'),

    # Sewage Type
    path('setting/sewage-type/list', setting_controller.sewage_type, name='setting.sewage_type'),
    path('setting/sewage-type/create', setting_controller.sewage_type_create, name='setting.sewage_type.create'),
    path('setting/sewage-type/delete/<int:id>', setting_controller.delete_sewage_type,
         name='setting.delete_sewage_type'),
    path('setting/sewage-type/edit/<int:id>', setting_controller.edit_sewage_type,
         name='setting.edit_sewage_type'),
    path('setting/sewage-type/update/<int:id>', setting_controller.update_sewage_type,
         name='setting.update_sewage_type'),

    # Technical Skill
    path('setting/technical-skill/list', setting_controller.technical_skill, name='setting.technical_skill'),
    path('setting/technical-skill/create', setting_controller.technical_skill_create,
         name='setting.technical_skill.create'),
    path('setting/technical-skill/delete/<int:id>', setting_controller.delete_technical_skill,
         name='setting.delete_technical_skill'),
     path('setting/technical-skill/edit/<int:id>', setting_controller.edit_technical_skill,
         name='setting.edit_technical_skill'),
     path('setting/technical-skill/update/<int:id>', setting_controller.update_technical_skill,
         name='setting.update_technical_skill'),

    # Toilet Type
    path('setting/toilet-type/list', setting_controller.toilet_type, name='setting.toilet_type'),
    path('setting/toilet-type/create', setting_controller.toilet_type_create, name='setting.toilet_type.create'),
    path('setting/toilet-type/delete/<int:id>', setting_controller.delete_toilet_type,
         name='setting.delete_toilet_type'),
    path('setting/toilet-type/edit/<int:id>', setting_controller.edit_toilet_type,
         name='setting.edit_toilet_type'),
    path('setting/toilet-type/update/<int:id>', setting_controller.update_toilet_type,
         name='setting.update_toilet_type'),

    # Vaccine Name
    path('setting/vaccine-name/list', setting_controller.vaccine_name, name='setting.vaccine_name'),
    path('setting/vaccine-name/create', setting_controller.vaccine_name_create, name='setting.vaccine_name.create'),
    path('setting/vaccine-name/delete/<int:id>', setting_controller.delete_vaccine, name='setting.delete_vaccine'),
    path('setting/vaccine-name/edit/<int:id>', setting_controller.edit_vaccine, name='setting.edit_vaccine'),
    path('setting/vaccine-name/update/<int:id>', setting_controller.update_vaccine, name='setting.update_vaccine'),

    # Vehicle Type
    path('setting/vehicle-type/list', setting_controller.vehicle_type, name='setting.vehicle_type'),
    path('setting/vehicle-type/create', setting_controller.vehicle_type_create, name='setting.vehicle_type.create'),
    path('setting/vehicle-type/delete/<int:id>', setting_controller.delete_vehicle_type,
         name='setting.delete_vehicle_type'),
    path('setting/vehicle-type/edit/<int:id>', setting_controller.edit_vehicle_type,
         name='setting.edit_vehicle_type'),
    path('setting/vehicle-type/update/<int:id>', setting_controller.update_vehicle_type,
         name='setting.update_vehicle_type'),

    # Ward
    path('setting/ward/list', setting_controller.ward, name='setting.ward'),
    path('setting/ward/create', setting_controller.ward_create, name='setting.ward.create'),
    path('setting/ward/delete/<int:id>', setting_controller.delete_ward, name='setting.delete_ward'),
    path('setting/ward/edit/<int:id>', setting_controller.edit_ward, name='setting.edit_ward'),
    path('setting/ward/update/<int:id>', setting_controller.update_ward, name='setting.update_ward'),

    # Collector
    path('setting/collector/list', collector_controller.index, name='setting.collector'),
    path('setting/collector/create', collector_controller.collector_create, name='setting.collector.create'),
    path('setting/collector/delete/<int:id>', collector_controller.delete_collector, name='setting.delete_collector'),
    path('setting/collector/edit/<int:id>', collector_controller.edit_collector, name='setting.edit_collector'),
    path('setting/collector/update/<int:id>', collector_controller.update_collector, name='setting.update_collector'),

    # Water Source
    path('setting/water-source/list', setting_controller.water_source, name='setting.water_source'),
    path('setting/water-source/create', setting_controller.water_source_create, name='setting.water_source.create'),
    path('setting/water-source/delete/<int:id>', setting_controller.delete_water_source,
         name='setting.delete_water_source'),
    path('setting/water-source/edit/<int:id>', setting_controller.edit_water_source, name='setting.edit_water_source'),
    path('setting/water-source/update/<int:id>', setting_controller.update_water_source,
         name='setting.update_water_source'),

    # Household Routes

    # household
    path('household/detail/create', household_controller.add_household, name="household.detail"),
    path('household/detail/update/<int:hh_id>', household_controller.update_household, name="household.detail.update"),

    path('household/house-hold/delete/<int:id>', reports_controller.delete_household, name="delete_household"),
    path('household/house-hold/edit/<int:id>', reports_controller.edit_household, name="household.edit"),
    path('household/house-hold/update/<int:id>', reports_controller.update_household, name="household.update"),


    # Househead
    path('household/househead/create/<int:hh_id>', household_controller.add_househead, name="household.househead"),
    path('household/househead/update/<int:hoh_id>', household_controller.update_househead,
         name="household.househead.update"),
    path('household/house-head/list', reports_controller.househead_report, name="househead_report"),
    path('household/house-head/delete/<int:id>', reports_controller.delete_househead, name="delete_househead"),
    path('household/house-head/edit/<int:id>', reports_controller.edit_househead, name="househead.edit"),
    path('household/house-head/update/<int:id>', reports_controller.update_househead, name="househead.update"),


    path('household/member/create/<int:hh_id>', household_controller.add_member, name="household.member"),
    # path('household/member/update/<int:hoh_id>', household_controller.update_member,
    #      name="household.member.update"),
    path('household/member/list', reports_controller.member_report, name="member_report"),
    path('household/member/delete/<int:id>', reports_controller.delete_member_details, name="delete_household_member"),
    path('household/member/edit/<int:id>', reports_controller.edit_household_member, name="household_member.edit"),
    path('household/member/update/<int:id>', reports_controller.update_household_member, name="household_member.update"),

    # Household Deceased Member
    path('household/deceased/create/<int:hh_id>', household_controller.add_deceased, name="household.deceased"),
    path('household/deceased/list', reports_controller.deceased_report, name="deceased_report"),
    path('household/deceased/delete/<int:id>', reports_controller.delete_deceased_details,
         name="delete_household_deceased"),
    path('household/deceased/edit/<int:id>', reports_controller.edit_household_deceased,
         name="household_deceased.edit"),
    path('household/deceased/update/<int:id>', reports_controller.update_household_deceased,
         name="household_deceased.update"),

    # House Details
    path('household/house-details/create/<int:hh_id>', household_controller.add_house_details,
         name="household.house_details"),
    path('household/house-details/list', reports_controller.house_report, name="house_report"),
    path('household/house-details/delete/<int:id>', reports_controller.delete_house_details,
         name="delete_household_house"),
    path('household/house-details/edit/<int:id>', reports_controller.edit_household_house,
         name="household_house.edit"),
    path('household/house-details/update/<int:id>', reports_controller.update_household_house,
         name="household_house.update"),


    path('household/rent-member/create/<int:hh_id>', household_controller.add_rent_member, name="household.rent_member"),
    path('household/rent-member/list', reports_controller.rent_member_report, name="rent_member_report"),
    path('household/rent-member/delete/<int:id>', reports_controller.delete_household_rent, name="delete_household_rent"),
    path('household/rent-member/edit/<int:id>', reports_controller.edit_household_rent, name="household_rent.edit"),
    path('household/rent-member/update/<int:id>', reports_controller.update_household_rent, name="household_rent.update"),

    # Household Land
    path('household/land-details/create/<int:hh_id>', household_controller.add_land_details,
         name="household.land_details"),
    path('household/land-details/list', reports_controller.land_report, name="land_report"),
    path('household/land-details/delete/<int:id>', reports_controller.delete_land_details, name="delete_household_land"),
    path('household/land-details/edit/<int:id>', reports_controller.edit_household_land, name="household_land.edit"),
    path('household/land-details/update/<int:id>', reports_controller.update_household_land,
         name="household_land.update"),

    # Household Animal
    path('household/animals-details/create/<int:hh_id>', household_controller.add_animals_details,
         name="household.animals_details"),
    path('household/animal/list', reports_controller.animal_report, name="animal_report"),
    path('household/animal/delete/<int:id>', reports_controller.delete_animal_details, name="delete_household_animal"),
    path('household/animal/edit/<int:id>', reports_controller.edit_household_animal, name="edit_household_animal"),
    path('household/animal/update/<int:id>', reports_controller.update_household_animal, name="household_animal.update"),

    # Household Business
    path('household/business-details/create/<int:hh_id>', household_controller.add_business_details,
         name="household.business_details"),
    path('household/business/list', reports_controller.business_report, name="business_report"),
    path('household/business/delete/<int:id>', reports_controller.delete_business_details,
         name="delete_household_business"),
    path('household/business/edit/<int:id>', reports_controller.edit_household_business,
         name="household_business.edit"),
    path('household/business/update/<int:id>', reports_controller.update_household_business,
         name="household_business.update"),

    path('household/festivals/create/<int:hh_id>', household_controller.add_festivals, name="household.festivals"),

    path('household/helper/create/<int:hh_id>', household_controller.add_helper,
         name="household.helper"),
    path('household/helper/list', reports_controller.helper_report, name="helper_report"),
    path('household/helper/delete/<int:id>', reports_controller.delete_helper_details, name="delete_household_helper"),
    path('household/helper/edit/<int:id>', reports_controller.edit_household_helper, name="household_helper.edit"),
    path('household/helper/update/<int:id>', reports_controller.update_household_helper, name="household_helper.update"),

    # Household Income
    path('household/household-income/create/<int:hh_id>', household_controller.add_income,
         name="household.income"),
    path('household/household-income/list', reports_controller.household_income_report,
         name="income_report"),
    path('household/household-income/delete/<int:id>', reports_controller.delete_household_income,
         name="delete_household_income"),
    path('household/household-income/edit/<int:id>', reports_controller.edit_household_income,
         name="household_income.edit"),
    path('household/household-income/update/<int:id>', reports_controller.update_household_income,
         name="household_income.update"),

    # Household Expenses
    path('household/household-expenses/create/<int:hh_id>', household_controller.add_expenses, name="household.expenses"),
    path('household/household-expenses/list', reports_controller.expenses_report, name="expenses_report"),
    path('household/household-expenses/delete/<int:id>', reports_controller.delete_household_expenses,
         name="delete_household_expenses"),
    path('household/household-expenses/edit/<int:id>', reports_controller.edit_household_expenses,
         name="household_expenses.edit"),
    path('household/household-expenses/update/<int:id>', reports_controller.update_household_expenses,
         name="household_expenses.update"),

    path('household/vehicle-details/create/<int:hh_id>', household_controller.add_vehicle_details,
         name="household.vehicle_details"),

    path('household/other-facility/create/<int:hh_id>', household_controller.add_other_facility,
         name="household.other_facility"),

    # Household Infrastructure
    path('household/infrastructure/create/<int:hh_id>', household_controller.add_infrastructure,
         name="household.infrastructure"),
    path('household/infrastructure/list', reports_controller.infrastructure_report, name="infrastructure_report"),
    path('household/infrastructure/delete/<int:id>', reports_controller.delete_infrastructure_details,
         name="delete_household_infrastructure"),
    path('household/infrastructure/edit/<int:id>', reports_controller.edit_household_infrastructure,
         name="household_infrastructure.edit"),
    path('household/infrastructure/update/<int:id>', reports_controller.update_household_infrastructure,
         name="household_infrastructure.update"),

    # Import Excel File
    path('import/excel', import_controller.import_excel, name='import'),
    path('upload/excel', import_controller.upload_excel, name='upload_excel'),

    path('404', home_controller.page_not_found, name='404'),

    #analytics
    path('animal-analytics/', animal_analytics_controller.index, name='animal_analytics'),
    path('animal-line-analytics/', AnimalLineChartJSONView.as_view(), name='animal_line_chart'),

    path('business-analytics/', business_analytics_controller.index, name='business_analytics'),
    path('business-line-analytics/', BusinessLineChartJSONView.as_view(), name='business_line_chart'),

    path('deceased-analytics/', deceased_analytics_controller.index, name='deceased_analytics'),
    path('deceased-line-analytics/', DeceasedLineChartJSONView.as_view(), name='deceased_line_chart'),

    path('income-analytics/', income_analytics_controller.index, name='income_analytics'),
    path('income-line-analytics/', IncomeLineChartJSONView.as_view(), name='income_line_chart'),

    path('househead-analytics/', househead_analytics_controller.index, name='househead_analytics'),
    path('househead-line-analytics/', HouseheadLineChartJSONView.as_view(), name='househead_line_chart'),

    path('infrastructure-analytics/', infrastructure_analytics_controller.index, name='infrastructure_analytics'),
    path('infrastructure-line-analytics/', InfrastructureLineChartJSONView.as_view(), name='infrastructure_line_chart'),

    path('member-analytics/', member_analytics_controller.index, name='member_analytics'),
    path('member-line-analytics/', MemberLineChartJSONView.as_view(), name='member_line_chart'),

    path('house-analytics/', house_analytics_controller.index, name='house_analytics'),
    path('house-line-analytics/', HouseLineChartJSONView.as_view(), name='house_line_chart'),

    path('land-analytics/', land_analytics_controller.index, name='land_analytics'),
    path('land-line-analytics/', LandLineChartJSONView.as_view(), name='land_line_chart'),

    path('rent-analytics/', rent_analytics_controller.index, name='rent_analytics'),
    path('rent-line-analytics/', RentLineChartJSONView.as_view(), name='rent_line_chart'),


    # analysis Page
    path('analysis/', analysis_controller.demography_page, name='analysis'),
    # path('analysis/by_gender', analysis_controller.get_gender, name='get_by_gender'),
    path('analysis/education', analysis_controller.education_page, name='education.analysis'),
    path('analysis/household', analysis_controller.household_page, name='household.analysis'),
    path('analysis/finance', analysis_controller.finance_page, name='finance.analysis'),
    path('analysis/health', analysis_controller.health_page, name='health.analysis'),
    path('analysis/agriculture', analysis_controller.agriculture_page, name='agriculture.analysis'),
]





