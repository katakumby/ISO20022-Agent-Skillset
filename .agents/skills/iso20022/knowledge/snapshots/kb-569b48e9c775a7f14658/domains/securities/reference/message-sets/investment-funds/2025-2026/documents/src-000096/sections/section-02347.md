---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.6 FinancialInstrumentDetails <FinInstrmDtls>", "52.4.5.10.6.1 Identification <Id>", "52.4.5.10.6.1.2 SEDOL <SEDOL>"]
file_pages: [3308]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.6.1.2 SEDOL <SEDOL>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3308 to 3308.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3308

```text
Datatype: "ISINOct2015Identifier" on page 5395
52.4.5.10.6.1.2  SEDOL <SEDOL>
Presence: [1..1]
Definition: Stock Exchange Daily Official List (SEDOL) number. A code used by the London Stock
Exchange to identify foreign stocks, especially those that aren't actively traded in the US and don't have
a CUSIP number.
Datatype: "SEDOLIdentifier" on page 5397
52.4.5.10.6.1.3  CUSIP <CUSIP>
Presence: [1..1]
Definition: Committee on Uniform Securities and Identification Procedures (CUSIP). The standards
body that created and maintains the securities classification system in the US. The CUSIP is composed
of a 9-character number that uniquely identifies a particular security. Non-US securities have a similar
number called the CINS number.
Datatype: "CUSIPIdentifier" on page 5392
52.4.5.10.6.1.4  RIC <RIC>
Presence: [1..1]
Definition: Reuters Identification Code (RIC). A numbering system used within the Reuters system to
identify instruments worldwide. The RIC contains an X-character market specific code (can be the
CUSIP or EPIC codes) followed by a full stop, then the two-digit ISO country code, for example, IBM in
UK is IBM.UK.
Datatype: "RICIdentifier" on page 5397
52.4.5.10.6.1.5  TickerSymbol <TckrSymb>
Presence: [1..1]
Definition: Letters that identify a stock traded on a stock exchange. The Ticker Symbol is a short and
convenient way of identifying a stock, for example, RTR.L for Reuters quoted in London.
Datatype: "TickerIdentifier" on page 5399
52.4.5.10.6.1.6  Bloomberg <Blmbrg>
Presence: [1..1]
Definition: Identifier of a security assigned by the Bloomberg organisation.
Datatype: "Bloomberg2Identifier" on page 5390
52.4.5.10.6.1.7  CTA <CTA>
Presence: [1..1]
Definition: Identifier of a security assigned by the Consolidated Tape Association.
Datatype: "ConsolidatedTapeAssociationIdentifier" on page 5392
52.4.5.10.6.1.8  QUICK <QUICK>
Presence: [1..1]
Definition: Identifier of a security assigned by the Japanese QUICK identification scheme for financial
instruments.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3308 May 2026
```

