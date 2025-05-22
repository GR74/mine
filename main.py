# Add this only if you're running from outside the THINKTANK directory
# import sys
# sys.path.append(r'C:\Users\gowri\thinktank\THINKTANK')

from EEG_Implement_Welch import EEG_Implement_Welch
from EEG_normalizedGamma_CMRO2 import plot_normalized_gamma_across_channels
from EEG_NeurovascularVariables import calculate_neurovascular_variables
from EEG_Plotting import EEG_Plotting


if __name__ == '__main__':
    # Path to your EEG input file (make sure the format matches expectations)
    EEG_file_path = 'C:/Users/gowri/thinktank/THINKTANK/last_time_testing_for_now.txt'

    # Step 1: Convert raw EEG to Welch spectra and get trial count
    ExampleCase = EEG_Implement_Welch(EEG_file_path)
    EEG_Welch_Spectra = ExampleCase[0]
    TrialCount = ExampleCase[1]

    # Step 2: Compute normalized gamma power from Welch spectra
    CMRO2Case = plot_normalized_gamma_across_channels(
        EEG_Welch_Spectra=EEG_Welch_Spectra,
        ElectrodeList=[
            'Fp1', 'Fp2', 'F3', 'F4', 'T5', 'T6', 'O1', 'O2',
            'F7', 'F8', 'C3', 'C4', 'T3', 'T4', 'P3', 'P4'
        ],
        Trials=TrialCount
    )

    # Step 3: Use gamma power to compute chemical variables (e.g., CMRO2, pO2)
    NeurovascularDataset = calculate_neurovascular_variables(CMRO2Case)

    # Step 4: Visualize or extract neurovascular output at a specific timestep
    # You can change the variable (e.g., 'CMRO2', 'pO2_cap', etc.), timestep, and number of nodes
    A = EEG_Plotting(
        Data_val=NeurovascularDataset['pO2_cap'],
        Timestep_Select=0,
        NodeNum=10
    )

    # Step 5: Get just the values for further use
    B = A[0]  # Concentration values
    print("First few chemical values:", B[:5])
