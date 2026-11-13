---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.45 SettlementInformation <SttlmInf>", "13.1.6.4.45.1 SecuritiesQuantityType <SctiesQtyTp>", "13.1.6.4.45.1.2 Proprietary <Prtry>"]
file_pages: [447]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.45.1.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 447 to 447.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 447

```text
CodeName Name Definition
FAMT FaceAmount Represent the face amount, for example
the principal of a debt instrument.
UNIT Unit Represent the unit as a number, for
example a number of shares.
13.1.6.4.45.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement unit type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.4.45.2  ContractSettlementMonth <CtrctSttlmMnth>
Presence: [0..1]
Definition: Specifies when the contract (i.e. MBS/TBA) will settle.
Datatype: "ISOYearMonth" on page 535
13.1.6.4.45.3  MinimumDenomination <MinDnmtn>
Presence: [0..1]
Definition: Indicates the minimum quantity (unit or nominal) of a security.
MinimumDenomination <MinDnmtn> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.6.4.45.4  MinimumMultipleQuantity <MinMltplQty>
Presence: [0..1]
Definition: Minimum multiple quantity (unit or nominal) of securities.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 447 March 2024
```

