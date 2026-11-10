---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.26 Status", "16.1.26.9 PendingCancellationStatus18Choice", "16.1.26.9.2 Reason <Rsn>", "16.1.26.9.2.1 ReasonCode <RsnCd>", "16.1.26.9.2.1.1 Code <Cd>"]
file_pages: [1152]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.26.9.2.1.1 Code <Cd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1152 to 1152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1152

```text
ReasonCode <RsnCd> contains one of the following PendingCancellationReason10Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1152
Or}   Proprietary <Prtry> [1..1] ± 1152
16.1.26.9.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the reason why a cancellation request sent for the related
instruction is pending.
Datatype: "PendingCancellationReason9Code" on page 1227
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
DQUA QuantityRejection Unrecognised or invalid instructed
quantity.
DQCS AmountRejection Unrecognised or invalid instructed cash
amount.
LATE MarketDeadlineMissed Received after market deadline.
OTHR Other Other. See Narrative.
ECRD ElectionToCounterpartyResponseDeadlineMiss
ed
Received after the election to
counterparty response market deadline.
16.1.26.9.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the reason why a cancellation request sent for the related
instruction is pending.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.26.9.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the processed instruction.
Datatype: "Max210Text" on page 1249
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1152 February 2026
```

