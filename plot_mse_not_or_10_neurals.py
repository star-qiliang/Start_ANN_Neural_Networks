import re
import matplotlib.pyplot as plt

def parse_and_plot_mse(string):
    """
    Parses a text file containing lines with epoch and MSE values,
    then plots the MSE over epochs.
    Expected line format:
        "Epoch <epoch_number>/<total>, Mean Squared Error: <mse_value>"
    """
    epochs = []
    mse_values = []
    
    # Regular expression to capture the epoch number and MSE value.
    # This regex looks for:
    #    - "Epoch " followed by one or more digits (captured)
    #    - A forward slash and some digits (ignored in this case)
    #    - ", Mean Squared Error: " followed by the mse value (captured)
    pattern = re.compile(r"Epoch (\d+)/\d+, Mean Squared Error: ([\d\.eE+-]+)")
    
    # # Open and parse the file line by line.
    # with open(file_path, "r") as file:
    #     for line in file:
    #         match = pattern.search(line)
    #         if match:
    #             epoch = int(match.group(1))
    #             mse = float(match.group(2))
    #             epochs.append(epoch)
    #             mse_values.append(mse)


    # Parse the string line by line.
    for line in string.split("\n"):
        match = pattern.search(line)
        if match:
            epoch = int(match.group(1))
            mse = float(match.group(2))
            epochs.append(epoch)
            mse_values.append(mse)

    # Check if any data was parsed.
    if not epochs or not mse_values:
        print("No valid data found in the file.")
        return
    
    # Create a plot of MSE values over epochs.
    plt.figure(figsize=(10, 6))
    plt.plot(epochs, mse_values, marker="o", linestyle="-", color="blue")
    plt.title("Mean Squared Error over Epochs")
    plt.xlabel("Epoch")
    plt.ylabel("Mean Squared Error")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    input_string = """

Epoch 1000/50000, Mean Squared Error: 0.0077804276663328
Epoch 2000/50000, Mean Squared Error: 0.0026614879027416416
Epoch 3000/50000, Mean Squared Error: 0.0014849775579338369
Epoch 4000/50000, Mean Squared Error: 0.0009999140416529666
Epoch 5000/50000, Mean Squared Error: 0.000742563639066824
Epoch 6000/50000, Mean Squared Error: 0.0005853773153074355
Epoch 7000/50000, Mean Squared Error: 0.00048033525307698366
Epoch 8000/50000, Mean Squared Error: 0.0004056202168795577
Epoch 9000/50000, Mean Squared Error: 0.00034998565915772214
Epoch 10000/50000, Mean Squared Error: 0.00030708154233247343
Epoch 11000/50000, Mean Squared Error: 0.0002730668120289172
Epoch 12000/50000, Mean Squared Error: 0.000245489143714802
Epoch 13000/50000, Mean Squared Error: 0.00022271323637427826
Epoch 14000/50000, Mean Squared Error: 0.00020360885891554777
Epoch 15000/50000, Mean Squared Error: 0.00018737107398438067
Epoch 16000/50000, Mean Squared Error: 0.0001734118130714607
Epoch 17000/50000, Mean Squared Error: 0.00016129191850365468
Epoch 18000/50000, Mean Squared Error: 0.00015067711986808057
Epoch 19000/50000, Mean Squared Error: 0.00014130868722695813
Epoch 20000/50000, Mean Squared Error: 0.00013298337154716338
Epoch 21000/50000, Mean Squared Error: 0.0001255393863558882
Epoch 22000/50000, Mean Squared Error: 0.00011884641635586719
Epoch 23000/50000, Mean Squared Error: 0.00011279836947280263
Epoch 24000/50000, Mean Squared Error: 0.0001073080348289825
Epoch 25000/50000, Mean Squared Error: 0.00010230308839337063
Epoch 26000/50000, Mean Squared Error: 9.772306695773238e-05
Epoch 27000/50000, Mean Squared Error: 9.351704810141373e-05
Epoch 28000/50000, Mean Squared Error: 8.964185180281167e-05
Epoch 29000/50000, Mean Squared Error: 8.606063224990419e-05
Epoch 30000/50000, Mean Squared Error: 8.274176484694206e-05
Epoch 31000/50000, Mean Squared Error: 7.96579588948339e-05
Epoch 32000/50000, Mean Squared Error: 7.678554447935783e-05
Epoch 33000/50000, Mean Squared Error: 7.410389505846682e-05
Epoch 34000/50000, Mean Squared Error: 7.159495664627488e-05
Epoch 35000/50000, Mean Squared Error: 6.924286139459263e-05
Epoch 36000/50000, Mean Squared Error: 6.703360849057419e-05
Epoch 37000/50000, Mean Squared Error: 6.495479911924009e-05
Epoch 38000/50000, Mean Squared Error: 6.299541513193714e-05
Epoch 39000/50000, Mean Squared Error: 6.114563326403275e-05
Epoch 40000/50000, Mean Squared Error: 5.939666843545899e-05
Epoch 41000/50000, Mean Squared Error: 5.7740640974590454e-05
Epoch 42000/50000, Mean Squared Error: 5.617046362365329e-05
Epoch 43000/50000, Mean Squared Error: 5.4679744981536925e-05
Epoch 44000/50000, Mean Squared Error: 5.326270666921661e-05
Epoch 45000/50000, Mean Squared Error: 5.1914112002302504e-05
Epoch 46000/50000, Mean Squared Error: 5.062920435384822e-05
Epoch 47000/50000, Mean Squared Error: 4.9403653710361715e-05
Epoch 48000/50000, Mean Squared Error: 4.823351018191107e-05
Epoch 49000/50000, Mean Squared Error: 4.7115163436384156e-05
Epoch 50000/50000, Mean Squared Error: 4.604530719822024e-05


    """


    # Change this if your file is located elsewhere
    parse_and_plot_mse(input_string)