---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.19 Financial Instrument Identification", "66.1.19.2 SecurityIdentification25Choice", "66.1.19.2.4 RIC <RIC>"]
file_pages: [4523]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.19.2.4 RIC <RIC>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4523 to 4523.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4523

```text
Definition: Committee on Uniform Securities and Identification Procedures (CUSIP). The standards
body that created and maintains the securities classification system in the US. The CUSIP is composed
of a 9-character number that uniquely identifies a particular security. Non-US securities have a similar
number called the CINS number.
Datatype: "CUSIPIdentifier" on page 5392
66.1.19.2.4  RIC <RIC>
Presence: [1..1]
Definition: Reuters Identification Code (RIC). A numbering system used within the Reuters system to
identify instruments worldwide. The RIC contains an X-character market specific code (can be the
CUSIP or EPIC codes) followed by a full stop, then the two-digit ISO country code, for example, IBM in
UK is IBM.UK.
Datatype: "RICIdentifier" on page 5397
66.1.19.2.5  TickerSymbol <TckrSymb>
Presence: [1..1]
Definition: Letters that identify a stock traded on a stock exchange. The Ticker Symbol is a short and
convenient way of identifying a stock, for example, RTR.L for Reuters quoted in London.
Datatype: "TickerIdentifier" on page 5399
66.1.19.2.6  Bloomberg <Blmbrg>
Presence: [1..1]
Definition: Identifier of a security assigned by the Bloomberg organisation.
Datatype: "Bloomberg2Identifier" on page 5390
66.1.19.2.7  CTA <CTA>
Presence: [1..1]
Definition: Identifier of a security assigned by the Consolidated Tape Association.
Datatype: "ConsolidatedTapeAssociationIdentifier" on page 5392
66.1.19.2.8  QUICK <QUICK>
Presence: [1..1]
Definition: Identifier of a security assigned by the Japanese QUICK identification scheme for financial
instruments.
Datatype: "QUICKIdentifier" on page 5397
66.1.19.2.9  Wertpapier <Wrtppr>
Presence: [1..1]
Definition: Wertpapier Kenn-nummer. A number issued in Germany by the Wertpapier Mitteilungen. The
Wertpapier Kenn-nummer, sometimes called WPK, contains 6-digits, but no check digit. There are
different ranges of numbers representing different classes of securities.
Datatype: "WertpapierIdentifier" on page 5399
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4523 May 2026
```

