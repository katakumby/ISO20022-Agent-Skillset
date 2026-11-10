---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["8 camt.009.001.08 GetLimitV08", "8.4 Message Building Blocks"]
file_pages: [367]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.009.001.08"]
---

# 8.4 Message Building Blocks

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 367 to 367.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 367

```text
If no occurrence of CurrentLimitType is MULT, then any occurrence of
BilateralLimitCounterpartyIdentification is optional.
If CurrentLimitType is not present, then any occurrence of
BilateralLimitCounterpartyIdentification is optional.
C4 BilateralLimitCounterparty4Rule
If at least one occurrence of DefaultLimitType is present and is MULT, then no occurrence of
BilateralLimitCounterpartyIdentification is allowed.
If no occurrence of DefaultLimitType is MULT, then any occurrence of
BilateralLimitCounterpartyIdentification is optional.
If DefaultLimitType is not present, then any occurrence of
BilateralLimitCounterpartyIdentification is optional.
C5 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C6 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C7 LimitCriteriaGuideline
If a bilateral limit regarding specific members in the system is required, then the identification of
the bilateral counterpart should be given.
By default, if there is no identification of the bilateral counterpart and the current or default
bilateral limit is required, then all the bilateral limits with the relevant counterpart identifications
are returned.
C8 ReturnCriteriaAndOrSearchCriteriaRule
If ReturnCriteria is not present, then at least one occurrence of SearchCriteria must be present.
If ReturnCriteria is present, then any occurrence of SearchCriteria is optional.
C9 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
8.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
8.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 367 February 2025
```

