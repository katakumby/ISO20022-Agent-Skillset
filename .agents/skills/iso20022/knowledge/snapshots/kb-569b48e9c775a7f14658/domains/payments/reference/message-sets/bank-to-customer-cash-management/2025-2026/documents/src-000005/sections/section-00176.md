---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.26 CardTransaction <CardTx>", "2.4.2.15.18.2.26.3 Transaction <Tx>", "2.4.2.15.18.2.26.3.2 Individual <Indv>", "2.4.2.15.18.2.26.3.2.2 PaymentContext <PmtCntxt>", "2.4.2.15.18.2.26.3.2.2.7 AttendantMessageCapable <AttndntMsgCpbl>"]
file_pages: [254]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.26.3.2.2.7 AttendantMessageCapable <AttndntMsgCpbl>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 254 to 254.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 254

```text
CodeName Name Definition
MAIL MailOrder Mail order.
TLPH TelephoneOrder Telephone order.
ECOM ElectronicCommerce Electronic commerce.
TVPY TelevisionPayment Payment on television.
2.4.2.15.18.2.26.3.2.2.7  AttendantMessageCapable <AttndntMsgCpbl>
Presence: [0..1]
Definition: Indicates whether a message can be sent or not on an attendant display (attendant display
present or not).
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 911):
• Meaning When True: True
• Meaning When False: False
2.4.2.15.18.2.26.3.2.2.8  AttendantLanguage <AttndntLang>
Presence: [0..1]
Definition: Language used to display messages to the attendant.
Datatype: "ISO2ALanguageCode" on page 901
2.4.2.15.18.2.26.3.2.2.9  CardDataEntryMode <CardDataNtryMd>
Presence: [1..1]
Definition: Entry mode of the card data.
Datatype: "CardDataReading1Code" on page 889
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
2.4.2.15.18.2.26.3.2.2.10  FallbackIndicator <FllbckInd>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
254 March 2026
```

