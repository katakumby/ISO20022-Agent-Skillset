---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.2 Instrument <Instrm>", "40.4.15.11.2.1 Security <Scty>", "40.4.15.11.2.1.1 Identification <Id>", "40.4.15.11.2.1.1.3 CUSIP <CUSIP>"]
file_pages: [1601]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.2.1.1.3 CUSIP <CUSIP>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1601 to 1601.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1601

```text
40.4.15.11.2.1.1.3  CUSIP <CUSIP>
Presence: [1..1]
Definition: Committee on Uniform Securities and Identification Procedures (CUSIP). The standards
body that created and maintains the securities classification system in the US. The CUSIP is composed
of a 9-character number that uniquely identifies a particular security. Non-US securities have a similar
number called the CINS number.
Datatype: "CUSIPIdentifier" on page 5392
40.4.15.11.2.1.1.4  RIC <RIC>
Presence: [1..1]
Definition: Reuters Identification Code (RIC). A numbering system used within the Reuters system to
identify instruments worldwide. The RIC contains an X-character market specific code (can be the
CUSIP or EPIC codes) followed by a full stop, then the two-digit ISO country code, for example, IBM in
UK is IBM.UK.
Datatype: "RICIdentifier" on page 5397
40.4.15.11.2.1.1.5  TickerSymbol <TckrSymb>
Presence: [1..1]
Definition: Letters that identify a stock traded on a stock exchange. The Ticker Symbol is a short and
convenient way of identifying a stock, for example, RTR.L for Reuters quoted in London.
Datatype: "TickerIdentifier" on page 5399
40.4.15.11.2.1.1.6  Bloomberg <Blmbrg>
Presence: [1..1]
Definition: Identifier of a security assigned by the Bloomberg organisation.
Datatype: "Bloomberg2Identifier" on page 5390
40.4.15.11.2.1.1.7  CTA <CTA>
Presence: [1..1]
Definition: Identifier of a security assigned by the Consolidated Tape Association.
Datatype: "ConsolidatedTapeAssociationIdentifier" on page 5392
40.4.15.11.2.1.1.8  QUICK <QUICK>
Presence: [1..1]
Definition: Identifier of a security assigned by the Japanese QUICK identification scheme for financial
instruments.
Datatype: "QUICKIdentifier" on page 5397
40.4.15.11.2.1.1.9  Wertpapier <Wrtppr>
Presence: [1..1]
Definition: Wertpapier Kenn-nummer. A number issued in Germany by the Wertpapier Mitteilungen. The
Wertpapier Kenn-nummer, sometimes called WPK, contains 6-digits, but no check digit. There are
different ranges of numbers representing different classes of securities.
Datatype: "WertpapierIdentifier" on page 5399
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1601 May 2026
```

