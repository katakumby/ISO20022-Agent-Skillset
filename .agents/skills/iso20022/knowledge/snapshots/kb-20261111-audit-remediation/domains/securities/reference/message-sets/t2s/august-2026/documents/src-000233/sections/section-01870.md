---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["73 semt.028.001.01 IntraPositionMovementQueryV01", "73.3 Constraints"]
file_pages: [2567]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 73.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2567 to 2567.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2567

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or           FromToDateTime <FrToDtTm> [1..1] ± 2610
Or           EqualDateTime <EQDtTm> [1..1] DateTime 2610
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 2610
   SupplementaryData <SplmtryData> [0..*] ± C10 2611
73.3 Constraints
C1 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of
BalanceTo.
C4 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C5 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C6 DescriptionUsageRule
Description must be used alone as the last resort.
C7 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C8 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C9 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C10 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2567 August 2026
```

