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
    Epoch 1000/50000, Mean Squared Error: 0.04325027496506921
Epoch 2000/50000, Mean Squared Error: 0.008820878088463845
Epoch 3000/50000, Mean Squared Error: 0.003982111500879858
Epoch 4000/50000, Mean Squared Error: 0.0024261732767400816
Epoch 5000/50000, Mean Squared Error: 0.00170212819836893
Epoch 6000/50000, Mean Squared Error: 0.0012939854899500028
Epoch 7000/50000, Mean Squared Error: 0.0010355756300989398
Epoch 8000/50000, Mean Squared Error: 0.0008587598599796632
Epoch 9000/50000, Mean Squared Error: 0.0007308788116768394
Epoch 10000/50000, Mean Squared Error: 0.0006344697524181635
Epoch 11000/50000, Mean Squared Error: 0.0005594077300516192
Epoch 12000/50000, Mean Squared Error: 0.0004994439689164265
Epoch 13000/50000, Mean Squared Error: 0.00045052568435356136
Epoch 14000/50000, Mean Squared Error: 0.00040991596519541974
Epoch 15000/50000, Mean Squared Error: 0.0003757034959322782
Epoch 16000/50000, Mean Squared Error: 0.00034651522655701353
Epoch 17000/50000, Mean Squared Error: 0.0003213406535994428
Epoch 18000/50000, Mean Squared Error: 0.0002994203878195782
Epoch 19000/50000, Mean Squared Error: 0.00028017324418810375
Epoch 20000/50000, Mean Squared Error: 0.0002631472191207463
Epoch 21000/50000, Mean Squared Error: 0.0002479857296822286
Epoch 22000/50000, Mean Squared Error: 0.00023440386449242448
Epoch 23000/50000, Mean Squared Error: 0.00022217135789946767
Epoch 24000/50000, Mean Squared Error: 0.0002111001747135287
Epoch 25000/50000, Mean Squared Error: 0.00020103531687207373
Epoch 26000/50000, Mean Squared Error: 0.00019184792037830784
Epoch 27000/50000, Mean Squared Error: 0.00018343000569684685
Epoch 28000/50000, Mean Squared Error: 0.00017569043888068355
Epoch 29000/50000, Mean Squared Error: 0.0001685517908287338
Epoch 30000/50000, Mean Squared Error: 0.00016194787078820864
Epoch 31000/50000, Mean Squared Error: 0.00015582177163723468
Epoch 32000/50000, Mean Squared Error: 0.00015012430761637098
Epoch 33000/50000, Mean Squared Error: 0.00014481275586869968
Epoch 34000/50000, Mean Squared Error: 0.00013984983525425104
Epoch 35000/50000, Mean Squared Error: 0.0001352028720088743
Epoch 36000/50000, Mean Squared Error: 0.0001308431136745939
Epoch 37000/50000, Mean Squared Error: 0.00012674516154530122
Epoch 38000/50000, Mean Squared Error: 0.00012288649848869209
Epoch 39000/50000, Mean Squared Error: 0.00011924709401538329
Epoch 40000/50000, Mean Squared Error: 0.00011580907229023952
Epoch 41000/50000, Mean Squared Error: 0.0001125564317228948
Epoch 42000/50000, Mean Squared Error: 0.00010947480705401279
Epoch 43000/50000, Mean Squared Error: 0.00010655126663265414
Epoch 44000/50000, Mean Squared Error: 0.00010377413897714097
Epoch 45000/50000, Mean Squared Error: 0.00010113286381586815
Epoch 46000/50000, Mean Squared Error: 9.861786368219622e-05
Epoch 47000/50000, Mean Squared Error: 9.622043283926725e-05
Epoch 48000/50000, Mean Squared Error: 9.393264087447151e-05
Epoch 49000/50000, Mean Squared Error: 9.174724875887762e-05
Epoch 50000/50000, Mean Squared Error: 8.965763553675559e-05
    
    
    """


    # Change this if your file is located elsewhere
    parse_and_plot_mse(input_string)