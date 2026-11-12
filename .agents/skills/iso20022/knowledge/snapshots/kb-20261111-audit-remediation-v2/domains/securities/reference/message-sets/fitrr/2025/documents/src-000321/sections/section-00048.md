---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.1 TechnicalRecordIdentification <TechRcrdId>"]
file_pages: [62]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.1 TechnicalRecordIdentification <TechRcrdId>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 62 to 62.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 62

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         SingleName <SnglNm> [1..1] ± 81
Or}       CreditDefaultSwapIndexDerivative
<CdtDfltSwpIndxDeriv>
[1..1]  81
         UnderlyingCreditDefaultSwapIdentification
<UndrlygCdtDfltSwpId>
[0..1] IdentifierSet 82
         UnderlyingCreditDefaultSwapIndex
<UndrlygCdtDfltSwpIndx>
[1..1]  82
           UnderlyingIndexIdentification <UndrlygIndxId> [0..1] IdentifierSet 82
           UnderlyingIndexName <UndrlygIndxNm> [0..1] Text 83
           Series <Srs> [0..1] Quantity 83
           Version <Vrsn> [0..1] Quantity 83
           RollMonth <RollMnth> [0..12] Quantity 83
           NextRollDate <NxtRollDt> [0..1] Date 83
           NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 83
Or}     EmissionAllowance <EmssnAllwnc> [1..1] CodeSet 84
Constraints
• ValidISINRule
ISIN code must pass checksum validation.
• ValidMICRule
Where reported, Market Identification code must be an active market for that reporting period.
6.4.2.1  TechnicalRecordIdentification <TechRcrdId>
Presence: [0..1]
Definition: Unique identifier of a record in a message used as part of error management and status
advice messages.
Usage:
This identification will be used in the status advice report sent back.
Datatype: "Max35Text" on page 456
6.4.2.2  Identification <Id>
Presence: [1..1]
Definition: Identifies the financial instrument using an ISIN.
Datatype: "ISINOct2015Identifier" on page 450
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
62 July 2025
```

