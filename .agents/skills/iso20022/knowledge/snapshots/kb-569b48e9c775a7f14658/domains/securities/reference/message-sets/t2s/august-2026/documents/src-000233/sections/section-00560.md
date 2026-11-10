---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.4 Derivative <Deriv>", "27.4.2.2.4.2 Option <Optn>", "27.4.2.2.4.2.8 StrikeValue <StrkVal>"]
file_pages: [735]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.4.2.8 StrikeValue <StrkVal>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 735 to 735.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 735

```text
Definition: Specifies whether it is a Call option (right to purchase a specific underlying asset) or a Put
option (right to sell a specific underlying asset).
OptionType <OptnTp> contains one of the following elements (see "OptionType8Choice" on
page 3047 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [0..*] CodeSet 3048
Or}   Proprietary <Prtry> [1..1] ± 3048
27.4.2.2.4.2.8  StrikeValue <StrkVal>
Presence: [0..1]
Definition: Used for derivatives. The number of shares/units for the financial instrument involved in the
option trade.
Datatype: "Number" on page 3324
27.4.2.2.4.2.9  StrikeMultiplier <StrkMltplr>
Presence: [0..1]
Definition: Used for derivatives. Multiplier applied to the strike price for the purpose of calculating the
settlement value.
Datatype: "Number" on page 3324
27.4.2.2.4.2.10  InstrumentAssignmentMethod <InstrmAssgnmtMtd>
Presence: [0..1]
Definition: Method under which assignment was conducted.
InstrumentAssignmentMethod <InstrmAssgnmtMtd> contains one of the following
AssignmentMethod2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 735
Or}   Proprietary <Prtry> [1..1] ± 735
27.4.2.2.4.2.10.1  Code <Cd>
Presence: [1..1]
Definition: Assignment method expressed as an ISO 20022 code.
Datatype: "AssignmentMethod1Code" on page 3214
CodeName Name Definition
RAND Random Assignment was conducted randomly.
PROR Prorata Assignment was conducted on a prorata
basis.
27.4.2.2.4.2.10.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 735 August 2026
```

