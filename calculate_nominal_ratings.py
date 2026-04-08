import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from pydantic import BaseModel, Field
import openmeteo_requests
import requests_cache
from retry_requests import retry
import math
import requests
import csv
import os
from datetime import datetime
from zoneinfo import ZoneInfo
import pvlib
import folium
import webbrowser
import random
#from weathercsv import get_solar_irradiance_for_location
import time