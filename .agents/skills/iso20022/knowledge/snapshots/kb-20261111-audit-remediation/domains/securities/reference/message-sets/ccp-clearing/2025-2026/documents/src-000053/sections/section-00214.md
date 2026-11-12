---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["9 MX secl.008.001.03 BuyInResponseV03", "9.4 Message Building Blocks", "9.4.2 BuyInResponseDetails <BuyInRspnDtls>", "9.4.2.3 NumberOfDays <NbOfDays>"]
file_pages: [280]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.008.001.03"]
---

# 9.4.2.3 NumberOfDays <NbOfDays>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 280 to 280.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 280

```text
• Meaning When True: Yes
• Meaning When False: No
9.4.2.3  NumberOfDays <NbOfDays>
Presence: [1..1]
Definition: Number of days associated to the request for delay.
Datatype: Number on page 491
9.4.2.4  InitialQuantity <InitlQty>
Presence: [1..1]
Definition: Buy in quantity called initially by the central counterparty.
InitialQuantity <InitlQty> contains one of the following elements (see
FinancialInstrumentQuantity1Choice on page 396 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 396
Or   FaceAmount <FaceAmt> [1..1] Amount 396
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 396
9.4.2.5  CoveredQuantity <CvrdQty>
Presence: [1..1]
Definition: Quantity amount covered by the clearing member after notification.
CoveredQuantity <CvrdQty> contains one of the following elements (see
FinancialInstrumentQuantity1Choice on page 396 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 396
Or   FaceAmount <FaceAmt> [1..1] Amount 396
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 396
9.4.2.6  UncoveredQuantity <UcvrdQty>
Presence: [1..1]
Definition: Quantity amount non covered by the clearing member after notification (this is, new buy in
amount to be executed).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.008.001.03 BuyInResponseV03
March 2026 280
```

