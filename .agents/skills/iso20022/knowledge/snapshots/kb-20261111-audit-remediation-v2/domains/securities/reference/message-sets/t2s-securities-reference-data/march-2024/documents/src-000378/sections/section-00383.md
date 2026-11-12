---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.5 SecurityIdentification39", "13.1.6.5.3 Description <Desc>"]
file_pages: [476]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.5.3 Description <Desc>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 476 to 476.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 476

```text
Type <Tp> contains one of the following elements (see "IdentificationSource3Choice" on page 480 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 480
Or}   Proprietary <Prtry> [1..1] Text 480
13.1.6.5.3  Description <Desc>
Presence: [0..1]
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 533
13.1.7 Financial Instrument Quantity
13.1.7.1  FinancialInstrumentQuantity1Choice
Definition: Choice between formats for the quantity of security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.7.1.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, for example, a number of shares.
Datatype: "DecimalNumber" on page 532
13.1.7.1.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is, the principal, of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 507
13.1.7.1.3  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 507
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 476 March 2024
```

