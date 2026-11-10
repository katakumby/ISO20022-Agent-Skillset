---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.3 Constraints"]
file_pages: [7]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.3 Constraints

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 7 to 7.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 7

```text
2.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C3 CounterpartyIdentification1Rule
If at least one occurrence of CounterpartyType is present and is equal to Multilateral (MULT),
then no occurrence of CounterpartyIdentification is allowed.
If CounterpartyType is not present, then any occurrence of CounterpartyIdentification is
optional.
C4 CounterpartyIdentification2Rule
If at least one occurrence of CounterpartyType is present and is equal to Bilateral (BILA), then
at least one occurrence of CounterpartyIdentification must be present.
If CounterpartyType is not present, then any occurrence of CounterpartyIdentification is
optional.
C5 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C6 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C7 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Set of elements to identify the report query request message.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
7 March 2024
```

