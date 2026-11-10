---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.8 Market", "22.1.8.2 TradingVenueAttributes1", "22.1.8.2.2 IssuerRequest <IssrReq>"]
file_pages: [335]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.8.2.2 IssuerRequest <IssrReq>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 335 to 335.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 335

```text
Definition: Segment MIC for the trading venue or systematic internaliser, where applicable, otherwise
the operating MIC.
Datatype: "MICIdentifier" on page 451
22.1.8.2.2  IssuerRequest <IssrReq>
Presence: [1..1]
Definition: Indicates whether the issuer of the financial instrument has requested or approved the
trading or admission to trading of their financial instruments on a trading venue.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
22.1.8.2.3  AdmissionApprovalDateByIssuer <AdmssnApprvlDtByIssr>
Presence: [0..1]
Definition: Date and time the issuer has approved the admission to trading or trading of its financial
instruments on the trading venue.
Datatype: "ISODateTime" on page 449
22.1.8.2.4  RequestForAdmissionDate <ReqForAdmssnDt>
Presence: [0..1]
Definition: Date and time when the request for admission on the trading venue was made for the
instrument.
Datatype: "ISODateTime" on page 449
22.1.8.2.5  FirstTradeDate <FrstTradDt>
Presence: [0..1]
Definition: Date and time of the admission to trading on the trading venue or the date and time when the
instrument was first traded or an order or quote was first received by the trading venue.
Datatype: "ISODateTime" on page 449
22.1.8.2.6  TerminationDate <TermntnDt>
Presence: [0..1]
Definition: Date and time when the financial instrument ceases to be traded or to be admitted to trading
on the trading venue. Where this date and time is unavailable, the field shall not be populated.
Datatype: "ISODateTime" on page 449
22.1.8.3  TradingVenueAttributes2
Definition: Traded venue related fields.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
335 July 2025
```

