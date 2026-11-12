---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "78.4 Message Building Blocks", "78.4.3 Cancellations <Cxls>", "78.4.3.4 Cancellation <Cxl>", "78.4.3.4.7 Underlying <Undrlyg>", "78.4.3.4.7.2 SettlementTransaction <SttlmTx>", "78.4.3.4.7.2.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [2719]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 78.4.3.4.7.2.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2719 to 2719.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2719

```text
SettlementTransaction <SttlmTx> contains the following TransactionDetails126 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
78.4.3.4.7.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C11 "DescriptionPresenceRule", C12 "DescriptionUsageRule", C13 "ISINGuideline", C14
"ISINPresenceRule", C15 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 2951 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2952
   OtherIdentification <OthrId> [0..*]  2952
     Identification <Id> [1..1] Text 2952
     Suffix <Sfx> [0..1] Text 2952
     Type <Tp> [1..1] ± 2952
   Description <Desc> [0..1] Text 2953
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2719 August 2026
```

