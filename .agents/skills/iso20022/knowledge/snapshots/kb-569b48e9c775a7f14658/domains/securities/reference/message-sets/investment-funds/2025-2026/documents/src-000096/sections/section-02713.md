---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.6 CopyDetails <CpyDtls>"]
file_pages: [3796]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.6 CopyDetails <CpyDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3796 to 3796.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3796

```text
Constraints
• WaiverElementRule
Either OrderWaiverReason or InformationValue must be present. Both may be present.
53.4.6 CopyDetails <CpyDtls>
Presence: [0..1]
Definition: Information provided when the message is a copy of a previous message.
CopyDetails <CpyDtls> contains the following elements (see "CopyInformation5" on page 4817 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CopyIndicator <CpyInd> [1..1] Indicator 4817
   OriginalReceiver <OrgnlRcvr> [0..1] IdentifierSet C4 4817
53.4.7 Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C15 "ExtensionRule"
Extension <Xtnsn> contains the following elements (see "Extension1" on page 4835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [1..1] Text 4836
   Text <Txt> [1..1] Text 4836
Constraints
• ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3796 May 2026
```

