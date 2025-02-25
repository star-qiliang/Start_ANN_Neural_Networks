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

Epoch 1000/50000, Mean Squared Error: 0.03837547778019553
Epoch 2000/50000, Mean Squared Error: 0.009431962205818949
Epoch 3000/50000, Mean Squared Error: 0.0047392955813999795
Epoch 4000/50000, Mean Squared Error: 0.003061506598109153
Epoch 5000/50000, Mean Squared Error: 0.002230157020828226
Epoch 6000/50000, Mean Squared Error: 0.0017413796798757565
Epoch 7000/50000, Mean Squared Error: 0.0014222657418601604
Epoch 8000/50000, Mean Squared Error: 0.001198672245420036
Epoch 9000/50000, Mean Squared Error: 0.0010338454165268946
Epoch 10000/50000, Mean Squared Error: 0.0009076039235497587
Epoch 11000/50000, Mean Squared Error: 0.0008079896535640906
Epoch 12000/50000, Mean Squared Error: 0.0007274868584610203
Epoch 13000/50000, Mean Squared Error: 0.0006611445205302883
Epoch 14000/50000, Mean Squared Error: 0.0006055735712456271
Epoch 15000/50000, Mean Squared Error: 0.0005583788810774363
Epoch 16000/50000, Mean Squared Error: 0.0005178214801037492
Epoch 17000/50000, Mean Squared Error: 0.0004826093010655879
Epoch 18000/50000, Mean Squared Error: 0.0004517629377997979
Epoch 19000/50000, Mean Squared Error: 0.0004245268918965249
Epoch 20000/50000, Mean Squared Error: 0.00040030933026536633
Epoch 21000/50000, Mean Squared Error: 0.0003786402373841667
Epoch 22000/50000, Mean Squared Error: 0.00035914174250969093
Epoch 23000/50000, Mean Squared Error: 0.0003415066903369701
Epoch 24000/50000, Mean Squared Error: 0.00032548290782560553
Epoch 25000/50000, Mean Squared Error: 0.00031086147979068326
Epoch 26000/50000, Mean Squared Error: 0.0002974678928922266
Epoch 27000/50000, Mean Squared Error: 0.0002851552632478503
Epoch 28000/50000, Mean Squared Error: 0.0002737990986050112
Epoch 29000/50000, Mean Squared Error: 0.0002632932050718756
Epoch 30000/50000, Mean Squared Error: 0.00025354645751419233
Epoch 31000/50000, Mean Squared Error: 0.0002444802287034165
Epoch 32000/50000, Mean Squared Error: 0.00023602632594731655
Epoch 33000/50000, Mean Squared Error: 0.0002281253223040248
Epoch 34000/50000, Mean Squared Error: 0.00022072519725197825
Epoch 35000/50000, Mean Squared Error: 0.00021378022201473654
Epoch 36000/50000, Mean Squared Error: 0.00020725003977134284
Epoch 37000/50000, Mean Squared Error: 0.00020109890220792884
Epoch 38000/50000, Mean Squared Error: 0.00019529503232488914
Epoch 39000/50000, Mean Squared Error: 0.00018981008984288262
Epoch 40000/50000, Mean Squared Error: 0.00018461872047651365
Epoch 41000/50000, Mean Squared Error: 0.00017969817414733433
Epoch 42000/50000, Mean Squared Error: 0.00017502798016434738
Epoch 43000/50000, Mean Squared Error: 0.00017058966971518074
Epoch 44000/50000, Mean Squared Error: 0.00016636653783458767
Epoch 45000/50000, Mean Squared Error: 0.00016234343846278416
Epoch 46000/50000, Mean Squared Error: 0.00015850660735881167
Epoch 47000/50000, Mean Squared Error: 0.00015484350855808816
Epoch 48000/50000, Mean Squared Error: 0.00015134270080827312
Epoch 49000/50000, Mean Squared Error: 0.0001479937210207022
Epoch 50000/50000, Mean Squared Error: 0.0001447869822656395



    """


    # Change this if your file is located elsewhere
    parse_and_plot_mse(input_string)