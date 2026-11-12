---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.43 FinancialInstrumentIdentificationValidity <FinInstrmIdVldty>", "13.1.6.3.43.2 ISINValidFrom <ISINVldFr>"]
file_pages: [370]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.43.2 ISINValidFrom <ISINVldFr>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 370 to 370.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 370

```text
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
13.1.6.3.43.2  ISINValidFrom <ISINVldFr>
Presence: [0..1]
Definition: Defines the date from which the instrument code is valid. This date can be before the actual
issue date of an instrument for 'when-issued' securities, but may not be a date in the future for a new
security.
Datatype: "ISODate" on page 529
13.1.6.3.44  SettlementInformation <SttlmInf>
Presence: [0..*]
Definition: Settlement of the securities in a securities transaction, that is, the instruction to deliver or
receive securities, involving the payment of an amount of money or not.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 370 March 2024
```

