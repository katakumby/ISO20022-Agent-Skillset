---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["8 semt.034.001.01 IntraPositionMovementPendingReportV01", "8.4 Message Building Blocks", "8.4.5 Movements <Mvmnts>", "8.4.5.2 Movement <Mvmnt>", "8.4.5.2.1 StatusAndReason <StsAndRsn>"]
file_pages: [181]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 8.4.5.2.1 StatusAndReason <StsAndRsn>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 181 to 181.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 181

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     ReferenceOwner <RefOwnr> [0..1] ± 190
   SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 190
   Priority <Prty> [0..1] ± 190
   CorporateActionEventType <CorpActnEvtTp> [0..1] ± C10 191
   MessageOriginator <MsgOrgtr> [0..1] ± 191
   CreationDateTime <CreDtTm> [1..1] DateTime 191
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 191
   SupplementaryData <SplmtryData> [0..*] ± C20 192
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
8.4.5.2.1  StatusAndReason <StsAndRsn>
Presence: [0..1]
Definition: Status and status reason of the transaction.
StatusAndReason <StsAndRsn> contains the following elements (see "PendingStatusAndReason4"
on page 268 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..*] ± 268
   SettlementStatus <SttlmSts> [0..*] ± C15 268
8.4.5.2.2  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 345
8.4.5.2.3  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 345
8.4.5.2.4  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Approved by the Securities SEG on 21 August 2025 semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities - Settlement Restrictions 181 September 2025
```

