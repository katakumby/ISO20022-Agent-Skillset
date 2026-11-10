---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["18 camt.080.001.02 IntraBalanceMovementModificationQueryV02", "18.3 Constraints"]
file_pages: [425]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.080.001.02"]
---

# 18.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 425 to 425.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 425

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or           EqualDateTime <EQDtTm> [1..1] DateTime 434
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 434
   SupplementaryData <SplmtryData> [0..*] ± C5 435
18.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C5 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
18.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
18.4.1 Identification <Id>
Presence: [0..1]
Definition: Unambiguous identification of the message as known by the account owner (or the
instructing party acting on its behalf).
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.080.001.02
IntraBalanceMovementModificationQueryV02
Target2-Securities 425 August 2026
```

