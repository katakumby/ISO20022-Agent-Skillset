---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.61 RepoCallRequestStatus7Choice", "35.1.29.61.1 AcknowledgedAccepted <AckdAccptd>", "35.1.29.61.1.2 Reason <Rsn>", "35.1.29.61.1.2.1 Code <Cd>"]
file_pages: [1973]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.61.1.2.1 Code <Cd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1973 to 1973.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1973

```text
35.1.29.61.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies additional information about the processed instruction.
Code <Cd> contains one of the following elements (see "AcknowledgementReason13Choice" on
page 1979 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1979
Or}   Proprietary <Prtry> [1..1] ± 1980
35.1.29.61.1.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.61.2  Denied <Dnd>
Presence: [1..1]
Definition: Instruction/Request will not be executed.
Denied <Dnd> contains one of the following elements (see "DeniedStatus17Choice" on page 1901 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1901
Or}   Reason <Rsn> [1..*]  1902
     Code <Cd> [1..1] ± 1902
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1902
35.1.29.61.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 1877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
35.1.29.62  CancellationStatus16Choice
Definition: Specifies whether the status is provided with a reason or not.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1973 March 2026
```

