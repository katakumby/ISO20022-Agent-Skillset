---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["7 reda.012.001.01 SecurityReportV01", "7.3 Constraints"]
file_pages: [96]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 7.3 Constraints

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 96 to 96.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 96

```text
7.3 Constraints
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.012.001.01 SecurityReportV01
Target2-Securities - Securities Reference Data 96 March 2024
```

