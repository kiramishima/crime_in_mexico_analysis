{#
    This macro returns a town_fact if it is null
#}

{% macro fill_town_fact(municipio_hecho) -%}
    IFNULL({{ dbt.safe_cast("municipio_hecho", api.Column.translate_type("string")) }}, 'No especificado')
{%- endmacro %}