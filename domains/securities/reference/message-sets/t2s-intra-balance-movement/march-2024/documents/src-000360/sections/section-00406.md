---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.2 Message Datatypes", "17.2.2 CodeSet", "17.2.2.5 AddressType2Code"]
file_pages: [476]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.2.2.5 AddressType2Code

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 476 to 476.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 476

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
17.2.2.5  AddressType2Code
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
17.2.2.6  CancellationProcessingStatus3Code
Definition: Specifies the status of a cancellation request.
Type: CodeSet
CodeName Name Definition
CANP PendingCancellation Cancellation is pending. It is not known
at this time whether cancellation can be
affected.
REJT Rejected Cancellation has been rejected for
further processing.
REPR InRepair Cancellation request is in repair.
PACK Accepted Cancellation request has been
acknowledged for further processing by
the account servicer.
DEND Denied Cancellation will not be executed.
CAND CancellationCompleted Cancellation has been completed.
17.2.2.7  CancelledStatusReason13Code
Definition: Specifies the underlying reason for the cancellation of the associated transaction.
Type: CodeSet
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
476 March 2024
```

