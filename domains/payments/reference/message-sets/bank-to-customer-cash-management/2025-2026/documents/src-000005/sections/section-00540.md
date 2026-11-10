---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.26 CardTransaction <CardTx>", "4.4.2.14.18.2.26.3 Transaction <Tx>", "4.4.2.14.18.2.26.3.2 Individual <Indv>", "4.4.2.14.18.2.26.3.2.2 PaymentContext <PmtCntxt>", "4.4.2.14.18.2.26.3.2.2.11 AuthenticationMethod <AuthntcnMtd>"]
file_pages: [773]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.26.3.2.2.11 AuthenticationMethod <AuthntcnMtd>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 773 to 773.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 773

```text
Definition: Indicator of a card entry mode fallback.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 911):
• Meaning When True: True
• Meaning When False: False
4.4.2.14.18.2.26.3.2.2.11  AuthenticationMethod <AuthntcnMtd>
Presence: [0..1]
Definition: Method used to authenticate a cardholder.
AuthenticationMethod <AuthntcnMtd> contains the following CardholderAuthentication2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AuthenticationMethod <AuthntcnMtd> [1..1] CodeSet 773
   AuthenticationEntity <AuthntcnNtty> [1..1] CodeSet 773
4.4.2.14.18.2.26.3.2.2.11.1  AuthenticationMethod <AuthntcnMtd>
Presence: [1..1]
Definition: Method used to authenticate the cardholder.
Datatype: "AuthenticationMethod1Code" on page 888
CodeName Name Definition
UKNW UnknownMethod Authentication method is performed
unknown.
BYPS Bypass Authentication bypassed by the
merchant.
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
4.4.2.14.18.2.26.3.2.2.11.2  AuthenticationEntity <AuthntcnNtty>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
773 March 2026
```

