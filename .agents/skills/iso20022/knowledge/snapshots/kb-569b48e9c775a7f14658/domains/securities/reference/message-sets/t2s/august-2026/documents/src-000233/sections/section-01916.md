---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["74 semt.029.001.01 IntraPositionMovementQueryResponseV01", "74.4 Message Building Blocks", "74.4.3 Movements <Mvmnts>", "74.4.3.4 Movement <Mvmnt>", "74.4.3.4.1 AccountOwner <AcctOwnr>"]
file_pages: [2626]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 74.4.3.4.1 AccountOwner <AcctOwnr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2626 to 2626.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2626

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Reference <Ref> [1..1]  2638
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2638
Or         IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 2638
Or         IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 2639
Or         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2639
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2639
Or         PoolIdentification <PoolId> [1..1] Text 2639
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 2639
       ReferenceOwner <RefOwnr> [0..1] ± 2639
     SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 2640
     Priority <Prty> [0..1] ± 2640
     CorporateActionEventType <CorpActnEvtTp> [0..1] ± C11 2640
     MessageOriginator <MsgOrgtr> [0..1] ± 2641
     CreationDateTime <CreDtTm> [1..1] DateTime 2641
     InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 2641
     SupplementaryData <SplmtryData> [0..*] ± C24 2641
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
74.4.3.4.1  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities 2626 August 2026
```

