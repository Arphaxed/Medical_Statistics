import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data for hospital management (e.g., patient admissions, occupancy, treatments)
# Example of DataFrame for patient admissions and hospital occupancy over time
data = {
    'Date': pd.date_range(start='2024-01-01', periods=6, freq='ME'),
    'PatientAdmissions': [120, 150, 140, 160, 180, 200],
    'HospitalOccupancy': [75, 80, 78, 85, 90, 92],
    'EmergencyTreatments': [50, 60, 55, 65, 70, 80],
    'SurgicalTreatments': [30, 35, 40, 45, 50, 55]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Create visualizations using Plotly
fig1 = px.line(df, x='Date', y='PatientAdmissions', title='Patient Admissions Over Time')
fig2 = px.line(df, x='Date', y='HospitalOccupancy', title='Hospital Occupancy Rate Over Time')
fig3 = px.bar(df, x='Date', y=['EmergencyTreatments', 'SurgicalTreatments'], barmode='group', title='Types of Treatments Over Time')

# Define the layout of the app
app.layout = html.Div([
    html.H1("Hospital Management Dashboard", style={'text-align': 'center'}),
    
    # Display patient admissions graph
    html.Div([
        dcc.Graph(
            id='patient-admissions',
            figure=fig1
        )
    ], style={'margin-bottom': '50px'}),
    
    # Display hospital occupancy graph
    html.Div([
        dcc.Graph(
            id='hospital-occupancy',
            figure=fig2
        )
    ], style={'margin-bottom': '50px'}),

    # Display treatments (emergency and surgical)
    html.Div([
        dcc.Graph(
            id='treatment-types',
            figure=fig3
        )
    ])
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
