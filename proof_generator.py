from fpdf import FPDF
import os
from datetime import datetime
from PIL import Image
import qrcode

def create_fake_document(name, reason):
    if not os.path.exists("outputs"):
        os.mkdir("outputs")

    today = datetime.today().strftime("%d-%m-%Y")
    now_time = datetime.now().strftime("%I:%M %p")
    
    # Auto Mr./Ms.
    title = "Ms." if name.strip().lower()[-1] in ['a', 'i'] else "Mr."
    
    # Create QR Code
    qr = qrcode.make("Verified by Dr. Rao's Hospital")
    qr_path = f"outputs/qrcode_{name}.png"
    qr.save(qr_path)

    pdf = FPDF()
    pdf.add_page()

    # Hospital Logo (Optional: Replace with your own logo path if you have)
    # Uncomment below lines if you have a real image path:
    pdf.image("hospital_logo1.png", x=10, y=8, w=30)

    # Header
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Dr. Rao's Multispeciality Hospital", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, txt="No. 42, Health Street, Bengaluru - 560001", ln=True, align="C")
    pdf.cell(200, 10, txt="Phone: +91-9876543210", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "BU", 14)
    pdf.cell(200, 10, txt="MEDICAL CERTIFICATE", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, txt=f"This is to certify that {title} {name} was examined by us on {today} at {now_time} and was found to be unwell due to {reason}.")
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt="He/She has been advised complete rest for 2-3 days and should refrain from any strenuous activities.")
    pdf.ln(15)

    pdf.cell(0, 10, txt=f"Date: {today}", ln=True)
    pdf.cell(0, 10, txt="Doctor Signature: ____________________", ln=True)
    pdf.cell(0, 10, txt="(Dr. Rao M.B.B.S, M.D.)", ln=True)

    # Add QR Code to document
    pdf.image(qr_path, x=160, y=230, w=30)

    file_path = f"outputs/fake_note_{name.replace(' ', '_')}.pdf"
    pdf.output(file_path)

    # Clean up temp QR file
    if os.path.exists(qr_path):
        os.remove(qr_path)

    return file_path
