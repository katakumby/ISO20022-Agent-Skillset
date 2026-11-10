---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.3.2.46 SettlementInformation <SttlmInf>", "28.4.2.1.3.2.46.1 SecuritiesQuantityType <SctiesQtyTp>", "28.4.2.1.3.2.46.1.2 Proprietary <Prtry>"]
file_pages: [1535]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.2.46.1.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1535 to 1535.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1535

```text
CodeName Name Definition
FAMT FaceAmount Represent the face amount, for example
the principal of a debt instrument.
UNIT Unit Represent the unit as a number, for
example a number of shares.
28.4.2.1.3.2.46.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement unit type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
28.4.2.1.3.2.46.2  ContractSettlementMonth <CtrctSttlmMnth>
Presence: [0..1]
Definition: Specifies when the contract (i.e. MBS/TBA) will settle.
Datatype: "ISOYearMonth" on page 3330
28.4.2.1.3.2.46.3  MinimumDenomination <MinDnmtn>
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
28.4.2.1.3.2.46.4  MinimumMultipleQuantity <MinMltplQty>
Presence: [0..1]
Definition: Minimum multiple quantity (unit or nominal) of securities.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1535 August 2026
```

