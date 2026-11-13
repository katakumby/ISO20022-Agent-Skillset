---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["79 semt.034.001.01 IntraPositionMovementPendingReportV01", "79.4 Message Building Blocks", "79.4.5 Movements <Mvmnts>", "79.4.5.2 Movement <Mvmnt>", "79.4.5.2.1 StatusAndReason <StsAndRsn>"]
file_pages: [2736]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 79.4.5.2.1 StatusAndReason <StsAndRsn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2736 to 2736.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2736

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     ReferenceOwner <RefOwnr> [0..1] ± 2745
   SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 2745
   Priority <Prty> [0..1] ± 2745
   CorporateActionEventType <CorpActnEvtTp> [0..1] ± C10 2746
   MessageOriginator <MsgOrgtr> [0..1] ± 2746
   CreationDateTime <CreDtTm> [1..1] DateTime 2746
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 2746
   SupplementaryData <SplmtryData> [0..*] ± C20 2747
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
79.4.5.2.1  StatusAndReason <StsAndRsn>
Presence: [0..1]
Definition: Status and status reason of the transaction.
StatusAndReason <StsAndRsn> contains the following elements (see "PendingStatusAndReason4"
on page 3202 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..*] ± 3202
   SettlementStatus <SttlmSts> [0..*] ± C15 3202
79.4.5.2.2  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 3328
79.4.5.2.3  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
79.4.5.2.4  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2736 August 2026
```

