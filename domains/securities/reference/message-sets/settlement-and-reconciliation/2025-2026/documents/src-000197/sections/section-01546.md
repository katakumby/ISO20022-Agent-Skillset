---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.8 AddressType2Code"]
file_pages: [2045]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.8 AddressType2Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2045 to 2045.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2045

```text
Format
pattern [A-Z]{3,3}
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
35.2.2.8  AddressType2Code
Definition: Specifies the type of address.
Type: CodeSet
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
35.2.2.9  AffirmationStatus1Code
Definition: Specifies the affirmation status of a trade.
Type: CodeSet
CodeName Name Definition
AFFI Affirmed Status of the transaction is affirmed.
NAFI Unaffirmed Status of the transaction is unaffirmed.
35.2.2.10  AllegementStatus1Code
Definition: Specifies the status of an allegement.
Type: CodeSet
CodeName Name Definition
CANC Cancelled Allegement has been cancelled since the
previous delta statement. The
allegement was cancelled because of a
mistake by the sender or because the
alleging party cancelled its instruction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2045 March 2026
```

