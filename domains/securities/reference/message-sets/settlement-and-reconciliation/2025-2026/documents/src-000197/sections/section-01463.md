---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.46 MatchingDenied3Choice"]
file_pages: [1951]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.46 MatchingDenied3Choice

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1951 to 1951.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1951

```text
Datatype: "Max210Text" on page 2191
35.1.29.46  MatchingDenied3Choice
Definition: Specifies the matching processing change requested.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1951
Or}   Proprietary <Prtry> [1..1] ± 1951
35.1.29.46.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the execution of a matching denial process.
Datatype: "MatchingProcess1Code" on page 2087
CodeName Name Definition
UNMT Unmatch The referenced transaction is requested
to be unmatched.
MTRE ResumeMatching Matching process is to be resumed for
the referenced transaction.
35.1.29.46.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the execution of a matching denial process.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.47  RejectionOrRepairStatus43Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1952
Or}   Reason <Rsn> [1..*]  1952
     Code <Cd> [1..1] ± 1952
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1952
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1951 March 2026
```

