---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "7.4 Message Building Blocks", "7.4.3 Cancellations <Cxls>", "7.4.3.4 Cancellation <Cxl>", "7.4.3.4.7 Underlying <Undrlyg>", "7.4.3.4.7.1 IntraPositionMovement <IntraPosMvmnt>"]
file_pages: [160]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 7.4.3.4.7.1 IntraPositionMovement <IntraPosMvmnt>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 160 to 160.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 160

```text
Underlying <Undrlyg> contains one of the following SettlementOrIntraPosition3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IntraPositionMovement <IntraPosMvmnt> [1..1]  160
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C15
161
     SettlementQuantity <SttlmQty> [1..1] ± 162
     SettlementDate <SttlmDt> [1..1] ± 162
     BalanceFrom <BalFr> [0..1] ± 162
     BalanceTo <BalTo> [0..1] ± 163
     SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 163
     Priority <Prty> [0..1] ± 163
Or}   SettlementTransaction <SttlmTx> [1..1]  163
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C15
164
     SettlementQuantity <SttlmQty> [1..1] ± 165
     SettlementAmount <SttlmAmt> [0..1] ± 165
     TradeDate <TradDt> [0..1] ± 166
     SettlementDate <SttlmDt> [1..1] ± 166
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C16,
C17,
C18,
C19
166
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C16,
C17,
C18,
C19
167
7.4.3.4.7.1  IntraPositionMovement <IntraPosMvmnt>
Presence: [1..1]
Definition: Specifies the requested intra-position movement details.
Approved by the Securities SEG on 21 August 2025 semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities - Settlement Restrictions 160 September 2025
```

