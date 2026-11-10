---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "3.4 Message Building Blocks", "3.4.3 Movements <Mvmnts>", "3.4.3.4 Movement <Mvmnt>", "3.4.3.4.10 MovementDetails <MvmntDtls>", "3.4.3.4.10.13 Linkages <Lnkgs>", "3.4.3.4.10.13.1 ProcessingPosition <PrcgPos>"]
file_pages: [82]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.029.001.01"]
---

# 3.4.3.4.10.13.1 ProcessingPosition <PrcgPos>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 82 to 82.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 82

```text
Linkages <Lnkgs> contains the following Linkages57 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C25 82
   MessageNumber <MsgNb> [0..1] ± C22 82
   Reference <Ref> [1..1]  83
{Or     SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 83
Or     IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 83
Or     IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 84
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 84
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 84
Or     PoolIdentification <PoolId> [1..1] Text 84
Or}     OtherTransactionIdentification <OthrTxId> [1..1] Text 84
   ReferenceOwner <RefOwnr> [0..1] ± 84
3.4.3.4.10.13.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: When the transaction is to be executed relative to a linked transaction.
Impacted by: C25 "WithLinkageRule"
ProcessingPosition <PrcgPos> contains one of the following elements (see
"ProcessingPosition7Choice" on page 244 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 244
Or}   Proprietary <Prtry> [1..1] ± 245
Constraints
• WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and which
must be executed together. Even if one single transactions/instructions/notifications can not be
executed, then all the other transactions/instructions/notifications must also be kept pending.
Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/instructions/
notifications.
3.4.3.4.10.13.2  MessageNumber <MsgNb>
Presence: [0..1]
Approved by the Securities SEG on 21 August 2025 semt.029.001.01
IntraPositionMovementQueryResponseV01
Target2-Securities - Settlement Restrictions 82 September 2025
```

