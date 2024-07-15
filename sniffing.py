import tkinter as tk
from tkinter import scrolledtext
from scapy.all import sniff, AsyncSniffer

class NetworkSnifferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Sniffer")
        self.root.geometry("800x600")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)
        self.text_area.grid(column=0, row=0, padx=10, pady=10)

        self.start_button = tk.Button(root, text="Start Sniffing", command=self.start_sniffing)
        self.start_button.grid(column=0, row=1, padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Stop Sniffing", command=self.stop_sniffing)
        self.stop_button.grid(column=0, row=2, padx=10, pady=10)
        self.stop_button.config(state=tk.DISABLED)

        self.sniffer = None

    def packet_callback(self, packet):
        self.text_area.insert(tk.END, packet.show(dump=True) + "\n" + "-"*50 + "\n")
        self.text_area.yview(tk.END)

    def start_sniffing(self):
        self.text_area.insert(tk.END, "Starting packet sniffing...\n")
        self.root.update()
        self.sniffer = AsyncSniffer(prn=self.packet_callback)
        self.sniffer.start()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_sniffing(self):
        if self.sniffer:
            self.sniffer.stop()
            self.sniffer = None
            self.text_area.insert(tk.END, "Stopped packet sniffing.\n")
            self.root.update()
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSnifferApp(root)
    root.mainloop()
