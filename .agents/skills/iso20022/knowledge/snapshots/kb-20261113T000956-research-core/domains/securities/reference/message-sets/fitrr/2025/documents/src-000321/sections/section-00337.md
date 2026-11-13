---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.12 AdditionalAttributes <AddtlAttrbts>", "22.1.13.2.12.1 WaiverIndicator <WvrInd>"]
file_pages: [391]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.12.1 WaiverIndicator <WvrInd>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 391 to 391.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 391

```text
22.1.13.2.12.1  WaiverIndicator <WvrInd>
Presence: [0..*]
Definition: Indicates whether the transaction was executed under a pre-trade waiver.
Datatype: "ReportingWaiverType1Code" on page 445
CodeName Name Definition
OILQ NegotiatedTransactionInIlliquidFinancialInstrum
ent
Pre-trade waiver was for a negotiated
transaction in illiquid financial
instruments. Applicable to equity
instruments.
NLIQ NegotiatedTransactionInLiquidFinancialInstrum
ent
Pre-trade waiver was for a negotiated
transaction in liquid financial
instruments. Applicable to equity
instruments.
PRIC NegotiatedTransactionWithConditions Pre-trade waiver was for a negotiated
transaction subject to conditions other
than the current market price of that
financial instruments. Applicable to
equity instruments.
ILQD IlliquidInstrumentTransaction Pre-trade waiver was for an illiquid
instrument transaction. Applicable to
non-equity instruments.
RFPT ReferencePriceTransaction Pre-trade waiver was for a reference
price transaction. Applicable to equity
instruments.
SIZE AboveSpecificSizeTransaction Pre-trade waiver was for an above
specific size transaction. Applicable to
non-equity instruments.
22.1.13.2.12.2  ShortSellingIndicator <ShrtSellgInd>
Presence: [0..1]
Definition: Indicates a short sell concluded by the investment agent on its own accounts or on behalf of
a client, as described in the local regulation.
Datatype: "Side5Code" on page 446
CodeName Name Definition
SESH SellShort An order to sell a security that the seller
does not own; a sale effected by
delivering a security borrowed by, or for
the account of, the seller. Can only be
executed on a plus or zero plus tick.
SELL Sell Order is sell driven.
SSEX SellShortExempt Short sale exempt from short-sale rules.
UNDI Undisclosed The side of the indication of interest is
not disclosed.
22.1.13.2.12.3  OTCPostTradeIndicator <OTCPstTradInd>
Presence: [0..*]
Definition: Indicates the type of transaction in accordance with the local regulation.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
391 July 2025
```

