---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["15 camt.084.001.02 IntraBalanceMovementPostingReportV02", "15.4 Message Building Blocks", "15.4.7 SubBalance <SubBal>", "15.4.7.1 BalanceFrom <BalFr>"]
file_pages: [343]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 15.4.7.1 BalanceFrom <BalFr>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 343 to 343.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 343

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     StatusDate <StsDt> [0..1] DateTime 352
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 353
     Linkages <Lnkgs> [0..*]  353
       ProcessingPosition <PrcgPos> [0..1] ± C16 353
       MessageNumber <MsgNb> [0..1] ± C14 354
       Reference <Ref> [1..1]  354
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 355
Or         IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 355
Or         IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 355
Or         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 355
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 355
Or         PoolIdentification <PoolId> [1..1] Text 356
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 356
       ReferenceOwner <RefOwnr> [0..1] ± 356
     Priority <Prty> [0..1] ± 356
     MessageOriginator <MsgOrgtr> [0..1] ± 356
     CreationDateTime <CreDtTm> [1..1] DateTime 357
     InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 357
     SupplementaryData <SplmtryData> [0..*] ± C15 357
15.4.7.1  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the amount of money is moved.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
343 March 2024
```

