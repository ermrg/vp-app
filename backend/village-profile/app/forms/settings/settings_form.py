from django import forms


class AnimalTypeForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class BastiForm(forms.Form):
    name = forms.CharField(required=False)
    ward = forms.CharField(required=False)
    
    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class BusinessTypeForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class CookingFuelForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class CountryForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class DeathReasonForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class DisabilityTypeForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class DisasterForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class EducationLevelForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class EducationStatusForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class FacilityForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class FestivalForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class ForeignReasonForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class GarbageManagementForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class HouseDamageStatusForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class HouseTypeForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class IncomeSourceForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class JaatiForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class LandTypeForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class LightFuelForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class MainOccupationForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class MargaForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class MaritalStatusForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class MotherTongueForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class RelationWithHohForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class ReligionForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class RoofTypeForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class SewageTypeForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class TechnicalSkillForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class ToiletTypeForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class VaccineNameForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class VehicleTypeForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class WardForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data


class CollectorForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    password = forms.CharField(required=False)


class WaterSourceForm(forms.Form):
    name = forms.CharField(required=False)

    def clean_name(self):
        data = self.cleaned_data['name']
        if not data:
            data = 'General'
            # forms.ValidationError("Name Required")
        return data
