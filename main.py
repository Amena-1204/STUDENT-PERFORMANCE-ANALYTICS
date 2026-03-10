from analysis.data_overview import data_overview
from analysis.performance_analysis import performance_analysis
from analysis.demographic_analysis import demographic_analysis
from analysis.risk_analysis import risk_analysis
from analysis.subject_analysis import subject_analysis

file_path = "data/students_large.csv"

df = data_overview(file_path)

performance_analysis(df)
demographic_analysis(df)
risk_analysis(df)
subject_analysis(df)