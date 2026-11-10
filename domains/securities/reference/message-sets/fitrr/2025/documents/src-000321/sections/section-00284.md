---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.8 Market", "22.1.8.1 TradingVenueIdentification2", "22.1.8.1.2 Type <Tp>"]
file_pages: [334]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.8.1.2 Type <Tp>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 334 to 334.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 334

```text
22.1.8.1.2  Type <Tp>
Presence: [1..1]
Definition: Code list of venues to populate free form text identification.
Datatype: "TradingVenue2Code" on page 447
CodeName Name Definition
APPA ApprovedPublicationArrangement Person authorised under the provisions
established in the regulation to provide
the service of publishing trade reports on
behalf of investment firms.
CTPS ConsolidatedTapeProvider Provider which will consolidate post-
trade information into a continuous
electronic data stream and make it
publicly available as close to real time as
technologically possible on a reasonable
commercial basis and free of charge
after 15 minutes.
22.1.8.2  TradingVenueAttributes1
Definition: Traded venue related fields.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] IdentifierSet 334
   IssuerRequest <IssrReq> [1..1] Indicator 335
   AdmissionApprovalDateByIssuer
<AdmssnApprvlDtByIssr>
[0..1] DateTime 335
   RequestForAdmissionDate <ReqForAdmssnDt> [0..1] DateTime 335
   FirstTradeDate <FrstTradDt> [0..1] DateTime 335
   TerminationDate <TermntnDt> [0..1] DateTime 335
Constraints
• ValidateAdmissionIssuerRule
When IssuerRequest is equal to true, then AdmissionApprovalDateByIssuer must be present.
On Condition
    /IssuerRequest is equal to value 'true'
Following Must be True
    /AdmissionApprovalDateByIssuer Must be present
• ValidMICRule
Market Identification code must be an active market at the time of reporting.
• ValidTerminationDateRule
TerminationDate cannot be a date earlier than FirstTradeDate, RequestForAdmissionDate or
AdmissionApprovalDate.
22.1.8.2.1  Identification <Id>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
334 July 2025
```

