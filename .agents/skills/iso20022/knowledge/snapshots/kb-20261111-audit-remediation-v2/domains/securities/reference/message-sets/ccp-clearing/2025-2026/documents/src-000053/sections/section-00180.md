---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["6 MX secl.005.001.02 MarginReportV02", "6.3 Constraints"]
file_pages: [234, 235, 236]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.005.001.02"]
topic_continuations: [{"constraint_ids": ["C16", "C17"], "until_heading": "6.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 237, "topic": "6.3 Constraints", "reference_path": "domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00181.md"}]
---

# 6.3 Constraints

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 234 to 236.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 6.3 Constraints topic continues in [Constraints continuation C16–C17 (file p237)](section-00181.md#file-page-237). Read the text before **6.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 234

```text
6.3 Constraints
The tick symbol (') means that the rule is validated on the SWIFT Network, if the message is part of a
solution for which validation is enabled.
C1 ActiveCurrency  '
(Rule)
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00005
– Error Text: Invalid currency code
C2 ActiveOrHistoricCurrency  '
(Rule)
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00006
– Error Text: Invalid currency code.
C3 AdditonalDetailsGuideline
(Guideline)
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C4 AnyBIC  '
(Rule)
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory,
and consists of eight (8) or eleven (11) contiguous characters. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00008
– Error Text: Invalid BIC.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.005.001.02 MarginReportV02
March 2026 234
```

## File page 235

```text
C5 Country  '
(Rule)
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code). (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00004
– Error Text: Invalid Country Code.
C6 CurrencyAmount  '
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
C7 CurrencyAmount  '
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
C8 DescriptionPresenceRule  '
(Rule)
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present. (CrossElementComplexRule)
Error handling:
– Error severity: Fatal
– Error Code: X00192
– Error Text: At least one identification must be present.
C9 DescriptionUsageRule
(Rule)
Description must be used alone as the last resort.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.005.001.02 MarginReportV02
March 2026 235
```

## File page 236

```text
C10 ISINGuideline
(Rule)
When a ISIN code exist. It is strongly recommended that the ISIN be used.
C11 ISINPresenceRule  '
(Rule)
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present. (CrossElementComplexRule)
Error handling:
– Error severity: Fatal
– Error Code: X00194
– Error Text: At least one identification must be present.
C12 MarginTypePresenceRule  '
(Rule)
 (CrossElementComplexRule)
Error handling:
– Error severity: Fatal
– Error Code: X00240
– Error Text: If Margin Details is present, then at least one of its elements (Initial Margin,
Variation Margin or Other Margin) must be present.
C13 OtherIdentificationPresenceRule  '
(Rule)
If OtherIdentification is not present then either ISIN or Description must be
present. (CrossElementComplexRule)
Error handling:
– Error severity: Fatal
– Error Code: X00193
– Error Text: At least one identification must be present.
C14 ReportNumberRule
(Rule)
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the
same safekeeping account must have different ReportNumbers. For example, a daily report
sent on day 1 would have ReportNumber 001, on day 2, 002, etc.
C15 SupplementaryDataRule
(Rule)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.005.001.02 MarginReportV02
March 2026 236
```

