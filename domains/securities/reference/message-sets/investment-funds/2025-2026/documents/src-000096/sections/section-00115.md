---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.4 FinancialInstrumentDetails <FinInstrmDtls>", "13.4.9.4.1 Identification <Id>", "13.4.9.4.1.2 SEDOL <SEDOL>"]
file_pages: [179]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.4.1.2 SEDOL <SEDOL>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 179 to 179.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 179

```text
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 5395
13.4.9.4.1.2  SEDOL <SEDOL>
Presence: [1..1]
Definition: Stock Exchange Daily Official List (SEDOL) number. A code used by the London Stock
Exchange to identify foreign stocks, especially those that aren't actively traded in the US and don't have
a CUSIP number.
Datatype: "SEDOLIdentifier" on page 5397
13.4.9.4.1.3  CUSIP <CUSIP>
Presence: [1..1]
Definition: Committee on Uniform Securities and Identification Procedures (CUSIP). The standards
body that created and maintains the securities classification system in the US. The CUSIP is composed
of a 9-character number that uniquely identifies a particular security. Non-US securities have a similar
number called the CINS number.
Datatype: "CUSIPIdentifier" on page 5392
13.4.9.4.1.4  RIC <RIC>
Presence: [1..1]
Definition: Reuters Identification Code (RIC). A numbering system used within the Reuters system to
identify instruments worldwide. The RIC contains an X-character market specific code (can be the
CUSIP or EPIC codes) followed by a full stop, then the two-digit ISO country code, for example, IBM in
UK is IBM.UK.
Datatype: "RICIdentifier" on page 5397
13.4.9.4.1.5  TickerSymbol <TckrSymb>
Presence: [1..1]
Definition: Letters that identify a stock traded on a stock exchange. The Ticker Symbol is a short and
convenient way of identifying a stock, for example, RTR.L for Reuters quoted in London.
Datatype: "TickerIdentifier" on page 5399
13.4.9.4.1.6  Bloomberg <Blmbrg>
Presence: [1..1]
Definition: Identifier of a security assigned by the Bloomberg organisation.
Datatype: "Bloomberg2Identifier" on page 5390
13.4.9.4.1.7  CTA <CTA>
Presence: [1..1]
Definition: Identifier of a security assigned by the Consolidated Tape Association.
Datatype: "ConsolidatedTapeAssociationIdentifier" on page 5392
13.4.9.4.1.8  QUICK <QUICK>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 179 May 2026
```

