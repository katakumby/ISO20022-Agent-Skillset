---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status"]
file_pages: [268]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21 Status

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 268 to 268.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 268

```text
Party5 <Pty5> contains the following elements (see "PartyIdentificationAndAccount170" on page 256
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 256
   LEI <LEI> [0..1] IdentifierSet 256
   SafekeepingAccount <SfkpgAcct> [0..1] ± 257
   ProcessingIdentification <PrcgId> [0..1] Text 257
9.1.21 Status
9.1.21.1  PendingStatusAndReason4
Definition: Choice of the intra-balance movement status type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..*] ± 268
   SettlementStatus <SttlmSts> [0..*] ± C15 268
9.1.21.1.1  ProcessingStatus <PrcgSts>
Presence: [0..*]
Definition: Provides details on the processing status of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus100Choice" on page 305 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 305
Or   Repair <Rpr> [1..1] ± 305
Or   Cancelled <Canc> [1..1] ± 306
Or}   Proprietary <Prtry> [1..1] ± 306
9.1.21.1.2  SettlementStatus <SttlmSts>
Presence: [0..*]
Definition: Provides the settlement status of a transaction.
Impacted by: C15 "PendingToFailingRule"
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 268 September 2025
```

