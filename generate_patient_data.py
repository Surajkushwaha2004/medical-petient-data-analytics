import pandas as pd
import numpy as np

def generate_patient_data(num_records=20):
    """
    Generate and display fake medical data for num_records patients.
    """
    np.random.seed(42)  
    data = pd.DataFrame({
        'id': np.arange(1, num_records + 1),
        'age': np.random.randint(20 * 365, 70 * 365, num_records),  
        'height': np.random.randint(150, 200, num_records), 
        'weight': np.random.uniform(50, 120, num_records),   
        'ap_hi': np.random.randint(90, 180, num_records),    
        'ap_lo': np.random.randint(60, 120, num_records),    
        'cholesterol': np.random.choice([1, 2, 3], num_records),  
        'gluc': np.random.choice([1, 2, 3], num_records),         
        'smoke': np.random.choice([0, 1], num_records),          
        'alco': np.random.choice([0, 1], num_records),           
        'active': np.random.choice([0, 1], num_records),         
        'cardio': np.random.choice([0, 1], num_records),          
    })
    print("\n📄 Generated Patient Data (Copy & Save This to a CSV File):\n")
    print(data.to_csv(index=False))

generate_patient_data(20)  
