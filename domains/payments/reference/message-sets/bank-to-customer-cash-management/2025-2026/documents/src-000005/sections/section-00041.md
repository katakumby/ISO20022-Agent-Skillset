---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.17 CardTransaction <CardTx>", "2.4.2.15.17.1 Card <Card>", "2.4.2.15.17.1.1 PlainCardData <PlainCardData>", "2.4.2.15.17.1.1.6 TrackData <TrckData>"]
file_pages: [85]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.17.1.1.6 TrackData <TrckData>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 85 to 85.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 85

```text
2.4.2.15.17.1.1.6  TrackData <TrckData>
Presence: [0..*]
Definition: Magnetic track or equivalent payment card data.
TrackData <TrckData> contains the following TrackData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TrackNumber <TrckNb> [0..1] Text 85
   TrackValue <TrckVal> [1..1] Text 85
2.4.2.15.17.1.1.6.1  TrackNumber <TrckNb>
Presence: [0..1]
Definition: Track number of the card.
Datatype: "Exact1NumericText" on page 913
2.4.2.15.17.1.1.6.2  TrackValue <TrckVal>
Presence: [1..1]
Definition: Card track content or equivalent.
Datatype: "Max140Text" on page 914
2.4.2.15.17.1.1.7  CardSecurityCode <CardSctyCd>
Presence: [0..1]
Definition: Card security code (CSC) associated with the card performing the transaction.
CardSecurityCode <CardSctyCd> contains the following CardSecurityInformation1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CSCManagement <CSCMgmt> [1..1] CodeSet 85
   CSCValue <CSCVal> [0..1] Text 86
2.4.2.15.17.1.1.7.1  CSCManagement <CSCMgmt>
Presence: [1..1]
Definition: Card security code (CSC) management associated with the transaction.
Datatype: "CSCManagement1Code" on page 892
CodeName Name Definition
PRST CSCPresent Card security code present.
BYPS CSCByPass Card security code by-passed or not
provided by the merchant.
UNRD CSCUnread Card security code unreadable.
NCSC NoCSC No card security code imprint.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
85 March 2026
```

