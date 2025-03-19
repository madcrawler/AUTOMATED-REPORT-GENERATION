import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

file_path = "sample_data.csv"
df = pd.read_csv(file_path)

summary = df.describe()

plt.figure(figsize=(6, 4))
df.hist(figsize=(8, 6))
plt.savefig("data_histogram.png")

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(200, 10, "Automated Data Report", ln=True, align="C")
        self.ln(10)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "", 12)

pdf.cell(200, 10, f"Dataset Summary:", ln=True, align="L")
pdf.ln(5)

for index, row in summary.iterrows():
    pdf.cell(200, 10, f"{index}: {row.to_list()}", ln=True)

pdf.image("data_histogram.png", x=10, y=None, w=180)

pdf.output("automated_report.pdf")

print("Report generated successfully!")
