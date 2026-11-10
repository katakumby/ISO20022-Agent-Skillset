---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.26 Status", "16.1.26.7 CancelledStatus12Choice", "16.1.26.7.2 Reason <Rsn>", "16.1.26.7.2.1 ReasonCode <RsnCd>", "16.1.26.7.2.1.1 Code <Cd>"]
file_pages: [1148]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.26.7.2.1.1 Code <Cd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1148 to 1148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1148

```text
ReasonCode <RsnCd> contains one of the following CancelledReason8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1148
Or}   Proprietary <Prtry> [1..1] ± 1148
16.1.26.7.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the reason why the instruction is cancelled.
Datatype: "CancelledStatusReason6Code" on page 1166
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
CANO CancelledByOther Transaction is cancelled by a party other
than the instructing party, for example, a
market infrastructure such as a stock
exchange.
CANS CancelledBySystem Transaction is cancelled by the system.
CSUB CancelledByAgent Instruction has been cancelled by the
agent due to an event deadline
extension.
OTHR Other Other. See Narrative.
16.1.26.7.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification specifying the reason why the instruction is cancelled.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.26.7.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the processed instruction.
Datatype: "Max210Text" on page 1249
16.1.26.8  PendingCancellationStatus21Choice
Definition: Choice between a reason or no reason for the corporate action instruction cancellation
pending cancellation status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1148 February 2026
```

