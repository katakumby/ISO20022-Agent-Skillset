---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.2 Derivative4", "13.1.2.2.2 Option <Optn>", "13.1.2.2.2.1 OptionSettlementStyle <OptnSttlmStyle>"]
file_pages: [177]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.2.2.1 OptionSettlementStyle <OptnSttlmStyle>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 177 to 177.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 177

```text
13.1.2.2.2.1  OptionSettlementStyle <OptnSttlmStyle>
Presence: [0..1]
Definition: Specifies whether the option contract settles at the open or close of the market.
OptionSettlementStyle <OptnSttlmStyle> contains one of the following SettleStyle2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [0..*] CodeSet 177
Or}   Proprietary <Prtry> [1..1] ± 177
13.1.2.2.2.1.1  Code <Cd>
Presence: [0..*]
Definition: Settle style expressed as an ISO 20022 code.
Datatype: "SettleStyle1Code" on page 524
CodeName Name Definition
SETC SettleOnClose Settlement is only allowed on the closing
of the future contract.
SETO SettleOnOpen Settlement is only allowed on the
opening of the future contract.
13.1.2.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settle style expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.2.2.2.2  ConversionDate <ConvsDt>
Presence: [0..1]
Definition: Deadline by which a convertible security must be converted according to the terms of the
issue.
Datatype: "ISODateTime" on page 529
13.1.2.2.2.3  StrikePrice <StrkPric>
Presence: [0..1]
Definition: Amount of money for which goods, services or assets are offered, sold, or bought.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 177 March 2024
```

