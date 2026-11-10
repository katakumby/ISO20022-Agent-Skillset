---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.43 Order23", "7.1.19.43.43 AdditionalTradeInstructionProcessingInformation <AddtlTradInstrPrcgInf>"]
file_pages: [353]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.43.43 AdditionalTradeInstructionProcessingInformation <AddtlTradInstrPrcgInf>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 353 to 353.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 353

```text
AdditionalPhysicalOrRegistrationDetails <AddtlPhysOrRegnDtls> contains the following elements
(see "RegistrationParameters3" on page 246 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CertificationIdentification <CertfctnId> [0..1] Text 246
   CertificationDateTime <CertfctnDtTm> [0..1] ± 246
   RegistrarAccount <RegarAcct> [0..1] Text 246
   CertificateNumber <CertNb> [0..*] ± C21 246
7.1.19.43.43  AdditionalTradeInstructionProcessingInformation <AddtlTradInstrPrcgInf>
Presence: [0..1]
Definition: Provides additional details of the trade process not included within structured fields of this
message.
Datatype: "Max350Text" on page 669
7.1.19.43.44  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Definition: Interest amount that has accrued in between two periods, for example, in between interest
payment periods.
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
"AmountAndDirection29" on page 228 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
7.1.19.44  Reporting6Choice
Definition: Choice of format for the reporting type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 353
Or}   Proprietary <Prtry> [1..1] ± 354
7.1.19.44.1  Code <Cd>
Presence: [1..1]
Definition: Third party reporting information expressed as an ISO 20022 code.
Datatype: "Reporting2Code" on page 644
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 353 February 2025
```

