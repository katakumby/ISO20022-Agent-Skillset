---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.44 SettlementInformation <SttlmInf>", "32.4.3.1.1.3.44.1 SecuritiesQuantityType <SctiesQtyTp>"]
file_pages: [2002]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.44.1 SecuritiesQuantityType <SctiesQtyTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2002 to 2002.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2002

```text
SettlementInformation <SttlmInf> contains the following SettlementInformation17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesQuantityType <SctiesQtyTp> [0..1]  2002
{Or     Code <Cd> [1..1] CodeSet 2002
Or}     Proprietary <Prtry> [1..1] ± 2002
   ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 2003
   MinimumDenomination <MinDnmtn> [0..1] ± 2003
   MinimumMultipleQuantity <MinMltplQty> [0..1] ± 2003
   DeviatingSettlementUnit <DevtgSttlmUnit> [0..*] ± 2003
32.4.3.1.1.3.44.1  SecuritiesQuantityType <SctiesQtyTp>
Presence: [0..1]
Definition: Choice between formats for the quantity of security.
SecuritiesQuantityType <SctiesQtyTp> contains one of the following SettlementUnitType3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2002
Or}   Proprietary <Prtry> [1..1] ± 2002
32.4.3.1.1.3.44.1.1  Code <Cd>
Presence: [1..1]
Definition: Settlement unit type expressed as an ISO 20022 code.
Datatype: "SettlementUnitType1Code" on page 3303
CodeName Name Definition
FAMT FaceAmount Represent the face amount, for example
the principal of a debt instrument.
UNIT Unit Represent the unit as a number, for
example a number of shares.
32.4.3.1.1.3.44.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement unit type expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 2002 August 2026
```

