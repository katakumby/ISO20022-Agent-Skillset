---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "3.4 Message Building Blocks", "3.4.3 Movements <Mvmnts>", "3.4.3.4 Movement <Mvmnt>", "3.4.3.4.1 AccountOwner <AcctOwnr>"]
file_pages: [71]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 3.4.3.4.1 AccountOwner <AcctOwnr>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 71 to 71.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 71

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Reference <Ref> [1..1]  83
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 83
Or         IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 83
Or         IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 84
Or         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 84
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 84
Or         PoolIdentification <PoolId> [1..1] Text 84
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 84
       ReferenceOwner <RefOwnr> [0..1] ± 84
     SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 85
     Priority <Prty> [0..1] ± 85
     CorporateActionEventType <CorpActnEvtTp> [0..1] ± C11 85
     MessageOriginator <MsgOrgtr> [0..1] ± 86
     CreationDateTime <CreDtTm> [1..1] DateTime 86
     InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 86
     SupplementaryData <SplmtryData> [0..*] ± C24 86
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
3.4.3.4.1  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 257 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 257
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 257
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 71 September 2025
```

