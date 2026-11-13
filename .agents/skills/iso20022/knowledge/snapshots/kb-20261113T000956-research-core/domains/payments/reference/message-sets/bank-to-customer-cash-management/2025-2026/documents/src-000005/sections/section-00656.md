---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.2 CodeSet", "6.2.2.7 CardDataReading1Code"]
file_pages: [889]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.2.7 CardDataReading1Code

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 889 to 889.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 889

```text
CodeName Name Definition
NPIN OnLinePIN On-line PIN authentication (Personal
Identification Number).
FPIN OfflinePIN Off-line PIN authentication (Personal
Identification Number).
CPSG SignatureCapture Electronic signature capture (handwritten
signature).
PPSG PaperSignature Handwritten paper signature.
MANU ManualVerification Manual verification, for example
passport or drivers license.
MERC MerchantAuthentication Merchant-related authentication.
SCRT SecureCertificate Electronic commerce transaction
secured with the X.509 certificate of a
customer.
SNCT SecureNoCertificate Secure electronic transaction without
cardholder certificate.
SCNL SecuredChannel Channel-encrypted transaction.
6.2.2.7  CardDataReading1Code
Definition: Type of reading of the card data.
Type: CodeSet
CodeName Name Definition
TAGC Tag Tag reading capabilities (RFID, etc.).
PHYS Physical Keyboard entry or OCR reading of
embossing or printed data, either at time
of transaction or after the event.
BRCD BarCode Bar code.
MGST MagneticStripe Magnetic stripe.
CICC ICC ICC (Integrated Circuit Card) with
contact containing software applications
conform to ISO 7816.
DFLE AccountData Account data on file.
CTLS ProximityReader Contactless proximity reader.
ECTL EMVProximityReader Contactless proximity reader, with
application conform to the standard EMV
(standard initiated by Europay,
Mastercard and Visa).
6.2.2.8  CardholderVerificationCapability1Code
Definition: Cardholder verification capabilities of the POI (Personal Identification Number) performing
the transaction.
Type: CodeSet
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
889 March 2026
```

