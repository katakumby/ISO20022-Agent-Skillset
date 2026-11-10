---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["31 sese.037.001.09 PortfolioTransferNotificationV09", "31.4 Message Building Blocks", "31.4.6 TransferNotificationDetails <TrfNtfctnDtls>", "31.4.6.6 Status <Sts>", "31.4.6.6.1 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [1109]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.037.001.09"]
---

# 31.4.6.6.1 AcknowledgedAccepted <AckdAccptd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1109 to 1109.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1109

```text
31.4.6.6.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus32Choice" on page 1894 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1894
Or}   Reason <Rsn> [1..*]  1894
     Code <Cd> [1..1] ± 1895
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1895
31.4.6.6.2  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Processing of the instruction/request is pending.
PendingProcessing <PdgPrcg> contains one of the following elements (see
"PendingProcessingStatus17Choice" on page 1959 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1959
Or}   Reason <Rsn> [1..*]  1959
     Code <Cd> [1..1] ± 1959
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1960
31.4.6.6.3  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction/request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionStatus30Choice" on
page 1993 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1993
Or}   Reason <Rsn> [1..*]  1993
     Code <Cd> [1..1]  1994
{Or       Code <Cd> [1..1] CodeSet 1994
Or}       Proprietary <Prtry> [1..1] ± 1994
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1995
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1109 March 2026
```

