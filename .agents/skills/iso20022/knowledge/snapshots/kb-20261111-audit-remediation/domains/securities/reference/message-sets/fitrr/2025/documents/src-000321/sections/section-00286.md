---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.8 Market", "22.1.8.3 TradingVenueAttributes2", "22.1.8.3.1 Identification <Id>"]
file_pages: [336]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.8.3.1 Identification <Id>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 336 to 336.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 336

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] IdentifierSet 336
   IssuerRequest <IssrReq> [0..1] Indicator 336
   AdmissionApprovalDateByIssuer
<AdmssnApprvlDtByIssr>
[0..1] DateTime 336
   RequestForAdmissionDate <ReqForAdmssnDt> [0..1] DateTime 337
   FirstTradeDate <FrstTradDt> [0..1] DateTime 337
   TerminationDate <TermntnDt> [0..1] DateTime 337
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
22.1.8.3.1  Identification <Id>
Presence: [1..1]
Definition: Segment MIC for the trading venue or systematic internaliser, where applicable, otherwise
the operating MIC.
Datatype: "MICIdentifier" on page 451
22.1.8.3.2  IssuerRequest <IssrReq>
Presence: [0..1]
Definition: Indicates whether the issuer of the financial instrument has requested or approved the
trading or admission to trading of their financial instruments on a trading venue.
Usage: when not present, the indicator in not applicable.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
22.1.8.3.3  AdmissionApprovalDateByIssuer <AdmssnApprvlDtByIssr>
Presence: [0..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
336 July 2025
```

