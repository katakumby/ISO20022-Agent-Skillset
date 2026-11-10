---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.26 CardTransaction <CardTx>", "3.4.2.15.18.2.26.3 Transaction <Tx>", "3.4.2.15.18.2.26.3.2 Individual <Indv>", "3.4.2.15.18.2.26.3.2.2 PaymentContext <PmtCntxt>", "3.4.2.15.18.2.26.3.2.2.7 AttendantMessageCapable <AttndntMsgCpbl>"]
file_pages: [514]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.26.3.2.2.7 AttendantMessageCapable <AttndntMsgCpbl>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 514 to 514.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 514

```text
CodeName Name Definition
MAIL MailOrder Mail order.
TLPH TelephoneOrder Telephone order.
ECOM ElectronicCommerce Electronic commerce.
TVPY TelevisionPayment Payment on television.
3.4.2.15.18.2.26.3.2.2.7  AttendantMessageCapable <AttndntMsgCpbl>
Presence: [0..1]
Definition: Indicates whether a message can be sent or not on an attendant display (attendant display
present or not).
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 911):
• Meaning When True: True
• Meaning When False: False
3.4.2.15.18.2.26.3.2.2.8  AttendantLanguage <AttndntLang>
Presence: [0..1]
Definition: Language used to display messages to the attendant.
Datatype: "ISO2ALanguageCode" on page 901
3.4.2.15.18.2.26.3.2.2.9  CardDataEntryMode <CardDataNtryMd>
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
3.4.2.15.18.2.26.3.2.2.10  FallbackIndicator <FllbckInd>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
514 March 2026
```

