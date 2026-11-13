---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["24 colr.001.001.02 CollateralValueQueryV02", "24.4 Message Building Blocks"]
file_pages: [580]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.001.001.02"]
---

# 24.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 580 to 580.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 580

```text
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C4 CashAccountIdentificationGuideline
If the account identification identifies a group of accounts with different types or in different
currencies, the currency and/or the account type can be used as additional search criteria.
C5 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C6 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C7 DescriptionUsageRule
Description must be used alone as the last resort.
C8 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C9 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C10 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C11 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C12 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
24.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
24.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Set of elements to identify the collateral value query message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.001.001.02 CollateralValueQueryV02
Target2-Securities 580 August 2026
```

