# Windows Attack Techniques Dataset
This project is a Python script used to process a dataset containing Windows attack techniques. The dataset is extracted from a YAML file, which includes information about the attack techniques, tactics, and associated attack commands. The script converts the YAML file into a Pandas DataFrame for further analysis and manipulation.

## How to Use ? 
Prepare the YAML file: Create a windows-index.yaml file or use an existing YAML file. This file should contain the attack techniques, tactics, and attack commands.

Install the required libraries: Make sure you have the pandas and pyyaml libraries installed. If not, you can install them using the following command:

```pip install pandas pyyaml```

```Run the script: Execute the main.py file to read the YAML file and generate the dataset. The script will process the attack techniques data and output a DataFrame.```

Utilize the dataset: Once you have the DataFrame, you can perform various operations such as data analysis, visualization, or any other tasks based on your requirements. You can explore the attack techniques, devise defense strategies, or use the dataset for any other purpose.

## Example Output
Below is an example of the dataset generated by running the script:

Tactic	Technique	Attack Command
Defense-Evasion	Signed Binary Proxy Execution: Rundll32	rundll32.exe javascript:"..\mshtml,RunHTMLApplication ";
Defense-Evasion	Signed Binary Proxy Execution: Rundll32	rundll32 vbscript:"..\mshtml,RunHTMLApplication ";
Defense-Evasion	Signed Binary Proxy Execution: Rundll32	rundll32 vbscript:"..\mshtml,#135 "+String(CryptoAPI();
Defense-Evasion	Signed Binary Proxy Execution: Rundll32	rundll32.exe advpack.dll,LaunchINFSection #{inf_file},...
Defense-Evasion	Signed Binary Proxy Execution: Rundll32	rundll32.exe ieadvpack.dll,LaunchINFSection #{inf_file}...
Please note that this is just a sample output to demonstrate the format of the dataset. The actual dataset will contain more entries with their corresponding attack techniques, tactics, and commands.

## Applications

The Windows Attack Techniques Dataset and the provided script can be used in various scenarios, including:

Cybersecurity research: Analyzing attack techniques and patterns to identify vulnerabilities and improve defense strategies.
Red teaming: Simulating real-world attacks to assess the security of systems and networks.
Blue teaming: Developing defensive strategies and countermeasures against known attack techniques.
Security training and education: Using the dataset as a learning resource for students and professionals interested in cybersecurity.
Feel free to explore and leverage this dataset according to your specific requirements.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
