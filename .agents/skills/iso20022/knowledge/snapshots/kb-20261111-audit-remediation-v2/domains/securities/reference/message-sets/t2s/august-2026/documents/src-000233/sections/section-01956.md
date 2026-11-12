---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.3 Modifications <Mods>", "76.4.3.4 Modification <Mod>", "76.4.3.4.6 RequestDetails <ReqDtls>", "76.4.3.4.6.13 Linkages <Lnkgs>"]
file_pages: [2676]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.3.4.6.13 Linkages <Lnkgs>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2676 to 2676.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2676

```text
UnilateralSplit <UnltrlSplt> contains one of the following elements (see "UnilateralSplit3Choice" on
page 3021 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3021
Or}   Proprietary <Prtry> [1..1] ± 3021
76.4.3.4.6.13  Linkages <Lnkgs>
Presence: [0..*]
Definition: Information regarding the linkage requested.
Linkages <Lnkgs> contains the following Linkages57 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C29 2676
   MessageNumber <MsgNb> [0..1] ± C27 2677
   Reference <Ref> [1..1]  2677
{Or     SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 2678
Or     IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 2678
Or     IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 2678
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2678
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2678
Or     PoolIdentification <PoolId> [1..1] Text 2679
Or}     OtherTransactionIdentification <OthrTxId> [1..1] Text 2679
   ReferenceOwner <RefOwnr> [0..1] ± 2679
76.4.3.4.6.13.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: When the transaction is to be executed relative to a linked transaction.
Impacted by: C29 "WithLinkageRule"
ProcessingPosition <PrcgPos> contains one of the following elements (see
"ProcessingPosition7Choice" on page 3028 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3028
Or}   Proprietary <Prtry> [1..1] ± 3029
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2676 August 2026
```

