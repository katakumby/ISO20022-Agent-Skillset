---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.17 CardTransaction <CardTx>", "4.4.2.14.17.1 Card <Card>", "4.4.2.14.17.1.1 PlainCardData <PlainCardData>", "4.4.2.14.17.1.1.6 TrackData <TrckData>"]
file_pages: [603]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.17.1.1.6 TrackData <TrckData>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 603 to 603.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 603

```text
4.4.2.14.17.1.1.6  TrackData <TrckData>
Presence: [0..*]
Definition: Magnetic track or equivalent payment card data.
TrackData <TrckData> contains the following TrackData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TrackNumber <TrckNb> [0..1] Text 603
   TrackValue <TrckVal> [1..1] Text 603
4.4.2.14.17.1.1.6.1  TrackNumber <TrckNb>
Presence: [0..1]
Definition: Track number of the card.
Datatype: "Exact1NumericText" on page 913
4.4.2.14.17.1.1.6.2  TrackValue <TrckVal>
Presence: [1..1]
Definition: Card track content or equivalent.
Datatype: "Max140Text" on page 914
4.4.2.14.17.1.1.7  CardSecurityCode <CardSctyCd>
Presence: [0..1]
Definition: Card security code (CSC) associated with the card performing the transaction.
CardSecurityCode <CardSctyCd> contains the following CardSecurityInformation1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CSCManagement <CSCMgmt> [1..1] CodeSet 603
   CSCValue <CSCVal> [0..1] Text 604
4.4.2.14.17.1.1.7.1  CSCManagement <CSCMgmt>
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
603 March 2026
```

