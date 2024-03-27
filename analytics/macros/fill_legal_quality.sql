{#
    This macro returns a type person if it is null
#}

{% macro fill_legal_quality(calidad_juridica) -%}
    IFNULL({{ dbt.safe_cast("calidad_juridica", api.Column.translate_type("string")) }}, 'No especificado')
{%- endmacro %}