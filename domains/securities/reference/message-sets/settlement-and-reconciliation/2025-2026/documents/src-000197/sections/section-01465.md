---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.48 SettlementStatus30Choice", "35.1.29.48.1 Pending <Pdg>"]
file_pages: [1953]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.48.1 Pending <Pdg>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1953 to 1953.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1953

```text
Constraints
• PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
35.1.29.48.1  Pending <Pdg>
Presence: [1..1]
Definition: Instruction is pending. Settlement at the instructed settlement date is still possible.
Pending <Pdg> contains one of the following elements (see "PendingStatus67Choice" on page 1900
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1901
Or}   Reason <Rsn> [1..*] ± 1901
35.1.29.48.2  Failing <Flng>
Presence: [1..1]
Definition: Instruction is failing. Settlement at the instructed settlement date is no longer possible.
Failing <Flng> contains one of the following elements (see "FailingStatus13Choice" on page 1956 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1956
Or}   Reason <Rsn> [1..*]  1957
     Code <Cd> [1..1] ± 1957
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1957
35.1.29.48.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 1877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
35.1.29.49  GeneratedReason5
Definition: Specifies the reason why the transaction was generated.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1953 March 2026
```

