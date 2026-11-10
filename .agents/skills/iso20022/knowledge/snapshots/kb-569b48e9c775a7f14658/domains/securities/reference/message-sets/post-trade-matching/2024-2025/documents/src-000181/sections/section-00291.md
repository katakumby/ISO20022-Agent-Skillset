---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.43 Order23", "7.1.19.43.36 ChargeTaxBasisType <ChrgTaxBsisTp>"]
file_pages: [351]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.43.36 ChargeTaxBasisType <ChrgTaxBsisTp>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 351 to 351.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 351

```text
Definition: Indicates whether the derivative product is covered or not by an underlying financial
instrument position.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.43.36  ChargeTaxBasisType <ChrgTaxBsisTp>
Presence: [0..1]
Definition: Type of charge/tax basis.
ChargeTaxBasisType <ChrgTaxBsisTp> contains one of the following elements (see
"ChargeTaxBasisType2Choice" on page 248 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 248
Or}   Proprietary <Prtry> [1..1] ± 248
7.1.19.43.37  CapitalGainType <CptlGnTp>
Presence: [0..1]
Definition: Specifies the type of capital gain.
CapitalGainType <CptlGnTp> contains one of the following elements (see
"EUCapitalGainType3Choice" on page 307 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   EUCapitalGain <EUCptlGn> [1..1] CodeSet 307
Or}   Proprietary <Prtry> [1..1] ± 307
7.1.19.43.38  MatchStatus <MtchSts>
Presence: [0..1]
Definition: Provides the matching status of the trade confirmation.
MatchStatus <MtchSts> contains one of the following elements (see "MatchingStatus27Choice" on
page 594 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 594
Or}   Proprietary <Prtry> [1..1] ± 594
7.1.19.43.39  CallInType <CallInTp>
Presence: [0..1]
Definition: Specifies the type of pay-in call report.
Datatype: "CallIn1Code" on page 619
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 351 February 2025
```

