---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.8 RepairedFee <RprdFee>", "56.4.3.2.8.1 Type <Tp>", "56.4.3.2.8.1.2 Proprietary <Prtry>"]
file_pages: [4150]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.8.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4150 to 4150.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4150

```text
CodeName Name Definition
NTWK NetworkFee Network fee assigned to a transaction on
a DLT network.
56.4.3.2.8.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Fee (charge/commission) expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
56.4.3.2.8.2  RepairedStandardAmount <RprdStdAmt>
Presence: [0..1]
Definition: Modified value of the standard fee (charge/commission) amount applied on the order (the
standard fee (charge/commission) amount in the original individual order that has been repaired so that
the order can be accepted).
Impacted by: C1 "ActiveCurrency", C8 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
56.4.3.2.8.3  RepairedStandardRate <RprdStdRate>
Presence: [0..1]
Definition: Modified value of the standard fee (charge/commission) rate applied on the order (the
standard fee (charge/commission) rate in the original individual order that has been repaired so that the
order can be accepted).
Datatype: "PercentageRate" on page 5401
56.4.3.2.8.4  RepairedDiscountAmount <RprdDscntAmt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4150 May 2026
```

