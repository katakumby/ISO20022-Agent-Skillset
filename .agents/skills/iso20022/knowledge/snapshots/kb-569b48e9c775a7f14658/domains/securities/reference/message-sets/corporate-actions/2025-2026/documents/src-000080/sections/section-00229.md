---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.9 CorporateActionInstruction <CorpActnInstr>", "5.4.9.3 OptionFeatures <OptnFeatrs>"]
file_pages: [306]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.9.3 OptionFeatures <OptnFeatrs>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 306 to 306.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 306

```text
OptionType <OptnTp> contains one of the following elements (see "CorporateActionOption40Choice"
on page 892 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 892
Or}   Proprietary <Prtry> [1..1] ± 894
5.4.9.3  OptionFeatures <OptnFeatrs>
Presence: [0..1]
Definition: Specifies the features that may apply to a corporate action option.
OptionFeatures <OptnFeatrs> contains one of the following elements (see
"OptionFeaturesFormat25Choice" on page 942 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 943
Or}   Proprietary <Prtry> [1..1] ± 943
5.4.9.4  FractionDisposition <FrctnDspstn>
Presence: [0..1]
Definition: Specifies how fractional amount/quantities are treated.
FractionDisposition <FrctnDspstn> contains one of the following elements (see
"FractionDispositionType28Choice" on page 974 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 974
Or}   Proprietary <Prtry> [1..1] ± 974
5.4.9.5  ChangeType <ChngTp>
Presence: [0..*]
Definition: Type of changes affecting the security form.
ChangeType <ChngTp> contains one of the following elements (see
"CorporateActionChangeTypeFormat6Choice" on page 964 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 964
Or}   Proprietary <Prtry> [1..1] ± 964
5.4.9.6  EligibleForCollateralIndicator <ElgblForCollInd>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 306 February 2026
```

