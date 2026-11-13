---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.6 AccountOwner <AcctOwnr>", "13.4.7.1 StatusDate <StsDt>"]
file_pages: [440]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.7.1 StatusDate <StsDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 440 to 440.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 440

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Code <Cd> [1..1]  453
{Or           Code <Cd> [1..1] CodeSet 453
Or}           Proprietary <Prtry> [1..1] ± 453
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 454
Or}     Proprietary <Prtry> [1..1] ± 454
   CancellationStatus <CxlSts> [0..1]  454
{Or     PendingCancellation <PdgCxl> [1..1] ± 454
Or     Rejected <Rjctd> [1..1] ± 455
Or     Repair <Rpr> [1..1] ± 455
Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 455
Or     Proprietary <Prtry> [1..1] ± 456
Or     Denied <Dnd> [1..1] ± 456
Or}     Cancelled <Canc> [1..1] ± 456
   Settled <Sttld> [0..1] ± C1 457
   SupplementaryData <SplmtryData> [0..*] ± C8 457
13.4.7.1  StatusDate <StsDt>
Presence: [1..1]
Definition: Date and time at which the status was assigned.
Datatype: "ISODateTime" on page 2185
13.4.7.2  SendingOrganisationIdentification <SndgOrgId>
Presence: [0..1]
Definition: Unique and unambiguous way to identify the organisation that sent the message instance.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 440 March 2026
```

