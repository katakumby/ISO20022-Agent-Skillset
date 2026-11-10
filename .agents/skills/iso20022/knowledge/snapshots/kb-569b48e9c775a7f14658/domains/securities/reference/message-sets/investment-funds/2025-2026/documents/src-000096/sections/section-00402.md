---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.6.16 UnitsDetails <UnitsDtls>", "26.4.6.16.8 TransactionOverhead <TxOvrhd>", "26.4.6.16.8.5 IndividualFee <IndvFee>", "26.4.6.16.8.5.2 Basis <Bsis>", "26.4.6.16.8.5.2.2 Proprietary <Prtry>"]
file_pages: [557]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.6.16.8.5.2.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 557 to 557.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 557

```text
CodeName Name Definition
GRAM GrossAmount Charge/Commission/tax basis is based
on the gross amount.
NEAM NetAmount Charge/commission/tax basis is based
on the net amount.
NAVP NetAssetValuePrice Charge/tax basis is the price.
PERU PerUnit Charges/tax basis is per unit of financial
instrument.
26.4.6.16.8.5.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Fee (charge/commission) basis expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
26.4.6.16.8.5.3  StandardAmount <StdAmt>
Presence: [0..1]
Definition: Standard fee (charge/commission) amount as specified in the fund prospectus or agreed for
the account.
Impacted by: C1 "ActiveCurrency", C10 "CurrencyAmount"
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
26.4.6.16.8.5.4  StandardRate <StdRate>
Presence: [0..1]
Definition: Standard fee (charge/commission) rate used to calculate the amount of the charge or fee, as
specified in the fund prospectus or agreed for the account.
Datatype: "PercentageRate" on page 5401
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 557 May 2026
```

