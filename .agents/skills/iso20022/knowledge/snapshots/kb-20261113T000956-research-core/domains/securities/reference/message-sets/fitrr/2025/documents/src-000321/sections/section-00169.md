---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02", "12.4 Message Building Blocks", "12.4.3 FinancialInstruments <FinInstrms>", "12.4.3.1 FinancialInstrument <FinInstrm>", "12.4.3.1.7 TechnicalAttributes <TechAttrbts>"]
file_pages: [208]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.042.001.02"]
---

# 12.4.3.1.7 TechnicalAttributes <TechAttrbts>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 208 to 208.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 208

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
12.4.3.1.7  TechnicalAttributes <TechAttrbts>
Presence: [0..1]
Definition: Technical attributes.
Impacted by: C12 "OneElementPresentRule"
TechnicalAttributes <TechAttrbts> contains the following RecordTechnicalData4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InconsistencyIndicator <IncnsstncyInd> [0..1] Indicator 208
   LastUpdate <LastUpd> [0..1] DateTime 208
   SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 208
   RelevantCompetentAuthority <RlvntCmptntAuthrty> [0..1] CodeSet C4 209
   PublicationPeriod <PblctnPrd> [0..1] ± 209
   NeverPublished <NvrPblshd> [0..1] Indicator 209
   RelevantTradingVenue <RlvntTradgVn> [0..1] IdentifierSet 209
Constraints
• OneElementPresentRule
At least one of the 5 elements must be present.
Following Must be True
    /InconsistencyIndicator Must be present
 Or    /LastUpdate Must be present
 Or    /SubmissionDateTime Must be present
 Or    /RelevantCompetentAuthority Must be present
 Or    /PublicationPeriod Must be present
12.4.3.1.7.1  InconsistencyIndicator <IncnsstncyInd>
Presence: [0..1]
Definition: Flag to say if there is an inconsistency across all submitting entities records.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
12.4.3.1.7.2  LastUpdate <LastUpd>
Presence: [0..1]
Definition: Last date for which data was received for this instrument.
Datatype: "ISODateTime" on page 449
12.4.3.1.7.3  SubmissionDateTime <SubmissnDtTm>
Presence: [0..1]
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
208 July 2025
```

