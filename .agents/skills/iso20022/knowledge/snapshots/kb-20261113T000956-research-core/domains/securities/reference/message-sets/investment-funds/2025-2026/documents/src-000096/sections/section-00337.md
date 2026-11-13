---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.5 MasterReference <MstrRef>", "24.4.6.12 UnitsDetails <UnitsDtls>", "24.4.6.12.8 TransactionOverhead <TxOvrhd>", "24.4.6.12.8.5 IndividualFee <IndvFee>", "24.4.6.12.8.5.5 DiscountDetails <DscntDtls>", "24.4.6.12.8.5.5.2 Rate <Rate>"]
file_pages: [471]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.6.12.8.5.5.2 Rate <Rate>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 471 to 471.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 471

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
24.4.6.12.8.5.5.2  Rate <Rate>
Presence: [0..1]
Definition: Difference between the standard fee (charge/commission) rate and the applied rate of the
fee (charge/commission).
EXAMPLE:
Standard rate is 5%
Discount rate is 3%
Applied rate is 2%.
Datatype: "PercentageRate" on page 5401
24.4.6.12.8.5.5.3  Basis <Bsis>
Presence: [0..1]
Definition: Form of the discount or rebate, for example, cash.
Basis <Bsis> contains one of the following WaivingInstruction2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 471
Or}   Proprietary <Prtry> [1..1] ± 471
24.4.6.12.8.5.5.3.1  Code <Cd>
Presence: [1..1]
Definition: Type of discount or waiving expressed as a code.
Datatype: "WaivingInstruction1Code" on page 5388
CodeName Name Definition
WICA WaiveInCash Form of commission waived is cash.
WIUN WaiveInUnits Form of commission waived is additional
units of a financial instrument.
24.4.6.12.8.5.5.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of discount or waiving expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 471 May 2026
```

