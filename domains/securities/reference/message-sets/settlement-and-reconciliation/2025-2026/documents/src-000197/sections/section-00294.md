---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.5 BlockChainAddressOrWallet <BlckChainAdrOrWllt>"]
file_pages: [438, 439]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.5 BlockChainAddressOrWallet <BlckChainAdrOrWllt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 438 to 439.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 438

```text
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount22" on
page 1344 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1344
   Type <Tp> [0..1] ± 1344
   Name <Nm> [0..1] Text 1344
13.4.5 BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 1572 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1572
   Type <Tp> [0..1] ± 1572
   Name <Nm> [0..1] Text 1572
13.4.6 AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification144" on
page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1664
   LEI <LEI> [0..1] IdentifierSet 1664
13.4.7 StatusTrail <StsTrl>
Presence: [0..*]
Definition: Provides the history of status and reasons for a pending, posted or cancelled transaction.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 438 March 2026
```

## File page 439

```text
StatusTrail <StsTrl> contains the following StatusTrail13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatusDate <StsDt> [1..1] DateTime 440
   SendingOrganisationIdentification <SndgOrgId> [0..1] ± 440
   UserIdentification <UsrId> [0..1] Text 441
   ProcessingStatus <PrcgSts> [0..1]  441
{Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 442
Or     PendingProcessing <PdgPrcg> [1..1] ± 442
Or     Rejected <Rjctd> [1..1] ± 443
Or     Repair <Rpr> [1..1] ± 443
Or     Cancelled <Canc> [1..1] ± 444
Or     PendingCancellation <PdgCxl> [1..1]  444
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 445
Or}       Reason <Rsn> [1..*]  445
         Code <Cd> [1..1]  445
{Or           Code <Cd> [1..1] CodeSet 446
Or}           Proprietary <Prtry> [1..1] ± 446
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 446
Or     Proprietary <Prtry> [1..1] ± 446
Or     CancellationRequested <CxlReqd> [1..1] ± C1 447
Or}     ModificationRequested <ModReqd> [1..1] ± C1 447
   InferredMatchingStatus <IfrrdMtchgSts> [0..1] ± 448
   MatchingStatus <MtchgSts> [0..1] ± 448
   SettlementStatus <SttlmSts> [0..1] ± C4 448
   ModificationProcessingStatus <ModPrcgSts> [0..1]  449
{Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 450
Or     PendingProcessing <PdgPrcg> [1..1] ± 450
Or     Denied <Dnd> [1..1] ± 451
Or     Rejected <Rjctd> [1..1] ± 451
Or     Repaired <Rprd> [1..1] ± 451
Or     Modified <Modfd> [1..1]  452
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 452
Or}       Reason <Rsn> [1..*]  452
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 439 March 2026
```

