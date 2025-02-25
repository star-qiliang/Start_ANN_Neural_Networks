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

Epoch 1000/50000, Mean Squared Error: 0.022762571923548226
Epoch 2000/50000, Mean Squared Error: 0.005495847950328016
Epoch 3000/50000, Mean Squared Error: 0.00275828118922366
Epoch 4000/50000, Mean Squared Error: 0.0017734502871442814
Epoch 5000/50000, Mean Squared Error: 0.001284986782361268
Epoch 6000/50000, Mean Squared Error: 0.0009981940726567784
Epoch 7000/50000, Mean Squared Error: 0.0008113869470725735
Epoch 8000/50000, Mean Squared Error: 0.0006808495761424441
Epoch 9000/50000, Mean Squared Error: 0.0005848909156167818
Epoch 10000/50000, Mean Squared Error: 0.000511600770405264
Epoch 11000/50000, Mean Squared Error: 0.00045392619804159257
Epoch 12000/50000, Mean Squared Error: 0.00040743862179189926
Epoch 13000/50000, Mean Squared Error: 0.00036922413538226803
Epoch 14000/50000, Mean Squared Error: 0.0003372907234331637
Epoch 15000/50000, Mean Squared Error: 0.00031023253686242574
Epoch 16000/50000, Mean Squared Error: 0.0002870303248419429
Epoch 17000/50000, Mean Squared Error: 0.0002669278712102983
Epoch 18000/50000, Mean Squared Error: 0.0002493527818595924
Epoch 19000/50000, Mean Squared Error: 0.0002338641550104116
Epoch 20000/50000, Mean Squared Error: 0.00022011709220132026
Epoch 21000/50000, Mean Squared Error: 0.000207838067920008
Epoch 22000/50000, Mean Squared Error: 0.00019680748139976474
Epoch 23000/50000, Mean Squared Error: 0.0001868470677809517
Epoch 24000/50000, Mean Squared Error: 0.00017781066448428252
Epoch 25000/50000, Mean Squared Error: 0.00016957733699014875
Epoch 26000/50000, Mean Squared Error: 0.00016204619147482672
Epoch 27000/50000, Mean Squared Error: 0.0001551324117779525
Epoch 28000/50000, Mean Squared Error: 0.00014876419732081712
Epoch 29000/50000, Mean Squared Error: 0.00014288037243988954
Epoch 30000/50000, Mean Squared Error: 0.000137428501934686
Epoch 31000/50000, Mean Squared Error: 0.00013236339240121924
Epoch 32000/50000, Mean Squared Error: 0.00012764589051560845
Epoch 33000/50000, Mean Squared Error: 0.0001232419120141218
Epoch 34000/50000, Mean Squared Error: 0.00011912165145042534
Epoch 35000/50000, Mean Squared Error: 0.00011525893475814327
Epoch 36000/50000, Mean Squared Error: 0.00011163068547657886
Epoch 37000/50000, Mean Squared Error: 0.00010821648208650644
Epoch 38000/50000, Mean Squared Error: 0.0001049981888651557
Epoch 39000/50000, Mean Squared Error: 0.00010195964643833971
Epoch 40000/50000, Mean Squared Error: 9.908641109343855e-05
Epoch 41000/50000, Mean Squared Error: 9.636553414336725e-05
Epoch 42000/50000, Mean Squared Error: 9.378537436156112e-05
Epoch 43000/50000, Mean Squared Error: 9.133543786159043e-05
Epoch 44000/50000, Mean Squared Error: 8.900624086064058e-05
Epoch 45000/50000, Mean Squared Error: 8.678919161037591e-05
Epoch 46000/50000, Mean Squared Error: 8.467648845141209e-05
Epoch 47000/50000, Mean Squared Error: 8.266103148663647e-05
Epoch 48000/50000, Mean Squared Error: 8.073634580266773e-05
Epoch 49000/50000, Mean Squared Error: 7.889651452024748e-05
Epoch 50000/50000, Mean Squared Error: 7.713612024010168e-05
    


    
    """


    # Change this if your file is located elsewhere
    parse_and_plot_mse(input_string)