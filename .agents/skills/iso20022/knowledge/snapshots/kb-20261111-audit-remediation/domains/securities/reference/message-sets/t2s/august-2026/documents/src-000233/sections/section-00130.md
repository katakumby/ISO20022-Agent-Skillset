---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["11 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "11.3 Constraints"]
file_pages: [177]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
topic_continuations: [{"constraint_ids": ["C10", "C11", "C12", "C13", "C14", "C15", "C16", "C17"], "until_heading": "11.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 178, "topic": "11.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00131.md"}]
---

# 11.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 177 to 177.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 11.3 Constraints topic continues in [Constraints continuation C10–C17 (file p178)](section-00131.md#file-page-178). Read the text before **11.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 177

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls> [0..1] Text 197
   SupplementaryData <SplmtryData> [0..*] ± C16 197
11.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AdditionalDetailsRule
Unless bilaterally agreed between the sender and the receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
C4 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C5 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C6 BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of
BalanceTo.
C7 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities 177 August 2026
```

