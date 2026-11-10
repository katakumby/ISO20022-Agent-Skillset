---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.17 CardTransaction <CardTx>", "2.4.2.15.17.2 POI <POI>", "2.4.2.15.17.2.4 Capabilities <Cpblties>", "2.4.2.15.17.2.4.2 CardholderVerificationCapabilities <CrdhldrVrfctnCpblties>"]
file_pages: [89]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.17.2.4.2 CardholderVerificationCapabilities <CrdhldrVrfctnCpblties>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 89 to 89.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 89

```text
CodeName Name Definition
DFLE AccountData Account data on file.
CTLS ProximityReader Contactless proximity reader.
ECTL EMVProximityReader Contactless proximity reader, with
application conform to the standard EMV
(standard initiated by Europay,
Mastercard and Visa).
2.4.2.15.17.2.4.2  CardholderVerificationCapabilities <CrdhldrVrfctnCpblties>
Presence: [0..*]
Definition: Cardholder verification capabilities of the POI performing the transaction.
Datatype: "CardholderVerificationCapability1Code" on page 889
CodeName Name Definition
MNSG ManualSignature Manual signature verification.
NPIN OnLinePIN Online PIN (Personal Identification
Number).
FCPN OfflinePINClear Offline PIN in clear (Personal
Identification Number).
FEPN OfflinePINEncrypted Offline PIN encrypted (Personal
Identification Number).
FDSG OfflineDigitalSignature Offline digital signature analysis.
FBIO OfflineBiometrics Offline biometrics.
MNVR ManualVerification Other manual verification, for example
passport or drivers license.
FBIG OfflineBiographics Offline biographics.
APKI AccountDigitalSignature Account based digital signature.
PKIS PKISignature PKI (Public Key Infrastructure) based
digital signature.
CHDT CardholderData Cardholder authentication data.
SCEC SecureElectronicCommerce Three domain secure (three domain
secure authentication of the cardholder).
2.4.2.15.17.2.4.3  OnLineCapabilities <OnLineCpblties>
Presence: [0..1]
Definition: On-line and off-line capabilities of the POI.
Datatype: "OnLineCapability1Code" on page 901
CodeName Name Definition
OFLN OffLine Off-line only capable.
ONLN OnLine On-line only capable.
SMON SemiOffLine Off-line capable with possible on-line
requests to the acquirer.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
89 March 2026
```

