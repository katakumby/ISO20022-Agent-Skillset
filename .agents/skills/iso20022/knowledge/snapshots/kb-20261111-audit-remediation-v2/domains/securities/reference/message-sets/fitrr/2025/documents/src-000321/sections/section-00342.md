---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.3 SecuritiesReferenceDataReport7", "22.1.13.3.5 DebtInstrumentAttributes <DebtInstrmAttrbts>"]
file_pages: [397]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.3.5 DebtInstrumentAttributes <DebtInstrmAttrbts>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 397 to 397.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 397

```text
TradingVenueRelatedAttributes <TradgVnRltdAttrbts> contains the following elements (see
"TradingVenueAttributes2" on page 335 for details)
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
22.1.13.3.5  DebtInstrumentAttributes <DebtInstrmAttrbts>
Presence: [0..1]
Definition: Attributes specific to debt instruments.
DebtInstrumentAttributes <DebtInstrmAttrbts> contains the following DebtInstrument2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 397
   MaturityDate <MtrtyDt> [0..1] Date 398
   NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 398
   InterestRate <IntrstRate> [1..1] ± 398
   DebtSeniority <DebtSnrty> [0..1] CodeSet 399
22.1.13.3.5.1  TotalIssuedNominalAmount <TtlIssdNmnlAmt>
Presence: [1..1]
Definition: Total issued nominal amount in monetary value.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
397 July 2025
```

