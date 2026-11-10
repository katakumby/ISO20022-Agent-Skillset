---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks"]
file_pages: [1802]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1802 to 1802.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1802

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C4 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C5 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C6 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C7 DescriptionUsageRule
Description must be used alone as the last resort.
C8 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C9 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C10 MailingIndicatorRule
If RegistrationAddressIndicator is "true" or "1" (Yes), then MailingIndicator must be "true" or "1".
C11 NextCallableDateAndCallableIndicatorRule
If CallableIndicator is present, then NextCalldate must be present.
C12 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C13 PutableDateAndPutableIndicatorRule
If PutableIndicator is present, then PutableDate must be present.
C14 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
32.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1802 August 2026
```

