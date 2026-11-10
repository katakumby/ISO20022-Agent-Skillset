---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.6 Credit <Cdt>", "6.4.2.12.6.3 SingleNameCreditDefaultSwapDerivative <SnglNmCdtDfltSwpDeriv>", "6.4.2.12.6.3.1 UnderlyingCreditDefaultSwapIdentification <UndrlygCdtDfltSwpId>"]
file_pages: [81]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.6.3.1 UnderlyingCreditDefaultSwapIdentification <UndrlygCdtDfltSwpId>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 81 to 81.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 81

```text
Constraints
• ValidISINRule
ISIN code must pass checksum validation.
6.4.2.12.6.3.1  UnderlyingCreditDefaultSwapIdentification <UndrlygCdtDfltSwpId>
Presence: [0..1]
Definition: Derivative on a credit default swap with the ISIN code of the underlying swap.
Datatype: "ISINOct2015Identifier" on page 450
6.4.2.12.6.3.2  ObligationIdentification <OblgtnId>
Presence: [1..1]
Definition: Identification of the reference obligation for a derivative on a credit default swap.
Datatype: "ISINOct2015Identifier" on page 450
6.4.2.12.6.3.3  SingleName <SnglNm>
Presence: [1..1]
Definition: Describes the single name specific details the derivative is being made on.
SingleName <SnglNm> contains the following elements (see "CreditDefaultSwapSingleName2" on
page 325 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SovereignIssuer <SvrgnIssr> [1..1] Indicator 325
   ReferenceParty <RefPty> [0..1] ± 325
   NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 325
6.4.2.12.6.4  CreditDefaultSwapIndexDerivative <CdtDfltSwpIndxDeriv>
Presence: [1..1]
Definition: A credit default swap derivative on an index.
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
81 July 2025
```

