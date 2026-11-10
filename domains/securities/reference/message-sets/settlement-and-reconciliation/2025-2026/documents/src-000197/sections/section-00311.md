---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.6 AccountOwner <AcctOwnr>", "13.4.7.9 CancellationStatus <CxlSts>", "13.4.7.9.5 Proprietary <Prtry>"]
file_pages: [456]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.7.9.5 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 456 to 456.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 456

```text
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus24Choice" on page 1983 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1983
Or}   Reason <Rsn> [1..*]  1983
     Code <Cd> [1..1] ± 1983
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1984
13.4.7.9.5  Proprietary <Prtry>
Presence: [1..1]
Definition: Status that cannot be reported using one of the available standard status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on page 1877
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
13.4.7.9.6  Denied <Dnd>
Presence: [1..1]
Definition: Instruction/Request will not be executed.
Denied <Dnd> contains one of the following elements (see "DeniedStatus16Choice" on page 1950 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1950
Or}   Reason <Rsn> [1..*]  1950
     Code <Cd> [1..1] ± 1950
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1950
13.4.7.9.7  Cancelled <Canc>
Presence: [1..1]
Definition: Cancellation requested executed.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 456 March 2026
```

