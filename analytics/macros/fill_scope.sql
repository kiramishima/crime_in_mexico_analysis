{#
    This macro returns a type person if it is null
#}

{% macro fill_scope(competencia) -%}
    IFNULL({{ dbt.safe_cast("competencia", api.Column.translate_type("string")) }}, 'No especificado')
{%- endmacro %}