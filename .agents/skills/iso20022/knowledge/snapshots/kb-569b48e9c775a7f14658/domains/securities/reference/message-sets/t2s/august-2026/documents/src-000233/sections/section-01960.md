---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.3 Modifications <Mods>", "76.4.3.4 Modification <Mod>", "76.4.3.4.7 Underlying <Undrlyg>", "76.4.3.4.7.1 IntraPositionMovement <IntraPosMvmnt>"]
file_pages: [2680]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.3.4.7.1 IntraPositionMovement <IntraPosMvmnt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2680 to 2680.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2680

```text
Underlying <Undrlyg> contains one of the following SettlementOrIntraPosition3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IntraPositionMovement <IntraPosMvmnt> [1..1]  2680
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C16
2681
     SettlementQuantity <SttlmQty> [1..1] ± 2682
     SettlementDate <SttlmDt> [1..1] ± 2682
     BalanceFrom <BalFr> [0..1] ± 2682
     BalanceTo <BalTo> [0..1] ± 2683
     SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 2683
     Priority <Prty> [0..1] ± 2683
Or}   SettlementTransaction <SttlmTx> [1..1]  2683
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C16
2684
     SettlementQuantity <SttlmQty> [1..1] ± 2685
     SettlementAmount <SttlmAmt> [0..1] ± 2685
     TradeDate <TradDt> [0..1] ± 2686
     SettlementDate <SttlmDt> [1..1] ± 2686
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C18,
C19,
C20,
C21
2686
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C18,
C19,
C20,
C21
2687
76.4.3.4.7.1  IntraPositionMovement <IntraPosMvmnt>
Presence: [1..1]
Definition: Specifies the requested intra-position movement details.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2680 August 2026
```

