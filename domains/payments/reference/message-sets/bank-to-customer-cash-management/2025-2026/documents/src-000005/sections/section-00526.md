---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.26 CardTransaction <CardTx>", "4.4.2.14.18.2.26.1 Card <Card>", "4.4.2.14.18.2.26.1.1 PlainCardData <PlainCardData>", "4.4.2.14.18.2.26.1.1.6 TrackData <TrckData>"]
file_pages: [757]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.26.1.1.6 TrackData <TrckData>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 757 to 757.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 757

```text
4.4.2.14.18.2.26.1.1.6  TrackData <TrckData>
Presence: [0..*]
Definition: Magnetic track or equivalent payment card data.
TrackData <TrckData> contains the following TrackData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TrackNumber <TrckNb> [0..1] Text 757
   TrackValue <TrckVal> [1..1] Text 757
4.4.2.14.18.2.26.1.1.6.1  TrackNumber <TrckNb>
Presence: [0..1]
Definition: Track number of the card.
Datatype: "Exact1NumericText" on page 913
4.4.2.14.18.2.26.1.1.6.2  TrackValue <TrckVal>
Presence: [1..1]
Definition: Card track content or equivalent.
Datatype: "Max140Text" on page 914
4.4.2.14.18.2.26.1.1.7  CardSecurityCode <CardSctyCd>
Presence: [0..1]
Definition: Card security code (CSC) associated with the card performing the transaction.
CardSecurityCode <CardSctyCd> contains the following CardSecurityInformation1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CSCManagement <CSCMgmt> [1..1] CodeSet 757
   CSCValue <CSCVal> [0..1] Text 758
4.4.2.14.18.2.26.1.1.7.1  CSCManagement <CSCMgmt>
Presence: [1..1]
Definition: Card security code (CSC) management associated with the transaction.
Datatype: "CSCManagement1Code" on page 892
CodeName Name Definition
PRST CSCPresent Card security code present.
BYPS CSCByPass Card security code by-passed or not
provided by the merchant.
UNRD CSCUnread Card security code unreadable.
NCSC NoCSC No card security code imprint.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
757 March 2026
```

