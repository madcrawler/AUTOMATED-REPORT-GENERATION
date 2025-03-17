# AUTOMATED-REPORT-GENERATION
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



*CSV FILE 
print("Report generated successfully!")
[Uploading sample_data.csv…]()Product,Sales,Profit,Quantity
Tablet,4858,2560,25
Keyboard,27252,3573,24
Tablet,48653,7885,20
Tablet,35411,9661,17
Smartwatch,35638,2962,30
Speakers,34613,6515,13
Monitor,58596,9295,11
Laptop,4371,2934,23
Monitor,28917,9946,19
Smartphone,20408,733,16
Monitor,22240,5078,20
Keyboard,34681,9307,19
Mouse,15926,5271,6
Keyboard,46344,5453,22
Monitor,49716,4616,6
Keyboard,33723,3114,8
Printer,19501,3264,27
Monitor,13914,5659,8
Headphones,24876,7024,5
Smartwatch,42636,5497,16
Keyboard,49841,3615,23
Smartphone,24554,5741,10
Laptop,42577,3510,27
Monitor,10612,6214,20
Mouse,44732,8790,7
Headphones,36967,1549,6
Headphones,40189,3308,11
Speakers,17604,3752,12
Smartwatch,51700,3223,21
Printer,35218,3902,27
Printer,58554,700,8
Headphones,55795,9311,17
Laptop,11489,1730,19
Keyboard,34708,1574,11
Headphones,36773,9158,27
Smartphone,34641,2130,10
Headphones,54225,2049,8
Headphones,14396,7278,26
Printer,31272,3141,13
Monitor,47547,4802,5
Printer,17718,7851,21
Smartphone,42411,3509,15
Tablet,45320,4400,22
Speakers,24138,5635,5
Laptop,39101,2014,27
Keyboard,53129,2428,14
Speakers,16235,1663,5
Smartwatch,24036,3794,19
Speakers,36811,2738,13
Smartwatch,23297,7850,25
Monitor,47897,8618,20
Laptop,25298,6065,15
Headphones,53392,7508,25
Tablet,26836,1133,6
Printer,23350,9508,15
Smartphone,30706,8687,12
Smartwatch,30649,8444,22
Headphones,22211,8305,9
Printer,20194,9775,20
Laptop,45124,5282,8
Headphones,11576,1518,18
Keyboard,36962,5720,22
Mouse,29350,951,17
Tablet,49609,1175,27
Keyboard,35709,9182,15
Mouse,18271,7714,12
Speakers,33526,8586,29
Headphones,34795,4520,29
Headphones,10154,2010,16
Headphones,39150,855,5
Smartphone,8625,6907,25
Smartwatch,55587,1123,12
Mouse,36108,6176,20
Speakers,36527,1680,14
Smartwatch,36792,1524,25
Headphones,24086,9777,9
Keyboard,36911,7278,22
Monitor,9863,7495,30
Tablet,14205,2099,26
Mouse,42816,8282,25
Smartwatch,9070,7583,24
Printer,5308,4239,9
Smartphone,39672,2385,30
Smartphone,12051,1840,6
Smartphone,55765,2383,30
Monitor,23915,3796,30
Keyboard,28023,2496,22
Laptop,26407,5316,11
Smartwatch,4698,8197,24
Headphones,38898,4544,19
Smartwatch,19266,8310,29
Speakers,56215,4318,16
Headphones,17014,9262,16
Mouse,44449,5609,23
Headphones,51410,5269,12
Speakers,9625,1047,6
Mouse,47190,8989,22
Keyboard,24064,7150,29
Laptop,22627,3371,30
Speakers,51718,6084,6




