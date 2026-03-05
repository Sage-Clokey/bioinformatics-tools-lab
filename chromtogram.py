from Bio import SeqIO
import matplotlib.pyplot as plt

# Load your .ab1 file
record = SeqIO.read("your_file.ab1", "abi")

# Extract trace data (A, C, G, T signals)
trace_channels = record.annotations["abif_raw"]
a_trace = trace_channels["DATA9"]
c_trace = trace_channels["DATA10"]
g_trace = trace_channels["DATA11"]
t_trace = trace_channels["DATA12"]

# Plot signals
plt.figure(figsize=(15, 5))
plt.plot(a_trace, label="A", alpha=0.7)
plt.plot(c_trace, label="C", alpha=0.7)
plt.plot(g_trace, label="G", alpha=0.7)
plt.plot(t_trace, label="T", alpha=0.7)
plt.title("Sanger Sequencing Trace")
plt.xlabel("Data Points")
plt.ylabel("Signal Intensity")
plt.legend()
plt.tight_layout()
plt.show()
