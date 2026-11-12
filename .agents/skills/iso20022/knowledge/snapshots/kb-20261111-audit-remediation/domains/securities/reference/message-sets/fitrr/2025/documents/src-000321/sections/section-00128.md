---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.3 TerminatedRecord <TermntdRcrd>", "8.4.2.3.7 TechnicalAttributes <TechAttrbts>"]
file_pages: [160]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.3.7 TechnicalAttributes <TechAttrbts>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 160 to 160.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 160

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
8.4.2.3.7  TechnicalAttributes <TechAttrbts>
Presence: [0..1]
Definition: Technical attributes.
Impacted by: C12 "OneElementPresentRule"
TechnicalAttributes <TechAttrbts> contains the following RecordTechnicalData4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InconsistencyIndicator <IncnsstncyInd> [0..1] Indicator 160
   LastUpdate <LastUpd> [0..1] DateTime 160
   SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 160
   RelevantCompetentAuthority <RlvntCmptntAuthrty> [0..1] CodeSet C4 161
   PublicationPeriod <PblctnPrd> [0..1] ± 161
   NeverPublished <NvrPblshd> [0..1] Indicator 161
   RelevantTradingVenue <RlvntTradgVn> [0..1] IdentifierSet 161
Constraints
• OneElementPresentRule
At least one of the 5 elements must be present.
Following Must be True
    /InconsistencyIndicator Must be present
 Or    /LastUpdate Must be present
 Or    /SubmissionDateTime Must be present
 Or    /RelevantCompetentAuthority Must be present
 Or    /PublicationPeriod Must be present
8.4.2.3.7.1  InconsistencyIndicator <IncnsstncyInd>
Presence: [0..1]
Definition: Flag to say if there is an inconsistency across all submitting entities records.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
8.4.2.3.7.2  LastUpdate <LastUpd>
Presence: [0..1]
Definition: Last date for which data was received for this instrument.
Datatype: "ISODateTime" on page 449
8.4.2.3.7.3  SubmissionDateTime <SubmissnDtTm>
Presence: [0..1]
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
160 July 2025
```

