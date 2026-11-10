---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.4 Message Building Blocks", "5.4.3 Modifications <Mods>", "5.4.3.4 Modification <Mod>", "5.4.3.4.7 Underlying <Undrlyg>", "5.4.3.4.7.1 IntraPositionMovement <IntraPosMvmnt>"]
file_pages: [125]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.4.3.4.7.1 IntraPositionMovement <IntraPosMvmnt>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 125 to 125.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 125

```text
Underlying <Undrlyg> contains one of the following SettlementOrIntraPosition3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IntraPositionMovement <IntraPosMvmnt> [1..1]  125
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C16
126
     SettlementQuantity <SttlmQty> [1..1] ± 127
     SettlementDate <SttlmDt> [1..1] ± 127
     BalanceFrom <BalFr> [0..1] ± 127
     BalanceTo <BalTo> [0..1] ± 128
     SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 128
     Priority <Prty> [0..1] ± 128
Or}   SettlementTransaction <SttlmTx> [1..1]  128
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C16
129
     SettlementQuantity <SttlmQty> [1..1] ± 130
     SettlementAmount <SttlmAmt> [0..1] ± 130
     TradeDate <TradDt> [0..1] ± 131
     SettlementDate <SttlmDt> [1..1] ± 131
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C18,
C19,
C20,
C21
131
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C18,
C19,
C20,
C21
132
5.4.3.4.7.1  IntraPositionMovement <IntraPosMvmnt>
Presence: [1..1]
Definition: Specifies the requested intra-position movement details.
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 125 September 2025
```

