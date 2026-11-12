---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.44 SettlementInformation <SttlmInf>", "32.4.3.1.1.3.44.2 ContractSettlementMonth <CtrctSttlmMnth>"]
file_pages: [2003]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.44.2 ContractSettlementMonth <CtrctSttlmMnth>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2003 to 2003.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2003

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
32.4.3.1.1.3.44.2  ContractSettlementMonth <CtrctSttlmMnth>
Presence: [0..1]
Definition: Specifies when the contract (i.e. MBS/TBA) will settle.
Datatype: "ISOYearMonth" on page 3330
32.4.3.1.1.3.44.3  MinimumDenomination <MinDnmtn>
Presence: [0..1]
Definition: Indicates the minimum quantity (unit or nominal) of a security.
MinimumDenomination <MinDnmtn> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
32.4.3.1.1.3.44.4  MinimumMultipleQuantity <MinMltplQty>
Presence: [0..1]
Definition: Minimum multiple quantity (unit or nominal) of securities.
MinimumMultipleQuantity <MinMltplQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
32.4.3.1.1.3.44.5  DeviatingSettlementUnit <DevtgSttlmUnit>
Presence: [0..*]
Definition: Minimum quantity of securities that can be purchased without incurring a larger fee. For
example, if the round lot size is 100 and the trade is for 125 shares, then 100 will be processed without
a fee and the remaining 25 will incur a service fee for being an odd lot size.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 2003 August 2026
```

