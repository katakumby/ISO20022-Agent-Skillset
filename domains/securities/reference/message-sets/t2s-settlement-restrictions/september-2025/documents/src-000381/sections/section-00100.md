---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.4 Message Building Blocks", "5.4.3 Modifications <Mods>", "5.4.3.4 Modification <Mod>", "5.4.3.4.7 Underlying <Undrlyg>", "5.4.3.4.7.2 SettlementTransaction <SttlmTx>", "5.4.3.4.7.2.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [129]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.4.3.4.7.2.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 129 to 129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 129

```text
SettlementTransaction <SttlmTx> contains the following TransactionDetails126 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
5.4.3.4.7.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C11 "DescriptionPresenceRule", C12 "DescriptionUsageRule", C13 "ISINGuideline", C14
"ISINPresenceRule", C16 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 207 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 208
   OtherIdentification <OthrId> [0..*]  208
     Identification <Id> [1..1] Text 208
     Suffix <Sfx> [0..1] Text 208
     Type <Tp> [1..1] ± 208
   Description <Desc> [0..1] Text 208
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 129 September 2025
```

