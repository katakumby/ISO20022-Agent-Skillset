---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.1 PensionTransferScope1Choice", "66.1.26.1.1 Code <Cd>"]
file_pages: [4711]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4711 to 4711.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4711

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4711
Or}   Proprietary <Prtry> [1..1] ± 4711
66.1.26.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of pension policy, plan or scheme transfer scope expressed as a code.
Datatype: "PensionTransferScope1Code" on page 5341
CodeName Name Definition
CRYS CrystallisedPart Transfer is for the crystallised portion.
SDDT DrawdownTranche Transfer is for a specific drawdown
tranche.
FULP FullPension Transfer is for the full pension.
UCRY UncrystallisedPart Transfer is for the uncrystallised portion.
66.1.26.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of pension policy, plan or scheme transfer scope expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.26.2  InvestmentRestrictions3
Definition: Investment restrictions linked to the trading of an investment fund, or an alternative/hedge
fund.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4711 May 2026
```

