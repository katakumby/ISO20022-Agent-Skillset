---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02", "3.4 Message Building Blocks", "3.4.2 ReferenceData <RefData>", "3.4.2.5 DebtInstrumentAttributes <DebtInstrmAttrbts>"]
file_pages: [24]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.017.001.02"]
---

# 3.4.2.5 DebtInstrumentAttributes <DebtInstrmAttrbts>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 24 to 24.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 24

```text
TradingVenueRelatedAttributes <TradgVnRltdAttrbts> contains the following elements (see
"TradingVenueAttributes1" on page 334 for details)
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
3.4.2.5  DebtInstrumentAttributes <DebtInstrmAttrbts>
Presence: [0..1]
Definition: Attributes specific to debt instruments.
DebtInstrumentAttributes <DebtInstrmAttrbts> contains the following DebtInstrument2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 24
   MaturityDate <MtrtyDt> [0..1] Date 25
   NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 25
   InterestRate <IntrstRate> [1..1] ± 25
   DebtSeniority <DebtSnrty> [0..1] CodeSet 26
3.4.2.5.1  TotalIssuedNominalAmount <TtlIssdNmnlAmt>
Presence: [1..1]
Definition: Total issued nominal amount in monetary value.
Approved by the Securities SEG on 17 July 2025 auth.017.001.02
FinancialInstrumentReportingReferenceDataReport
V02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
24 July 2025
```

