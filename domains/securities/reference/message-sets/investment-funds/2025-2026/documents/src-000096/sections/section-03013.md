---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "57.4 Message Building Blocks", "57.4.3 StatusReport <StsRpt>", "57.4.3.2 IndividualCancellationStatusReport <IndvCxlStsRpt>", "57.4.3.2.3 ClientReference <ClntRef>"]
file_pages: [4219]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.017.001.05"]
---

# 57.4.3.2.3 ClientReference <ClntRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4219 to 4219.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4219

```text
57.4.3.2.3  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
Datatype: "Max35Text" on page 5403
57.4.3.2.4  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 5403
57.4.3.2.5  CancellationReference <CxlRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the order cancellation, as assigned by the instructing
party.
Datatype: "Max35Text" on page 5403
57.4.3.2.6  CancellationStatus <CxlSts>
Presence: [1..1]
Definition: Cancellation status of the order cancellation.
CancellationStatus <CxlSts> contains one of the following CancellationStatus33Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Status <Sts> [1..1] CodeSet 4219
Or}   Rejected <Rjctd> [1..1]  C8 4220
     Reason <Rsn> [0..1]  4220
{Or       Code <Cd> [1..1] CodeSet 4220
Or}       Proprietary <Prtry> [1..1] ± 4221
     AdditionalInformation <AddtlInf> [0..1] Text 4221
57.4.3.2.6.1  Status <Sts>
Presence: [1..1]
Definition: Status of the order cancellation request is cancelled.
Datatype: "OrderCancellationStatus2Code" on page 5332
CodeName Name Definition
STNP SentToNextParty Order cancellation request has been
sent to the next party, eg, the next
intermediary.
RECE Received Status of the order cancellation request
is received, that is, technical validation of
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4219 May 2026
```

