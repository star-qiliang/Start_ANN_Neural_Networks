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

Epoch 1000/50000, Mean Squared Error: 0.06883548211097312
Epoch 2000/50000, Mean Squared Error: 0.012796758264368428
Epoch 3000/50000, Mean Squared Error: 0.005353006977896305
Epoch 4000/50000, Mean Squared Error: 0.0031429210734732357
Epoch 5000/50000, Mean Squared Error: 0.0021578489271422844
Epoch 6000/50000, Mean Squared Error: 0.0016171667140479956
Epoch 7000/50000, Mean Squared Error: 0.0012810245078447155
Epoch 8000/50000, Mean Squared Error: 0.0010540714768797698
Epoch 9000/50000, Mean Squared Error: 0.0008916058545907704
Epoch 10000/50000, Mean Squared Error: 0.0007701223182367613
Epoch 11000/50000, Mean Squared Error: 0.0006761705205975343
Epoch 12000/50000, Mean Squared Error: 0.0006015374565855576
Epoch 13000/50000, Mean Squared Error: 0.0005409433774184037
Epoch 14000/50000, Mean Squared Error: 0.0004908494141337684
Epoch 15000/50000, Mean Squared Error: 0.000448800079651032
Epoch 16000/50000, Mean Squared Error: 0.00041304127159587036
Epoch 17000/50000, Mean Squared Error: 0.00038228840939438075
Epoch 18000/50000, Mean Squared Error: 0.0003555803637157373
Epoch 19000/50000, Mean Squared Error: 0.0003321844381370736
Epoch 20000/50000, Mean Squared Error: 0.00031153281279392776
Epoch 21000/50000, Mean Squared Error: 0.000293178978894948
Epoch 22000/50000, Mean Squared Error: 0.00027676722196287855
Epoch 23000/50000, Mean Squared Error: 0.0002620108283955786
Epoch 24000/50000, Mean Squared Error: 0.0002486762496019062
Epoch 25000/50000, Mean Squared Error: 0.00023657141372868836
Epoch 26000/50000, Mean Squared Error: 0.00022553697544985758
Epoch 27000/50000, Mean Squared Error: 0.00021543968009584902
Epoch 28000/50000, Mean Squared Error: 0.00020616727139650026
Epoch 29000/50000, Mean Squared Error: 0.00019762454112521075
Epoch 30000/50000, Mean Squared Error: 0.00018973023377952714
Epoch 31000/50000, Mean Squared Error: 0.00018241459870217843
Epoch 32000/50000, Mean Squared Error: 0.00017561743755297832
Epoch 33000/50000, Mean Squared Error: 0.00016928653443063293
Epoch 34000/50000, Mean Squared Error: 0.00016337638424179237
Epoch 35000/50000, Mean Squared Error: 0.00015784715548123934
Epoch 36000/50000, Mean Squared Error: 0.00015266383869486043
Epoch 37000/50000, Mean Squared Error: 0.0001477955431072157
Epoch 38000/50000, Mean Squared Error: 0.00014321491229194963
Epoch 39000/50000, Mean Squared Error: 0.00013889763610805303
Epoch 40000/50000, Mean Squared Error: 0.00013482204095918406
Epoch 41000/50000, Mean Squared Error: 0.00013096874414583715
Epoch 42000/50000, Mean Squared Error: 0.00012732036095192156
Epoch 43000/50000, Mean Squared Error: 0.00012386125534476629
Epoch 44000/50000, Mean Squared Error: 0.00012057732692224258
Epoch 45000/50000, Mean Squared Error: 0.00011745582812506381
Epoch 46000/50000, Mean Squared Error: 0.00011448520683169519
Epoch 47000/50000, Mean Squared Error: 0.00011165497033078004
Epoch 48000/50000, Mean Squared Error: 0.00010895556737038078
Epoch 49000/50000, Mean Squared Error: 0.00010637828555160077
Epoch 50000/50000, Mean Squared Error: 0.00010391516179508468

    
    """


    # Change this if your file is located elsewhere
    parse_and_plot_mse(input_string)