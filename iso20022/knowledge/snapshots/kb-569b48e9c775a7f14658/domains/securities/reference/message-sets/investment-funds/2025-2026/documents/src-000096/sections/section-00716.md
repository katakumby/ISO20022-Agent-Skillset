---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.5 Portfolio <Prtfl>", "35.4.14.5.3 Pension <Pnsn>", "35.4.14.5.3.4 TaxReference <TaxRef>"]
file_pages: [984]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.5.3.4 TaxReference <TaxRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 984 to 984.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 984

```text
TransferScope <TrfScp> contains one of the following elements (see "PensionTransferScope1Choice"
on page 4710 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4711
Or}   Proprietary <Prtry> [1..1] ± 4711
35.4.14.5.3.4  TaxReference <TaxRef>
Presence: [0..*]
Definition: Tax reference issued to the pension policy, plan or scheme by a central organisation.
TaxReference <TaxRef> contains the following elements (see "TaxReference1" on page 5234 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxType <TaxTp> [0..1]  5235
{Or     Code <Cd> [1..1] CodeSet 5235
Or}     Proprietary <Prtry> [1..1] ± 5235
   Reference <Ref> [1..1] Text 5236
   HolderType <HldrTp> [0..1]  5236
{Or     Code <Cd> [1..1] CodeSet 5236
Or}     Proprietary <Prtry> [1..1] ± 5236
35.4.14.5.3.5  DrawdownTrancheIdentification <DrwdwnTrchId>
Presence: [0..1]
Definition: Reference of the drawdown.
Datatype: "Max35Text" on page 5403
35.4.14.5.3.6  NonWrapperTransfer <NonWrpprTrf>
Presence: [0..1]
Definition: Indicates that the transfer is only in relation to underlying assets, and that the wrapper
transfer will occur separately.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
35.4.14.5.3.7  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the pension policy, plan or scheme.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 984 May 2026
```

