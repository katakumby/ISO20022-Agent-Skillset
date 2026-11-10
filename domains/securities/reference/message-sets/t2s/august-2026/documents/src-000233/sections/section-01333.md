---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.4 Derivative <Deriv>", "32.4.3.1.1.2.4.2 Option <Optn>", "32.4.3.1.1.2.4.2.1 OptionSettlementStyle <OptnSttlmStyle>"]
file_pages: [1932]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.4.2.1 OptionSettlementStyle <OptnSttlmStyle>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1932 to 1932.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1932

```text
32.4.3.1.1.2.4.2.1  OptionSettlementStyle <OptnSttlmStyle>
Presence: [0..1]
Definition: Specifies whether the option contract settles at the open or close of the market.
OptionSettlementStyle <OptnSttlmStyle> contains one of the following SettleStyle2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [0..*] CodeSet 1932
Or}   Proprietary <Prtry> [1..1] ± 1932
32.4.3.1.1.2.4.2.1.1  Code <Cd>
Presence: [0..*]
Definition: Settle style expressed as an ISO 20022 code.
Datatype: "SettleStyle1Code" on page 3303
CodeName Name Definition
SETC SettleOnClose Settlement is only allowed on the closing
of the future contract.
SETO SettleOnOpen Settlement is only allowed on the
opening of the future contract.
32.4.3.1.1.2.4.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settle style expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
32.4.3.1.1.2.4.2.2  ConversionDate <ConvsDt>
Presence: [0..1]
Definition: Deadline by which a convertible security must be converted according to the terms of the
issue.
Datatype: "ISODateTime" on page 3320
32.4.3.1.1.2.4.2.3  StrikePrice <StrkPric>
Presence: [0..1]
Definition: Amount of money for which goods, services or assets are offered, sold, or bought.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1932 August 2026
```

