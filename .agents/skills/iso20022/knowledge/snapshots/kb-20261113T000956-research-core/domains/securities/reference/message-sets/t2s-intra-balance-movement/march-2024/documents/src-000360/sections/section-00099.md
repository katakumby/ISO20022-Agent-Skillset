---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02", "7.4 Message Building Blocks"]
file_pages: [119]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.074.001.02"]
preceding_topic_continuations: [{"constraint_ids": ["C6", "C7", "C8", "C9", "C10", "C11", "C12"], "until_heading": "7.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 119, "topic": "7.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000360/sections/section-00098.md"}]
---

# 7.4 Message Building Blocks

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 119 to 119.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 119, C6–C12 before **7.4 Message Building Blocks** continue [7.3 Constraints](section-00098.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 119

```text
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
C10 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C11 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C12 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
7.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
7.4.1 Identification <Id>
Presence: [0..1]
Definition: Unambiguous identification of the message as known by the account owner (or the
instructing party acting on its behalf).
Identification <Id> contains the following DocumentIdentification51 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 120
   CreationDateTime <CreDtTm> [0..1] ± 120
   CopyDuplicate <CpyDplct> [0..1] CodeSet 120
   MessageOriginator <MsgOrgtr> [0..1] ± 120
   MessageRecipient <MsgRcpt> [0..1] ± 121
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.074.001.02
IntraBalanceMovementCancellationRequestV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
119 March 2024
```

