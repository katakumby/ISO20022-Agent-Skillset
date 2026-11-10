---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.11 CurrencyOption <CcyOptn>"]
file_pages: [145]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.11 CurrencyOption <CcyOptn>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 145 to 145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 145

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
3.4.11.11  CurrencyOption <CcyOptn>
Presence: [0..1]
Definition: Currency in which cash proceeds are to be credited/debited.
Impacted by: C2 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 1157
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
3.4.11.12  DefaultProcessingOrStandingInstruction <DfltPrcgOrStgInstr>
Presence: [1..1]
Definition: Indicates whether the corporate action movement is a default processing or a standing
instruction.
DefaultProcessingOrStandingInstruction <DfltPrcgOrStgInstr> contains one of the following
elements (see "DefaultProcessingOrStandingInstruction2Choice" on page 998 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DefaultOptionIndicator <DfltOptnInd> [1..1] Indicator 998
Or}   StandingInstructionIndicator <StgInstrInd> [1..1] Indicator 998
3.4.11.13  ChargesAppliedIndicator <ChrgsApldInd>
Presence: [0..1]
Definition: Indicates whether charges apply to the holder, for instance redemption charges.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
3.4.11.14  CertificationBreakdownIndicator <CertfctnBrkdwnInd>
Presence: [0..1]
Definition: Indicates whether certification/breakdown is required from the account owner.
Yes: certification required
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 145 February 2026
```

