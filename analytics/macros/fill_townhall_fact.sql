{#
    This macro returns a townhall_fact if it is null
#}

{% macro fill_townhall_fact(alcaldia_hecho) -%}
    IFNULL({{ dbt.safe_cast("alcaldia_hecho", api.Column.translate_type("string")) }}, 'No especificado')
{%- endmacro %}