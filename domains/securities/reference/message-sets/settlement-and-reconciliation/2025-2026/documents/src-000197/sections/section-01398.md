---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.1 SettlementStatus32Choice", "35.1.29.1.2 Failing <Flng>", "35.1.29.1.2.2 Reason <Rsn>", "35.1.29.1.2.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [1871]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.1.2.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1871 to 1871.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1871

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.1.2.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.1.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 1877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
35.1.29.2  AllegementStatus3Choice
Definition: Choice of format for the allegement status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1871
Or}   Proprietary <Prtry> [1..1] ± 1872
35.1.29.2.1  Code <Cd>
Presence: [1..1]
Definition: Status of the allegement reported.
Datatype: "AllegementStatus1Code" on page 2045
CodeName Name Definition
CANC Cancelled Allegement has been cancelled since the
previous delta statement. The
allegement was cancelled because of a
mistake by the sender or because the
alleging party cancelled its instruction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1871 March 2026
```

