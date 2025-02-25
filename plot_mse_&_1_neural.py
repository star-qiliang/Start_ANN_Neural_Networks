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
Epoch 1000/50000, Mean Squared Error: 0.162062026420012
Epoch 2000/50000, Mean Squared Error: 0.03885440015709809
Epoch 3000/50000, Mean Squared Error: 0.010705322465758556
Epoch 4000/50000, Mean Squared Error: 0.0054203376295673365
Epoch 5000/50000, Mean Squared Error: 0.0034899795326087443
Epoch 6000/50000, Mean Squared Error: 0.0025310592880581663
Epoch 7000/50000, Mean Squared Error: 0.001968238357622246
Epoch 8000/50000, Mean Squared Error: 0.0016018016213906624
Epoch 9000/50000, Mean Squared Error: 0.0013458076748461521
Epoch 10000/50000, Mean Squared Error: 0.001157632355009969
Epoch 11000/50000, Mean Squared Error: 0.0010138896455002305
Epoch 12000/50000, Mean Squared Error: 0.000900741823147481
Epoch 13000/50000, Mean Squared Error: 0.0008095061377908452
Epoch 14000/50000, Mean Squared Error: 0.0007344727786303026
Epoch 15000/50000, Mean Squared Error: 0.0006717401207043247
Epoch 16000/50000, Mean Squared Error: 0.0006185555394850926
Epoch 17000/50000, Mean Squared Error: 0.0005729238304957278
Epoch 18000/50000, Mean Squared Error: 0.0005333649076825722
Epoch 19000/50000, Mean Squared Error: 0.0004987585544267203
Epoch 20000/50000, Mean Squared Error: 0.00046824190944386916
Epoch 21000/50000, Mean Squared Error: 0.00044113997077276513
Epoch 22000/50000, Mean Squared Error: 0.00041691737931083274
Epoch 23000/50000, Mean Squared Error: 0.00039514427133905436
Epoch 24000/50000, Mean Squared Error: 0.00037547164653792373
Epoch 25000/50000, Mean Squared Error: 0.0003576133040703678
Epoch 26000/50000, Mean Squared Error: 0.0003413323961569294
Epoch 27000/50000, Mean Squared Error: 0.00032643128219643036
Epoch 28000/50000, Mean Squared Error: 0.0003127437780038488
Epoch 29000/50000, Mean Squared Error: 0.0003001291672847501
Epoch 30000/50000, Mean Squared Error: 0.0002884675262253382
Epoch 31000/50000, Mean Squared Error: 0.00027765603801826165
Epoch 32000/50000, Mean Squared Error: 0.0002676060617688218
Epoch 33000/50000, Mean Squared Error: 0.00025824078204465345
Epoch 34000/50000, Mean Squared Error: 0.00024949330950944026
Epoch 35000/50000, Mean Squared Error: 0.00024130513503198823
Epoch 36000/50000, Mean Squared Error: 0.00023362486302756763
Epoch 37000/50000, Mean Squared Error: 0.00022640716705539488
Epoch 38000/50000, Mean Squared Error: 0.00021961192357978845
Epoch 39000/50000, Mean Squared Error: 0.00021320348950435664
Epoch 40000/50000, Mean Squared Error: 0.00020715009645689149
Epoch 41000/50000, Mean Squared Error: 0.00020142334044404096
Epoch 42000/50000, Mean Squared Error: 0.00019599774984710737
Epoch 43000/50000, Mean Squared Error: 0.00019085041811219363
Epoch 44000/50000, Mean Squared Error: 0.00018596069013365448
Epoch 45000/50000, Mean Squared Error: 0.00018130989341295616
Epoch 46000/50000, Mean Squared Error: 0.00017688110672559038
Epoch 47000/50000, Mean Squared Error: 0.0001726589603435741
Epoch 48000/50000, Mean Squared Error: 0.0001686294629147903
Epoch 49000/50000, Mean Squared Error: 0.00016477985094918038
Epoch 50000/50000, Mean Squared Error: 0.00016109845754874906
    
    """


    # Change this if your file is located elsewhere
    parse_and_plot_mse(input_string)