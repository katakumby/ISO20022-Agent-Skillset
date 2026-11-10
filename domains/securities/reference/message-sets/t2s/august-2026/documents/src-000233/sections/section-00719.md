---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.1.1.4 Derivative <Deriv>", "28.4.2.1.1.1.4.2 Option <Optn>", "28.4.2.1.1.1.4.2.1 OptionSettlementStyle <OptnSttlmStyle>"]
file_pages: [1090]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.1.4.2.1 OptionSettlementStyle <OptnSttlmStyle>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1090 to 1090.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1090

```text
28.4.2.1.1.1.4.2.1  OptionSettlementStyle <OptnSttlmStyle>
Presence: [0..1]
Definition: Specifies whether the option contract settles at the open or close of the market.
OptionSettlementStyle <OptnSttlmStyle> contains one of the following SettleStyle2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [0..*] CodeSet 1090
Or}   Proprietary <Prtry> [1..1] ± 1090
28.4.2.1.1.1.4.2.1.1  Code <Cd>
Presence: [0..*]
Definition: Settle style expressed as an ISO 20022 code.
Datatype: "SettleStyle1Code" on page 3303
CodeName Name Definition
SETC SettleOnClose Settlement is only allowed on the closing
of the future contract.
SETO SettleOnOpen Settlement is only allowed on the
opening of the future contract.
28.4.2.1.1.1.4.2.1.2  Proprietary <Prtry>
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
28.4.2.1.1.1.4.2.2  ConversionDate <ConvsDt>
Presence: [0..1]
Definition: Deadline by which a convertible security must be converted according to the terms of the
issue.
Datatype: "ISODateTime" on page 3320
28.4.2.1.1.1.4.2.3  StrikePrice <StrkPric>
Presence: [0..1]
Definition: Amount of money for which goods, services or assets are offered, sold, or bought.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1090 August 2026
```

