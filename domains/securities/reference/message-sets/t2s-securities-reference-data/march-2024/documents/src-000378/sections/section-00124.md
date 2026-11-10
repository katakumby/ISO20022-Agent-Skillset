---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.2 Derivative4", "13.1.2.2.2 Option <Optn>", "13.1.2.2.2.8 StrikeValue <StrkVal>"]
file_pages: [182]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.2.2.8 StrikeValue <StrkVal>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 182 to 182.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 182

```text
Definition: Specifies whether it is a Call option (right to purchase a specific underlying asset) or a Put
option (right to sell a specific underlying asset).
OptionType <OptnTp> contains one of the following elements (see "OptionType8Choice" on page 481
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [0..*] CodeSet 481
Or}   Proprietary <Prtry> [1..1] ± 482
13.1.2.2.2.8  StrikeValue <StrkVal>
Presence: [0..1]
Definition: Used for derivatives. The number of shares/units for the financial instrument involved in the
option trade.
Datatype: "Number" on page 532
13.1.2.2.2.9  StrikeMultiplier <StrkMltplr>
Presence: [0..1]
Definition: Used for derivatives. Multiplier applied to the strike price for the purpose of calculating the
settlement value.
Datatype: "Number" on page 532
13.1.2.2.2.10  InstrumentAssignmentMethod <InstrmAssgnmtMtd>
Presence: [0..1]
Definition: Method under which assignment was conducted.
InstrumentAssignmentMethod <InstrmAssgnmtMtd> contains one of the following
AssignmentMethod2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 182
Or}   Proprietary <Prtry> [1..1] ± 182
13.1.2.2.2.10.1  Code <Cd>
Presence: [1..1]
Definition: Assignment method expressed as an ISO 20022 code.
Datatype: "AssignmentMethod1Code" on page 509
CodeName Name Definition
RAND Random Assignment was conducted randomly.
PROR Prorata Assignment was conducted on a prorata
basis.
13.1.2.2.2.10.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 182 March 2024
```

