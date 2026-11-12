---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03", "5.4 Message Building Blocks", "5.4.1 Identification <Id>", "5.4.1.1 TransactionIdentification <TxId>"]
file_pages: [151]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.030.001.03"]
---

# 5.4.1.1 TransactionIdentification <TxId>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 151 to 151.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 151

```text
5.4.1.1  TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the instructing party.
Datatype: "Max35Text" on page 669
5.4.2 References <Refs>
Presence: [1..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
References <Refs> contains the following elements (see "Linkages76" on page 285 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageNumber <MsgNb> [0..1] ± C9 285
   Reference <Ref> [1..1] ± C7 286
5.4.3 Status <Sts>
Presence: [1..1]
Definition: Provides details on the processing status of the trade.
Impacted by: C1 "AdditionalReasonInforrmationRule", C10 "UnaffirmedReasonRule"
Status <Sts> contains the following StatusAndReason46 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AffirmationStatus <AffirmSts> [1..1] ± 151
   UnaffirmedReason <UaffrmdRsn> [0..1] ± 152
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 152
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
• UnaffirmedReasonRule
If AffirmationStatus is Unaffirmed then UnaffirmedReason must be present.
On Condition
    /AffirmationStatus/Code is equal to value 'Unaffirmed'
Following Must be True
    /UnaffirmedReason Must be present
5.4.3.1  AffirmationStatus <AffirmSts>
Presence: [1..1]
Definition: Status of affirmation of a trade.
Approved by the Securities SEG on 13 February 2025 setr.030.001.03
SecuritiesTradeConfirmationResponseV03
Post Trade Matching - Maintenance 2024 - 2025 151 February 2025
```

