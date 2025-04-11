Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    forecast_hourly_metric_0 = SourceTask(
        task_id = "forecast_hourly_metric_0", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "dbxsql"), 
        format = DATABRICKSFormat(
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          description = "Comprehensive weather data capturing various atmospheric conditions, aiding in weather analysis and forecasting.", 
          schema = {
            "fields": [{"dataType" : {"type" : "utf8"}, "description" : "Name of the city", "name" : "city_name"},                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "Code representing the country of the city", 
                          "name": "country_code"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Geographical latitude of the city", 
                          "name": "latitude"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "The longitudinal coordinate of the city", 
                          "name": "longitude"
                        },                         {
                          "dataType": {"type" : "timestamp"}, 
                          "description": "The local date and time when the weather data is valid", 
                          "name": "datetime_valid_local"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "The offset from GMT for the local time zone", 
                          "name": "gmt_offset"
                        },                         {
                          "dataType": {"type" : "int32"}, 
                          "description": "Height of the cloud base above ground level in meters", 
                          "name": "cloud_base_height"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Total percentage of cloud cover in the sky", 
                          "name": "cloud_cover_perc_total"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Relative humidity percentage in the air", 
                          "name": "humidity_relative"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "UV index indicating the strength of ultraviolet radiation", 
                          "name": "index_uv"
                        },                         {
                          "dataType": {"type" : "bool"}, 
                          "description": "Indicates whether ice is present in the weather conditions", 
                          "name": "has_ice"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Liquid equivalent of ice measured in the weather conditions", 
                          "name": "ice_lwe"
                        },                         {
                          "dataType": {"type" : "int32"}, 
                          "description": "Probability of ice occurrence in the weather conditions", 
                          "name": "ice_probability"
                        },                         {
                          "dataType": {"type" : "int32"}, 
                          "description": "Total minutes of sunshine expected", 
                          "name": "minutes_of_sun"
                        },                         {
                          "dataType": {"type" : "bool"}, 
                          "description": "Indicates whether precipitation is expected", 
                          "name": "has_precipitation"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Liquid equivalent of precipitation measured", 
                          "name": "precipitation_lwe"
                        },                         {
                          "dataType": {"type" : "int32"}, 
                          "description": "Probability of precipitation occurring", 
                          "name": "precipitation_probability"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "Description of the type of precipitation expected", 
                          "name": "precipitation_type_desc"
                        },                         {
                          "dataType": {"type" : "bool"}, 
                          "description": "Indicates whether it is currently raining", 
                          "name": "has_rain"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Liquid equivalent of rain measured", 
                          "name": "rain_lwe"
                        },                         {
                          "dataType": {"type" : "int32"}, 
                          "description": "Probability of rain occurring", 
                          "name": "rain_probability"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Ratio of liquid equivalent of snow as reported by AccuWeather", 
                          "name": "snow_liquid_ratio_accuweather"
                        },                         {
                          "dataType": {"type" : "bool"}, 
                          "description": "Indicates whether snow is present", 
                          "name": "has_snow"
                        },                         {"dataType" : {"type" : "float64"}, "description" : "Amount of snow measured", "name" : "snow"},                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Liquid equivalent of snow measured in the area", 
                          "name": "snow_lwe"
                        },                         {
                          "dataType": {"type" : "int32"}, 
                          "description": "Probability of snow occurring in the forecast", 
                          "name": "snow_probability"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Amount of solar energy received in the area", 
                          "name": "solar_irradiance"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Current temperature in the specified location", 
                          "name": "temperature"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Dew point temperature indicating moisture in the air", 
                          "name": "temperature_dew_point"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Apparent temperature considering humidity and temperature effects", 
                          "name": "temperature_heat_index"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "The perceived temperature experienced by individuals", 
                          "name": "temperature_realfeel"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "The perceived temperature in shaded areas", 
                          "name": "temperature_realfeel_shade"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "The temperature adjusted for wind chill effects", 
                          "name": "temperature_wind_chill"
                        },                         {
                          "dataType": {"type" : "int32"}, 
                          "description": "Probability of a thunderstorm occurring", 
                          "name": "thunderstorm_probability"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Distance at which objects can be clearly seen", 
                          "name": "visibility"
                        },                         {
                          "dataType": {"type" : "int32"}, 
                          "description": "Code representing the current weather conditions", 
                          "name": "weather_code"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Direction from which the wind is blowing", 
                          "name": "wind_direction"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Maximum wind gust speed recorded", 
                          "name": "wind_gust"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Average speed of the wind", 
                          "name": "wind_speed"
                        }], 
            "providerType": "Arrow"
          }
        ), 
        tableFullName = {"database" : "samples", "name" : "forecast_hourly_metric", "schema" : "accuweather"}
    )
