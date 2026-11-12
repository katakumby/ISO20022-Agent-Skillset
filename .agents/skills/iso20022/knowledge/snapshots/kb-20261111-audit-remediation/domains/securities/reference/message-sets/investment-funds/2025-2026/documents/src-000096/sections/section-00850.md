---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.5 Portfolio <Prtfl>", "36.4.15.5.3 Pension <Pnsn>", "36.4.15.5.3.16 RetirementAge <RtrmntAge>"]
file_pages: [1177]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.5.3.16 RetirementAge <RtrmntAge>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1177 to 1177.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1177

```text
36.4.15.5.3.16  RetirementAge <RtrmntAge>
Presence: [0..1]
Definition: Age at which the pension policy, plan or scheme holder retires.
Datatype: "DecimalNumber" on page 5400
36.4.15.5.3.17  Sharing <Shrg>
Presence: [0..1]
Definition: Indicates whether the pension benefits are shared.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
36.4.15.5.3.18  LumpSumType <LumpSumTp>
Presence: [0..*]
Definition: Type of lump sum paid to a member of the pension policy, plan or scheme.
LumpSumType <LumpSumTp> contains one of the following elements (see "LumpSumType1Choice"
on page 4780 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4780
Or}   Proprietary <Prtry> [1..1] ± 4781
36.4.15.5.3.19  PensionOrder <PnsnOrdr>
Presence: [0..*]
Definition: Order attached to the pension policy, plan or scheme.
PensionOrder <PnsnOrdr> contains the following elements (see "PensionOrder1" on page 4741 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  4742
{Or     Code <Cd> [1..1] CodeSet 4742
Or}     Proprietary <Prtry> [1..1] ± 4742
   AdditionalInformation <AddtlInf> [0..*] ± 4743
36.4.15.5.3.20  RingFencedDrawdownAssets <RingFncdDrwdwnAssts>
Presence: [0..1]
Definition: Indicates whether assets held within the pension are ring-fenced into specific tranches.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1177 May 2026
```

