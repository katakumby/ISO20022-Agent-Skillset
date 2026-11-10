---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "78.4 Message Building Blocks", "78.4.3 Cancellations <Cxls>", "78.4.3.4 Cancellation <Cxl>", "78.4.3.4.7 Underlying <Undrlyg>", "78.4.3.4.7.1 IntraPositionMovement <IntraPosMvmnt>"]
file_pages: [2715]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 78.4.3.4.7.1 IntraPositionMovement <IntraPosMvmnt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2715 to 2715.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2715

```text
Underlying <Undrlyg> contains one of the following SettlementOrIntraPosition3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IntraPositionMovement <IntraPosMvmnt> [1..1]  2715
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C15
2716
     SettlementQuantity <SttlmQty> [1..1] ± 2717
     SettlementDate <SttlmDt> [1..1] ± 2717
     BalanceFrom <BalFr> [0..1] ± 2717
     BalanceTo <BalTo> [0..1] ± 2718
     SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 2718
     Priority <Prty> [0..1] ± 2718
Or}   SettlementTransaction <SttlmTx> [1..1]  2718
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C15
2719
     SettlementQuantity <SttlmQty> [1..1] ± 2720
     SettlementAmount <SttlmAmt> [0..1] ± 2720
     TradeDate <TradDt> [0..1] ± 2721
     SettlementDate <SttlmDt> [1..1] ± 2721
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C16,
C17,
C18,
C19
2721
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C16,
C17,
C18,
C19
2722
78.4.3.4.7.1  IntraPositionMovement <IntraPosMvmnt>
Presence: [1..1]
Definition: Specifies the requested intra-position movement details.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2715 August 2026
```

