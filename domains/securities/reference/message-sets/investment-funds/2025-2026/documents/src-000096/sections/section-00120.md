---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.5 FundManagementCompany <FndMgmtCpny>"]
file_pages: [184]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.5 FundManagementCompany <FndMgmtCpny>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 184 to 184.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 184

```text
Definition: Name of the fund series. It is typically applicable to a redemption order, subscription order
confirmation or redemption order confirmation, but may be specified in the subscription, if known.
Datatype: "Max35Text" on page 5403
13.4.9.5  FundManagementCompany <FndMgmtCpny>
Presence: [0..1]
Definition: Issuer of the fund.
FundManagementCompany <FndMgmtCpny> contains one of the following elements (see
"PartyIdentification125Choice" on page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
13.4.9.6  TotalNAV <TtlNAV>
Presence: [0..*]
Definition: Value of all the holdings, less the fund's liabilities, attributable to a specific investment fund
class.
Impacted by: C3 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
13.4.9.7  TotalUnitsNumber <TtlUnitsNb>
Presence: [0..1]
Definition: Total number of investment fund class units that have been issued.
TotalUnitsNumber <TtlUnitsNb> contains the following elements (see "FinancialInstrumentQuantity1"
on page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 184 May 2026
```

