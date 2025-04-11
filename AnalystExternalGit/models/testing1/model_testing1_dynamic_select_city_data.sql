{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_testing1_post_dynamic_select_city_data_0",
    "database": "pipelinehub",
    "schema": "katherine"
  })
}}

WITH forecast_hourly_metric_0 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_testing1_source', 'prophecy__temp_testing1_pre_dynamic_select_city_data_0') }}

),

dynamic_select_city_data AS (

  {{
    DatabricksSqlBasics.DynamicSelect(
      'forecast_hourly_metric_0', 
      [
        { "name": "city_name", "dataType": "String" }, 
        { "name": "country_code", "dataType": "String" }, 
        { "name": "latitude", "dataType": "Double" }, 
        { "name": "longitude", "dataType": "Double" }, 
        { "name": "datetime_valid_local", "dataType": "Timestamp" }, 
        { "name": "gmt_offset", "dataType": "Double" }, 
        { "name": "cloud_base_height", "dataType": "Integer" }, 
        { "name": "cloud_cover_perc_total", "dataType": "Double" }, 
        { "name": "humidity_relative", "dataType": "Double" }, 
        { "name": "index_uv", "dataType": "Double" }, 
        { "name": "has_ice", "dataType": "Boolean" }, 
        { "name": "ice_lwe", "dataType": "Double" }, 
        { "name": "ice_probability", "dataType": "Integer" }, 
        { "name": "minutes_of_sun", "dataType": "Integer" }, 
        { "name": "has_precipitation", "dataType": "Boolean" }, 
        { "name": "precipitation_lwe", "dataType": "Double" }, 
        { "name": "precipitation_probability", "dataType": "Integer" }, 
        { "name": "precipitation_type_desc", "dataType": "String" }, 
        { "name": "has_rain", "dataType": "Boolean" }, 
        { "name": "rain_lwe", "dataType": "Double" }, 
        { "name": "rain_probability", "dataType": "Integer" }, 
        { "name": "snow_liquid_ratio_accuweather", "dataType": "Double" }, 
        { "name": "has_snow", "dataType": "Boolean" }, 
        { "name": "snow", "dataType": "Double" }, 
        { "name": "snow_lwe", "dataType": "Double" }, 
        { "name": "snow_probability", "dataType": "Integer" }, 
        { "name": "solar_irradiance", "dataType": "Double" }, 
        { "name": "temperature", "dataType": "Double" }, 
        { "name": "temperature_dew_point", "dataType": "Double" }, 
        { "name": "temperature_heat_index", "dataType": "Double" }, 
        { "name": "temperature_realfeel", "dataType": "Double" }, 
        { "name": "temperature_realfeel_shade", "dataType": "Double" }, 
        { "name": "temperature_wind_chill", "dataType": "Double" }, 
        { "name": "thunderstorm_probability", "dataType": "Integer" }, 
        { "name": "visibility", "dataType": "Double" }, 
        { "name": "weather_code", "dataType": "Integer" }, 
        { "name": "wind_direction", "dataType": "Double" }, 
        { "name": "wind_gust", "dataType": "Double" }, 
        { "name": "wind_speed", "dataType": "Double" }
      ], 
      ["String"], 
      'SELECT_FIELD_TYPES', 
      ''
    )
  }}

)

SELECT *

FROM dynamic_select_city_data
