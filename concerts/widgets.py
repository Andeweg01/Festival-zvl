from django.forms.widgets import ClearableFileInput, DateTimeBaseInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'concerts/custom_widget_templates/custom_clearable_file_input.html'


class CustomDateInput(DateTimeBaseInput):
    format_key = 'DATE_INPUT_FORMATS'
    template_name = 'concerts/custom_widget_templates/custom_date.html'


class CustomTimeInput(DateTimeBaseInput):
    format_key = 'TIME_INPUT_FORMATS'
    template_name = 'concerts/custom_widget_templates/custom_time.html'
