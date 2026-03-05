import os
from Bio import SeqIO
import matplotlib.pyplot as plt

def plot_ab1_trace(file_path):
    try:
        record = SeqIO.read(file_path, "abi")
        trace_channels = record.annotations["abif_raw"]

        # Extract signal data
        a_trace = trace_channels["DATA9"]
        c_trace = trace_channels["DATA10"]
        g_trace = trace_channels["DATA11"]
        t_trace = trace_channels["DATA12"]

        # Plot
        plt.figure(figsize=(15, 5))
        plt.plot(a_trace, label="A", color="green", alpha=0.7)
        plt.plot(c_trace, label="C", color="blue", alpha=0.7)
        plt.plot(g_trace, label="G", color="black", alpha=0.7)
        plt.plot(t_trace, label="T", color="red", alpha=0.7)

        plt.title(f"Chromatogram Trace: {os.path.basename(file_path)}")
        plt.xlabel("Data Points")
        plt.ylabel("Signal Intensity")
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"⚠️ Error with {file_path}: {e}")

def plot_all_ab1_in_folder(folder_path="."):
    ab1_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".ab1")]
    if not ab1_files:
        print("❌ No .ab1 files found in the folder.")
        return
    for file in ab1_files:
        print(f"📄 Plotting: {file}")
        plot_ab1_trace(os.path.join(folder_path, file))

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"🔍 Searching for .ab1 files in: {current_dir}")
    plot_all_ab1_in_folder(current_dir)
