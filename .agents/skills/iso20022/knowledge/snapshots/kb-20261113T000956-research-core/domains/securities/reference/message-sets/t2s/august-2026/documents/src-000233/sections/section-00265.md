---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["16 camt.078.001.02 IntraBalanceMovementQueryV02", "16.4 Message Building Blocks"]
file_pages: [346]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
preceding_topic_continuations: [{"constraint_ids": ["C5", "C6", "C7", "C8", "C9", "C10"], "until_heading": "16.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 346, "topic": "16.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-00264.md"}]
---

# 16.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 346 to 346.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 346, C5–C10 before **16.4 Message Building Blocks** continue [16.3 Constraints](section-00264.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 346

```text
C5 BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of
BalanceTo.
C6 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C7 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C8 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C9 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C10 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
16.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
16.4.1 Identification <Id>
Presence: [0..1]
Definition: Unambiguous identification of the message as known by the account owner (or the
instructing party acting on its behalf).
Identification <Id> contains the following DocumentIdentification51 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 346
   CreationDateTime <CreDtTm> [0..1] ± 347
   CopyDuplicate <CpyDplct> [0..1] CodeSet 347
   MessageOriginator <MsgOrgtr> [0..1] ± 347
   MessageRecipient <MsgRcpt> [0..1] ± 347
16.4.1.1  Identification <Id>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 346 August 2026
```

