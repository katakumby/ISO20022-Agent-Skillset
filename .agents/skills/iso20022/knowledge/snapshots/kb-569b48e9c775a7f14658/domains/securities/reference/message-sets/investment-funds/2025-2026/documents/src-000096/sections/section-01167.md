---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.10 UnitsDetails <UnitsDtls>", "40.4.15.11.10.8 TransactionOverhead <TxOvrhd>", "40.4.15.11.10.8.5 IndividualFee <IndvFee>", "40.4.15.11.10.8.5.6 AppliedAmount <ApldAmt>"]
file_pages: [1627]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.10.8.5.6 AppliedAmount <ApldAmt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1627 to 1627.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1627

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
40.4.15.11.10.8.5.6  AppliedAmount <ApldAmt>
Presence: [0..1]
Definition: Fee (charge/commission) amount applied to the transaction.
Impacted by: C1 "ActiveCurrency", C18 "CurrencyAmount"
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
40.4.15.11.10.8.5.7  AppliedRate <ApldRate>
Presence: [0..1]
Definition: Final rate used to calculate the fee (charge/commission) amount.
Datatype: "PercentageRate" on page 5401
40.4.15.11.10.8.5.8  NonStandardSLAReference <NonStdSLARef>
Presence: [0..1]
Definition: Reference to a sales agreement that overrides normal processing or the Service Level
Agreement (SLA), such as a fee (charge/commission).
Datatype: "Max35Text" on page 5403
40.4.15.11.10.8.5.9  RecipientIdentification <RcptId>
Presence: [0..1]
Definition: Party entitled to the amount of money resulting from a fee (charge/commission).
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1627 May 2026
```

