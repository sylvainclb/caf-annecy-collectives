""" List of Form used to modify configuration """

from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    BooleanField,
    IntegerField,
    FloatField,
    TextAreaField,
    StringField,
    DateTimeField,
    FileField,
    HiddenField,
)
from wtforms_alchemy.utils import strip_string


class ConfigurationBaseForm(FlaskForm):
    """Base form for all configuration item."""

    name = HiddenField()
    submit = SubmitField("Update")


class ConfigurationTextAreaForm(ConfigurationBaseForm):
    """Base form for long configuration item."""

    content = TextAreaField(render_kw={"rows": 10})


class ConfigurationIntegerForm(ConfigurationBaseForm):
    """Form for Integer configuration item."""

    content = IntegerField()


class ConfigurationFloatForm(ConfigurationBaseForm):
    """Form for Float configuration item."""

    content = FloatField()


class ConfigurationDateForm(ConfigurationBaseForm):
    """Form for date configuration item."""

    content = DateTimeField()


class ConfigurationShortStringForm(ConfigurationBaseForm):
    """Form for short string configuration item."""

    content = StringField(filters=[strip_string])


class ConfigurationLongStringForm(ConfigurationTextAreaForm):
    """Form for long string configuration item (textarea)"""

    # pylint: disable=unnecessary-pass
    pass


class ConfigurationArrayForm(ConfigurationTextAreaForm):
    """Form for Array configuration item."""

    # pylint: disable=unnecessary-pass
    pass


class ConfigurationDictionnaryForm(ConfigurationTextAreaForm):
    """Form for dictionnary configuration item."""

    # pylint: disable=unnecessary-pass
    pass


class ConfigurationBooleanForm(ConfigurationBaseForm):
    """Form for boolean configuration item."""

    content = BooleanField()


class ConfigurationFileForm(ConfigurationBaseForm):
    """Form for file configuration item."""

    content = FileField()


def get_form_from_configuration(item):
    """Select right type of form from the input configuration item.

    :param ConfigurationItem item: configuration item that will determine the field type"""
    return globals()[f"Configuration{item.type.name}Form"]