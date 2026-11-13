---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.4 Derivative <Deriv>", "32.4.3.1.1.2.4.2 Option <Optn>", "32.4.3.1.1.2.4.2.16 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "32.4.3.1.1.2.4.2.16.9 StartValue <StartVal>"]
file_pages: [1950]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.4.2.16.9 StartValue <StartVal>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1950 to 1950.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1950

```text
CodeName Name Definition
sell financial instruments at 67 or to buy
at 60.
NET2 Net Price is a net price, ie, net only of local
broker's commission, local fees and local
taxes.
NDIS NetDisclosed Price is net to the disclosed client.
NET1 NetOfAll Price is a net price, ie, net of all charges,
fees and taxes.
NUND NetUndisclosed Price is net to the client undisclosed
(used in the UK market).
NOGR NotionalGross Price is notional gross (used in the UK
market).
PARV ParValue Price is equal to the nominal or face
value of the instrument.
RDAV RoundedAverage Price is a rounded average price.
STOP Stop Price is a stop price used in an order to
buy. The order becomes a market order
when the financial instrument trades at
or above the stop price after the order is
submitted. In an order to sell the order
becomes a market order when the
financial instrument trades at or below
the stop price.
32.4.3.1.1.2.4.2.16.9  StartValue <StartVal>
Presence: [0..1]
Definition: Currency value attributed to this collateral at the start of the agreement.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
32.4.3.1.1.2.4.2.16.10  CurrentValue <CurVal>
Presence: [0..1]
Definition: Currency value currently attributed to this collateral.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1950 August 2026
```

