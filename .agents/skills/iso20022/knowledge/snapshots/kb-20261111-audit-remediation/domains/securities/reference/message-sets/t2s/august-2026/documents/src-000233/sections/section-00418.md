---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["22 camt.084.001.02 IntraBalanceMovementPostingReportV02", "22.4 Message Building Blocks", "22.4.7 SubBalance <SubBal>", "22.4.7.1 BalanceFrom <BalFr>"]
file_pages: [534]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 22.4.7.1 BalanceFrom <BalFr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 534 to 534.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 534

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     StatusDate <StsDt> [0..1] DateTime 543
     CashSubBalanceIdentification <CshSubBalId> [0..1] ± 544
     Linkages <Lnkgs> [0..*]  544
       ProcessingPosition <PrcgPos> [0..1] ± C16 544
       MessageNumber <MsgNb> [0..1] ± C14 545
       Reference <Ref> [1..1]  545
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 546
Or         IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 546
Or         IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 546
Or         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 546
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 546
Or         PoolIdentification <PoolId> [1..1] Text 547
Or}         OtherTransactionIdentification <OthrTxId> [1..1] Text 547
       ReferenceOwner <RefOwnr> [0..1] ± 547
     Priority <Prty> [0..1] ± 547
     MessageOriginator <MsgOrgtr> [0..1] ± 547
     CreationDateTime <CreDtTm> [1..1] DateTime 548
     InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 548
     SupplementaryData <SplmtryData> [0..*] ± C15 548
22.4.7.1  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the amount of money is moved.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 534 August 2026
```

