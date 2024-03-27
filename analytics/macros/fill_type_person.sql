{#
    This macro returns a type person if it is null
#}

{% macro fill_type_person(tipo_persona) -%}
    IFNULL({{ dbt.safe_cast("tipo_persona", api.Column.translate_type("string")) }}, 'MORAL')
{%- endmacro %}