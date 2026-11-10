---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.3.1.4 Derivative <Deriv>", "28.4.2.1.3.1.4.2 Option <Optn>", "28.4.2.1.3.1.4.2.8 StrikeValue <StrkVal>"]
file_pages: [1471]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.1.4.2.8 StrikeValue <StrkVal>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1471 to 1471.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1471

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
28.4.2.1.3.1.4.2.8  StrikeValue <StrkVal>
Presence: [0..1]
Definition: Used for derivatives. The number of shares/units for the financial instrument involved in the
option trade.
Datatype: "Number" on page 3324
28.4.2.1.3.1.4.2.9  StrikeMultiplier <StrkMltplr>
Presence: [0..1]
Definition: Used for derivatives. Multiplier applied to the strike price for the purpose of calculating the
settlement value.
Datatype: "Number" on page 3324
28.4.2.1.3.1.4.2.10  InstrumentAssignmentMethod <InstrmAssgnmtMtd>
Presence: [0..1]
Definition: Method under which assignment was conducted.
InstrumentAssignmentMethod <InstrmAssgnmtMtd> contains one of the following
AssignmentMethod2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1471
Or}   Proprietary <Prtry> [1..1] ± 1471
28.4.2.1.3.1.4.2.10.1  Code <Cd>
Presence: [1..1]
Definition: Assignment method expressed as an ISO 20022 code.
Datatype: "AssignmentMethod1Code" on page 3214
CodeName Name Definition
RAND Random Assignment was conducted randomly.
PROR Prorata Assignment was conducted on a prorata
basis.
28.4.2.1.3.1.4.2.10.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1471 August 2026
```

